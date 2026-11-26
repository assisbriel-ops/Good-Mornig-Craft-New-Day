# 10 — Animação (pixel art, troca de quadros)

Consultar ao **criar ou revisar qualquer textura animada** (`.png.mcmeta`). Ferramenta: `tools/` + o roteiro descrito em "Como construir".

## 1. Princípios (o que faz a animação parecer viva e não "dançando")
- **Pensar em movimento antes de desenhar.** Primeiro decidir: o que fica preso (base, raiz, moldura), o que se move, para onde, quanto (em px) e em quantos quadros. Só depois desenhar a **pose neutra**.
- **Pose neutra + deslocamento.** Desenha-se uma pose só (a do meio do balanço) e os quadros saem dela por deslocamento de linhas/partes. Assim forma, cor e espessura são iguais em todos os quadros: nada "pisca".
- **Base presa, ponta solta.** A amplitude cresce da base para a ponta (curva, não reta: `(h/H)^1,4`). Base 0 px, ponta 2–3 px no máximo num bloco 16x16.
- **Atraso (follow-through / overlap).** A ponta chega depois da base: a fase atrasa com a altura. É isso que dá a sensação de água/vento empurrando, e não da planta mexendo sozinha.
- **Entrada e saída lentas.** Movimento senoidal: devagar nos extremos, rápido no meio. Nada de vai-e-volta com velocidade constante.
- **Arcos.** Ponta descreve curva, não linha reta.
- **Vizinho máx. 1 px.** Entre duas linhas vizinhas, a diferença de deslocamento é no máximo 1 px; senão o traço quebra.
- **Ritmo calmo.** Debaixo d'água mais lento que no ar. Laço de 3–4 s (ex.: 20 quadros × frametime 3–4). Tempo em ticks: 20 ticks = 1 s.
- **Laço sem costura.** O último quadro precisa levar ao primeiro (onda periódica).
- **Peças empilhadas.** Partes que se encaixam (kelp + kelp_plant; tall_seagrass top + bottom) são animadas **como uma peça só**, com o mesmo número de quadros e o mesmo frametime. Peça que se repete (kelp_plant) usa onda de período 16 linhas, para a emenda bater em qualquer altura.
- **Sub-pixel (opcional).** Para movimentos menores que 1 px: em vez de mover, trocar a cor de 1 pixel da borda por um tom intermediário (só tons já existentes na textura).
- **`"interpolate": true` no mcmeta:** só para mudança de cor/brilho (lava, portal, brilho). **Nunca** para movimento: mistura dois quadros e gera fantasma.

## 2. Como construir (roteiro)
1. Pose neutra 16x16 (cores da GM, regras normais).
2. Para cada linha `y`: deslocamento `round(A · peso(h) · sin(2π·t/F − atraso·h))`, onde `h` é a altura desde a base.
3. Peça repetível: `round(A · sin(2π(t/F + y/16)))`.
4. Conferir no GIF (cena com a superfície da água), não quadro a quadro.

## 3. Valores usados (aprovados ou em teste)
- Kelp / kelp_plant: onda subindo, A 1,5 px, 20 quadros, frametime 4.
- Seagrass: A 2 px, 20 quadros, frametime 3.
- Tall seagrass (top+bottom como 32 linhas): A 3 px, 20 quadros, frametime 3.
