# Game Menu System

class Menu:
    def __init__(self):
        self.options = ["Start Game", "Options", "Exit"]

    def render(self):
        # Render the main menu (console output as a placeholder)
        print("Main Menu:")
        for option in self.options:
            print(f" - {option}")

# Example usage:
if __name__ == '__main__':
    menu = Menu()
    menu.render()