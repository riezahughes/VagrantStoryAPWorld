from enum import IntEnum
from typing import Optional, NamedTuple, Dict

from BaseClasses import Location, Region
from .Items import VagrantStoryItem
from .rooms import all_minor_regions


class VagrantStoryLocationCategory(IntEnum):
    FILLER = 0
    PROGRESSION = 1
    CHEST = 2
    BOSS = 3
    BOSS_PLUS = 4
    BOSS_UNLOCKS_PLUS = 5
    GRIMOIRE_UNLOCKS = 6
    KEY_UNLOCKS = 7
    SIGIL_UNLOCKS = 8
    ROOD_INVERSE_UNLOCKS = 9
    ABILITY_UNLOCKS = 10
    BREAK_UNLOCKS = 11
    FLOOR_TRAPS = 12
    PUZZLE_CLEAR = 13
    ROOM_ENTERED = 14
    GAME_END = 15


class VagrantStoryLocationData(NamedTuple):
    name: str
    default_item: str
    category: VagrantStoryLocationCategory


class VagrantStoryLocation(Location):
    game: str = "Vagrant Story"
    category: VagrantStoryLocationCategory
    default_item_name: str

    def __init__(
        self,
        player: int,
        name: str,
        category: VagrantStoryLocationCategory,
        default_item_name: str,
        address: Optional[int] = None,
        parent: Optional[Region] = None,
    ):
        super().__init__(player, name, address, parent)
        self.default_item_name = default_item_name
        self.category = category
        self.name = name

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 99350000
        region_offset = 1000
        table_order = ["Ashley", "Prologue", *all_minor_regions.keys(), "Credits"]

        output = {}
        for i, region_name in enumerate(table_order):
            current_region_base_id = base_id + (i * region_offset)
            # Ensure the region exists in location_tables
            if region_name in location_tables:
                # Enumerate the items within the current region, starting from current_region_base_id
                for j, location_data in enumerate(location_tables[region_name]):
                    # Assign an ID to each location within the region
                    # The ID for each location in a region will be current_region_base_id + j
                    print(f"{current_region_base_id + j}: {location_data.name}")
                    output[location_data.name] = current_region_base_id + j

        return output

        # return {location_data.name: (base_id + location_data.m_code) for location_data in location_tables["MainWorld"]}

    def place_locked_item(self, item: VagrantStoryItem):
        self.item = item
        self.locked = True
        item.location = self


# Gold shield ammo is used as a default. If you start picking up a lot, there's something wrong


# 1	    Wine Cellar
# 2     Catacombs
# 3     Sanctum
# 4     Abandoned Mines B1
# 5     Abandoned Mines B2
# 6     Limestone Quarry
# 7     Temple of Kiltia
# 8     Great Cathedral B1
# 9     Great Cathedral L1
# 10	Great Cathedral L2
# 11	Great Cathedral L3
# 12	Great Cathedral L4
# 13	Forgotten Pathway
# 14	Escapeway
# 15	Iron Maiden B1
# 16	Iron Maiden B2
# 17	Iron Maiden B3
# 18	unused (Town Center, but very different)
# 19	Undercity West
# 20	Undercity East
# 21	The Keep
# 22	City Walls West
# 23	City Walls South
# 24	City Walls East
# 25	City Walls North
# 26	Snowfly Forest
# 27	Snowfly Forest East
# 28	Town Center West
# 29	Town Center West
# 30	Town Center West
# 31	unused (Snowfly Forest)


# VagrantStoryLocationData("Key Unlock: Rood Inverse - To Undercity West", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS), NEED TO FIND WHERE THIS IS USED


location_tables = {
    "Ashley": [
        # Defence and Chain Ability Unlocks
        VagrantStoryLocationData("Ability: Heavy Shot", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Gain Life", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Mind Assault", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Gain Magic", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Raging Ache", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Mind Ache", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Temper", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Crimson Pain", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Instill", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Phantom Pain", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Paralysis Pulse", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Numbing Claw", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Dulling Impact", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Snake Venom", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Ward", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Siphon Soul", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Reflect Magic", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Reflect Damage", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Absorb Magic", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Absorb Damage", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Impact Guard", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Wind Break", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Fire Proof", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Terra Ward", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Aqua Ward", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Shadow Guard", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Demonscale", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Phantom Shield", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        # Grimoire Unlocks
        VagrantStoryLocationData("Grimoire: Degenerate", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Psychodrain", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Leadbones", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Tarnish", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Analyze", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Herakles", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Enlighten", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Invigorate", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Prostasia", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Luft Fusion", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Spark Fusion", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Soil Fusion", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Frost Fusion", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Aero Guard", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Pyro Guard", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Terra Guard", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Silence", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Magic Ward", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Surging Balm", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Fixate", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Dispel", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Stun Cloud", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Poison Mist", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Curse", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Restoration", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Antidote", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Blessing", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Clearance", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Unlock", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Eureka", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Drain Heart", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Drain Mind", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Heal", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Solid Shock", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Lightning Bolt", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Fireball", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Vulcan Lance", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Aqua Blast", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Spirit Surge", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Dark Chant", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Exorcism", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Banish", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        # Levelable Grimoires
        VagrantStoryLocationData("Grimoire: Explosion Max Level", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Thunderburst Max Level", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Flame Sphere Max Level", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Gaea Strike Max Level", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Avalanche Max Level", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Radial Surge Max Level", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        VagrantStoryLocationData("Grimoire: Meteor Max Level", "Vera Root", VagrantStoryLocationCategory.GRIMOIRE_UNLOCKS),
        # Break Skill Unlocks
        VagrantStoryLocationData("Break: Whistle Sting", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Shadoweave", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Double Fang", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Wyrm Scorn", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Rending Gale", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Vile Scar", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Cherry Ronde", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Papillon Reel", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Sunder", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Thunderwave", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Swallow Slash", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Advent Sign", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Mistral Edge", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Glacial Gale", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Killer Mantis", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Black Nebula", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Bear Claw", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Accursed Umbra", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Iron Ripper", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Emetic Bomb", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Sirocco", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Riskbreak", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Gravis Aether", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Trinity Pulse", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Bonecrusher", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Quickshock", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Ignis Wheel", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Hex Flux", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Ruination Polearm", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Scythe Wind", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Giga Tempest", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Spiral Scourge", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Brimstone Hail", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Heaven's Scorn", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Death Wail", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Sanctus Flare", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Lotus Palm", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Vertigo", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Vermillion Aura", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Retribution", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
    ],
    "Prologue": [
        VagrantStoryLocationData("PR - Prologue - Injured Wyvern Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        # two soldiers at start?
    ],
    # Wine Cellar
    "Entrance to Darkness": [
        VagrantStoryLocationData("WC - Entrance to Darkness Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Worker's Breakroom": [
        VagrantStoryLocationData("WC - Worker's Breakroom - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("WC - Worker's Breakroom Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Hall of Struggle": [
        VagrantStoryLocationData("WC - Hall of Struggle Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Smokebarrel Stair": [
        VagrantStoryLocationData("WC - Smokebarrel Stair - Gust Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("WC - Smokebarrel Stair - Chamomile Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.BOSS_UNLOCKS_PLUS),
        VagrantStoryLocationData("WC - Smokebarrel Stair Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Wine Guild Hall": [
        VagrantStoryLocationData("WC - Wine Guild Hall Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Wine Magnate's Chambers": [
        VagrantStoryLocationData("WC - Wine Magnate's Chambers - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("WC - Wine Magnate's Chambers Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Fine Vintage Vault": [
        VagrantStoryLocationData("WC - Fine Vintage Vault Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Chamber of Fear": [
        VagrantStoryLocationData("WC - Chamber of Fear Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Reckoning Room": [
        VagrantStoryLocationData("WC - The Reckoning Room - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("WC - The Reckoning Room", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "A Laborer's Thirst": [
        VagrantStoryLocationData("WC - A Laborer's Thirst Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Rich Drown in Wine": [
        VagrantStoryLocationData("WC - The Rich Drown in Wine Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Room of Rotten Grapes": [
        VagrantStoryLocationData("WC - Room of Rotten Grapes - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("WC - Room of Rotten Grapes - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("WC - Room of Rotten Grapes Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Blackmarket of Wines": [
        VagrantStoryLocationData("WC - Blackmarket of Wines - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        # This is a Boss Unlock in NG+. Not sure the best way to handle that
        VagrantStoryLocationData("WC - Blackmarket of Wines - Stock Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("WC - Blackmarket of Wines Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Gallows": [
        VagrantStoryLocationData("WC - The Gallows - Minotaur Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - The Gallows (Again) - Minotaur Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("WC - The Gallows (Again) - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("WC - The Gallows - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("WC - The Gallows Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Room of Cheap Red Wine": [
        VagrantStoryLocationData("WC - Room of Cheap Red Wine - Mandel Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - Room of Cheap Red Wine - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("WC - Room of Cheap Red Wine Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Room of Cheap White Wine": [
        VagrantStoryLocationData("WC - Room of Cheap White Wine - Zombie Fighter Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - Room of Cheap White Wine - Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - Room of Cheap White Wine - Ghoul Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - Room of Cheap White Wine Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Greedy One's Den": [
        VagrantStoryLocationData("WC - The Greedy One's Den Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Hero's Winehall": [
        VagrantStoryLocationData("WC - The Hero's Winehall - Dullahan Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - The Hero's Winehall - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("WC - The Hero's Winehall Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Undercity West
    "The Bread Peddler's Way": [
        VagrantStoryLocationData("UW - The Bread Peddler's Way Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Way of the Mother Lode": [
        VagrantStoryLocationData("UW - Way of the Mother Lode Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Sewer of Ravenous Rats": [
        VagrantStoryLocationData("UW - Sewer of Ravenous Rats - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - Sewer of Ravenous Rats Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Underdark Fishmarket": [
        VagrantStoryLocationData("UW - Underdark Fishmarket - Giant Crab Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("UW - Underdark Fishmarket Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Sunless Way": [
        VagrantStoryLocationData("UW - The Sunless Way - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - The Sunless Way Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Remembering Days of Yore": [
        VagrantStoryLocationData("UW - Remembering Days of Yore - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - Remembering Days of Yore Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Larder for a Lean Winter": [
        VagrantStoryLocationData("UW - Larder for a Lean Winter - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("UW - Larder for a Lean Winter Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Where the Hunter Climbed": [
        VagrantStoryLocationData("UW - Where the Hunter Climbed Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Hall of Poverty": [
        VagrantStoryLocationData("UW - Hall of Poverty Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Washing-Woman's Way": [
        VagrantStoryLocationData("UW - The Washing-Woman's Way - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - The Washing-Woman's Way - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Washing-Woman's Way - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Washing-Woman's Way Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Nameless Dark Oblivion": [
        VagrantStoryLocationData("UW - Nameless Dark Oblivion - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - Nameless Dark Oblivion Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Sinner's Corner": [
        VagrantStoryLocationData("UW - Sinner's Corner Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Fear of the Fall": [
        VagrantStoryLocationData("UW - Fear of the Fall - Dark Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("UW - Fear of the Fall Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Children's Hideout": [
        VagrantStoryLocationData("UW - The Children's Hideout - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("UW - The Children's Hideout Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Corner of Prayers": [
        VagrantStoryLocationData("UW - Corner of Prayers - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - Corner of Prayers Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Hope Obstructed": [VagrantStoryLocationData("UW - Hope Obstructed Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Beggars of the Mouthharp": [
        VagrantStoryLocationData("UW - Beggars of the Mouthharp - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - Beggars of the Mouthharp Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Corner of the Wretched": [
        VagrantStoryLocationData("UW - Corner of the Wretched Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Crossroads of Rest": [
        VagrantStoryLocationData("UW - Crossroads of Rest - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - Crossroads of Rest Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Path to the Greengrocer": [
        VagrantStoryLocationData("UW - Path to the Greengrocer Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Path of the Children": [VagrantStoryLocationData("UW - Path of the Children Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Salvation for the Mother": [
        VagrantStoryLocationData("UW - Salvation for the Mother - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - Salvation for the Mother - Diabolos Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - Salvation for the Mother - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - Salvation for the Mother Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Body Fragile Yields": [
        VagrantStoryLocationData("UW - The Body Fragile Yields - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - The Body Fragile Yields Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Bite the Master's Wounds": [
        VagrantStoryLocationData("UW - Bite the Master's Wounds Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Workshop 'Godhands'": [VagrantStoryLocationData("UW - Workshop 'Godhands' Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Crumbling Market (South)": [
        VagrantStoryLocationData("UW - The Crumbling Market (South) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Crumbling Market (North)": [
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData(
            "UW - The Crumbling Market (North) - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS
        ),
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Crumbling Market (North) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Where Flood Waters Ran": [
        VagrantStoryLocationData("UW - Where Flood Waters Ran Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Tears from Empty Sockets": [
        VagrantStoryLocationData("UW - Tears from Empty Sockets Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    # Undercity East
    "Hall to a New World": [VagrantStoryLocationData("UE - Hall to a New World Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Place of Free Words": [
        VagrantStoryLocationData("UE - Place of Free Words - Harpy Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("UE - Place of Free Words Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Bazaar of the Bizarre": [
        VagrantStoryLocationData("UE - Bazaar of the Bizarre - Lich Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("UE - Bazaar of the Bizarre Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Noble Gold and Silk": [
        VagrantStoryLocationData("UE - Noble Gold and Silk - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UE - Noble Gold and Silk Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Weapons Not Allowed": [
        VagrantStoryLocationData("UE - Weapons Not Allowed - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("UE - Weapons Not Allowed Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "A Knight Sells his Sword": [
        VagrantStoryLocationData("UE - A Knight Sells his Sword Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Gemsword Blackmarket": [
        VagrantStoryLocationData("UE - Gemsword Blackmarket - Nightstalker Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("UE - Gemsword Blackmarket Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Pirate's Son": [VagrantStoryLocationData("UE - The Pirate's Son Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Sale of the Sword": [
        VagrantStoryLocationData("UE - Sale of the Sword - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("UE - Sale of the Sword Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Undercity East (North Side)
    "The Greengrocer's Stair": [
        VagrantStoryLocationData("UEN - The Greengrocer's Stair - Neesa Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("UEN - The Greengrocer's Stair - Tieger Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("UEN - The Greengrocer's Stair Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Where Black Waters Ran": [
        VagrantStoryLocationData("UEN - Where Black Waters Ran Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Arms Against Invaders": [
        VagrantStoryLocationData("UEN - Arms Against Invaders Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Catspaw Blackmarket": [
        VagrantStoryLocationData("UEN - Catspaw Blackmarket - Diabolos Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UEN - Catspaw Blackmarket - Trap Clear Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UEN - Catspaw Blackmarket - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("UEN - Catspaw Blackmarket Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Town Centre South
    "Forcas Rise": [VagrantStoryLocationData("TCS - Forcas Rise Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Valdiman Gates": [VagrantStoryLocationData("TCS - Valdiman Gates Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Rue Aliano": [
        VagrantStoryLocationData("TCS - Rue Aliano - Mandrake Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("TCS - Rue Aliano Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The House Khazabas": [
        VagrantStoryLocationData("TCS - The House Khazabas - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("TCS - The House Khazabas Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Zebel's Walk": [VagrantStoryLocationData("TCS - Zebel's Walk Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Rue Volnac": [VagrantStoryLocationData("TCS - Rue Volnac Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Rue Faltes": [VagrantStoryLocationData("TCS - Rue Faltes Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Rue Morgue": [VagrantStoryLocationData("TCS - Rue Morgue Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # Town Centre East
    "Rue Lejour": [VagrantStoryLocationData("TCE - Rue Lejour Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Kesch Bridge": [VagrantStoryLocationData("TCE - Kesch Bridge Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Rue Crimnade": [
        VagrantStoryLocationData("TCE - Rue Crimnade - Cattleya Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("TCE - Rue Crimnade Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Workshop 'Junction Point'": [
        VagrantStoryLocationData("TCE - Workshop 'Junction Point' Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Rue Fisserano": [
        VagrantStoryLocationData("TCE - Rue Fisserano - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("TCE - Rue Fisserano Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Workshop 'Metal Works'": [
        VagrantStoryLocationData("TCE - Workshop 'Metal Works' Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Shasras Hill Park": [
        VagrantStoryLocationData("TCE - Shasras Hill Park - Bronze Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("TCE - Shasras Hill Park Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The House Gilgitte": [
        VagrantStoryLocationData("TCE - The House Gilgitte - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("TCE - The House Gilgitte Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Gharmes Walk": [
        VagrantStoryLocationData("TCE - Gharmes Walk - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("TCE - Gharmes Walk Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Plateia Lumitar": [
        VagrantStoryLocationData("TCE - Plateia Lumitar - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("TCE - Plateia Lumitar Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Towen Centre West
    "Rue Vermillion": [
        VagrantStoryLocationData("TCW - Rue Vermillion - Crimson Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("TCW - Rue Vermillion Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Rene Coastroad": [
        VagrantStoryLocationData("TCW - The Rene Coastroad - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("TCW - The Rene Coastroad Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Workshop 'Magic Hammer'": [
        VagrantStoryLocationData("TCW - Workshop 'Magic Hammer' Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Rue Mal Fallde": [VagrantStoryLocationData("TCW - Rue Mal Fallde Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Tircolas Flow (North)": [
        VagrantStoryLocationData("TCW - Tircolas Flow (North) - Duane Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("TCW - Tircolas Flow (North) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Tircolas Flow (South)": [
        VagrantStoryLocationData("TCW - Tircolas Flow (South) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Rue Bouquet": [VagrantStoryLocationData("TCW - Rue Bouquet Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Glacialdra Kirk Ruins": [
        VagrantStoryLocationData("TCW - Glacialdra Kirk Ruins - Rood Inverse Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("TCW - Glacialdra Kirk Ruins Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Rue Sant D'alsa": [VagrantStoryLocationData("TCW - Rue Sant D'alsa Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Dinas Walk": [VagrantStoryLocationData("TCW - Dinas Walk Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Villeport Way": [VagrantStoryLocationData("TCW - Villeport Way Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # The Keep
    "The Soldier's Bedding": [
        VagrantStoryLocationData("KEP - The Soldier's Bedding - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("KEP - The Soldier's Bedding Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "A Storm of Arrows": [
        VagrantStoryLocationData("KEP - A Storm of Arrows - Kalmia Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - A Storm of Arrows - Columbine Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - A Storm of Arrows Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Time Trial (Minotaur)": [
        VagrantStoryLocationData("KEP - Time Trial (Minotaur) - Minotaur Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Minotaur) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Time Trial (Dragon)": [
        VagrantStoryLocationData("KEP - Time Trial (Dragon) - Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Dragon) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Urge the Boy On": [
        VagrantStoryLocationData("KEP - Urge the Boy On - Anemone Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - Urge the Boy On - Verbena Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - Urge the Boy On Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Time Trial (Earth Dragon)": [
        VagrantStoryLocationData("KEP - Time Trial (Earth Dragon) - Earth Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Earth Dragon) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Time Trial (Snow Dragon)": [
        VagrantStoryLocationData("KEP - Time Trial (Snow Dragon) - Snow Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Snow Dragon) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "A Taste of the Spoils": [
        VagrantStoryLocationData("KEP - A Taste of the Spoils - Schirra Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - A Taste of the Spoils - Marigold Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - A Taste of the Spoils Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Time Trial (Damascus Golem)": [
        VagrantStoryLocationData("KEP - Time Trial (Damascus Golem) - Damascus Golem Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Damascus Golem) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Time Trial (Damascus Crab)": [
        VagrantStoryLocationData("KEP - Time Trial (Damascus Crab) - Damascus Crab Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Damascus Crab) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Wiping Blood from Blades": [
        VagrantStoryLocationData("KEP - Wiping Blood from Blades - Azalea Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - Wiping Blood from Blades - Tigertail Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - Wiping Blood from Blades Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Time Trial (Death + Ogre Zombie)": [
        VagrantStoryLocationData("KEP - Time Trial (Death + Ogre Zombie) - Death Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Death + Ogre Zombie) - Ogre Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Death + Ogre Zombie) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Time Trial (Asura)": [
        VagrantStoryLocationData("KEP - Time Trial (Asura) - Asura Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - Time Trial (Asura) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Warrior's Rest": [
        VagrantStoryLocationData("KEP - The Warrior's Rest - Rosencrantz Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("KEP - The Warrior's Rest - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("KEP - The Warrior's Rest Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Workshop 'Keane's Crafts'": [
        VagrantStoryLocationData("KEP - Workshop 'Keane's Crafts' Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Temple of Kiltia
    "The Dark Coast": [
        VagrantStoryLocationData("TOK - The Dark Coast - Trap Clear Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("TOK - The Dark Coast - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("TOK - The Dark Coast Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Hall of Prayer": [
        VagrantStoryLocationData("TOK - Hall of Prayer - Last Crusader Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("TOK - Hall of Prayer Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Those who Drink the Dark": [
        VagrantStoryLocationData("TOK - Those who Drink the Dark - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("TOK - Those who Drink the Dark Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Chapel of Meschaunce": [
        VagrantStoryLocationData("TOK - The Chapel of Meschaunce - Minotaur Lord Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("TOK - The Chapel of Meschaunce Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Resentful Ones": [
        VagrantStoryLocationData("TOK - The Resentful Ones - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("TOK - The Resentful Ones Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Those who Fear the Light": [
        VagrantStoryLocationData("TOK - Those who Fear the Light Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Chamber of Reason": [
        VagrantStoryLocationData("TOK - Chamber of Reason - Kali Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("TOK - Chamber of Reason Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Exit to City Center": [VagrantStoryLocationData("TOK - Exit to City Center Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # Snowfly Forest
    "The Faerie Circle": [VagrantStoryLocationData("SFF - The Faerie Circle Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Hunt Begins": [VagrantStoryLocationData("SFF - The Hunt Begins Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Which Way Home": [VagrantStoryLocationData("SFF - Which Way Home Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Giving Trees": [VagrantStoryLocationData("SFF - The Giving Trees Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Birds and the Bees": [
        VagrantStoryLocationData("SFF - The Birds and the Bees Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Wounded Boar": [VagrantStoryLocationData("SFF - The Wounded Boar Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Golden Egg Way": [VagrantStoryLocationData("SFF - Golden Egg Way Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Traces of the Beast": [VagrantStoryLocationData("SFF - Traces of the Beast Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Fluttering Hope": [VagrantStoryLocationData("SFF - Fluttering Hope Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Return to the Land": [VagrantStoryLocationData("SFF - Return to the Land Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Yellow Wood": [VagrantStoryLocationData("SFF - The Yellow Wood Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "They Also Feed": [VagrantStoryLocationData("SFF - They Also Feed Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Spirit Trees": [VagrantStoryLocationData("SFF - The Spirit Trees Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Where Soft Rains Fell": [
        VagrantStoryLocationData("SFF - Where Soft Rains Fell Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Forest River": [
        VagrantStoryLocationData("SFF - Forest River - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("SFF - Forest River - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("SFF - Forest River Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Lamenting to the Moon": [
        VagrantStoryLocationData("SFF - Lamenting to the Moon Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Running with the Wolves": [
        VagrantStoryLocationData("SFF - Running with the Wolves Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "You Are the Prey": [VagrantStoryLocationData("SFF - You Are the Prey Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Secret Path": [VagrantStoryLocationData("SFF - The Secret Path Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Hewn from Nature": [
        VagrantStoryLocationData("SFF - Hewn from Nature - Grissom Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("SFF - Hewn from Nature - Dark Crusader Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("SFF - Hewn from Nature - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("SFF - Hewn from Nature Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Wood Gate": [VagrantStoryLocationData("SFF - The Wood Gate Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Wolves' Choice": [VagrantStoryLocationData("SFF - The Wolves' Choice Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Woodcutter's Run": [VagrantStoryLocationData("SFF - The Woodcutter's Run Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Hollow Hills": [VagrantStoryLocationData("SFF - The Hollow Hills Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Howl of the Wolf King": [
        VagrantStoryLocationData("SFF - Howl of the Wolf King Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Silent Hedges": [VagrantStoryLocationData("SFF - The Silent Hedges Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # Snowfly Forest East
    "Steady the Boar-Spears": [
        VagrantStoryLocationData(
            "SFE - Steady the Boar-Spears - Rood Inverse Unlock", "Vera Root", VagrantStoryLocationCategory.ROOD_INVERSE_UNLOCKS
        ),
        VagrantStoryLocationData("SFE - Steady the Boar-Spears Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Boar's Revenge": [VagrantStoryLocationData("SFE - The Boar's Revenge Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Nature's Womb": [
        VagrantStoryLocationData("SFE - Nature's Womb - Damascus Crab Boss", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("SFE - Nature's Womb Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Sanctum
    "Prisoners' Niche": [VagrantStoryLocationData("SNC - Prisoners' Niche Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Corridor of the Clerics": [
        VagrantStoryLocationData("SNC - Corridor of the Clerics Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Priests' Confinement": [VagrantStoryLocationData("SNC - Priests' Confinement Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Alchemists' Laboratory": [
        VagrantStoryLocationData("SNC - Alchemists' Laboratory - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("SNC - Alchemists' Laboratory Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Academia Corridor": [
        VagrantStoryLocationData("SNC - The Academia Corridor Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Theology Classroom": [VagrantStoryLocationData("SNC - Theology Classroom Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Shrine of the Martyrs": [
        VagrantStoryLocationData("SNC - Shrine of the Martyrs Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Hallowed Hope": [VagrantStoryLocationData("SNC - Hallowed Hope Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Hall of Sacrilege": [
        VagrantStoryLocationData("SNC - Hall of Sacrilege - Golem Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("SNC - Hall of Sacrilege Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Advent Ground (South)": [
        VagrantStoryLocationData("SNC - Advent Ground (South) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Passage of the Refugees (South)": [
        VagrantStoryLocationData(
            "SNC - Passage of the Refugees (South) - Hall of Sacrilege Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS
        ),
        VagrantStoryLocationData("SNC - Passage of the Refugees (South) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Passage of the Refugees (North)": [
        VagrantStoryLocationData("SNC - Passage of the Refugees (North) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Advent Ground (North)": [
        VagrantStoryLocationData("SNC - Advent Ground (North) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Cleansing Chantry": [
        VagrantStoryLocationData("SNC - The Cleansing Chantry - Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("SNC - The Cleansing Chantry Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Stairway to the Light": [
        VagrantStoryLocationData("SNC - Stairway to the Light Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    # Limestone Quarry
    "Dark Abhors Light": [VagrantStoryLocationData("LQ - Dark Abhors Light Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Dream of the Holy Land": [
        VagrantStoryLocationData("LQ - Dream of the Holy Land - Water Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("LQ - Dream of the Holy Land - Aster Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("LQ - Dream of the Holy Land Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Ore Road": [VagrantStoryLocationData("LQ - The Ore Road Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Air Stirs": [
        VagrantStoryLocationData("LQ - The Air Stirs - Eulelia Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("LQ - The Air Stirs Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Bonds of Friendship": [
        VagrantStoryLocationData("LQ - Bonds of Friendship - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("LQ - Bonds of Friendship Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Atone for Eternity": [
        VagrantStoryLocationData("LQ - Atone for Eternity - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("LQ - Atone for Eternity Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Stair to Sanctuary": [VagrantStoryLocationData("LQ - Stair to Sanctuary Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Fallen Hall": [VagrantStoryLocationData("LQ - The Fallen Hall Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Rotten Core": [VagrantStoryLocationData("LQ - The Rotten Core Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Dreamer's Climb": [
        VagrantStoryLocationData("LQ - The Dreamer's Climb - Eulelia Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("LQ - The Dreamer's Climb - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("LQ - The Dreamer's Climb Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Ore-Bearers": [
        VagrantStoryLocationData("LQ - The Ore-Bearers - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("LQ - The Ore-Bearers Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Screams of the Wounded": [
        VagrantStoryLocationData("LQ - Screams of the Wounded Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Bacchus is Cheap": [VagrantStoryLocationData("LQ - Bacchus is Cheap Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Sinner's Sustenence": [VagrantStoryLocationData("LQ - Sinner's Sustenence Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Timely Dew of Sleep": [
        VagrantStoryLocationData("LQ - The Air Stirs - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("LQ - The Timely Dew of Sleep Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Companions in Arms": [
        VagrantStoryLocationData("LQ - Companions in Arms - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("LQ - Companions in Arms Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Auction Block": [
        VagrantStoryLocationData("LQ - The Auction Block - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("LQ - The Auction Block Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Ascension": [VagrantStoryLocationData("LQ - Ascension Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Where the Serpent Hunts": [
        VagrantStoryLocationData("LQ - Where the Serpent Hunts Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Drowned in Fleeting Joy": [
        VagrantStoryLocationData("LQ - Drowned in Fleeting Joy - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("LQ - Drowned in Fleeting Joy Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Ants Prepare for Winter": [
        VagrantStoryLocationData("LQ - Ants Prepare for Winter Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Laborer's Bonfire": [
        VagrantStoryLocationData("LQ - The Laborer's Bonfire - Melissa Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("LQ - The Laborer's Bonfire - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("LQ - The Laborer's Bonfire Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Stone and Sulfurous Fire": [
        VagrantStoryLocationData("LQ - Stone and Sulfurous Fire - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("LQ - Stone and Sulfurous Fire Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Torture Without End": [
        VagrantStoryLocationData("LQ - Torture Without End - Ogre Lord Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("LQ - Torture Without End Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Way Down": [VagrantStoryLocationData("LQ - Way Down Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Excavated Hollow": [
        VagrantStoryLocationData("LQ - Excavated Hollow - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("LQ - Excavated Hollow Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Parting Regrets": [VagrantStoryLocationData("LQ - Parting Regrets Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Corridor of Tales": [VagrantStoryLocationData("LQ - Corridor of Tales Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Dust Shall Eat the Days": [
        VagrantStoryLocationData("LQ - Dust Shall Eat the Days Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Hall of the Wage-Paying": [
        VagrantStoryLocationData("LQ - Hall of the Wage-Paying - Snow Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("LQ - Hall of the Wage-Paying Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Tunnel of the Heartless": [
        VagrantStoryLocationData("LQ - Tunnel of the Heartless Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    # Iron Maiden B1
    "The Cage": [VagrantStoryLocationData("IM1 - The Cage Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Cauldron": [
        VagrantStoryLocationData("IM1 - The Cauldron - Gargoyle Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - The Cauldron - Wraith Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - The Cauldron - Tearose Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("IM1 - The Cauldron Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Wooden Horse": [VagrantStoryLocationData("IM1 - Wooden Horse Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Starvation": [
        VagrantStoryLocationData("IM1 - Starvation - Wraith Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - Starvation - Mummy Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - Starvation Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Breast Ripper": [VagrantStoryLocationData("IM1 - The Breast Ripper Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Wheel": [
        VagrantStoryLocationData("IM1 - The Wheel - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("IM1 - The Wheel Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Branks": [
        VagrantStoryLocationData("IM1 - The Branks - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("IM1 - The Branks Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Pear": [VagrantStoryLocationData("IM1 - The Pear Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Judas Cradle": [
        VagrantStoryLocationData("IM1 - The Judas Cradle - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("IM1 - The Judas Cradle Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Whirlygig": [VagrantStoryLocationData("IM1 - The Whirlygig Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Spanish Tickler": [
        VagrantStoryLocationData("IM1 - Spanish Tickler - Wyvern Knight Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - Spanish Tickler Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Heretic's Fork": [
        VagrantStoryLocationData("IM1 - Heretic's Fork - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Heretic's Fork - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Heretic's Fork Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Chair of Spikes": [VagrantStoryLocationData("IM1 - The Chair of Spikes Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Blooding": [
        VagrantStoryLocationData("IM1 - Blooding - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Blooding - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Blooding Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Bootikens": [VagrantStoryLocationData("IM1 - Bootikens Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Burial": [
        VagrantStoryLocationData("IM1 - Burial - Iron Golem Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - Burial Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Burning": [
        VagrantStoryLocationData("IM1 - Burning - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Burning - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Burning Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Cleansing the Soul": [VagrantStoryLocationData("IM1 - Cleansing the Soul Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Ducking Stool": [
        VagrantStoryLocationData("IM1 - The Ducking Stool - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("IM1 - The Ducking Stool Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Garotte": [VagrantStoryLocationData("IM1 - The Garotte Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Hanging": [
        VagrantStoryLocationData("IM1 - Hanging - Steel Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("IM1 - Hanging Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Impalement": [
        VagrantStoryLocationData("IM1 - Impalement - Platinum Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("IM1 - Impalement Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Knotting": [
        VagrantStoryLocationData("IM1 - Knotting - Wyvern Queen Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - Knotting Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Iron Maiden B2
    "The Eunics' Lot": [VagrantStoryLocationData("IM2 - The Eunics' Lot Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Ordeal By Fire": [
        VagrantStoryLocationData("IM2 - Ordeal By Fire - Dark Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM2 - Ordeal By Fire Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Oven at Neisse": [VagrantStoryLocationData("IM2 - The Oven at Neisse Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Pressing": [
        VagrantStoryLocationData("IM2 - Pressing - Ravana Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM2 - Pressing Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Mind Burns": [
        VagrantStoryLocationData("IM2 - The Mind Burns - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - The Mind Burns - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - The Mind Burns Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Rack": [VagrantStoryLocationData("IM2 - The Rack Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Saw": [
        VagrantStoryLocationData("IM2 - The Saw - Dragon Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM2 - The Saw Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Cold's Bridle": [
        VagrantStoryLocationData("IM2 - The Cold's Bridle - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - The Cold's Bridle - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - The Cold's Bridle - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - The Cold's Bridle Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Shin-Vice": [
        VagrantStoryLocationData("IM2 - The Shin-Vice - Ogre Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM2 - The Shin-Vice - Death Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM2 - The Shin-Vice Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Spider": [VagrantStoryLocationData("IM2 - The Spider Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Lead Sprinkler": [
        VagrantStoryLocationData("IM2 - Lead Sprinkler - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("IM2 - Lead Sprinkler - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - Lead Sprinkler Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Squassation": [
        VagrantStoryLocationData("IM2 - Squassation - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("IM2 - Squassation - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - Squassation - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - Squassation Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    ## ////////////////////////////////////////////////////
    "The Strappado": [VagrantStoryLocationData("IM2 - The Strappado Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Thumbscrews": [VagrantStoryLocationData("IM2 - Thumbscrews Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Pendulum": [
        VagrantStoryLocationData("IM2 - Pendulum - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - Pendulum Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Dragging": [
        VagrantStoryLocationData("IM2 - Dragging - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - Dragging Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Strangulation": [VagrantStoryLocationData("IM2 - Strangulation Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Tablillas": [VagrantStoryLocationData("IM2 - Tablillas Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Tongue Slicer": [VagrantStoryLocationData("IM2 - Tongue Slicer Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Ordeal by Water": [VagrantStoryLocationData("IM2 - Ordeal by Water Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Brank": [VagrantStoryLocationData("IM2 - Brank Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Tormentum Insomniae": [VagrantStoryLocationData("IM2 - Tormentum Insomniae Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # Iron Maiden B3
    "The Iron Maiden": [
        VagrantStoryLocationData("IM3 - The Iron Maiden - Asura Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM3 - The Iron Maiden Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Judgement": [VagrantStoryLocationData("IM3 - Judgement Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Saint Elmo's Belt": [
        VagrantStoryLocationData("IM3 - Saint Elmo's Belt - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("IM3 - Saint Elmo's Belt Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Dunking the Witch": [
        VagrantStoryLocationData("IM3 - Dunking the Witch - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("IM3 - Dunking the Witch Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # The Great Cathedral L1
    "Into Holy Battle": [
        VagrantStoryLocationData("GC1 - Into Holy Battle Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Poisoned Chapel": [
        VagrantStoryLocationData("GC1 - The Poisoned Chapel - Laurel Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("GC1 - The Poisoned Chapel Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Sin and Punishment": [
        VagrantStoryLocationData("GC1 - Sin and Punishment - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC1 - Sin and Punishment - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC1 - Sin and Punishment Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # //////////////////////////////////////////
    "A Light in the Dark": [
        VagrantStoryLocationData("GC1 - A Light in the Dark - Arch Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GC1 - A Light in the Dark Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Monk's Leap": [
        VagrantStoryLocationData("GC1 - Monk's Leap - Lich Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GC1 - Monk's Leap Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Hieratic Recollections": [
        VagrantStoryLocationData("GC1 - Hieratic Recollections Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Flayed Confessional": [
        VagrantStoryLocationData("GC1 - The Flayed Confessional - Djinn Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GC1 - The Flayed Confessional - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("GC1 - The Flayed Confessional Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Cracked Pleasures": [VagrantStoryLocationData("GC1 - Cracked Pleasures Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Where Darkness Spreads": [
        VagrantStoryLocationData("GC1 - Where Darkness Spreads - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("GC1 - Where Darkness Spreads Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # The Great Cathedral B1
    "Struggle for the Soul": [
        VagrantStoryLocationData("GCB - Struggle for the Soul - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GCB - Struggle for the Soul Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Order and Chaos": [
        VagrantStoryLocationData("GCB - Order and Chaos - Marid Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GCB - Order and Chaos Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "An Offering of Souls": [VagrantStoryLocationData("GCB - An Offering of Souls Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Truth and Lies": [
        VagrantStoryLocationData("GCB - Truth and Lies - Ifrit Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GCB - Truth and Lies Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Sanity and Madness": [
        VagrantStoryLocationData("GCB - Sanity and Madness - Iron Crab Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GCB - Sanity and Madness Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Victor's Laurels": [VagrantStoryLocationData("GCB - The Victor's Laurels Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # The Great Cathedral L2
    "Free from Base Desires": [
        VagrantStoryLocationData("GC2 - Free from Base Desires Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Abasement from Above": [
        VagrantStoryLocationData("GC2 - Abasement from Above - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC2 - Abasement from Above - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC2 - Abasement from Above - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC2 - Abasement from Above Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Convent Room": [VagrantStoryLocationData("GC2 - The Convent Room Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Hall of Broken Vows": [
        VagrantStoryLocationData("GC2 - The Hall of Broken Vows - Acacia Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("GC2 - The Hall of Broken Vows - Flame Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GC2 - The Hall of Broken Vows Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Light and Dark Wage War": [
        VagrantStoryLocationData("GC2 - Light and Dark Wage War Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "An Arrow into Darkness": [
        VagrantStoryLocationData("GC2 - An Arrow into Darkness - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("GC2 - An Arrow into Darkness Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "He Screams for Mercy": [
        VagrantStoryLocationData("GC2 - He Screams for Mercy - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC2 - He Screams for Mercy - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC2 - He Screams for Mercy Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Acolyte's Weakness": [
        VagrantStoryLocationData("GC2 - The Acolyte's Weakness Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Maelstrom of Malice": [
        VagrantStoryLocationData("GC2 - Maelstrom of Malice - Lich Lord Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GC2 - Maelstrom of Malice Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Melodics of Madness": [
        VagrantStoryLocationData("GC2 - The Melodics of Madness - Palm Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("GC2 - The Melodics of Madness Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "What Ails You, Kills You": [
        VagrantStoryLocationData("GC2 - What Ails You, Kills You - Nightmare Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GC2 - What Ails You, Kills You Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # The Great Cathedral L3
    "The Wine-Lecher's Fall": [
        VagrantStoryLocationData("GC3 - The Wine-Lecher's Fall Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Heretics' Story (Lower)": [
        VagrantStoryLocationData("GC3 - The Heretics' Story (Lower) - Calla Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("GC3 - The Heretics' Story (Lower) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Heretics' Story (Upper)": [
        VagrantStoryLocationData("GC3 - The Heretics' Story (Upper) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Despair of the Fallen": [
        VagrantStoryLocationData("GC3 - Despair of the Fallen Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Hopes of the Idealist": [
        VagrantStoryLocationData("GC3 - Hopes of the Idealist - Dao Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GC3 - Hopes of the Idealist Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Where the Soul Rots": [VagrantStoryLocationData("GC3 - Where the Soul Rots Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # The Great Cathedral L4
    "The Atrium": [VagrantStoryLocationData("GC4 - The Atrium Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # The Great Cathedral Dome
    "Dome": [
        VagrantStoryLocationData("GCD - Dome - Guildenstern Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GCD - Dome Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Paling": [
        VagrantStoryLocationData("GCD - Paling - Guildenstern Apotheos Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GCD - Paling Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Forgotten Pathway
    "Stair to the Sinners": [VagrantStoryLocationData("FP - Stair to the Sinners Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Slaughter of the Innocent": [
        VagrantStoryLocationData("FP - Slaughter of the Innocent - Damascus Golem Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("FP - Slaughter of the Innocent Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Oracle Sins No More": [
        VagrantStoryLocationData("FP - The Oracle Sins No More - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("FP - The Oracle Sins No More - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("FP - The Oracle Sins No More Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Fallen Knight": [
        VagrantStoryLocationData("FP - The Fallen Knight - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("FP - The Fallen Knight Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Awaiting Retribution": [
        VagrantStoryLocationData("FP - Awaiting Retribution - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("FP - Awaiting Retribution Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Escapeway
    "Shelter From the Quake": [
        VagrantStoryLocationData("ESC - Shelter From the Quake - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("ESC - Shelter From the Quake - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("ESC - Shelter From the Quake Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Buried Alive": [
        VagrantStoryLocationData("ESC - Buried Alive - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("ESC - Buried Alive Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Movement of Fear": [VagrantStoryLocationData("ESC - Movement of Fear Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Facing Your Illusions": [
        VagrantStoryLocationData("ESC - Facing Your Illusions - Diabolos Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("ESC - Facing Your Illusions Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Darkness Drinks": [VagrantStoryLocationData("ESC - The Darkness Drinks Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Fear and Loathing": [
        VagrantStoryLocationData("ESC - Fear and Loathing - Ifrit Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("ESC - Fear and Loathing - Marid Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("ESC - Fear and Loathing Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Blood and The Beast": [
        VagrantStoryLocationData("ESC - Blood and The Beast - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("ESC - Blood and The Beast Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Where Body and Soul Part": [
        VagrantStoryLocationData("ESC - Where Body and Soul Part - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("ESC - Where Body and Soul Part Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # City Walls West
    "Students of Death": [
        VagrantStoryLocationData("CWW - Students of Death - Crimson Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("CWW - Students of Death Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Gabled Hall": [VagrantStoryLocationData("CWW - The Gabled Hall Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Where the Master Fell": [
        VagrantStoryLocationData("CWW - Where the Master Fell Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    # City Walls South
    "In Wait of the Foe": [VagrantStoryLocationData("CWS - In Wait of the Foe Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Swords for the Land": [VagrantStoryLocationData("CWS - Swords for the Land Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Weeping Boy": [VagrantStoryLocationData("CWS - The Weeping Boy Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Where Weary Riders Rest": [
        VagrantStoryLocationData("CWS - Where Weary Riders Rest Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Boy's Training Room": [
        VagrantStoryLocationData("CWS - The Boy's Training Room Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    # City Walls North
    "From Squire to Knight": [
        VagrantStoryLocationData("CWN - From Squire to Knight - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("CWN - From Squire to Knight Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Traces of Invasion Past": [
        VagrantStoryLocationData("CWN - Traces of Invasion Past Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Be for Battle Prepared": [
        VagrantStoryLocationData("CWN - Be for Battle Prepared Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Destruction and Rebirth": [
        VagrantStoryLocationData("CWN - Destruction and Rebirth Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "From Boy to Hero": [
        VagrantStoryLocationData("CWN - From Boy to Hero - Clematis Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("CWN - From Boy to Hero Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "A Welcome Invasion": [VagrantStoryLocationData("CWN - A Welcome Invasion Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # City Walls East
    "Train and Grow Strong": [
        VagrantStoryLocationData("CWE - Train and Grow Strong - Rood Inverse Unlock", "Vera Root", VagrantStoryLocationCategory.ROOD_INVERSE_UNLOCKS),
        VagrantStoryLocationData("CWE - Train and Grow Strong Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Squire's Gathering": [
        VagrantStoryLocationData("CWE - The Squire's Gathering Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Invaders are Found": [
        VagrantStoryLocationData("CWE - The Invaders are Found Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Dream Weavers": [VagrantStoryLocationData("CWE - The Dream Weavers Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Cornered Savage": [VagrantStoryLocationData("CWE - The Cornered Savage Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # Catacombs
    "Hall of Sworn Revenge": [
        VagrantStoryLocationData("CAT - Hall of Sworn Revenge - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("CAT - Hall of Sworn Revenge - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("CAT - Hall of Sworn Revenge Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Last Blessing": [VagrantStoryLocationData("CAT - The Last Blessing Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Weeping Corridor": [
        VagrantStoryLocationData("CAT - The Weeping Corridor - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("CAT - The Weeping Corridor Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Persecution Hall": [VagrantStoryLocationData("CAT - Persecution Hall Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Rodent-Ridden Chamber": [
        VagrantStoryLocationData("CAT - Rodent-Ridden Chamber - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("CAT - Rodent-Ridden Chamber Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Shrine to the Martyrs": [
        VagrantStoryLocationData("CAT - Shrine to the Martyrs Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Lamenting Mother (West)": [
        VagrantStoryLocationData("CAT - The Lamenting Mother (West) - Ghost Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("CAT - The Lamenting Mother (West) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Lamenting Mother (East)": [
        VagrantStoryLocationData("CAT - The Lamenting Mother (East) - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("CAT - The Lamenting Mother (East) Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Hall of Dying Hope": [VagrantStoryLocationData("CAT - Hall of Dying Hope Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Bandits' Hideout": [
        VagrantStoryLocationData("CAT - Bandits' Hideout - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("CAT - Bandits' Hideout Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Bloody Hallway": [VagrantStoryLocationData("CAT - The Bloody Hallway Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Faith Overcame Fear": [VagrantStoryLocationData("CAT - Faith Overcame Fear Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Withered Spring": [
        VagrantStoryLocationData("CAT - The Withered Spring - Lily Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("CAT - The Withered Spring Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Workshop 'Work of Art'": [
        VagrantStoryLocationData('CAT - Workshop "Work of Art" Entered', "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Repent, O ye Sinners": [VagrantStoryLocationData("CAT - Repent, O ye Sinners Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Reaper's Victims": [VagrantStoryLocationData("CAT - The Reaper's Victims Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Last Stab of Hope": [
        VagrantStoryLocationData("CAT - The Last Stab of Hope - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("CAT - The Last Stab of Hope Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Hallway of Heroes": [VagrantStoryLocationData("CAT - Hallway of Heroes Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Beast's Domain": [
        VagrantStoryLocationData("CAT - The Beast's Domain - Lizardman Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("CAT - The Beast's Domain Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    # Abandoned Mine B1
    "Dreamers' Entrance": [VagrantStoryLocationData("AM1 - Dreamers' Entrance Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Crossing": [VagrantStoryLocationData("AM1 - The Crossing Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Miners' Resting Hall": [
        VagrantStoryLocationData("AM1 - Miners' Resting Hall - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("AM1 - Miners' Resting Hall Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Conflict and Accord": [VagrantStoryLocationData("AM1 - Conflict and Accord Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The End of the Line": [VagrantStoryLocationData("AM1 - The End of the Line Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Earthquake's Mark": [
        VagrantStoryLocationData("AM1 - The Earthquake's Mark - Hyacinth Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("AM1 - The Earthquake's Mark - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM1 - The Earthquake's Mark Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Coal Mine Storage": [
        VagrantStoryLocationData("AM1 - Coal Mine Storage - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("AM1 - Coal Mine Storage - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM1 - Coal Mine Storage - Trap Clear Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM1 - Coal Mine Storage Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Suicide King": [VagrantStoryLocationData("AM1 - The Suicide King Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Battle's Beginning": [
        VagrantStoryLocationData("AM1 - The Battle's Beginning - Wyvern Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("AM1 - The Battle's Beginning Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "What Lies Ahead?": [
        VagrantStoryLocationData("AM1 - What Lies Ahead? - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM1 - What Lies Ahead? Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Fruits of Friendship": [
        VagrantStoryLocationData("AM1 - The Fruits of Friendship Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "The Passion of Lovers": [
        VagrantStoryLocationData("AM1 - The Passion of Lovers - Hyacinth Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("AM1 - The Passion of Lovers Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Hall of Hope": [VagrantStoryLocationData("AM1 - The Hall of Hope Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Dark Tunnel": [VagrantStoryLocationData("AM1 - The Dark Tunnel Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Everwant Passage": [
        VagrantStoryLocationData("AM1 - Everwant Passage - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("AM1 - Everwant Passage Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Mining Regrets": [
        VagrantStoryLocationData("AM1 - Mining Regrets - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("AM1 - Mining Regrets - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM1 - Mining Regrets Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Rust in Peace": [
        VagrantStoryLocationData("AM1 - Rust in Peace - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("AM1 - Rust in Peace Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Smeltry": [
        VagrantStoryLocationData("AM1 - The Smeltry - Fire Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("AM1 - The Smeltry Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Clash of Hyaenas": [VagrantStoryLocationData("AM1 - Clash of Hyaenas Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Greed Knows No Bounds": [
        VagrantStoryLocationData("AM1 - Greed Knows No Bounds Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Live Long and Prosper": [
        VagrantStoryLocationData("AM1 - Live Long and Prosper - Fern Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("AM1 - Live Long and Prosper Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Pray to the Mineral Gods": [
        VagrantStoryLocationData("AM1 - Pray to the Mineral Gods - Fern Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("AM1 - Pray to the Mineral Gods Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Traitor's Parting": [
        VagrantStoryLocationData("AM1 - Traitor's Parting - Ogre Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("AM1 - Traitor's Parting Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Escapeway": [VagrantStoryLocationData("AM1 - Escapeway Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    # Abandoned Mine B2
    "Subtellurian Horrors": [VagrantStoryLocationData("AM2 - Subtellurian Horrors Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Dining in Darkness": [
        VagrantStoryLocationData("AM2 - Dining in Darkness - Sky Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("AM2 - Dining in Darkness Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Bandit's Hollow": [
        VagrantStoryLocationData("AM2 - Bandit's Hollow - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("AM2 - Bandit's Hollow Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Delusions of Happiness": [
        VagrantStoryLocationData("AM2 - Delusions of Happiness - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("AM2 - Delusions of Happiness Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Work, Then Die": [VagrantStoryLocationData("AM2 - Work, Then Die Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Rock Bottom": [VagrantStoryLocationData("AM2 - Rock Bottom Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Lunatic Veins": [VagrantStoryLocationData("AM2 - The Lunatic Veins Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Tomb of the Reborn": [
        VagrantStoryLocationData("AM2 - Tomb of the Reborn - Earth Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("AM2 - Tomb of the Reborn Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Fool's Gold, Fool's Loss": [
        VagrantStoryLocationData(
            "AM2 - Fool's Gold, Fool's Loss - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS
        ),
        VagrantStoryLocationData("AM2 - Fool's Gold, Fool's Loss Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Kilroy Was Here": [VagrantStoryLocationData("AM2 - Kilroy Was Here Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "A Wager of Noble Gold": [
        VagrantStoryLocationData("AM2 - A Wager of Noble Gold Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Lambs to the Slaughter": [
        VagrantStoryLocationData("AM2 - Lambs to the Slaughter - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Lambs to the Slaughter Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Ore of Legend": [VagrantStoryLocationData("AM2 - The Ore of Legend Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Suicidal Desires": [
        VagrantStoryLocationData("AM2 - Suicidal Desires - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Trap Clear Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Cry of the Beast": [VagrantStoryLocationData("AM2 - Cry of the Beast Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Fallen Bricklayer": [
        VagrantStoryLocationData("AM2 - The Fallen Bricklayer Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Hall of Contemplation": [
        VagrantStoryLocationData("AM2 - Hall of Contemplation - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Hall of Contemplation Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Hall of the Empty Sconce": [
        VagrantStoryLocationData("AM2 - Hall of the Empty Sconce Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Acolyte's Burial Vault": [
        VagrantStoryLocationData("AM2 - Acolyte's Burial Vault - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("AM2 - Acolyte's Burial Vault Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "The Abandoned Catspaw": [
        VagrantStoryLocationData("AM2 - The Abandoned Catspaw Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)
    ],
    "Crossing of Blood": [
        VagrantStoryLocationData("AM2 - Crossing of Blood - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Crossing of Blood - Diabolos Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Crossing of Blood Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Senses Lost": [
        VagrantStoryLocationData("AM2 - Senses Lost - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Senses Lost - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Senses Lost Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Desire's Passage": [
        VagrantStoryLocationData("AM2 - Desire's Passage - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Desire's Passage Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Way of Lost Children": [VagrantStoryLocationData("AM2 - Way of Lost Children Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Hidden Resources": [
        VagrantStoryLocationData("AM2 - Hidden Resources - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("AM2 - Hidden Resources Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Treaty Room": [VagrantStoryLocationData("AM2 - Treaty Room Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "The Miner's End": [
        VagrantStoryLocationData("AM2 - The Miner's End - Air Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("AM2 - The Miner's End Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED),
    ],
    "Gambler's Passage": [VagrantStoryLocationData("AM2 - Gambler's Passage Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Revelation Shaft": [VagrantStoryLocationData("AM2 - Revelation Shaft Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Corridor of Shade": [VagrantStoryLocationData("AM2 - Corridor of Shade Entered", "Vera Root", VagrantStoryLocationCategory.ROOM_ENTERED)],
    "Credits": [
        VagrantStoryLocationData("Game End: Credits", "Vera Root", VagrantStoryLocationCategory.GAME_END),
    ],
}

location_dictionary: Dict[str, VagrantStoryLocationData] = {}  #
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})
