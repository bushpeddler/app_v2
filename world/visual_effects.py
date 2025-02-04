# Visual Effects Module

class VisualEffects:
    @staticmethod
    def apply_shader(shader_name):
        print(f"Applying shader: {shader_name}")

    @staticmethod
    def play_particle_effect(effect_name):
        print(f"Playing particle effect: {effect_name}")

# Example usage:
if __name__ == '__main__':
    VisualEffects.apply_shader("glow")
    VisualEffects.play_particle_effect("sparkle")