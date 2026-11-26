# 3. O processo do autor

## 3.1 Colorizar sobre cinza
A maioria dos blocos é **um desenho em cinza colorizado com um único par matiz/saturação** (o Colorizar do Photoshop). Isso explica sozinho as "regras de croma":
- O croma é máximo na luminosidade HSL 0,5 (L ~0,64) e cai para as pontas.
- Os materiais escuros e médios ganham croma na luz; os claros perdem (desbotam ao sol).

| bloco | H | S | luminosidade HSL (mín / mediana / máx) |
|---|---|---|---|
| terra | 22 | 0,43 | 0,30 / 0,36 / 0,42 |
| areia | 46 | 0,54 | 0,72 / 0,78 / 0,81 |
| cascalho | 19 | 0,07 | 0,43 / 0,54 / 0,61 |
| argila | 223 | 0,11 | 0,58 / 0,65 / 0,85 |
| areia das almas | 31 | 0,26 | 0,43 / 0,58 / 0,72 |
| netherrack | 0 | 0,41 | 0,08 / 0,28 / 0,47 |
| arenito (lado) | 44 | 0,44 | 0,63 / 0,80 / 0,87 |
| tijolo de pedra | 177 | 0,04 | 0,31 / 0,60 / 0,83 |
| tijolo do Nether | 342 | 0,49 | 0,06 / 0,23 / 0,32 |
| quartzo | 51 | 0,14 | 0,81 / 0,90 / 0,94 |
| grama (topo) | 59 | 0,50 | 0,37 / 0,43 / 0,50 |
| pedra musgosa | 51 | 0,075 | |

## 3.2 Exceções: mapa de gradiente
Quando a saturação muda com a luz, ou a sombra puxa para outra matiz. É raro: a lã amarela e o ouro (sombra para o laranja, de 12 a 17°), as madeiras escuras (sombra avermelhada, de 17 a 21°), a lava (+26°) e o lápis (sombra mais violeta).

## 3.3 Montagem com peças
- Quando um bloco tem dois materiais, cada um recebe o seu Colorizar (tijolo e argamassa; grama e terra; pedra e minério).
- O autor reaproveita **tecidos-base**: os minérios são a pedra pixel a pixel com o minério por cima; as 16 lãs são o mesmo mapa de luz; todas as madeiras usam o mesmo desenho de tábua e de anel; o tijolo musgoso e o rachado são o tijolo de pedra com algo por cima.
- **Tudo se cita:** o couro do item é o couro da vaca holandesa, o cobertor da cama é a lã lima, a cabeça do golem de neve é a abóbora.
- **Regra:** um bloco novo do mesmo material nasce do tecido que já existe e só recebe o que é novo.

## 3.4 Duas linguagens
A superfície é **pintada** (degradê) e o objeto é feito em **cel** (3 a 5 tons chapados), como o minério sobre a pedra.
