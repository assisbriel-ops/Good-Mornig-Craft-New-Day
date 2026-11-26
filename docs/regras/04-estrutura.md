# 4. Estrutura (valor)

## 4.1 Três camadas
Todo bloco natural tem **base**, **massa** (manchas macias de 6 a 10 px, ladrilháveis), **motivo** (o gesto que identifica o material) e **grão** (variação de 1 px, baixa).

| material | motivo | polaridade | faixa (p10 a p90) |
|---|---|---|---|
| terra | nuvens claras + pintas escuras 2x2 (massa forte) | claro | 0,07 |
| areia | traços curtos inclinados "\\" (vento) | equilíbrio | 0,02 |
| pedra | traços horizontais escuros (estratos) | escuro | 0,06 |
| cascalho | pixel solto (o único com 16% de pixels isolados) | escuro | 0,09 |
| argila | bolhas claras de 3 px com 1 px de brilho | claro | |
| grama | grão de 2 px, massa diagonal | equilíbrio | 0,06 |
| neve | ondas horizontais longas | escuro suave | |
| areia das almas | cristas "/" com sulco escuro abaixo | relevo | |
| netherrack | bolhas redondas claras com fresta embaixo | relevo | 0,23 |

- Motivo escuro sobre fundo claro = rocha. Motivo claro = material macio.
- Fora o cascalho, cada pixel conversa com o vizinho (traço ou mancha, nunca sujeira): de 0 a 5% de pixels isolados.
- **A forma vem do desenho** (tijolos, tábuas, painéis), não do ruído.

## 4.2 Luz
| situação | luz |
|---|---|
| chão natural | frontal (sem gradiente) |
| muro e construído | de cima, dentro de cada peça |
| objeto em parede (minério) | alto à direita, com sombra projetada de 1 a 2 px embaixo à esquerda |
| item no slot | de cima, centralizada |
| entidade | sombra de contato, sem luz global |

## 4.3 Piso de escuridão
- Coisa viva não desce de L ~0,24. **O olho de mob é carvão** (#2F2F2F, L ~0,31), muitas vezes com 1 px de brilho.
- Os mobs "pretos" viram escuros coloridos: enderman vinho (#33262F), esqueleto wither ameixa (#423C45), morcego azul-marinho (#2F3046).
- Preto de verdade só em material preto por natureza: bedrock, carvão, manchas da vaca, gato preto, extremidades.

## 4.4 Emenda (continuidade)
- **Contínuo** (a emenda some, índice de 0,7 a 1,2): pedra, terra, grama, areia, cascalho, neve, netherrack, argila, folhas, tijolo, arenito.
- **Direcional:** tronco e tábua (contínuos na vertical), pedregulho, abóbora, feno.
- **Unitário por moldura:** lã (moldura de 0,13 a 0,17 mais escura), laje, bancada, topo do tronco, estante, talhados.
- **Unidade de 8 px:** os blocos de minério (2x2 painéis).
- Bloco de superfície é visto de longe, então a massa pensa no macro. Bloco de caverna é visto de perto, então motivo e grão pesam mais.

## 4.5 Construídos
- **Um sedimento calmo recortado em peças por uma junta forte.** O miolo da peça volta a ser calmo.
- **Junta clara** = argamassa, sempre neutra (C 0): tijolo (L 0,84), tijolo de pedra (0,81). **Junta escura** = fresta: pedregulho (0,47), tijolo do Nether (0,22).
- Aparelho: o tijolo tem fiadas de 3 + 1 px e peças de 7 + 1; o tijolo de pedra, fiadas de **4, 4 e 5 px** (desiguais, feito à mão) com uma **peça de acento mais escura**; o arenito é um trançado.
- Variação entre peças: à mão ~0,05; industrial ~0.
- **Polido** = o mesmo miolo do bruto + a **moldura simétrica da laje** (1 px escuro na borda, ~0,15 abaixo, e 1 px claro logo dentro, ~0,07 acima). Nada de chanfro direcional.
- **Talhado** = ornamento geométrico de traço de 1 px, em 2 ou 3 valores.
- Variantes vêm por cima: musgo pelas juntas, rachadura em X, sobre o mesmo arquivo de base.
