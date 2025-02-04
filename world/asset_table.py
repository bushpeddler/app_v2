# Asset Management and Periodic Table

class Asset:
    def __init__(self, code, name, rarity, element, effect):
        self.code = code
        self.name = name
        self.rarity = rarity
        self.element = element
        self.effect = effect

class PeriodicTable:
    def __init__(self):
        self.assets = {}

    def add_asset(self, asset):
        self.assets[asset.code] = asset

    def get_asset(self, code):
        return self.assets.get(code)

# Example usage:
if __name__ == '__main__':
    table = PeriodicTable()
    asset1 = Asset("AT-01", "Emberstone", "Rare", "Fire", "Boosts attack power")
    table.add_asset(asset1)
    print(f"Asset Retrieved: {table.get_asset('AT-01').name}")