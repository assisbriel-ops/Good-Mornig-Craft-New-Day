# STATUS do pacote (Minecraft Java 1.21.1)

**Baixar a versão mais nova:** aba *Releases* → "Versão mais nova" → MinhaTextura-1.21.1.zip

## ✅ Feito
- Estrutura do pacote criada
- 26/11: pacote unificado GM_25-11 subido (3305 arquivos): base 25-11 + efeitos, receitas e interface, estandartes e escudos, shulker (cores e concha), colete do cão de resgate, pendências (empty_slot, light, water_overlay), variações de blocos (coarse_dirt, mud, nether_wart_block, minérios, dirt/stone/granite) e pé de mirtilo.
- `entity/banner/base.png` e `widget/text_field` (+ `highlighted`) ficaram na versão antiga, de propósito.

- 26/11: couro de coelho com silhueta própria; ensopado de coelho só com as orelhas.
- 26/11: favo de mel (`item/honeycomb`) menor, 3 células.
- 26/11: colmeia artificial (`beehive_*`) refeita como caixa pintada com grão de bétula.
- 26/11: instruções reorganizadas para economizar tokens: `CLAUDE.md` curto + `docs/` (regras e decisões por assunto) + `tools/gm_tools.py` lendo direto do repo. O projeto no Claude não precisa mais do zip.
- 26/11: velas coloridas mais vivas (opção 1) + velas em grupo com variação (modelos `template_*_candles`).
- 26/11: plantas e chão: musgo com grão e granulado; lírio-do-vale com 1 flor; pétalas rosas ovais com miolo rosa + 3 variações (85/5/5/5); partículas da cerejeira ovais; líquen brilhante sem o quadrado + 3 variações + espiral rara (68/10/10/10/2).
- 26/11: tijolos de tufo e de ardósia com mais contraste + 3 variações cada.
- 26/11: tufo liso e ardósia lisa com moldura mais suave; ardósia lisa sem variação.
- 26/11: basalto liso refeito (vesículas, cinza aquecido do basalto).
- 26/11: pedra negra com topo igual à lateral e emenda limpa.
- 26/11: farejador (São Bernardo): grão + véu creme, manchas na cor do pelo, boca, junção cabeça/focinho e orelhas ajustadas.
- 26/11: fogueira e fogueira das almas: chamas próprias, toras acesas animadas por troca de quadros; fogo do bloco com ponta laranja e pontinhas (frametime 2).
- 26/11: aldeões do pântano, da savana e da selva refeitos a partir do aldeão base da planície.
- 26/11: piglins do Nether: bruto avermelhado (netherrack), zumbificado verde (pele do zumbi) sem terra nas patas, hoglin redesenhado com crina.

- 26/11: bancada de ferraria (`gui/container/smithing` + `sprites/container/smithing/error`): metal da fornalha, martelo e ">" da bigorna, elipse no resultado, painel rebaixado do manequim.

- 26/11: kelp ajustado (20 quadros, caule conectado); seagrass e tall_seagrass redesenhadas e reanimadas (regras em `docs/regras/10-animacao.md`).

- 27/11: arenitos: cinzelados (normal refeito a partir do vermelho, encaixe com o tijolo, topo com moldura), bases de peças grandes (`sandstone_bottom`, `red_sandstone_bottom`) e modelos novos `cut_sandstone`, `cut_sandstone_slab(_top)`, `chiseled_*`. Falta testar no jogo e o "ficou pronto".
- 27/11: ninho de abelha (`bee_nest_top`): topo novo em domo, claro no centro, emendando com a lateral.
- 27/11: cobre encerado (4 blocos inteiros) refeito: brilho metálico leve e largo, sem embranquecer; cada estágio sobre o seu cobre normal. Cortado, cinzelado, grade, lâmpada, porta e alçapão encerados ficaram como estavam.
- 27/11: obsidiana chorona (`block/crying_obsidian`) sem animação: ficou parada no quadro 1 (o mais brilhante); `.mcmeta` removido. Falta o "ficou pronto".
- 27/11: tear: topo girado (pano encaixa no pano da frente); atrás nova `block/loom_back` (prateleiras vazias, fundo com a madeira da bancada de cartografia) via modelo próprio `models/block/loom.json`; novelos só nas laterais. Falta testar no jogo e o "ficou pronto".
- 27/11: pepino-do-mar (`block/sea_pickle`) refeito no clima dos corais: verde-oliva +18%, poros suaves, fio de luz amarelo claro conectado (pedra luminosa + leque de coral-de-chifre). Ícone `item/sea_pickle` ainda o antigo. Falta testar no jogo e o "ficou pronto".
- 27/11: bolinha de experiência (`entity/experience_orb`) virou estrela âmbar com centro claro (5 tamanhos repetidos nos 11 níveis).
- 27/11: brilho de encantamento dos itens (`misc/enchanted_glint_item`, 128x128): 10 faixas verticais que passam da esquerda para a direita, rampa inteira do olho do Ender (#331C47 → #B49DC8), item sempre banhado (piso 25%) com frestas finas sem cor. Alternativa com o olho só até #9367BC em `inbox/`. Falta testar no jogo e o "ficou pronto".
- 27/11: cobre cortado (4 estágios) com grão no padrão GM + 4 variações sorteadas cada (normal e exposto ±3%; desgastado e oxidado só escurecem 3%). Aprovado. Cortados encerados com o grão novo + brilho, sem variação (de propósito).
- 27/11: portas e alçapões de cobre (4 estágios + encerados): grão bem leve, no nível da porta de ferro GM (fino ±0,6% + pintinhas raras ±2%), desenho igual; encerados com o mesmo brilho de antes. Lâmpada não mexida. Falta o "ficou pronto".

## 🔨 Em andamento
- 26/11: **revisão do bambu.** Feito: rampas (casca verde + descascado caqui, em `docs/decisoes/blocos.md`), tronco, folhas, bloco com casca, bloco descascado (redesenho), tábua (desenho próprio). Falta: broto (`bamboo_stage0`, ainda bege), mosaico (inspirado na pedra talhada GM), porta, alçapão, cerca/portão, andaimes, jangada/bote, placas, ícones. Alternativas para testar no jogo em `inbox/`.
- 26/11: menu do beacon (`gui/container/beacon` + `sprites/container/beacon/*`): papel do baú duplo, painéis rebaixados, pirâmides de blocos de minério, botões de madeira, escolhido = face do beacon, visto/X das lãs. Falta testar no jogo e o "ficou pronto".

- 26/11: gerador de montras (`block/spawner`): principal = opção com detalhes em cáqui nos cantos e no aro; alternativa cinza puro em `inbox/spawner_alt1.png`. Falta testar no jogo e o "ficou pronto".
- 26/11: tijolo do nether rachado (`block/cracked_nether_bricks`): desenho do Gabriel; só as 25 px abaixo de L 0,15 subiram para 0,15 (mesmo matiz e saturação). Falta testar no jogo e o "ficou pronto".

## 📋 Próximo
- Ícones de slot vazio da armadura (`empty_armor_slot_*`, também no inventário) em contorno marrom, diferente dos outros cinza pintados: Gabriel decide depois.
- Piglin bruto "sem uma orelha" no jogo: a textura tem as duas orelhas (iguais às do piglin); falta print para achar a causa.
- Zoglin: ainda é o desenho antigo do hoglin em marrom (sem crina, mancha borrada no dorso, disco de nariz, presas mais brancas que o osso GM). Decidir se segue o hoglin novo.
- Brilho de encantamento de armadura vestida, tridente e élitro (`misc/enchanted_glint_entity`) ainda é o vanilla: decidir se segue o dos itens.
- Conferir `colormap()` do `gm_tools`: para planície devolve #F5C300 (amarelo).

## 📥 Inbox (imagens soltas para organizar)
- `bamboo_block(_top)_alt2`, `stripped_bamboo_block(_top)_alt1`, `_alt2`: alternativas do bambu para testar no jogo (trocar pelos de `block/`).
- `kelp_alt1` + `kelp_plant_alt1` (kelp redesenhado) e `seagrass_alt1` (seagrass antiga ajustada), com `.mcmeta`: alternativas das algas para testar no jogo.
- `enchanted_glint_item_alt1`: alternativa do brilho de encantamento (olho do Ender só até o médio, mais perto do roxo conhecido) para testar no jogo (trocar por `misc/enchanted_glint_item`).
- `spawner_alt1`: alternativa do gerador de montras (cinza puro, sem o cáqui) para testar no jogo (trocar por `block/spawner`).
