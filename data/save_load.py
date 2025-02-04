import json

# Save/Load Manager for Game States

class SaveLoadManager:
    def __init__(self, save_file='savegame.json'):
        self.save_file = save_file

    def save_game(self, game_state):
        with open(self.save_file, 'w') as f:
            json.dump(game_state, f)
        print("Game saved.")

    def load_game(self):
        try:
            with open(self.save_file, 'r') as f:
                game_state = json.load(f)
            print("Game loaded.")
            return game_state
        except FileNotFoundError:
            print("Save file not found.")
            return None

# Example usage:
if __name__ == '__main__':
    manager = SaveLoadManager()
    state = {"level": 1, "player_health": 100}
    manager.save_game(state)
    loaded_state = manager.load_game()
    print("Loaded State:", loaded_state)