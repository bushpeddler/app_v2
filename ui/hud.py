# Heads-Up Display (HUD)

class HUD:
    def __init__(self):
        self.health = 100
        self.temporal_energy = 100

    def render(self):
        # Render HUD elements (console output as a placeholder)
        print(f"HUD --> Health: {self.health} | Temporal Energy: {self.temporal_energy}")

# Example usage:
if __name__ == '__main__':
    hud = HUD()
    hud.render()