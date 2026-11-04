"""Terminal menu and presentation for Mystery Island Adventure."""

from game import DIRECTIONS, GameState, move, new_game


def show_status(state: GameState) -> None:
    print(f"\nLocation: ({state.x}, {state.y}) | Energy: {state.energy}")
    print(f"Rations collected: {len(state.collected_rations)}/2")
    if state.message:
        print(state.message)


def play_game() -> None:
    state = new_game()
    print("\nYou are stranded on Mystery Island. Reach the treasure at (4, 4)!")
    print("Move with north, south, east, or west. Type quit to return to the menu.")

    while state.status == "playing":
        show_status(state)
        choice = input("Your move: ").strip().lower()
        if choice in {"quit", "q"}:
            return
        if choice not in DIRECTIONS:
            print("Choose north, south, east, west, or quit.")
            continue
        state = move(state, choice)

    show_status(state)
    if state.status == "won":
        print("You found the treasure and escaped the island. You win!")
    else:
        print("You have run out of energy. The island adventure is over.")


def main() -> None:
    while True:
        print("\n=== Mystery Island Adventure ===")
        print("1. Play")
        print("2. Rules")
        print("3. Quit")
        choice = input("Select an option: ").strip().lower()

        if choice in {"1", "play", "p"}:
            play_game()
        elif choice in {"2", "rules", "r"}:
            print("Reach (4, 4) before your energy runs out. Each move costs 1 energy;")
            print("the swamp at (2, 2) costs 2 extra. Rations at (1, 2) and (3, 3)")
            print("restore up to 3 energy each. Boundary bumps cost no energy.")
        elif choice in {"3", "quit", "q"}:
            print("Goodbye!")
            return
        else:
            print("Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
