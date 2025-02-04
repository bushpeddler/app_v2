# In-Game Resource Management

class ResourceManager:
    def __init__(self):
        self.resources = {
            "temporal_energy": 100,
            "currency": 50
        }

    def update(self, delta):
        # Update resources if needed (e.g., regeneration over time)
        pass

    def allocate_resource(self, resource, amount):
        if resource in self.resources:
            self.resources[resource] += amount

    def consume_resource(self, resource, amount):
        if resource in self.resources and self.resources[resource] >= amount:
            self.resources[resource] -= amount
            return True
        return False

# Example usage:
if __name__ == '__main__':
    manager = ResourceManager()
    print("Initial Resources:", manager.resources)
    manager.allocate_resource("currency", 10)
    print("After Allocation:", manager.resources)