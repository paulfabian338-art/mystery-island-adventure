import unittest

from game import GameState, move, new_game


class GameTests(unittest.TestCase):
    def test_new_game_starts_at_origin_with_full_energy(self):
        state = new_game()
        self.assertEqual((state.x, state.y, state.energy), (0, 0, 10))
        self.assertEqual(state.status, "playing")

    def test_valid_move_changes_location_and_costs_energy(self):
        state = move(new_game(), "east")
        self.assertEqual((state.x, state.y, state.energy), (1, 0, 9))

    def test_move_is_case_insensitive(self):
        state = move(new_game(), "EAST")
        self.assertEqual((state.x, state.y), (1, 0))

    def test_invalid_direction_does_not_change_position_or_energy(self):
        state = move(new_game(), "northeast")
        self.assertEqual((state.x, state.y, state.energy), (0, 0, 10))
        self.assertIn("not a valid", state.message)

    def test_boundary_move_does_not_cost_energy(self):
        state = move(new_game(), "north")
        self.assertEqual((state.x, state.y, state.energy), (0, 0, 10))

    def test_rations_restore_energy_and_are_collected_once(self):
        state = GameState(x=0, y=2, energy=5)
        state = move(state, "east")
        self.assertEqual(state.energy, 7)
        state.energy = 4
        state = move(state, "west")
        state = move(state, "east")
        self.assertEqual(state.energy, 2)
        self.assertEqual(len(state.collected_rations), 1)

    def test_energy_is_capped_at_starting_maximum(self):
        state = GameState(x=0, y=2, energy=10)
        state = move(state, "east")
        self.assertEqual(state.energy, 10)

    def test_swamp_has_additional_energy_cost(self):
        state = GameState(x=2, y=1)
        state = move(state, "south")
        self.assertEqual(state.energy, 7)

    def test_reaching_treasure_wins(self):
        state = GameState(x=4, y=3, energy=2)
        state = move(state, "south")
        self.assertEqual(state.status, "won")

    def test_running_out_of_energy_loses(self):
        state = GameState(x=1, y=0, energy=1)
        state = move(state, "east")
        self.assertEqual(state.energy, 0)
        self.assertEqual(state.status, "lost")

    def test_finished_game_cannot_be_moved(self):
        state = GameState(status="lost", energy=0)
        result = move(state, "east")
        self.assertEqual((result.x, result.y, result.energy), (0, 0, 0))


if __name__ == "__main__":
    unittest.main()
