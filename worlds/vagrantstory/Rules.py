from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState, Iterable


def has_key_required(self, location: str, state: CollectionState):
    return state.can_reach_location("Cleared: " + location, self.player)


def has_sigil_required(self, state: CollectionState):
    return state.has("Skill: Daring Dash", self.player)


def is_boss_defeated(self, boss: str, state: CollectionState):  # can used later
    return state.has("Boss: " + boss, self.player, 1)


def has_keyitems_required(self, items: list[str], state: CollectionState):
    passed_check = True
    for item in items:
        if state.has("Key Item: " + item, self.player, 1) is False:
            passed_check = False
    return passed_check
