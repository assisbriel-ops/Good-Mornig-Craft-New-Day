# Decisões fechadas — Interface e partículas

Formato: `caminho(s)` · data · o que ficou (forma, cor e fonte da cor). Só quando o Gabriel disser que ficou pronto.

- `gui/sprites/widget/scroller`, `scroller_background`, `container/villager/scroller(_disabled)`, `container/stonecutter/scroller(_disabled)` · 25-11 · rolagem vertical sempre no padrão do criativo: cápsula de 6 px nas cores do botão do criativo (#DFDED0 a #ADAC9A), nine-slice borda 4; trilho = linha de 2 px da madeira da lista −9%. Cortador de pedra = cópia exata do criativo.
- `gui/header_separator`, `footer_separator` · 25-11 · junta de madeira (linha clara da madeira do menu +6% em cima, escura −6% embaixo). Os `inworld_*` continuam vanilla.
- `gui/sprites/widget/text_field(_highlighted)` · 25-11 · mancha de nanquim (preto do frasco #202020–#3E3E3E, anel de tinta seca); focado +6%. Vale para todos os campos de texto dos menus. (No repo ficou a versão antiga, de propósito — ver STATUS.)
- `gui/recipe_book.png` · 25-11 · livro da GM (`gui/book.png`) espelhado, espiral do lado do inventário, 145x166 (3 px livres até o inventário); capa esquerda 2 px + 1 px de borda de página; 10 argolas encurtadas 2 px; cantoneiras de metal menores; margem esquerda da página num tom só para a aba emendar; brilho do papel limitado a L 0,92; pena da GM espelhada em sépia (lã marrom −45% sat.) no lugar da lupa; manchinha de nanquim atrás do número da página.
- `gui/sprites/recipe_book/tab(_selected)` · 25-11 · marcador de página recortado do papel do livro, 22 px de altura; aba de baixo −9% e parada na borda da 2ª página (fica na 3ª); aba escolhida emenda na página aberta.
- `gui/sprites/recipe_book/slot_*` · 25-11 · quadrado de 22 px, sombra marrom #3D2A21 translúcida (36%); "não dá" = mesma sombra a 58%; "várias" = segundo quadro deslocado 2 px.
- `gui/sprites/recipe_book/page_forward/backward(_highlighted)` · 25-11 · ponta da seta de página da GM cortada na haste, com a ponta cortada arredondada; mouse = versão escura da GM.
- `gui/sprites/recipe_book/filter_*`, `furnace_filter_*` · 25-11 · etiqueta no papel da página com sombra translúcida; grade (ou chama) de nanquim + visto de nanquim / X no vermelho da capa; mouse +4%.
- `gui/sprites/recipe_book/button(_highlighted)` · 25-11 · papel quadrado de 17 px (fundo dos efeitos de poção) com sombra translúcida; livro da GM na cor da capa do livro de receitas, sem fita, linhas da capa −8%; mouse +4%.
- Pendente: janelinha das variações (`overlay_recipe`, `crafting_overlay*`, `furnace_overlay*`) segue vanilla.
- `particle/cherry_0–11` · 26-11 · pétalas ovais de ponta cortada (mesmos 3 tamanhos e 3 cores; claro em cima-esquerda, escuro embaixo-direita).
- `gui/container/smithing`, `gui/sprites/container/smithing/error` · 26-11 · bancada de ferraria no metal da fornalha (painel, slots e grão dela); martelo da bigorna no canto esq.; ">" de nanquim da bigorna; resultado = elipse no chão copiada da fornalha; manequim em painel rebaixado (receita do beacon) em x 120–165, y 26–81, 3% mais escuro que os slots vazios (L 0,56); erro = X da bigorna. Ícones de slot vazio seguem como estão (decidir depois).
