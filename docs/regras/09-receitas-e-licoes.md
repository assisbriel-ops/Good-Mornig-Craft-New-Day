# 9. Receitas

## 9.1 Ordem de trabalho
Primeiro os materiais transversais (madeira, pedras), depois os lugares. Para cada grupo: inventário, papéis (chão, parede, acento), paleta do grupo, fontes de desenho, recolor por material, emenda, cena e triagem (só cor / cor + retoque / redesenho).

## 9.2 Três ferramentas de cor, nesta ordem
1. **Colorizar sobre cinza:** a estrutura em cinza; os níveis levando a mediana à luminosidade do material; o Colorizar com o par de um bloco parente; uma máscara por material. Conferir sempre em OKLCH.
2. **Mapa de gradiente:** quando a saturação muda com a luz ou a sombra deriva.
3. **Rampa da própria GM:** descrever a passagem do escuro ao claro, caçar na GM quem já faz isso (em entidades, itens ou partes pequenas), montar 6 a 15 cores, **mostrar a rampa como imagem** e repintar. Pode ser por transferência de valor (L novo = L alvo + (L − L médio) × ganho) ou escolhendo, para cada pixel, entre as 3 cores reais mais próximas. Os metais (C < 0,02) não são recoloridos.

## 9.3 Calibrar na cena
- O valor é sempre relativo ao vizinho.
- O material carrega um pouco do que está ao redor: o contraste não pode ser muleta.
- Um bloco de lugar escuro pede amplitude maior; um bloco iluminado de dia pede calma.

## 9.4 Conferência (a régua é a GM)
- Desvio de matiz de 1 a 3°; diferença entre vizinhos de ~0,02 a 0,05; de 0 a 5% de pixels isolados; emenda de 0,7 a 1,2; piso de 0,24 em coisa viva; alfa só 0 ou 255.
- Pranchas: **mosaico 3x3, cena, cena em preto e branco e vista de longe.** Sempre ampliado.

# 10. Lições

1. Medir em OKLCH, nunca em HSL.
2. Uma cor só, clareando em faixa uniforme, fica artificial. A vida vem da variação de croma.
3. A croma máxima mora no meio da escala, não no escuro.
4. Não descartar as variações de cor da fonte, senão a mão do desenho morre.
5. Não esticar o contraste por percentil.
6. Matiz pulando dentro de um material é o erro que a GM nunca comete.
7. A mesma base não é o mesmo carimbo: uma família fica coerente quando cada membro tem o seu desenho.
8. A irregularidade de tamanho dá vida.
9. Os neutros pedem cuidado próprio (saturação proporcional).
10. Transparência baixa apaga a cor.
11. **Bege ou creme na luz de um vermelho ou salmão lê como presunto:** comprimir a faixa de valor.
12. O branco "de máquina de lavar" denuncia. Linho, osso e bandagem pedem creme envelhecido.
13. **Rosa precisa de valor alto**, senão lê como salmão.
14. Girar pixel art com vizinho mais próximo quebra o desenho; usar cisalhamento por colunas.
15. Linhas de 1 px em objetos pequenos somem; usar 2 px.
16. Mover só a tinta de um desenho deixa fantasmas. Para deslocamentos pequenos, mover a faixa inteira com as bordas fundidas.
