import time
from engine.time_engine import TimeController
from input.input_manager import InputManager
from ui.hud import HUD
from ui.menu import Menu
from world.world_manager import WorldManager
from engine.resource_manager import ResourceManager

def compute_delta_time(last_time):
    current_time = time.time()
    delta = current_time - last_time
    return delta, current_time

def main():
    # Initialize core components
    time_controller = TimeController()
    input_manager = InputManager()
    hud = HUD()
    menu = Menu()
    world_manager = WorldManager()
    resource_manager = ResourceManager()

    last_time = time.time()
    game_running = True

    while game_running:
        # Compute elapsed time since last frame
        delta_time, last_time = compute_delta_time(last_time)
        
        # Process user input
        input_manager.process_input()
        
        # Update game state
        time_controller.update(delta_time)
        world_manager.update(delta_time)
        resource_manager.update(delta_time)
        
        # Render UI elements
        hud.render()
        menu.render()

        # Exit condition based on user input
        if input_manager.quit_requested:
            game_running = False

if __name__ == '__main__':
    main()