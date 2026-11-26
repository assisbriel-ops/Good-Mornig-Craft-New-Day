# Textura GM (GoodMorning Craft) — Minecraft Java 1.21.1, pack_format 34

Este arquivo é o único que se lê sempre. **Todo o resto é consulta sob demanda:** abra só o arquivo (e a seção) do pedido. Não leia pastas inteiras, não liste `assets/` inteira, não baixe o zip do projeto (o pacote inteiro já está aqui no repo).

## Início de cada chat
1. Ler `STATUS.md` (curto).
2. Ir direto ao pedido. Só abrir o que a tabela abaixo manda para aquele tipo de trabalho.

## Onde está cada coisa (abrir só o necessário)
| preciso de… | abrir |
|---|---|
| a textura em si | `assets/minecraft/textures/<pasta>/<nome>.png` (achar com `ls` / `git ls-files \| grep nome`) |
| o que já foi decidido sobre ela | `grep -n "<nome>" docs/decisoes/*.md` (só a linha) |
| regra do material/assunto | o arquivo de `docs/regras/` do tema (lista abaixo); dentro dele, só a seção |
| fazer peça **nova** (não revisão) | `docs/metodo-producao.md` |
| o que é vanilla / nomes próprios do pacote | `docs/indice-pacote.md` |
| código (cor OKLCH, ajuste, pranchas) | `tools/gm_tools.py` → `sys.path.insert(0,'tools'); from gm_tools import *` |

`docs/regras/`: `01-principios-e-gm` · `03-processo` (colorizar, tabela H/S) · `04-estrutura` (motivos, luz, emenda, construídos) · `05-cor` (lãs, madeiras, metais, folhagem) · `06-entidades` · `07-itens-interface` · `08-lugares` (Nether, End, Sculk) · `09-receitas-e-licoes`.

## Regras de conversa (pedidos do Gabriel)
- Português, curto e objetivo. Diferenças em **porcentagem** (claridade e saturação); matiz pelo nome da cor.
- **Até 3 opções**, diferentes no que foi pedido, numeradas a partir de 1 a cada entrega (dois eixos: 1.1, 1.2). A atual sempre ao lado, marcada "atual".
- Durante as rodadas, só **uma prancha** de visualização (`prancha_revisao`, com cena ou slots). Olhar uma vez antes de enviar; problema pequeno → enviar e avisar.
- Opção aprovada vale como foi mostrada. Ajuste mexe **só no que foi pedido**. Não "corrigir" sem perguntar.
- **Nenhuma cor sai do nada:** toda cor vem de pixels da GM, e a fonte é dita junto.
- Pedido ambíguo: perguntar em uma linha.
- Desenho do Gabriel em 2 cores é um **mapa** para construir em cima, não para copiar.
- Fase atual: **revisão** (ajustar o que existe).

## Estilo em 5 linhas (o resto está em docs/regras)
- Pintada, sem contorno escuro, calma e clara. Matiz fixa dentro de cada material (1 a 3°). Cinza é cinza puro (C 0).
- Coisa viva não desce de L 0,24; itens não descem de L 0,30. Alfa só 0 ou 255.
- O valor é relativo ao vizinho: julgar na cena (bloco) ou no slot (item).
- Medir em OKLCH, nunca HSL.

## Ao terminar / quando o Gabriel aprovar
- Salvar a textura final no caminho certo em `assets/minecraft/textures/` (16x16 salvo outro tamanho combinado; `salvar()` força o alfa). Imagem sem lugar → `inbox/`.
- Aprovado ("ficou pronto"): **uma linha** em `docs/decisoes/<categoria>.md` (formato no topo do arquivo). Não registrar rodadas.
- Atualizar `STATUS.md` (curto: só mudar as listas, sem histórico longo) e fazer commit + push.
