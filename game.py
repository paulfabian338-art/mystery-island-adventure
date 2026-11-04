"""Pure game rules for Mystery Island Adventure (no terminal I/O)."""

from dataclasses import dataclass, field

GRID_SIZE = 5
STARTING_ENERGY = 10
MAX_ENERGY = STARTING_ENERGY
TREASURE = (4, 4)
SWAMP = (2, 2)
SWAMP_EXTRA_COST = 2
RATION_ENERGY = 3
RATIONS = frozenset({(1, 2), (3, 3)})
DIRECTIONS = {
    "north": (0, -1),
    "south": (0, 1),
    "east": (1, 0),
    "west": (-1, 0),
}


@dataclass
class GameState:
    x: int = 0
    y: int = 0
    energy: int = STARTING_ENERGY
    collected_rations: set[tuple[int, int]] = field(default_factory=set)
    status: str = "playing"
    message: str = ""


def new_game() -> GameState:
    """Create a fresh game state."""
    return GameState()


def move(state: GameState, direction: str) -> GameState:
    """Apply one cardinal move and return the updated state.

    Invalid directions, moves after the game ends, and moves beyond the island
    leave the state unchanged except for a short explanatory message.
    """
    direction = direction.lower()
    if state.status != "playing":
        return state
    if direction not in DIRECTIONS:
        state.message = "That is not a valid direction."
        return state

    dx, dy = DIRECTIONS[direction]
    next_x, next_y = state.x + dx, state.y + dy
    if not (0 <= next_x < GRID_SIZE and 0 <= next_y < GRID_SIZE):
        state.message = "The island ends here; choose another direction."
        return state

    state.x, state.y = next_x, next_y
    cost = 1 + (SWAMP_EXTRA_COST if (next_x, next_y) == SWAMP else 0)
    state.energy -= cost
    state.message = f"You moved {direction}."

    if (next_x, next_y) in RATIONS and (next_x, next_y) not in state.collected_rations:
        state.collected_rations.add((next_x, next_y))
        state.energy = min(MAX_ENERGY, state.energy + RATION_ENERGY)
        state.message += " You found rations and restored energy."

    if (next_x, next_y) == TREASURE:
        state.status = "won"
        state.message = "You reached the treasure!"
    elif state.energy <= 0:
        state.energy = 0
        state.status = "lost"
        state.message = "You ran out of energy."
    return state
