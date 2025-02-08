# PokemonQoLPatcher

### Pokemon QoL Patcher
* A tool to modify the Generation 3/4 games with various QoL tweaks such as not consuming the TM on use like Generation 5

### Setup to get this tool working
* Have one of the following ROMs
  * ----------- Gen 3 -----------
  * Pokemon - FireRed Version (USA, Europe) (Rev 1 works too)
  * Pokemon - LeafGreen Version (USA, Europe) (Rev 1 works too)
  * Pokemon - Emerald Version (USA, Europe)
  * Pokemon Colosseum (USA)
  * Pokemon XD - Gale of Darkness (USA)
  * ----------- Gen 4 -----------
  * Pokemon - Platinum Version (USA) (Rev 1 works too)
  * Pokemon - HeartGold Version (USA)
  * Pokemon - SoulSilver Version (USA)
* Navigate to the tab for the game you'd like to patch and select the ROM
* Please be patient when your ROM is being patched. It'll look like nothing is happening, but wait for the confirmation that it's done
* Have fun playing Pokemon Gen 3/4 with some QoL tweaks!

### Note for Gen 3
* It'll appear the TMs are limited, but this is purely visual. Just use the TM and it won't get consumed

### Why not Gen 1 and 2?
* I don't believe they're necessary for this project since FireRed/LeafGreen and HeartGold/SoulSilver exist
* Also, I don't know how to edit the ROMs for those games to support this

### Credits
* Credit to Pseurae for their code for modifying the Gen 4 games to not have TM usage and even making them behave as HMs in the bag
  * Platinum Code Link: https://gist.github.com/Pseurae/3c47b93bec10f9a1b1792466e26c456d
  * HeartGold/SoulSilver Code Link: https://gist.github.com/Pseurae/3ef6b0285966db6f389974f8be8ab4d1
* Credit to everybody who contributed to this repo for the Python library to extract and write the dol back to an ISO
  * Repo Link: https://github.com/pfirsich/gciso
* Credit to Stars and their amazing work modding XD and Colosseum (Used this tool to figure out the DOL offsets to edit and create the ips patch for PC anywhere)
  * Code is here: https://github.com/PekanMmd/Pokemon-XD-Code
* Credit to the various forum threads I've found to find the offsets to modify in the Gen 3/4 games
  * Emerald Infinite TMs: https://www.pokecommunity.com/threads/quick-research-development-thread.205158/page-20#post-7993745
  * FireRed Infinite TMs: https://www.pokecommunity.com/threads/solved-infinite-tm-usage-in-fire-red.420956/
  * LeafGreen Infinite TMs: https://www.pokecommunity.com/threads/unlimited-tm-usage-pokemon-leaf-green-usa.374831/
  * Gen 4 Disable Frame Limiter: https://www.pokecommunity.com/threads/d-p-pt-hg-ss-remove-the-framerate-limiter.378618/
  * Gen 3 Running Shoes Indoors: https://www.pokecommunity.com/threads/running-indoors-the-easy-way-fr-lg-r-s-e.291269/
  * FireRed/LeafGreen Evolve without National Dex: https://www.pokecommunity.com/threads/firered-pok%C3%A9dex-hacking.249530/
    * Had to find the offset for LeafGreen myself, but thankfully was pretty easy to find