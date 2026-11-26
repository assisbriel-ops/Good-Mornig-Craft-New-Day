# Decisões fechadas — Blocos

Uma linha por textura ou grupo, só quando o Gabriel disser que ficou pronto. O que está aqui não muda sem pedido.
Formato: `caminho(s)` · data · o que ficou (forma, cor e fonte da cor).

Regra das variações (25-11): toda variação = bloco principal intacto por baixo + detalhe por cima. Nenhum detalhe novo encosta na borda; pinta/pedrinha que atravessa a emenda fica.

- `block/dirt1–4` · 25-11 · terra principal + pedrinhas de 1 a 3 px (cinzas #705F57, #807169, #90837B do dirt5/6), sombra −6%. `dirt5`, `dirt6`, `dirt_worm1–2`: mesmo detalhe de antes, transplantado sobre a terra principal. Pesos sem mudança.
- `block/stone1–6`, `stone_fossil` · 25-11 · pedra principal com um dos dois estratos longos e marcas pequenas apagados (tons da própria stone), estratos novos (#808080–#8F8F8F), clastos de diorito (#C0C0C0, #B8B8B8, #A4A4A4, sombra −6%) e fissuras (#737373, #808080) em stone2 e stone5. Fóssil: concha recortada sobre a pedra principal. Pesos sem mudança (700/50).
- `block/granite1–4` · 25-11 · desenho anterior; só as pintas que encostavam na borda entraram 2 px. O granite principal ainda tem 4 pintas na borda (não mexido).
- `block/nether_wart_block1–4` · 25-11 · fundo laranja do principal sem pintas + 1 a 3 pintas espalhadas (moldes 3x3 e 2x2 com aro, recortados do principal). Blockstate novo: principal 4, variações 1.
- `block/mud1–4` · 25-11 · lama principal com 4 das 6 pedrinhas internas tiradas e 1 movida (mesmo contraste). Blockstate novo: 4/1.
- `block/coarse_dirt1–4` · 25-11 · 1 e 2 tiram 3 e 4 pedrinhas internas; 3 só com a pedrinha do meio; 4 sem as pedras da metade esquerda. Cor de preenchimento: tons de terra da própria coarse_dirt. Blockstate novo: 4/1.
- `block/copper_ore1–3` · 25-11 · pedaços do cobre principal (com sombra) reposicionados sobre a stone principal; o 3 sem o nódulo maior. Blockstate novo: 1/1.
- `block/iron_ore1–3`, `gold_ore1–2`, `diamond_ore1–3` · 25-11 · formatos novos desenhados (ferro menor e fragmentado; ouro em blocos com degrau; diamante com pontas, o 3 sem fragmentos). Cor = tons do minério principal na mesma proporção; luz do alto à direita; sombra na pedra −10% / −5% embaixo à esquerda. Blockstates novos: 1/1.
- `block/<cor>_candle(_lit)`, `item/<cor>_candle` (12 cores com matiz) · 26-11 · opção "clara": claridade da vela anterior (azul −6% para separar do azul-claro), matiz e 85% do croma da lã da mesma cor (5.3); desenho de luz da vela simples, croma cai na luz. Vela simples e neutras (branca, cinzas, preta) sem mudança de cor.
- `models/block/template_two/three/four_candles` + colunas 2–7 de todas as `block/*candle(_lit)` · 26-11 · cada vela do grupo usa a própria coluna (0, 2, 4, 6). Nas coloridas: col. 2 L −4%, h −3°, escorrido à esquerda; col. 4 L +3%, h +3°, faixa um tom abaixo; col. 6 L −2%, h −1°, escorrido longo à direita. Simples e neutras: coluna 0 copiada (iguais).
- `block/beehive_side`, `beehive_front`, `beehive_front_honey`, `beehive_end` · 26-11 · caixa pintada: tinta creme da colmeia anterior (L 0,84) com o fio do `stripped_birch_log` (deitado, só o fio, 90% de L/C/matiz) por baixo; peça unitária (cada ripa e o painel do topo com trecho próprio do grão e tom ±1%); luz de cima em cada ripa (4,5%) + luz geral alto-esquerda (2,5%); sombras mais quentes e 7% mais saturadas. Sulcos, alças, entrada, mel e moldura do topo iguais aos anteriores. ~150 cores.
