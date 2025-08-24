import typing
from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Option, Range, Choice, ItemDict, DeathLink, PerGameCommonOptions

class GoalOptions():
    DEFEAT_FINAL_BOSS = 1

class ProgressionOptions():
    VANILLA = 0
    RANDOM = 1

class GuaranteedItemsOption(ItemDict):
    """Guarantees that the specified items will be in the item pool"""
    display_name = "Guaranteed Items"

class GoalOption(Choice):
    """Lets the user choose the completion goal
    Defeat Zarok - Beat the boss at the end
    Chalices - Collect all chalices (Collect all chalices doesn't work right now)"""
    display_name = "Completion Goal"
    default = GoalOptions.DEFEAT_FINAL_BOSS
    option_defeat_final_boss = GoalOptions.DEFEAT_FINAL_BOSS
    
class ProgressionOption(Choice):
    """Lets users choose how they wish to progress
    Vanilla - Plays the game like normal
    (Will only do Vanilla for now)"""
    display_name = "Game Progression Options"
    default = ProgressionOptions.VANILLA
    option_vanilla = ProgressionOptions.VANILLA
    
class DeathLinkToggle(Toggle):
    """Sets if you want deathlink or not"""
    display_name = "Death Link"
    default = 0
    option_true = 1
    option_false = 0

@dataclass
class MedievilOption(PerGameCommonOptions):
    goal: GoalOption
    progression_option: ProgressionOption
    deathlink: DeathLinkToggle
    guaranteed_items: GuaranteedItemsOption