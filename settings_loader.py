import os
import yaml
import json
from importlib import import_module

class ConfigLoader:
    def __init__(self):
        self.config = {}
        self.load_config()

    def load_config(self):
        """Automatically detects and loads the available config file."""
        if os.path.exists("config.yaml"):
            self.load_yaml("config.yaml")
        elif os.path.exists("settings.json"):
            self.load_json("settings.json")
        elif os.path.exists("config.py"):
            self.load_python("config")
        else:
            print("[ERROR] No valid configuration file found!")
            exit(1)

    def load_yaml(self, file_path):
        """Loads configuration from a YAML file."""
        with open(file_path, "r") as file:
            self.config = yaml.safe_load(file)
        print(f"[INFO] Loaded settings from {file_path}")

    def load_json(self, file_path):
        """Loads configuration from a JSON file."""
        with open(file_path, "r") as file:
            self.config = json.load(file)
        print(f"[INFO] Loaded settings from {file_path}")

    def load_python(self, module_name):
        """Loads configuration from a Python file (config.py)."""
        module = import_module(module_name)
        self.config = getattr(module, "CONFIG", {})
        print(f"[INFO] Loaded settings from {module_name}.py")

    def get(self, key, default=None):
        """Retrieves a setting from the config dictionary."""
        keys = key.split(".")
        value = self.config
        for k in keys:
            value = value.get(k, default) if isinstance(value, dict) else default
        return value

# Create a global configuration object
CONFIG = ConfigLoader()