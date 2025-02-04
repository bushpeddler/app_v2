# Narrative Engine for Branching Storylines

class NarrativeEngine:
    def __init__(self):
        self.story_state = {}

    def update_story(self, choice):
        # Update narrative state based on player choice
        self.story_state.update(choice)
        print("Narrative updated with:", choice)

    def get_current_narrative(self):
        return self.story_state

# Example usage:
if __name__ == '__main__':
    narrative = NarrativeEngine()
    narrative.update_story({"decision": "helped_villager"})
    print("Current Narrative:", narrative.get_current_narrative())