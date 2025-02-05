import time
from settings_loader import CONFIG
from engine.time_engine import TimeController
from input.input_manager import InputManager
from ui.hud import HUD
from ui.menu import Menu
from world.world_manager import WorldManager
from engine.resource_manager import ResourceManager

def compute_delta_time(last_time):
    """Calculates the time difference between frames."""
    current_time = time.time()
    delta = current_time - last_time
    return delta, current_time

def main():
    """Main entry point for Arcane Empires."""
    print(f"⚡ Starting {CONFIG.get('game.title', 'Arcane Empires')} v{CONFIG.get('game.version', '1.0')}")

    # Graphics Configuration
    if CONFIG.get("graphics.fullscreen"):
        print("[INFO] Running in Fullscreen Mode")
    
    # Multiplayer Configuration
    if CONFIG.get("networking.enable_multiplayer"):
        print(f"[INFO] Multiplayer Enabled | Max Players: {CONFIG.get('networking.max_players', 4)}")

    # Cyberpunk Feature Checks
    if CONFIG.get("gameplay.hacking_system"):
        print("[INFO] Hacking Mechanics are ENABLED")

    if CONFIG.get("world.dynamic_time_cycle"):
        print("[INFO] Dynamic Day-Night Cycle ACTIVE")

    # Initialize Core Components
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
        
        # Process User Input
        input_manager.process_input()
        
        # Update Game State
        time_controller.update(delta_time)
        world_manager.update(delta_time)
        resource_manager.update(delta_time)
        
        # Render UI Elements
        hud.render()
        menu.render()

        # Exit Condition Based on User Input
        if input_manager.quit_requested:
            print("[INFO] Game Exit Requested. Shutting down...")
            game_running = False

    print("[GAME SHUTDOWN]")

if __name__ == "__main__":
    main()