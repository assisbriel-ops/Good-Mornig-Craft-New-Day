# 5. Cor

## 5.1 Regras gerais
1. Cinzas puros na pedra, pedregulho, bedrock, carvão, ferro, neve, esqueleto, ghast e metais. As exceções do cânone são o tijolo de pedra (cinza levemente frio, h 191, C 0,011), o cascalho (cinza quente, h 47) e a pedra musgosa (esquentada).
2. **O brilho depende do material.** No metal e na gema, a luz perde saturação e vai para o branco. No orgânico, segue o Colorizar. Branco quase puro (L > 0,93) só em metal, gema, vidro e osso.
3. **Verde de planta:** h 104 a 122, C 0,08 a 0,14. Nunca frio e saturado ao mesmo tempo. As plantas não tingidas ficam na matiz da grama da selva (h 115).
4. **Saturação forte só no fogo, na luz e na energia:** redstone (C 0,186), blaze, pedra luminosa, lava.
5. **A temperatura conta história:** bicho de fazenda é quente (h 29 a 97); monstro de superfície é apagado (C ≤ 0,07); **violeta = sobrenatural, End e magia**; o vermelho é o acento de personagem (gravatas, lenço, capa); o vinho (h 3 a 4) é o Nether "de carne".
6. **O ciano da GM é verde-água** (h ~160), não azul-piscina.
7. **O beacon é a cor de iluminação da GM:** frio, verde-ciano (h ~204).

## 5.2 Princípios de colorização [decisão]
- A cor tem as suas próprias camadas (massa, motivo, grão). Não é uma capa por cima.
- **Pensar a substância:** de onde vem a cor (mineral, pigmento, poeira)? Onde há mais dela, há mais cor.
- Escurecer não é só baixar o valor: a sombra perde croma e pode derivar de matiz.
- **Nada de extremos:** dentro do "quente" existem pixels frios, neutros e dessaturados. Sutil.
- A pedra comum e a ardósia são **neutras**. Os derivados podem ganhar personalidade.

## 5.3 Dicionário das lãs (base de tudo o que é tingido)
| cor | sombra | média | luz |
|---|---|---|---|
| white | #BABABA | #D5D5D5 | #EEEEEE |
| silver | #777777 | #959595 | #B0B0B0 |
| gray | #444444 | #626262 | #7C7C7C |
| black | #1D1D1D | #343434 | #4E4E4E |
| brown | #59340D | #84531F | #A57037 |
| red | #701818 | #A22C2C | #C64343 |
| orange | #864719 | #BD6C30 | #DF8A4C |
| yellow | #CE8601 | #D89F11 | #E0B32A |
| lime | #566510 | #7F9521 | #9FB736 |
| green | #2C4E0C | #48751D | #629533 |
| cyan | #246A4A | #3D9C71 | #56BF8F |
| light_blue | #2862AD | #5188CF | #73A5E5 |
| blue | #2C4885 | #4B6CB2 | #6B8BD0 |
| purple | #532DA6 | #7752C7 | #9373DE |
| magenta | #A64FAF | #C873D0 | #DD90E6 |
| pink | #E36F6F | #ED9494 | #F5B4B4 |

- **[decisão]** A lã azul é usada em L 0,50 (h 264, C ~0,12), para se separar da azul-clara.
- As tintas (itens) seguem as lãs com croma maior.
- **Tingidos:** a mistura subtrativa (média geométrica da refletância em luz linear) entre o corante e o material. Com dose 0,30 o material manda; com 0,60 o corante manda. Os neutros ficam à parte, em escada igualmente espaçada. Ao recolorir uma família a partir de uma base, usar saturação proporcional para os neutros saírem cinza puro.

## 5.4 Madeiras
- **Escada das tábuas (L):** pinheiro e carvalho escuro 0,34; carvalho 0,46; acácia 0,51; selva 0,52; bétula 0,69. Madeira nova procura um degrau livre (há um buraco em ~0,40).
- Matizes: carvalho, pinheiro e bétula h 67 a 72; selva h 88; acácia h 42.
- A casca é ~0,05 mais escura e ~8° mais avermelhada que a tábua. O topo do tronco é mais claro e rosado, com anéis de alto contraste.
- Tudo o que é de madeira segue a tábua de carvalho (h 67 a 76). Moldura dos quadros: #8F6C47.
- Madeira com croma muito baixo lê como pedra ou aço (C 0,036 é o mínimo).

## 5.5 Metais, gemas e luz
| coisa | sombra | média | luz |
|---|---|---|---|
| lingote de ouro | #EBA700 | #EBBF3A | #EAC861 |
| pepita de ouro | #FAD05C | #FFE295 | #FCF4D8 |
| diamante | #63C1D6 | #9EE0F1 | #DBFAFF |
| esmeralda | #65A733 | #B5EE8D | #DDFFC2 |
| lingote de ferro | #686868 | #A6A6A6 | #BABABA |
| redstone | #AC232D | #D8352D | #E57830 |
| pó de pedra luminosa | #DE9F2A | #E5B132 | #E9BC36 |
| vara de blaze | #FF8C0D | #FFA23A | #FEBB71 |
| beacon | #54989E | | #D8EAEB |

- **Rampa de ouro:** #AB752F, #B48242, #B88A4D, #CA9635, #DD9E46, #E1AD4C, #E9BC36, #FEC044, #FED05E, #FFDF7A, #FEEB93.
- **Ferramentas da GM:** uma matiz por ferramenta, croma em platô e ~7 degraus de valor (o resto é ruído de ±1 RGB).

## 5.6 Folhagem
A GM pinta grama e folhas já em verde-amarelado: **cor final = textura × colormap**. Folhas de planície, floresta e selva em #A5AF30; taiga #79A638. Grama de selva #99A72A (final h 115). A bétula dourada é intencional.
