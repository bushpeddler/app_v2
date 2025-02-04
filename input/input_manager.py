# Input Manager to Process User Inputs

class InputManager:
    def __init__(self):
        self.quit_requested = False

    def process_input(self):
        # Simplified input processing for demonstration purposes
        user_input = input("Enter command (type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            self.quit_requested = True

# Example usage:
if __name__ == '__main__':
    input_manager = InputManager()
    input_manager.process_input()
    if input_manager.quit_requested:
        print("Quit requested.")