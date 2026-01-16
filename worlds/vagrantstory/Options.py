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


class IncludePuzzleModeChecks(Toggle):
    """An optional way to add puzzle mode checks to the game if you really hate yourself (DOES NOT WORK)"""

    display_name = "Include Puzzle Mode Checks"
    default = 0
    option_true = 1
    option_false = 0


class RoomSanityToggle(Toggle):
    """Include every room in the game as a check. If you have put on NG+ options, then it will include those as well."""

    display_name = "Roomsanity"
    default = 0
    option_true = 1
    option_false = 0


class IncludeNewGamePlusItems(Toggle):
    """Adds new game plus locations (rood inverse doors, extra bosses, etc)"""

    display_name = "New Game Plus Locations"
    default = 0
    option_true = 1
    option_false = 0


@dataclass
class VagrantStoryOption(PerGameCommonOptions):
    goal: GoalOption
    progression_option: ProgressionOption
    include_new_game_plus: IncludeNewGamePlusItems
    include_puzzle_mode_checks: IncludePuzzleModeChecks
    roomsanity: RoomSanityToggle
    deathlink: DeathLinkToggle
    guaranteed_items: GuaranteedItemsOption
