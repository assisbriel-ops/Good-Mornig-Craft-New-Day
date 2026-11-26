"""gm_tools (versao de revisao): cor em OKLCH, ajuste, conferencia e pranchas.
Uso (na raiz do repo): import sys; sys.path.insert(0, 'tools'); from gm_tools import *
Imagens = arrays float (h, w, 4) RGBA 0..255. As texturas sao lidas direto do repo (sem zip)."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX = os.path.join(REPO, 'assets', 'minecraft', 'textures')
FONTE = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'          # aceita acento
def _f(t): return ImageFont.truetype(FONTE, t) if os.path.exists(FONTE) else None

# ---------- pacote ----------
def caminho(nome): return os.path.join(TEX, f'{nome}.png')          # 'block/dirt' -> caminho no repo

def carregar(nomes):
    """Le so as texturas pedidas do repo. nomes = ['block/dirt', 'item/apple', ...]. Devolve {nome: array}."""
    return {n: abrir(caminho(n)) for n in nomes}
extrair = carregar                                                    # nome antigo

def gravar(a, nome):
    """Salva a textura final no lugar certo do repo ('block/dirt')."""
    salvar(a, caminho(nome))

def abrir(p, quadro=True):
    a = np.asarray(Image.open(p).convert('RGBA')).astype(float)
    h, w = a.shape[:2]
    return a[:w] if quadro and h > w and h % w == 0 else a            # 1o quadro de animacao

def salvar(a, p):
    a = np.clip(np.rint(a), 0, 255).astype(np.uint8)
    a[..., 3] = np.where(a[..., 3] >= 128, 255, 0); a[a[..., 3] == 0] = 0   # alfa so 0 ou 255
    os.makedirs(os.path.dirname(p) or '.', exist_ok=True); Image.fromarray(a, 'RGBA').save(p)

def hexs(cores): return ['#%02X%02X%02X' % tuple(int(round(v)) for v in c[:3]) for c in cores]
def de_hex(lst): return np.array([[int(h[i:i+2], 16) for i in (1, 3, 5)] for h in lst], float)

# ---------- cor ----------
def oklab(rgb):
    c = np.asarray(rgb, float)[..., :3] / 255.
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    l = 0.4122214708*c[..., 0] + 0.5363325363*c[..., 1] + 0.0514459929*c[..., 2]
    m = 0.2119034982*c[..., 0] + 0.6806995451*c[..., 1] + 0.1073969566*c[..., 2]
    s = 0.0883024619*c[..., 0] + 0.2817188376*c[..., 1] + 0.6299787005*c[..., 2]
    l, m, s = np.cbrt(l), np.cbrt(m), np.cbrt(s)
    return np.stack([0.2104542553*l + 0.7936177850*m - 0.0040720468*s,
                     1.9779984951*l - 2.4285922050*m + 0.4505937099*s,
                     0.0259040371*l + 0.7827717662*m - 0.8086757660*s], -1)

def rgb(lab):
    lab = np.asarray(lab, float)
    l = (lab[..., 0] + 0.3963377774*lab[..., 1] + 0.2158037573*lab[..., 2]) ** 3
    m = (lab[..., 0] - 0.1055613458*lab[..., 1] - 0.0638541728*lab[..., 2]) ** 3
    s = (lab[..., 0] - 0.0894841775*lab[..., 1] - 1.2914855480*lab[..., 2]) ** 3
    c = np.stack([4.0767416621*l - 3.3077115913*m + 0.2309699292*s,
                  -1.2684380046*l + 2.6097574011*m - 0.3413193965*s,
                  -0.0041960863*l - 0.7034186147*m + 1.7076147010*s], -1)
    c = np.clip(c, 0, 1)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055) * 255

def lch(a):
    lab = oklab(a)
    return lab[..., 0], np.hypot(lab[..., 1], lab[..., 2]), np.degrees(np.arctan2(lab[..., 2], lab[..., 1])) % 360

def opaco(a): return a[..., 3] > 127

def rampa(a, n=7, mascara=None):
    """Rampa real de n cores (escuro -> claro): cada degrau e uma cor EXISTENTE da textura."""
    m = opaco(a) if mascara is None else mascara & opaco(a)
    px = a[m][:, :3]; lab = oklab(px); out = []
    for t in np.percentile(lab[:, 0], np.linspace(3, 97, n)):
        q = np.where(np.abs(lab[:, 0] - t) <= 0.012)[0]
        if len(q) == 0: q = np.array([np.abs(lab[:, 0] - t).argmin()])
        med = np.median(lab[q], 0); out.append(px[q[np.argmin(((lab[q] - med) ** 2).sum(1))]])
    return np.array(out)

def repintar(a, rmp, ganho=1.0, L_alvo=None, suave=True, mascara=None):
    """L novo = L_alvo + (L - L mediano) * ganho; a cor sai da rampa. suave=False escolhe o degrau (cel)."""
    m = opaco(a) if mascara is None else mascara & opaco(a)
    rl = oklab(rmp); rl = rl[np.argsort(rl[:, 0])]; L = oklab(a)[..., 0]
    alvo = np.median(rl[:, 0]) if L_alvo is None else L_alvo
    Ln = np.clip(alvo + (L - np.median(L[m])) * ganho, rl[0, 0], rl[-1, 0])
    lab = (np.stack([Ln, np.interp(Ln, rl[:, 0], rl[:, 1]), np.interp(Ln, rl[:, 0], rl[:, 2])], -1) if suave
           else rl[np.abs(Ln[..., None] - rl[:, 0]).argmin(-1)])
    out = a.copy(); out[..., :3] = np.where(m[..., None], rgb(lab), a[..., :3]); return out

def colorizar(a, H, S, niveis=None):
    """Colorizar do Photoshop (H graus, S 0..1); niveis = mediana de luminosidade HSL alvo."""
    g = a[..., :3] / 255.; Lh = (g.max(-1) + g.min(-1)) / 2
    if niveis is not None: Lh = np.clip(Lh + (niveis - np.median(Lh[opaco(a)])), 0, 1)
    C = (1 - np.abs(2 * Lh - 1)) * S; hp = (H % 360) / 60; X = C * (1 - abs(hp % 2 - 1))
    r, g_, b = [(C, X, 0), (X, C, 0), (0, C, X), (0, X, C), (X, 0, C), (C, 0, X)][int(hp) % 6]
    out = a.copy(); mm = Lh - C / 2
    for i, ch in enumerate((r, g_, b)): out[..., i] = (ch + mm) * 255
    return out

def tingir(material, corante, dose=0.45):
    """Mistura subtrativa (luz linear). dose 0.30 o material manda; 0.60 o corante manda."""
    lin = lambda c: np.where(c/255. <= 0.04045, c/255./12.92, ((c/255. + 0.055)/1.055) ** 2.4)
    x = np.maximum(lin(material[..., :3]), 1e-4) ** (1 - dose) * np.maximum(lin(np.asarray(corante, float)[:3]), 1e-4) ** dose
    out = material.copy(); out[..., :3] = np.where(x <= 0.0031308, x*12.92, 1.055*x**(1/2.4) - 0.055) * 255
    return out

def ajustar(a, dL=0.0, kC=1.0, dH=0.0, mascara=None):
    """Pedido em porcentagem: dL 0.03 = 3% mais claro; kC 0.8 = 20% menos saturado; dH gira a matiz."""
    lab = oklab(a); m = opaco(a) if mascara is None else mascara & opaco(a)
    L = lab[..., 0] + dL; C = np.hypot(lab[..., 1], lab[..., 2]) * kC
    h = np.arctan2(lab[..., 2], lab[..., 1]) + np.radians(dH)
    out = a.copy(); out[..., :3] = np.where(m[..., None], rgb(np.stack([L, C*np.cos(h), C*np.sin(h)], -1)), a[..., :3])
    return out

def trocar(a, de, para):
    """Troca cores exatas (paleta indexada): de/para = listas de RGB."""
    out = a.copy()
    for s, d in zip(de, para):
        m = (np.abs(a[..., :3] - np.asarray(s[:3], float)).sum(-1) < 1) & opaco(a); out[m, :3] = d[:3]
    return out

# ---------- colormap ----------
BIOMA = {'planicie': (.8, .4), 'floresta': (.7, .8), 'taiga': (.25, .8), 'taiga_nevada': (-.5, .4),
         'selva': (.95, .9), 'savana': (2., 0.), 'deserto': (2., 0.), 'pantano': (.8, .9), 'betula': (.6, .6)}
def colormap(mapa, bioma):
    """Cor do colormap ('grass' ou 'foliage') no bioma."""
    cm = abrir(caminho(f'colormap/{mapa}'), quadro=False)
    t, d = BIOMA[bioma]; t = min(max(t, 0), 1); d = min(max(d, 0), 1) * t
    return cm[int((1 - d) * 255), int((1 - t) * 255), :3]

def tintar(a, cor): out = a.copy(); out[..., :3] = a[..., :3] * np.asarray(cor, float) / 255; return out

# ---------- conferencia ----------
def medir(a):
    m = opaco(a); L, C, H = lch(a)
    d = np.concatenate([np.abs(L[:, 1:] - L[:, :-1])[m[:, 1:] & m[:, :-1]], np.abs(L[1:] - L[:-1])[m[1:] & m[:-1]]])
    cm = m & (C > 0.03); ys, xs = np.where(m)
    return dict(px=int(m.sum()), caixa=f'{np.ptp(xs)+1}x{np.ptp(ys)+1}' if m.any() else '0',
                vizinhos=round(float(np.median(d)), 3) if len(d) else 0, L=(round(float(L[m].min()), 2),
                round(float(np.median(L[m])), 2), round(float(L[m].max()), 2)), C=round(float(np.median(C[m])), 3),
                matiz=round(float(np.median(H[cm]))) if cm.any() else None,
                cores=len(np.unique(a[m][:, :3].astype(int), axis=0)), alfa_parcial=int(((a[..., 3] > 0) & (a[..., 3] < 255)).sum()))

def comparar(texs):
    """Tabela curta: {nome: array} -> uma linha por textura (atual x opcoes x parentes)."""
    return '\n'.join(f'{n:16s} {medir(a)}' for n, a in texs.items())

# ---------- pranchas (so visualizacao) ----------
def _img(a): return Image.fromarray(np.clip(np.rint(a), 0, 255).astype(np.uint8), 'RGBA')
def _amp(a, e): t = _img(a); return t.resize((t.width * e, t.height * e), Image.NEAREST)

def cena(grade, tex, escala=4, ceu=(150, 190, 230)):
    """grade = linhas de nomes ('' = vazio); tex = {nome: array}."""
    h, w = next(iter(tex.values())).shape[:2]; im = Image.new('RGBA', (w * len(grade[0]), h * len(grade)), (*ceu, 255))
    for r, lin in enumerate(grade):
        for c, n in enumerate(lin):
            if n: t = _img(tex[n]); im.paste(t, (c * w, r * h), t)
    return im.resize((im.width * escala, im.height * escala), Image.NEAREST)

def slots(itens, escala=4):
    """Itens no slot de inventario, lado a lado."""
    s = 18; im = Image.new('RGBA', (len(itens) * s + 2, s + 2), (139, 139, 139, 255)); d = ImageDraw.Draw(im)
    for i, a in enumerate(itens):
        d.rectangle([i*s+1, 1, i*s+s, s], outline=(55, 55, 55)); t = _img(a); im.paste(t, (i*s+2, 2), t)
    return im.resize((im.width * escala, im.height * escala), Image.NEAREST)

def prancha_revisao(atual, opcoes, nomes=None, extra=None, escala=10, fundo=(90, 110, 80)):
    """'atual' + opcoes numeradas de 1, ampliadas. extra = funcao(array) -> PIL (cena, slots, mosaico),
    desenhada embaixo de cada uma. Uma imagem so por rodada."""
    todas = [atual] + list(opcoes); rot = ['atual'] + [str(i + 1) for i in range(len(opcoes))]
    nomes = [''] + list(nomes or [''] * len(opcoes))
    blocos = [(_amp(a, escala), extra(a) if extra else None) for a in todas]
    cw = max(max(b.width, e.width if e else 0) for b, e in blocos) + 24
    ch = max(b.height + (e.height + 10 if e else 0) for b, e in blocos)
    im = Image.new('RGB', (cw * len(todas) + 10, ch + 60), fundo); d = ImageDraw.Draw(im)
    for i, (b, e) in enumerate(blocos):
        x = 10 + i * cw; im.paste(b, (x, 54), b)
        if e: im.paste(e, (x, 64 + b.height), e)
        d.text((x, 4), rot[i], fill='white', font=_f(38)); d.text((x + 30 + 22 * len(rot[i]), 18), nomes[i], fill=(235, 235, 220), font=_f(18))
    return im

def mosaico(a, n=3, escala=3):
    h, w = a.shape[:2]; im = Image.new('RGBA', (w * n, h * n)); t = _img(a)
    for r in range(n):
        for c in range(n): im.paste(t, (c * w, r * h))
    return im.resize((im.width * escala, im.height * escala), Image.NEAREST)

def ver_rampa(rampas, nomes=None, lado=24):
    im = Image.new('RGB', (max(len(r) for r in rampas) * lado + 170, len(rampas) * (lado + 6) + 6), (60, 60, 60)); d = ImageDraw.Draw(im)
    for j, r in enumerate(rampas):
        for i, c in enumerate(r): d.rectangle([170+i*lado, 6+j*(lado+6), 170+(i+1)*lado-2, 6+j*(lado+6)+lado], fill=tuple(int(v) for v in c[:3]))
        if nomes: d.text((6, 10 + j * (lado + 6)), nomes[j], fill='white', font=_f(14))
    return im
