<img src="docs/imgs/sandpiles.svg" alt="Sandpiles">

## Overview :eyes:

Single player board game based on the Abelian sandpile model.

### Rules :scroll:

- Single player game.
- Played on a generic *n* x *m* grid.
- Not all tiles are 'playable' (the grid can have unregular shapes).
- When __tapping__ on a tile, its number increases by one.
- A __tile value__ is an integer that ranges from 0 to game specific value __M__ (default: 4).
- When a tile value is equal or grater than M, the tile __topples__.
- A tile __adjacent tiles__ are the neighbors above, below, left and right.
- When a tile __topples__, its value is set to 0 and the adjacent tiles are incremented by 1. Toppling can be imagined
 as 4 stones sliding to the adjacent tiles.
- If one of the four adjacent tiles is not present, the increment get lost. For example when a tile on the top-left
 corner topples, the tiles below and on the left get incremented by one.
- The goal is to set every __target tile__ to its __target value__ using a limited number of moves.

## Worth mentioning :ear:

- Abelian sandpile model: https://en.wikipedia.org/wiki/Abelian_sandpile_model
- Inspirational video on Numberphile's YouTube channel:
https://www.youtube.com/watch?v=1MtEUErz7Gg