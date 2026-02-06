import typing
from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Option, Range, Choice, ItemDict, DeathLink, PerGameCommonOptions


class GoalOptions:
    DEFEAT_ANGEL = 1


class ProgressionOptions:
    VANILLA = 0
    OPEN = 1


class OpenWorldOptions:
    MAGIC_HAMMER = 0
    JUNCTION_POINT = 1
    METAL_WORKS = 2
    GODHANDS = 3
    KEANES_CRAFT = 4
    WORK_OF_ART = 5


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
    option_open = ProgressionOptions.OPEN


class OpenWorldOption(Choice):
    """If you've chosen open world, then select how you would like to begin. You can start
    from any of the workshops. Alternatively, it can be randomized
    - Magic Hammer (Town City East)
    - Junction Point (Town City East)
    - Metal Works (Town City East)
    - GodHands (Undercity West)
    - Keane's Craft (The Keep)
    - Work of Art (Catacombs)
    - Random (any of them)
    """

    display_name = "Open World beginning choice"
    default = "random"
    option_magic_hammer = OpenWorldOptions.MAGIC_HAMMER
    option_junction_point = OpenWorldOptions.JUNCTION_POINT
    option_metal_works = OpenWorldOptions.METAL_WORKS
    option_godhands = OpenWorldOptions.GODHANDS
    option_keanes_craft = OpenWorldOptions.KEANES_CRAFT
    option_work_of_art = OpenWorldOptions.WORK_OF_ART


class IncludePrologueToggle(Toggle):
    """Include Prologue checks (May work? Not 100% sure. There's been a lot going on)"""

    display_name = "Include Prologue Checks"
    default = 0
    option_true = 1
    option_false = 0


class IncludeTeleportSpellToggle(Toggle):
    """Start the game with the teleport spell"""

    display_name = "Start With Teleport Spell"
    default = 0
    option_true = 1
    option_false = 0


class SetTeleportZeroCostToggle(Toggle):
    """The Teleport Spell will be Zero MP cost"""

    display_name = "Teleport has zero MP Cost"
    default = 0
    option_true = 1
    option_false = 0


class OpenAllTeleportLocationsToggle(Toggle):
    """Allow all teleport locations to be available"""

    display_name = "Teleport to any valid save point without finding it first."
    default = 0
    option_true = 1
    option_false = 0


class DeathLinkToggle(Toggle):
    """Sets if you want deathlink or not (DOES NOT WORK)"""

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


class PanelSanityToggle(Toggle):
    """Include every trap floor in the game as a check. If you have put on NG+ options, then it will include those as well. (DOES NOT WORK)"""

    display_name = "Panelsanity"
    default = 0
    option_true = 1
    option_false = 0


class NewGamePlusToggle(Toggle):
    """Adds new game plus locations (rood inverse doors, extra bosses, etc)"""

    display_name = "New Game Plus Locations"
    default = 0
    option_true = 1
    option_false = 0


@dataclass
class VagrantStoryOption(PerGameCommonOptions):
    goal: GoalOption
    progression_option: ProgressionOption
    open_world_option: OpenWorldOption
    include_prologue: IncludePrologueToggle
    include_new_game_plus: NewGamePlusToggle
    include_puzzle_mode_checks: IncludePuzzleModeChecks
    include_teleport: IncludeTeleportSpellToggle
    zero_mp_teleport: SetTeleportZeroCostToggle
    open_teleport_locations: OpenAllTeleportLocationsToggle
    roomsanity: RoomSanityToggle
    panelsanity: PanelSanityToggle
    deathlink: DeathLinkToggle
    guaranteed_items: GuaranteedItemsOption
