# Multiplayer Module for Networking (Optional)

class Multiplayer:
    def __init__(self):
        self.connected = False

    def connect(self, server_address):
        self.connected = True
        print(f"Connected to server at {server_address}")

    def send_data(self, data):
        if self.connected:
            print("Data sent:", data)

    def disconnect(self):
        self.connected = False
        print("Disconnected from server.")

# Example usage:
if __name__ == '__main__':
    multiplayer = Multiplayer()
    multiplayer.connect("127.0.0.1")
    multiplayer.send_data({"action": "move", "direction": "north"})
    multiplayer.disconnect()