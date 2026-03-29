import typing
from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Option, Range, Choice, ItemDict, DeathLink, PerGameCommonOptions


class GoalOptions:
    DEFEAT_ANGEL = 1


class ProgressionOptions:
    VANILLA = 0
    OPEN = 1


class ItemPoolDropOptions:
    VANILLA = 0
    HEAVY = 1


class ChainSkillUnlockOptions:
    VANILLA = 0
    SET = 1


class BreakArtUnlockOptions:
    VANILLA = 0
    SET = 1


class ItemRewardDropOptions:
    NOTHING = 0
    HEAL_HEAVY = 1
    RISK_HEAVY = 2


class NewGamePlusOptions:
    OFF = 0
    ON = 1
    IN_POOL = 2


class TeleportPoolOptions:
    OFF = 0
    ON = 1
    IN_POOL = 2


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
    Open - Allows you to start from a number of set positions"""

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


class ItemPoolDropOption(Choice):
    """
    There are two types of major choices for how you want the loot to go in the AP World
    - "Vanilla"  will give you the item pool from the original game.
    - "Heavy" will give you every possible combination of blades, weopons, gems and shields from the
    game as well as vanilla.

    Both options will use consumables for junk items.
    """

    display_name = "Basic Item Pool Choice"
    default = ItemPoolDropOptions.VANILLA
    option_vanilla = ItemPoolDropOptions.VANILLA
    option_heavy = ItemPoolDropOptions.HEAVY


class HeavyDropLimitOption(Range):
    """
    Sets the maxinum number of heavy drop items before you revert back to regular items for junk.
    """

    range_start = 0
    range_end = 200
    default = 20


class ChestItemChoices(Choice):
    """
    Select the kind of items you would like to be served from chests.
    Healing Heavy will provide:
    - 1 x Cure Bulb
    - 1 x Vera Root
    - 1 x Alchemist's Reagent

    Risk Heavy will provide:
    - 1 x Cure Root
    - 1 x Vera Bulb
    - 1 x Alchemist's Reagent
    """

    display_name = "Chest Item Rewards"
    default = ItemRewardDropOptions.HEAL_HEAVY
    option_healing_heavy = ItemRewardDropOptions.HEAL_HEAVY
    option_risk_heavy = ItemRewardDropOptions.RISK_HEAVY


class BossItemChoices(Choice):
    """
    Select the kind of items you would like to be served from boss encounters.
    Healing Heavy will provide:
    - 1 x Cure Bulb
    - 1 x Vera Root
    - 1 x Alchemist's Reagent

    Risk Heavy will provide:
    - 1 x Cure Root
    - 1 x Vera Bulb
    - 1 x Alchemist's Reagent
    """

    display_name = "Boss Item Rewards"
    default = ItemRewardDropOptions.HEAL_HEAVY
    option_healing_heavy = ItemRewardDropOptions.HEAL_HEAVY
    option_risk_heavy = ItemRewardDropOptions.RISK_HEAVY


class ChainSkillUnlockOptionChoice(Choice):
    """
    Set how you want to unlock chain skills.
    vanilla - As it was in the original game with the same values
    set - uses a set number per unlock instead, allowing for faster unlocking
    """

    display_name = "Chain Skill Unlock Option"
    default = ChainSkillUnlockOptions.SET
    option_vanilla = ChainSkillUnlockOptions.VANILLA
    option_set = ChainSkillUnlockOptions.SET


class CountPerChainUnlock(Range):
    """
    Set how much BP you need per chain ability unlock - Requires SET in Chain Skill Unlock Option
    """

    range_start = 1
    range_end = 50
    default = 20


class BreakArtUnlockOptionChoice(Choice):
    """
    Set how you want to unlock break arts.
    vanilla - As it was in the original game with the same values
    set - uses a set number per unlock instead, allowing for faster unlocking
    """

    display_name = "Break Art Unlock Option"
    default = BreakArtUnlockOptions.SET
    option_vanilla = BreakArtUnlockOptions.VANILLA
    option_set = BreakArtUnlockOptions.SET


class CountPerBreakUnlock(Range):
    """
    Set how many points needed per break art unlock - Requires SET in Break Skill Unlock Option
    """

    range_start = 1
    range_end = 50
    default = 15


class IncludePrologueToggle(Toggle):
    """Include Prologue checks. 3 simple checks for you going through the prologue if you want to."""

    display_name = "Include Prologue Checks"
    default = 0
    option_true = 1
    option_false = 0


class IncludeTimeTrialToggle(Toggle):
    """Include Time Trial Room Checks (DON'T TOUCH THIS, LEAVE IT ON, PLEASE.)"""

    display_name = "Include Time Trial Room and Boss Checks"
    default = 1
    option_true = 1
    option_false = 0


class IncludeTeleportSpellToggle(Choice):
    """Start the game with the teleport spell"""

    display_name = "Teleport Spell Toggle"
    default = TeleportPoolOptions.ON
    option_on = TeleportPoolOptions.ON
    option_off = TeleportPoolOptions.OFF
    option_inpool = TeleportPoolOptions.IN_POOL


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
    """Sets if you want deathlink or not"""

    display_name = "Death Link"
    default = 0
    option_true = 1
    option_false = 0


class IncludePuzzleModeChecks(Toggle):
    """An optional way to add puzzle mode checks to the game if you really hate yourself (NO IMPLIMENTATION YET)"""

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
    """Include every trap floor in the game as a check. If you have put on NG+ options, then it will include those as well."""

    display_name = "Panelsanity"
    default = 0
    option_true = 1
    option_false = 0


class NewGamePlusToggle(Choice):
    """
    Provides options to include the New Game + content in your run.
    ON: Provides you the Rood Inverse immediately allowing you to open all doors.
    OFF: Removes the ability to go into any ng+ content
    IN_POOL: Provides the Rood Inverse as an item pickup in your item pool.
    """

    display_name = "New Game Plus Settings"
    default = NewGamePlusOptions.IN_POOL
    option_on = NewGamePlusOptions.ON
    option_off = NewGamePlusOptions.OFF
    option_inpool = NewGamePlusOptions.IN_POOL


@dataclass
class VagrantStoryOption(PerGameCommonOptions):
    goal: GoalOption
    progression_option: ProgressionOption
    open_world_option: OpenWorldOption
    include_prologue: IncludePrologueToggle
    include_time_trial: IncludeTimeTrialToggle
    include_new_game_plus: NewGamePlusToggle
    include_puzzle_mode_checks: IncludePuzzleModeChecks
    item_drop_option: ItemPoolDropOption
    heavy_drop_limit: HeavyDropLimitOption
    chest_item_choices: ChestItemChoices
    boss_item_choices: BossItemChoices
    chain_skill_unlock_option: ChainSkillUnlockOptionChoice
    chain_skill_counter: CountPerChainUnlock
    break_art_unlock_option: BreakArtUnlockOptionChoice
    break_art_counter: CountPerBreakUnlock
    include_teleport: IncludeTeleportSpellToggle
    zero_mp_teleport: SetTeleportZeroCostToggle
    open_teleport_locations: OpenAllTeleportLocationsToggle
    roomsanity: RoomSanityToggle
    panelsanity: PanelSanityToggle
    deathlink: DeathLinkToggle
    guaranteed_items: GuaranteedItemsOption
