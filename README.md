# snakes-ladders-game-system
Console-based Snakes and Ladders game with multi-player support (1-4), special tiles mechanics, turn-by-turn gameplay, and progressive complexity implementation using Python data structures and modular functions.
Implements progressive Python game development with modular architecture, multi-player support, special tile mechanics, and interactive gameplay featuring dynamic data structure evolution from lists to dictionaries with comprehensive input validation and turn-based control flow.

Support 1-4 players with dynamic list management and circular turn rotation.
Implement boundary enforcement preventing positions below 0 or above 100.
Apply immediate snake/ladder effects with index-based position mapping.
Integrate special tiles with random effects using external helper functions.

Approach

Modeled using progressive complexity methodology with seven distinct implementation phases.
Built modular function architecture with type hints and tuple/dictionary return types.
Implemented data structure migration from lists → tuples → nested dictionaries.
Applied external module integration with diceroll and helpers for game mechanics.
Structured using turn-based loop control with modular arithmetic for player cycling.

Phase 1-2: Foundation and Movement

Task: Establish basic game setup with dice-based movement mechanics.
Constraints: Two-player system, boundary checking, position display.
Input: Hardcoded player names and snake/ladder coordinates with dice integration.
Output: Updated player positions with movement validation.

Approach

Built static variable initialization for Red/Blue players with predefined game board.
Implemented boundary validation logic preventing movement beyond position 100.
Applied dice integration using external roll_the_dice() function calls.
Ensured efficient complexity:

Position Update: O(1) for boundary checking and dice application.
Movement Validation: O(1) for range checking with reversion logic.



Phase 3-4: Game Mechanics and Loop Control

Task: Implement snake/ladder effects with complete game loop and winner detection.
Constraints: Immediate position updates, parallel array indexing, continuous play until victory.
Implementation: Index-based lookups with while loop control and winner announcement.

Approach

Implemented parallel array indexing using snake_heads.index() for position mapping.
Used conditional position updates with if-elif-else structures for snake/ladder/normal moves.
Applied game loop termination with position-based winner detection at exactly 100.
Integrated move narration system with detailed action descriptions and effect announcements.

Phase 5: Multi-Player Architecture

Task: Support variable player count (1-4) with dynamic list management and turn rotation.
Constraints: Input validation, fair turn distribution, list modification based on player count.
Implementation: Dynamic deletion with modular arithmetic indexing for circular turns.

Approach

Built recursive input validation with range checking and error messaging for player count.
Implemented conditional list modification using del players[n:] operations based on player count.
Applied modular arithmetic turn cycling with i = (i+1) % len(players) for fair rotation.
Used position-based winner detection scanning for any player reaching position 100.

Phase 6: Function Modularization

Task: Refactor into modular functions with type hints and tuple-based data management.
Constraints: Type safety, immutable return types, clean separation of concerns.
Functions: initialise_game(), get_num_players(), update_players_positions_list(), play_game(), pick_winner().

Approach

Implemented tuple-based game initialization returning players, positions, snakes, ladders configuration.
Used recursive function design for input validation with automatic re-prompting on invalid entries.
Applied list slicing operations players[:-n] for dynamic player management based on count.
Integrated return-based winner detection scanning final positions array for value 100.

Phase 7: Advanced Dictionary Architecture

Task: Migrate to dictionary-based state with special tiles and interactive turn-by-turn gameplay.
Constraints: Nested dictionary management, string-to-integer conversion, dual gameplay modes.
Features: Special tile effects, interactive user control, comprehensive game state management.

Approach

Built nested dictionary structure with separate players, snakes, ladders, special_tiles sections.
Implemented string-to-integer key conversion using list comprehension for dictionary key processing.
Applied special dice mechanics with three distinct effects:

Effect 0: Extra turn using continue statement to skip turn increment.
Effect 1: Skip next player with i = ((i+2) % len(player)) double increment.
Effect 2: Multi-player penalty applying -5 position to all non-current players.


Integrated interactive turn control with roll/quit input validation and recursive error handling.

Special Mechanics Implementation

Boundary enforcement with position clamping: if positions[j] < 0: positions[j] = 0.
Index-based snake/ladder lookup using parallel arrays with snake_heads.index(position).
Special tile integration using generate_surprises() with random effect application.
Turn management with skip mechanics and extra turn processing via loop control.

Results

Implemented a seven-phase incremental development system demonstrating progressive software complexity.
Implemented multi-paradigm architecture evolution from procedural to functional with dictionary-based state management.
Both automatic and interactive gameplay modes documented with complete input validation and comprehensive error handling.

Author
Nashmia Shakeel
