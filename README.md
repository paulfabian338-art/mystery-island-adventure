# Mystery Island Adventure

## Design decisions

- Keep the game rules in `game.py`; it has no terminal input or output. `main.py` owns the menu, prompts, display, and replay loop.
- Represent a location as `(x, y)` on a 5 by 5 grid. Moves are cardinal only; a move outside the island is rejected without using energy.
- The player starts at `(0, 0)` with 10 energy and wins by reaching the treasure at `(4, 4)`.
- A valid move normally costs 1 energy. The swamp at `(2, 2)` costs 2 additional energy. Rations at `(1, 2)` and `(3, 3)` restore 3 energy, up to the starting maximum, and are collected once.
- The game ends immediately on reaching the treasure or when energy reaches zero. These rules keep the adventure small and make movement, items, and outcomes straightforward to test.

## How to run

Requires Python 3.10 or later. From this directory, run:

```sh
python3 main.py
```

Choose **Play** from the menu, then enter `north`, `south`, `east`, or `west` to move. Enter `quit` during a game to return to the menu. The menu also has a rules option and a quit option. After a win or loss, the menu appears again so you can play another round.

## Rules

The island is a 5 by 5 grid. You start at `(0, 0)` with 10 energy and need to reach the treasure at `(4, 4)`. Each successful step costs 1 energy. Entering the swamp at `(2, 2)` costs 2 extra energy. Rations at `(1, 2)` and `(3, 3)` each restore 3 energy once, up to 10. Trying to leave the island or entering an invalid direction does not move or spend energy. Reach the treasure to win; reaching zero energy first means you lose.

## Limits

This is a small, text-only game with a fixed map, fixed item locations, and no saved progress. The player can see coordinates and energy, but there is no graphical map or random island generation. A run can be abandoned with `quit` from the movement prompt.
