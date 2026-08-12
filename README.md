# snakes-ladders-game-system

A console-based Snakes and Ladders game built up in seven incremental stages, each adding a layer of complexity and moving to a more appropriate data structure — from hardcoded variables to lists, then tuples, then nested dictionaries.

## Overview

The game itself is standard Snakes and Ladders: players roll a die, move forward that many spaces, land on a snake and slide back, land on a ladder and climb up, and the first to reach position 100 wins. Later stages add support for 1-4 players and special tiles with randomized effects.

Each `taskN.py` file is a self-contained stage of the same game, not separate features — later files supersede earlier ones in functionality.

## Task 1 — Setup (`task1.py`)

Hardcodes two players (Red, Blue) at position 0, along with fixed snake and ladder coordinates. No gameplay yet — just prints each player's starting position.

## Task 2 — Dice Movement (`task2.py`)

Adds a single dice roll per player (via `roll_the_dice()`), moves each player's position, and reverts the move if it would exceed 100. Still no snake/ladder logic and no win condition.

## Task 3 — Snake/Ladder Effects (`task3.py`)

Adds snake and ladder detection using parallel lists (`snake_heads.index()` to find the matching tail/top). Still only a single round for two players, no loop.

## Task 4 — Full Game Loop (`task4.py`)

Wraps movement and snake/ladder logic in a loop that alternates between two hardcoded players (Red, Blue) until one reaches exactly 100, then declares a winner.

## Task 5 — Variable Player Count (`task5.py`)

Extends the game to 1-4 players using parallel lists for names and positions, with input validation on player count and list slicing (`del players[n:]`) to trim the roster. Turn order cycles via `i = (i+1) % len(players)`.

## Task 6 — Modular Functions (`task6.py`)

Refactors Task 5's logic into named functions (`initialise_game`, `get_num_players`, `update_players_positions_list`, `play_game`, `pick_winner`) with type hints, returning a tuple of players/positions/snake/ladder data instead of relying on module-level globals.

## Task 7 — Dictionary State and Special Tiles (`task7.py`)

Migrates game state into a nested dictionary (`players`, `snakes`, `ladders`, `special_tiles`) and adds:
- **Special tiles** with three randomized effects (via `special_roll()`): an extra turn, skipping the next player, or moving every other player back 5 spaces (clamped at 0).
- **Two gameplay modes**: `play_game()` runs a full automatic 1-4 player game, and `turn_by_turn_gameplay()` runs an interactive 2-player (Red vs Blue) mode where each turn prompts the user to roll or quit.

Note: the snake/ladder coordinates differ between `task1.py`-`task4.py` (e.g. snake heads `[14, 24, 44, 65, 98]` then `[32, 48, 56, 63, 97]`) and `task5.py`-`task7.py` (`[25, 44, 65, 76, 99]`) — this is expected across the staged tasks, not an inconsistency to fix.

## Dependencies

- `diceroll.py` — provides `roll_the_dice()` and, from Task 7, `special_roll()` (not included in this upload)
- `helpers.py` — provides `generate_surprises()` for Task 7's special tile positions (not included in this upload)

## Project Structure

```
.
├── task1.py    # Hardcoded setup, no gameplay
├── task2.py     # Single dice roll, two players
├── task3.py      # Snake/ladder detection added
├── task4.py       # Full game loop, win condition
├── task5.py         # 1-4 player support via lists
├── task6.py           # Refactored into functions with type hints
├── task7.py             # Dictionary-based state, special tiles, interactive mode

```

## Author

Nashmia Shakeel
