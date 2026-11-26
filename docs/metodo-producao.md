# Método de produção (só para peça NOVA; revisão não precisa deste arquivo)

Como construir uma textura para que saia com a mão da GM na primeira rodada. Código em `tools/gm_tools.py`. Obs.: as funções de molde e tecido (`tecido`, `laudo`, `caixa`, `mapa_uv`, `volume`, `prancha`) saíram da versão de revisão do `gm_tools`; se precisar, reescrever na hora a partir da descrição abaixo e adicionar ao arquivo.

## 0. O erro que mais custa rodadas
Gerar a imagem inteira por fórmula (ruído + cor) e só depois olhar. O resultado sai "dentro da régua" e sem vida, porque **não tem motivo**. A medida diz se algo está errado, nunca se está certo. Ordem:
1. **Achar o parente** na GM e medi-lo (`medir`, `rampa`).
2. **Desenhar o motivo** de propósito, pixel a pixel, em valor (cinza).
3. **Pôr massa e grão** por baixo, com amplitude copiada do parente.
4. **Colorir** com cor que já existe na GM (`colorizar`, `repintar`, `tingir`).
5. **Medir e olhar** antes de mostrar.

## 1. Achar e medir o parente
- O parente é o mais próximo **em substância**, não em cor. Solo das almas → areia das almas. Bloco de osso → item osso. Barril → tábua de pinheiro. Mel → pedra luminosa e rampa do ouro.
- Copiar dele: **faixa de valor**, **diferença mediana entre vizinhos** e **croma mediano**. A peça nova fica a até 20% desses números, salvo motivo dito.
- Referências (diferença entre vizinhos): pedra, terra, areia, lã e neve < 2,5%; entidades pintadas 1,5 a 2,1%; lingote de ouro 0,9%; lingote de ferro 3,1%; osso 4,2%.
- Dois materiais na textura: separar por máscara, ex. `rampa(a, 5, mascara=(lch(a)[1] > 0.05))`; por matiz, `abs(lch(a)[2] - 30) < 15`. Toda rampa é mostrada (`ver_rampa`).

## 2. Desenhar o motivo
- **Escrever o motivo numa frase antes de desenhar.** Se a frase não sai, falta conceito: perguntar ao Gabriel.
- Desenhar em grade de texto ou lista de formas (elipses `(cx, cy, rx, ry)` à mão, tamanhos desiguais), não em ruído. O acaso só na posição fina (±1 px) e no grão.
- **Ladrilho:** posicionar com `% 16`; nunca terminar forma exatamente na borda.
- Três valores bastam: face, sombra de baixo (fresta) e 1 px de luz no alto.
- Tamanho mínimo: 2 px para linha em objeto pequeno, 3 px para redondo, 5 px para ter luz e sombra.
- **Objeto (item, minério):** cel. Silhueta primeiro, conferida em preto chapado a 1x; depois 3 a 5 tons, borda 2% mais escura que o miolo, sem contorno.

## 3. Massa e grão
- Grão em **traços de 2 px**, nunca pixel solto. Direção: horizontal (estrato), diagonal (vento, cachos), vertical (pelo, veio).
- Amplitudes: chão calmo (areia) massa 0,010, grão 0,006; pedra e terra massa 0,03, grão 0,012; bicho liso grão ≤ 0,010; pelo curto grão 0,015 vertical.
- `mapa = motivo + massa`; o motivo pesa 2 a 4 vezes a massa. Testar várias seeds no mosaico 3x3; repetição diagonal denuncia o ladrilho.

## 4. Colorir
```python
c1 = colorizar(cinza, H=22, S=0.43, niveis=0.36)    # par de um parente (docs/regras/03-processo.md)
c2 = repintar(cinza, rampa(parente, 9))             # croma e matiz certos em cada valor
c3 = tingir(material, de_hex(['#A22C2C'])[0], 0.45) # tingidos: dose 0,30 a 0,60
c4 = ajustar(c2, dL=-0.03, kC=0.8)                  # "3% mais escuro, 20% menos saturado"
```
- `repintar` quando a sombra muda de matiz/croma (ouro, madeira escura, pele, fogo); `suave=False` para cel; `ganho` 0,75 acalma.
- **Neutros nunca passam por rampa colorida**; só `ajustar(dL=...)`.
- Escurecer = `ajustar(dL=-x, kC=0.9)`, nunca multiplicar RGB.

## 5. Bichos e moldes
1. Montar o mapa de caixas do modelo 1.21.1 (texOffs e tamanho de cada cubo) **antes de pintar** e conferir contra o vanilla: as faces devem cobrir exatamente os pixels opacos. Se não, os números estão errados.
2. Pintar por face: cor chapada por material → volume (dorso claro, flanco −13%, barriga escura; no quadrúpede a "frente" do UV do corpo é o dorso) → sombra de contato (2 linhas, −4% e −2%) → superfície → rosto por último.
3. Costuras: direita → frente → esquerda → trás formam faixa contínua; listras e barriga batem nas emendas e no topo.
4. Rosto: olho #2F2F2F + 1 px de brilho; expressão por sobrancelha e boca. Testar a 8x e a 1x.
5. Espelhamento: desenho assimétrico só em caixas não espelhadas.
6. Família (lobos, lhamas, gatos): guardar o mapa de valor aprovado como tecido-base e repintar com a rampa de cada pelagem, mudando as manchas.
7. Mostrar bicho de frente e de lado sobre grama, não a prancha plana.

## 6. Recortar e reaproveitar
- Molde de item: silhueta aprovada vira máscara da família (`repintar(lingote_ferro, rampa_do_metal)`, `suave=False`, 5 a 7 degraus).
- Peça sobre base: base intacta + peça em cel + sombra projetada de 1 a 2 px embaixo à esquerda (`ajustar(dL=-0.08)`), nunca preto.
- Recorte: fundir a borda com o vizinho de fora (borda dura lê como adesivo).
- Nunca interpolar ao redimensionar/girar (90° exatos ou cisalhamento por colunas).
- Antes de usar algo "da GM" como fonte, comparar com o vanilla 1.21.1 e o 1.8.

## 7. Conferir e mostrar
- Medir a peça **e o parente** e mostrar lado a lado. Isolados: pedra/terra/areia < 5%, cascalho/netherrack ~12%; alerta acima de 15%.
- Olhar a prancha antes de enviar e descrever em uma frase. "Parece ruído" ou "parece chapado" → refazer.
- As opções diferem **no motivo ou no conceito**, não em 2% de cor.

## 8. O que produzir para o projeto melhorar (por retorno)
1. Biblioteca de tecidos-base em cinza (pedra, terra, areia, tábua, lã, pelo curto/longo) em `tools/tecidos/`.
2. Dicionário de rampas (`rampa(…, 7)` nos ~60 materiais de referência) num documento só.
3. Moldes de UV prontos dos mobs que faltam (raposa, abelha, strider, tatu, morcego, gatos).
4. Cena-padrão fixa (grama, terra, pedra, tábua, areia, água).
5. Visualizador de mob de frente e de lado.
