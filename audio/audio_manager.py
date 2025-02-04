# Audio Manager for Music and Sound Effects

class AudioManager:
    def __init__(self):
        self.current_track = None

    def play_music(self, track):
        self.current_track = track
        print(f"Playing music: {track}")

    def stop_music(self):
        print("Music stopped.")
        self.current_track = None

    def play_sound_effect(self, effect):
        print(f"Playing sound effect: {effect}")

# Example usage:
if __name__ == '__main__':
    audio = AudioManager()
    audio.play_music("theme.mp3")
    audio.play_sound_effect("explosion.wav")