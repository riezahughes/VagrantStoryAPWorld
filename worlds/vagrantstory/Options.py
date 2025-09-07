import typing
from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Option, Range, Choice, ItemDict, DeathLink, PerGameCommonOptions


class GoalOptions:
    DEFEAT_ANGEL = 1


class ProgressionOptions:
    VANILLA = 0
    RANDOM = 1


class GuaranteedItemsOption(ItemDict):
    """Guarantees that the specified items will be in the item pool"""

    display_name = "Guaranteed Items"


class GoalOption(Choice):
    """Lets the user choose the completion goal
    Defeat Final Boss - Beat the boss at the end"""

    display_name = "Completion Goal"
    default = GoalOptions.DEFEAT_ANGEL
    option_defeat_final_boss = GoalOptions.DEFEAT_ANGEL


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


class IncludeNewGamePlusItems(Toggle):
    display_name = "Include New Game Plus Items"
    default = 1
    option_true = 1
    option_false = 0


class IncludePuzzleModeChecks(Toggle):
    display_name = "Include Puzzle Mode Checks"
    default = 0
    option_true = 1
    option_false = 0


class IncludeMidBossChecks(Toggle):
    display_name = "Include Mini Bosses that hold keys/sigils as checks"
    default = 1
    option_true = 1
    options_false = 0


class AllDoorsUnlocked(Toggle):
    display_name = "All Doors Unlocked"
    default = 0
    option_true = 1
    option_false = 0


@dataclass
class VagrantStoryOption(PerGameCommonOptions):
    goal: GoalOption
    progression_option: ProgressionOption
    include_new_game_plus: IncludeNewGamePlusItems
    include_puzzle_mode_checks: IncludePuzzleModeChecks
    include_mid_boss_checks: IncludeMidBossChecks
    deathlink: DeathLinkToggle
    guaranteed_items: GuaranteedItemsOption
