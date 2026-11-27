# Índice do pacote (o repo é o pacote; 1.21.1, pack_format 34)

**Não listar tudo.** Para achar uma textura: `git ls-files assets | grep <nome>`. Caminhos seguem o vanilla: `assets/minecraft/textures/<pasta>/<nome>.png`.

## Conteúdo (PNG por pasta)
block 1145 · item 593 · entity 408 · particle 293 · gui 236 · mob_effect 35 · models/armor 15 · environment 6 · misc 3 · colormap 2 · font 1 · map 1. Mais blockstates, modelos de bloco/item e arquivos de partícula.

## Nomes que não são do vanilla
**Variações aleatórias de bloco** (blockstate com vários modelos; o número é a quantidade de variantes):
- stone 8 (`stone1` a `stone6` + `stone_fossil`) · dirt 9 (`dirt1` a `dirt6`, `dirt_worm1`, `dirt_worm2`) · sand 7 (`sand1` a `sand5`, `sand_face`) · soul_sand 8 (`soul_sand1` a `6`, `soul_sand_face`) · snow_block 8 (`snow1` a `6`, `snow_footprint`) · cobblestone 5 (`cobblestone1` a `4`) · stone_bricks 5 (`stone_bricks1` a `4`) · tuff_bricks 4 (`tuff_bricks1` a `3`) · deepslate_bricks 4 (`deepslate_bricks1` a `3`) · grass_block 2
- prismarine 10 (`prismarine1` a `9`) · prismarine_bricks 12 (`prismarine_bricks1` a `11`) · dark_prismarine 12 (`dark_prismarine1` a `10`, `dark_prismarine_coin`)
- bookshelf 15 (`bookshelf`, `bookshelf_2` a `bookshelf_15`)
- Variações de 25-11: dirt1–4, stone1–6, nether_wart_block1–4, mud1–4, coarse_dirt1–4, copper_ore1–3, iron_ore1–3, gold_ore1–2, diamond_ore1–3 (ver `docs/decisoes/blocos.md`).

**Modelos trocados:** `dripstone_block` vira `cube_bottom_top` (`dripstone_block_top` e `dripstone_block_bottom`); `soul_campfire` tem blockstate próprio; o cobre encerado (waxed_*) tem texturas próprias em vez de reaproveitar as do cobre.

**Partículas próprias** (`textures/particle/gm_*`, ligadas em `particles/*.json`):
- `gm_pontinho`: ash, white_ash, crimson_spore, warped_spore, underwater, dolphin, mycelium (com `gm_cruz`)
- `gm_cruz` (+ `gm_cruz_aberta`): glow, scrape, happy_villager, wax_off (com `gm_cera_x`)
- `gm_redstone` (12 quadros): dust, dust_color_transition · `gm_vaso`: dust_plume · `gm_po_caindo`: falling_dust
- `gm_fogueira`: campfire_cosy_smoke · `gm_sinal`: campfire_signal_smoke · `gm_sopro`: dragon_breath · `gm_puf`: poof
- `gm_portal`: portal, reverse_portal · `gm_pocao`: effect, entity_effect · `gm_magico`: enchanted_hit · `gm_critico`: crit · `gm_brilho_x`: electric_spark · `gm_bravo`: angry_villager
- `gm_bolha_p` / `gm_bolha_m`: bubble_column_up, current_down · `gm_estouro`: bubble_pop · `gm_ink`: squid_ink, glow_squid_ink · `gm_neve`: snowflake · `gm_pesca`: fishing · `gm_cuspe`: spit, wax_on (com `gm_mel`), nectar e esporo (com `gm_polen_x`)
- pingos `gm_pingo_{agua,lava,mel}_{pendurado,caindo,chao}` e `gm_gosma_{pendurada,caindo,chao}` (lágrima da obsidiana)

## Ainda vanilla (o jogo usa o padrão)
Lista de 25-11; o pacote de 26-11 já cobriu parte (empty_slot, light, water_overlay, estandartes e escudos, shulker, colete do lobo). Confirmar com `git ls-files` antes de afirmar que falta.
- **Blocos:** bell_side, bell_top, calibrated_sculk_sensor (3), campfire_fire, soul_campfire_fire, cracked_nether_bricks, honey_block (3), redstone_dust_overlay, spawner
- **Itens:** bundle_filled, spyglass_model
- **Entidades:** os gatos domésticos (all_black, british_shorthair, calico, jellie, persian, ragdoll, tabby, white, cat_collar), zombie_villager inteiro, `wolf_collar`, os skins de jogador, fishing_hook, guardian_beam, end_gateway_beam, evoker_fangs, llama/spit, conduit/wind, trident_riptide, as flechas espectral e com efeito e wind_charge
- **Outros:** pinturas (51), acabamentos de armadura (`trims`, 55), ícones do mapa (36), parte das partículas vanilla, parte dos sprites de interface

**Alternativa x variação** (não confundir):
- **Alternativa**: outra versão inteira da mesma textura, para o Gabriel testar no jogo e escolher a principal. Fica em `inbox/` como `<nome>_altN.png` (+ `.mcmeta` se animada); para testar, renomear e copiar por cima da principal. Não entra no blockstate.
- **Variação**: versões pequenas do mesmo bloco sorteadas pelo jogo (blockstate com `weight`), ex.: coarse_dirt1–4.
