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
    GRIMOIRES = 6
    KEY_UNLOCKS = 7
    SIGIL_UNLOCKS = 8
    ROOD_INVERSE_UNLOCKS = 9
    ABILITY_UNLOCKS = 10
    BREAK_UNLOCKS = 11
    FLOOR_TRAPS = 12
    PUZZLE_CLEAR = 13
    LEVEL_END = 14


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
        base_id = 99250000
        region_offset = 10000
        table_order = ["Ashley", "Prologue", *all_minor_regions.keys()]

        output = {}
        for i, region_name in enumerate(table_order):
            current_region_base_id = base_id + (i * region_offset)
            # Ensure the region exists in location_tables
            if region_name in location_tables:
                # Enumerate the items within the current region, starting from current_region_base_id
                for j, location_data in enumerate(location_tables[region_name]):
                    # Assign an ID to each location within the region
                    # The ID for each location in a region will be current_region_base_id + j
                    # print(f"{current_region_base_id + j}: {location_data.name}")
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
        VagrantStoryLocationData("Ability: Unlock Level 1", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 2", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 3", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 4", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 5", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 6", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 7", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 8", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 9", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 10", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 11", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 12", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 13", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 14", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 15", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 16", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 17", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 18", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 19", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 20", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 21", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 22", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 23", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 24", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 25", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 26", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 27", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        VagrantStoryLocationData("Ability: Unlock Level 28", "Vera Root", VagrantStoryLocationCategory.ABILITY_UNLOCKS),
        # Break Skill Unlocks
        VagrantStoryLocationData("Break: Unlock Dagger Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Dagger Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Dagger Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Dagger Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Sword Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Sword Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Sword Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Sword Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Great Sword Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Great Sword Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Great Sword Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Great Sword Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Axes and Maces Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Axes and Maces Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Axes and Maces Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Axes and Maces Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Great Axe Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Great Axe Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Great Axe Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Great Axe Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Staff Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Staff Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Staff Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Staff Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Heavy Mace Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Heavy Mace Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Heavy Mace Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Heavy Mace Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Polearm Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Polearm Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Polearm Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Polearm Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Crossbow Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Crossbow Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Crossbow Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Crossbow Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Hands Level 1", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Hands Level 2", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Hands Level 3", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
        VagrantStoryLocationData("Break: Unlock Hands Level 4", "Vera Root", VagrantStoryLocationCategory.BREAK_UNLOCKS),
    ],
    "Prologue": [
        VagrantStoryLocationData("Boss: Injured Wyvern - Prologue", "Vera Root", VagrantStoryLocationCategory.BOSS),
        # two soldiers at start?
    ],
    # Wine Cellar
    "Entrance to Darkness": [],
    "Worker's Breakroom": [VagrantStoryLocationData("WC - Worker's Breakroom - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Hall of Struggle": [],
    "Smokebarrel Stair": [
        VagrantStoryLocationData("WC - Smokebarrel Stair - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("WC - Smokebarrel Stair - Chamomile Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.BOSS_UNLOCKS_PLUS),
    ],
    "Wine Guild Hall": [],
    "Wine Magnate's Chambers": [
        VagrantStoryLocationData("WC - Wine Magnate's Chambers - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Fine Vintage Vault": [],
    "Chamber of Fear": [],
    "The Reckoning Room": [VagrantStoryLocationData("WC - The Reckoning Room - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "A Laborer's Thirst": [],
    "The Rich Drown in Wine": [],
    "Room of Rotten Grapes": [
        VagrantStoryLocationData("WC - Room of Rotten Grapes - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("WC - Room of Rotten Grapes - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Blackmarket of Wines": [
        VagrantStoryLocationData("WC - Blackmarket of Wines - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
        # This is a Boss Unlock in NG+. Not sure the best way to handle that
        VagrantStoryLocationData("WC - Blackmarket of Wines - Stock Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    "The Gallows": [
        VagrantStoryLocationData("WC - The Gallows - Minotaur Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - The Gallows - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "The Gallows (Again)": [
        VagrantStoryLocationData("WC - The Gallows (Again) - Minotaur Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - The Gallows (Again) - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Room of Cheap Red Wine": [
        VagrantStoryLocationData("WC - Room of Cheap Red Wine - Mandel Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - Room of Cheap Red Wine - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Room of Cheap White Wine": [
        VagrantStoryLocationData("WC - Room of Cheap White Wine - Zombie Fighter Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - Room of Cheap White Wine - Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - Room of Cheap White Wine - Ghoul Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "The Greedy One's Den": [],
    "The Hero's Winehall": [
        VagrantStoryLocationData("WC - The Hero's Winehall - Dullahan Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("WC - The Hero's Winehall - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    # Undercity West
    "The Bread Peddler's Way": [],
    "Way of the Mother Lode": [],
    "Sewer of Ravenous Rats": [
        VagrantStoryLocationData("UW - Sewer of Ravenous Rats - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Underdark Fishmarket": [VagrantStoryLocationData("UW - Underdark Fishmarket - Giant Crab Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "The Sunless Way": [VagrantStoryLocationData("UW - The Sunless Way - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)],
    "Remembering Days of Yore": [
        VagrantStoryLocationData("UW - Remembering Days of Yore - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Larder for a Lean Winter": [VagrantStoryLocationData("UW - Larder for a Lean Winter - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Where the Hunter Climbed": [],
    "Hall of Poverty": [],
    "The Washing-Woman's Way": [
        VagrantStoryLocationData("UW - The Washing-Woman's Way - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - The Washing-Woman's Way - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Washing-Woman's Way - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Nameless Dark Oblivion": [
        VagrantStoryLocationData("UW - Nameless Dark Oblivion - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
    ],
    "Sinner's Corner": [],
    "Fear of the Fall": [VagrantStoryLocationData("UW - Fear of the Fall - Dark Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "The Children's Hideout": [VagrantStoryLocationData("UW - The Children's Hideout - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Corner of Prayers": [
        VagrantStoryLocationData("UW - Corner of Prayers - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Hope Obstructed": [],
    "Beggars of the Mouthharp": [
        VagrantStoryLocationData("UW - Beggars of the Mouthharp - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Corner of the Wretched": [],
    "Crossroads of Rest": [
        VagrantStoryLocationData("UW - Crossroads of Rest - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Path to the Greengrocer": [],
    "Path of the Children": [],
    "Salvation for the Mother": [
        VagrantStoryLocationData("UW - Salvation for the Mother - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("UW - Salvation for the Mother - Diabolos Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - Salvation for the Mother - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Body Fragile Yields": [
        VagrantStoryLocationData("UW - The Body Fragile Yields - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Bite the Master's Wounds": [],
    "Workshop 'Godhands'": [],
    "The Crumbling Market (South)": [],
    "The Crumbling Market (North)": [
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData(
            "UW - The Crumbling Market (North) - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS
        ),
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UW - The Crumbling Market (North) - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Where Flood Waters Ran": [],
    "Tears from Empty Sockets": [],
    # Undercity East
    "Hall to a New World": [],
    "Place of Free Words": [VagrantStoryLocationData("UE - Place of Free Words - Harpy Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Bazaar of the Bizarre": [VagrantStoryLocationData("UE - Bazaar of the Bizarre - Lich Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Noble Gold and Silk": [
        VagrantStoryLocationData("UE - Noble Gold and Silk - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Weapons Not Allowed": [VagrantStoryLocationData("UE - Weapons Not Allowed - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "A Knight Sells his Sword": [],
    "Gemsword Blackmarket": [
        VagrantStoryLocationData("UE - Gemsword Blackmarket - Nightstalker Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "The Pirate's Son": [],
    "Sale of the Sword": [VagrantStoryLocationData("UE - Sale of the Sword - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    # Undercity East (North Side)
    "The Greengrocer's Stair": [
        VagrantStoryLocationData("UEN - The Greengrocer's Stair - Neesa Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("UEN - The Greengrocer's Stair - Tieger Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "Where Black Waters Ran": [],
    "Arms Against Invaders": [],
    "Catspaw Blackmarket": [
        VagrantStoryLocationData("UEN - Catspaw Blackmarket - Diabolos Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UEN - Catspaw Blackmarket - Trap Clear Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("UENF - Catspaw Blackmarket - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    # Town Centre South
    "Forcas Rise": [],
    "Valdiman Gates": [],
    "Rue Aliano": [VagrantStoryLocationData("TCS - Rue Aliano - Mandrake Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)],
    "The House Khazabas": [VagrantStoryLocationData("TCS - The House Khazabas - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Zebel's Walk": [],
    "Rue Volnac": [],
    "Rue Faltes": [],
    "Rue Morgue": [],
    # Town Centre East
    "Rue Lejour": [],
    "Kesch Bridge": [],
    "Rue Crimnade": [VagrantStoryLocationData("TCE - Rue Crimnade - Cattleya Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)],
    "Workshop 'Junction Point'": [],
    "Rue Fisserano": [VagrantStoryLocationData("TCE - Rue Fisserano - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)],
    "Workshop 'Metal Works'": [],
    "Shasras Hill Park": [
        VagrantStoryLocationData("TCE - Shasras Hill Park - Bronze Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "The House Gilgitte": [VagrantStoryLocationData("TCE - The House Gilgitte - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Gharmes Walk": [VagrantStoryLocationData("TCE - Gharmes Walk - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Plateia Lumitar": [
        VagrantStoryLocationData("TCE - Plateia Lumitar - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    # Towen Centre West
    "Rue Vermillion": [VagrantStoryLocationData("TCW - Rue Vermillion - Crimson Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)],
    "The Rene Coastroad": [
        VagrantStoryLocationData("TCW - The Rene Coastroad - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    'Workshop "Magic Hammer"': [],
    "Rue Mal Fallde": [],
    "Tircolas Flow (North)": [VagrantStoryLocationData("TCW - Tircolas Flow (North) - Duane Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Tircolas Flow (South)": [],
    "Rue Bouquet": [],
    "Glacialdra Kirk Ruins": [
        VagrantStoryLocationData("TCW - Glacialdra Kirk Ruins - Rood Inverse Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)
    ],
    "Rue Sant D'alsa": [],
    "Dinas Walk": [],
    "Villeport Way": [],
    # The Keep
    "The Soldier's Bedding": [
        VagrantStoryLocationData("KEP - The Soldier's Bedding - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "A Storm of Arrows": [
        VagrantStoryLocationData("KEP - A Storm of Arrows - Kalmia Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - A Storm of Arrows - Columbine Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    "Time Trial (Minotaur)": [VagrantStoryLocationData("TK - Time Trial (Minotaur) - Minotaur Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Time Trial (Dragon)": [VagrantStoryLocationData("TK - Time Trial (Dragon) - Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Urge the Boy On": [
        VagrantStoryLocationData("KEP - Urge the Boy On - Anemone Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - Urge the Boy On - Verbena Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    "Time Trial (Earth Dragon)": [
        VagrantStoryLocationData("TK - Time Trial (Earth Dragon) - Earth Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "Time Trial (Snow Dragon)": [
        VagrantStoryLocationData("TK - Time Trial (Snow Dragon) - Snow Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "A Taste of the Spoils": [
        VagrantStoryLocationData("KEP - A Taste of the Spoils - Schirra Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - A Taste of the Spoils - Marigold Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    "Time Trial (Damascus Golem)": [
        VagrantStoryLocationData("TK - Time Trial (Damascus Golem) - Damascus Golem Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "Time Trial (Damascus Crab)": [
        VagrantStoryLocationData("TK - Time Trial (Damascus Crab) - Damascus Crab Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "Wiping Blood from Blades": [
        VagrantStoryLocationData("KEP - Wiping Blood from Blades - Azalea Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("KEP - Wiping Blood from Blades - Tigertail Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    "Time Trial (Death + Ogre Zombie)": [
        VagrantStoryLocationData("TK - Time Trial (Death + Ogre Zombie) - Death Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("TK - Time Trial (Death + Ogre Zombie) - Ogre Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "Time Trial (Asura)": [VagrantStoryLocationData("TK - Time Trial (Asura) - Asura Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "The Warrior's Rest": [
        VagrantStoryLocationData("TK - The Warrior's Rest - Rosencrantz Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("TK - The Warrior's Rest - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Workshop 'Keane's Crafts'": [],
    # Temple of Kiltia
    "The Dark Coast": [
        VagrantStoryLocationData("ToK - The Dark Coast - Trap Clear Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("ToK - The Dark Coast - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Hall of Prayer": [VagrantStoryLocationData("ToK - Hall of Prayer - Last Crusader Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Those who Drink the Dark": [
        VagrantStoryLocationData("TOK - Those who Drink the Dark - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "The Chapel of Meschaunce": [
        VagrantStoryLocationData("ToK - The Chapel of Meschaunce - Minotaur Lord Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "The Resentful Ones": [
        VagrantStoryLocationData("TOK - The Resentful Ones - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Those who Fear the Light": [],
    "Chamber of Reason": [VagrantStoryLocationData("ToK - Chamber of Reason - Kali Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Exit to City Center": [],
    # Snowfly Forest
    "The Faerie Circle": [],
    "The Hunt Begins": [],
    "Which Way Home": [],
    "The Giving Trees": [],
    "The Birds and the Bees": [],
    "The Wounded Boar": [],
    "Golden Egg Way": [],
    "Traces of the Beast": [],
    "Fluttering Hope": [],
    "Return to the Land": [],
    "The Yellow Wood": [],
    "They Also Feed": [],
    "The Spirit Trees": [],
    "Where Soft Rains Fell": [],
    "Forest River": [
        VagrantStoryLocationData("SFF - Forest River - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("SFF - Forest River - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Lamenting to the Moon": [],
    "Running with the Wolves": [],
    "You Are the Prey": [],
    "The Secret Path": [],
    "Hewn from Nature": [
        VagrantStoryLocationData("SFF - Hewn from Nature - Grissom Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("SFF - Hewn from Nature - Dark Crusader Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("SFF - Hewn from Nature - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "The Wood Gate": [],
    "The Wolves' Choice": [],
    "The Woodcutter's Run": [],
    "The Hollow Hills": [],
    "Howl of the Wolf King": [],
    "The Silent Hedges": [],
    # Snowfly Forest East
    "Steady the Boar-Spears": [
        VagrantStoryLocationData(
            "SFE - Steady the Boar-Spears - Rood Inverse Unlock", "Vera Root", VagrantStoryLocationCategory.ROOD_INVERSE_UNLOCKS
        ),
    ],
    "The Boar's Revenge": [],
    "Nature's Womb": [VagrantStoryLocationData("SFE - Nature's Womb - Damascus Crab Boss", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS)],
    # Sanctum
    "Prisoners' Niche": [],
    "Corridor of the Clerics": [],
    "Priests' Confinement": [],
    "Alchemists' Laboratory": [VagrantStoryLocationData("SNC - Alchemists' Laboratory - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Academia Corridor": [],
    "Theology Classroom": [],
    "Shrine of the Martyrs": [],
    "Hallowed Hope": [],
    "Hall of Sacrilege": [VagrantStoryLocationData("SNC - Hall of Sacrilege - Golem Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Advent Ground (South)": [],
    "Passage of the Refugees (South)": [
        VagrantStoryLocationData(
            "SNC - Passage of the Refugees (South) - Hall of Sacrilege Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS
        )
    ],
    "Passage of the Refugees (North)": [],
    "Advent Ground (North)": [],
    "The Cleansing Chantry": [VagrantStoryLocationData("SNC - The Cleansing Chantry - Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Stairway to the Light": [],
    # Limestone Quarry
    "Dark Abhors Light": [],
    "Dream of the Holy Land": [
        VagrantStoryLocationData("LQ - Dream of the Holy Land - Water Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("LQ - Dream of the Holy Land - Aster Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    "The Ore Road": [],
    "The Air Stirs": [VagrantStoryLocationData("LQ - The Air Stirs - Eulelia Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)],
    "Bonds of Friendship": [VagrantStoryLocationData("LQ - Bonds of Friendship - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Atone for Eternity": [
        VagrantStoryLocationData("LQ - Atone for Eternity - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Stair to Sanctuary": [],
    "The Fallen Hall": [],
    "The Rotten Core": [],
    "The Dreamer's Climb": [
        VagrantStoryLocationData("LQ - The Dreamer's Climb - Eulelia Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("LQ - The Dreamer's Climb - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Ore-Bearers": [
        VagrantStoryLocationData("LQ - The Ore-Bearers - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Screams of the Wounded": [],
    "Bacchus is Cheap": [],
    "Sinner's Sustenence": [],
    "The Timely Dew of Sleep": [
        VagrantStoryLocationData("LQ - The Air Stirs - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Companions in Arms": [VagrantStoryLocationData("LQ - Companions in Arms - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Auction Block": [
        VagrantStoryLocationData("LQ - The Auction Block - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Ascension": [],
    "Where the Serpent Hunts": [],
    "Drowned in Fleeting Joy": [VagrantStoryLocationData("LQ - Drowned in Fleeting Joy - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Ants Prepare for Winter": [],
    "The Laborer's Bonfire": [
        VagrantStoryLocationData("LQ - The Laborer's Bonfire - Melissa Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("LQ - The Laborer's Bonfire - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Stone and Sulfurous Fire": [VagrantStoryLocationData("LQ - Stone and Sulfurous Fire - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Torture Without End": [VagrantStoryLocationData("LQ - Torture Without End - Ogre Lord Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Way Down": [],
    "Excavated Hollow": [VagrantStoryLocationData("LQ - Excavated Hollow - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Parting Regrets": [],
    "Corridor of Tales": [],
    "Dust Shall Eat the Days": [],
    "Hall of the Wage-Paying": [
        VagrantStoryLocationData("LQ - Hall of the Wage-Paying - Snow Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "Tunnel of the Heartless": [],
    # Iron Maiden B1
    "The Cage": [],
    "The Cauldron": [
        VagrantStoryLocationData("IM1 - The Cauldron - Gargoyle Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - The Cauldron - Gargoyle Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - The Cauldron - Wraith Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - The Cauldron - Tearose Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    "Wooden Horse": [],
    "Starvation": [
        VagrantStoryLocationData("IM1 - Starvation - Wraith Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM1 - Starvation - Mummy Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "The Breast Ripper": [],
    "The Wheel": [VagrantStoryLocationData("IM1 - The Wheel - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Branks": [VagrantStoryLocationData("IM1 - The Branks - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Pear": [],
    "The Judas Cradle": [VagrantStoryLocationData("IM1 - The Judas Cradle - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Whirlygig": [],
    "Spanish Tickler": [VagrantStoryLocationData("IM1 - Spanish Tickler - Wyvern Knight Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Heretic's Fork": [
        VagrantStoryLocationData("IM1 - Heretic's Fork - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Heretic's Fork - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Chair of Spikes": [],
    "Blooding": [
        VagrantStoryLocationData("IM1 - Blooding - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Blooding - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Bootikens": [],
    "Burial": [VagrantStoryLocationData("IM1 - Burial - Iron Golem Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Burning": [
        VagrantStoryLocationData("IM1 - Burning - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM1 - Burning - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Cleansing the Soul": [],
    "The Ducking Stool": [VagrantStoryLocationData("IM1 - The Ducking Stool - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Garotte": [],
    "Hanging": [VagrantStoryLocationData("IM1 - Hanging - Steel Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)],
    "Impalement": [VagrantStoryLocationData("IM1 - Impalement - Platinum Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)],
    "Knotting": [VagrantStoryLocationData("IM1 - Knotting - Wyvern Queen Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    # Iron Maiden B2
    "The Eunics' Lot": [],
    "Ordeal By Fire": [VagrantStoryLocationData("IM2 - Ordeal By Fire - Dark Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "The Oven at Neisse": [],
    "Pressing": [VagrantStoryLocationData("IM2 - Pressing - Ravana Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "The Mind Burns": [
        VagrantStoryLocationData("IM2 - The Mind Burns - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - The Mind Burns - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Rack": [],
    "The Saw": [VagrantStoryLocationData("IM2 - The Saw - Dragon Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "The Cold's Bridle": [
        VagrantStoryLocationData("IM2 - The Cold's Bridle - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - The Cold's Bridle - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - The Cold's Bridle - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Shin-Vice": [
        VagrantStoryLocationData("IM2 - The Shin-Vice - Ogre Zombie Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("IM2 - The Shin-Vice - Death Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "The Spider": [],
    "Lead Sprinkler": [
        VagrantStoryLocationData("IM2 - Lead Sprinkler - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - Lead Sprinkler - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Squassation": [
        VagrantStoryLocationData("IM2 - Squassation - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - Squassation - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("IM2 - Squassation - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "The Strappado": [],
    "Thumbscrews": [],
    "Pendulum": [VagrantStoryLocationData("IM2 - Pendulum - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)],
    "Dragging": [VagrantStoryLocationData("IM2 - Dragging - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)],
    "Strangulation": [],
    "Tablillas": [],
    "Tongue Slicer": [],
    "Ordeal by Water": [],
    "Brank": [],
    "Tormentum Insomniae": [],
    # Iron Maiden B3
    "The Iron Maiden": [VagrantStoryLocationData("IM3 - The Iron Maiden - Asura Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Judgement": [],
    "Saint Elmo's Belt": [VagrantStoryLocationData("IM3 - Saint Elmo's Belt - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Dunking the Witch": [VagrantStoryLocationData("IM3 - Dunking the Witch - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    # The Great Cathedral L1
    "Into Holy Battle": [
        VagrantStoryLocationData("GC1 - Into Holy Battle - Truth and Lies Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)
    ],
    "The Poisoned Chapel": [
        VagrantStoryLocationData("GC1 - The Poisoned Chapel - Laurel Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)
    ],
    "Sin and Punishment": [
        VagrantStoryLocationData("GC1 - Sin and Punishment - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC1 - Sin and Punishment - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "A Light in the Dark": [VagrantStoryLocationData("GC1 - A Light in the Dark - Arch Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Monk's Leap": [VagrantStoryLocationData("GC1 - Monk's Leap - Lich Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Hieratic Recollections": [],
    "The Flayed Confessional": [
        VagrantStoryLocationData("GC1 - The Flayed Confessional - Djinn Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("GC1 - The Flayed Confessional - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Cracked Pleasures": [],
    "Where Darkness Spreads": [VagrantStoryLocationData("GC1 - Where Darkness Spreads - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    # The Great Cathedral B1
    "Struggle for the Soul": [
        VagrantStoryLocationData("GCB - Struggle for the Soul - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Order and Chaos": [VagrantStoryLocationData("GCB - Order and Chaos - Marid Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "An Offering of Souls": [],
    "Truth and Lies": [VagrantStoryLocationData("GCB - Truth and Lies - Ifrit Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Sanity and Madness": [VagrantStoryLocationData("GCB - Sanity and Madness - Iron Crab Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "The Victor's Laurels": [],
    # The Great Cathedral L2
    "Free from Base Desires": [],
    "Abasement from Above": [
        VagrantStoryLocationData("GC2 - Abasement from Above - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC2 - Abasement from Above - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC2 - Abasement from Above - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Convent Room": [],
    "The Hall of Broken Vows": [
        VagrantStoryLocationData("GC2 - The Hall of Broken Vows - Acacia Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("GC2 - The Hall of Broken Vows - Flame Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "Light and Dark Wage War": [],
    "An Arrow into Darkness": [VagrantStoryLocationData("GC2 - An Arrow into Darkness - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "He Screams for Mercy": [
        VagrantStoryLocationData("GC2 - He Screams for Mercy - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("GC2 - He Screams for Mercy - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Acolyte's Weakness": [],
    "Maelstrom of Malice": [VagrantStoryLocationData("GC2 - Maelstrom of Malice - Lich Lord Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "The Melodics of Madness": [
        VagrantStoryLocationData("GC2 - The Melodics of Madness - Palm Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    "What Ails You, Kills You": [
        VagrantStoryLocationData("GC2 - What Ails You, Kills You - Nightmare Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    # The Great Cathedral L3
    "The Wine-Lecher's Fall": [],
    "The Heretics' Story (Lower)": [
        VagrantStoryLocationData("GC3 - The Heretics' Story (Lower) - Calla Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)
    ],
    "The Heretics' Story (Upper)": [],
    "Despair of the Fallen": [],
    "Hopes of the Idealist": [VagrantStoryLocationData("GC3 - Hopes of the Idealist - Dao Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Where the Soul Rots": [],
    # The Great Cathedral L4
    "The Atrium": [],
    # The Great Cathedral Dome
    "Dome": [VagrantStoryLocationData("GCD - Dome - Guildenstern Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Paling": [VagrantStoryLocationData("GCD - Paling - Guildenstern Apotheos Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    # Forgotten Pathway
    "Stair to the Sinners": [],
    "Slaughter of the Innocent": [
        VagrantStoryLocationData("FP - Slaugher of the Innocent - Damascus Golem Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "The Oracle Sins No More": [
        VagrantStoryLocationData("FP - The Oracle Sins No More - Curse Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("FP - The Oracle Sins No More - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Fallen Knight": [VagrantStoryLocationData("FP - The Fallen Knight - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Awaiting Retribution": [VagrantStoryLocationData("FP - Awaiting Retribution - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    # Escapeway
    "Shelter From the Quake": [
        VagrantStoryLocationData("ESC - Shelter From the Quake - Gold Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("ESC - Shelter From the Quake - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
    ],
    "Buried Alive": [VagrantStoryLocationData("ESC - Buried Alive - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Movement of Fear": [],
    "Facing Your Illusions": [
        VagrantStoryLocationData("ESC - Facing Your Illusions - Diabolos Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "The Darkness Drinks": [],
    "Fear and Loathing": [
        VagrantStoryLocationData("ESC - Fear and Loathing - Ifrit Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("ESC - Fear and Loathing - Marid Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "Blood and The Beast": [
        VagrantStoryLocationData("ESC - Blood and The Beast - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Where Body and Soul Part": [VagrantStoryLocationData("ESC - Where Body and Soul Part - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    # City Walls West
    "Students of Death": [
        VagrantStoryLocationData("CWW - Students of Death - Crimson Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "The Gabled Hall": [],
    "Where the Master Fell": [],
    # City Walls South
    "In Wait of the Foe": [],
    "Swords for the Land": [],
    "The Weeping Boy": [],
    "Where Weary Riders Rest": [],
    "The Boy's Training Room": [],
    # City Walls North
    "From Squire to Knight": [
        VagrantStoryLocationData("CWN - From Squire to Knight - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Traces of Invasion Past": [],
    "Be for Battle Prepared": [],
    "Destruction and Rebirth": [],
    "From Boy to Hero": [
        VagrantStoryLocationData("CWN - From Boy to Hero - Clematis Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)
    ],
    "A Welcome Invasion": [],
    # City Walls East
    "Train and Grow Strong": [
        VagrantStoryLocationData("CWE - Train and Grow Strong - Rood Inverse Unlock", "Vera Root", VagrantStoryLocationCategory.ROOD_INVERSE_UNLOCKS)
    ],
    "The Squire's Gathering": [],
    "The Invaders are Found": [],
    "The Dream Weavers": [],
    "The Cornered Savage": [],
    # Catacombs
    "Hall of Sworn Revenge": [
        VagrantStoryLocationData("CAT - Hall of Sworn Revenge - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("CAT - Hall of Sworn Revenge - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "The Last Blessing": [],
    "The Weeping Corridor": [
        VagrantStoryLocationData("CAT - The Weeping Corridor - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Persecution Hall": [],
    "Rodent-Ridden Chamber": [VagrantStoryLocationData("CAT - Rodent-Ridden Chamber - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Shrine to the Martyrs": [],
    "The Lamenting Mother (West)": [
        VagrantStoryLocationData("CAT - The Lamenting Mother (West) - Ghost Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "The Lamenting Mother (East)": [
        VagrantStoryLocationData("CAT - The Lamenting Mother (East) - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)
    ],
    "Hall of Dying Hope": [],
    "Bandits' Hideout": [VagrantStoryLocationData("CAT - Bandits' Hideout - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Bloody Hallway": [],
    "Faith Overcame Fear": [],
    "The Withered Spring": [
        VagrantStoryLocationData("CAT - The Withered Spring - Lily Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
    ],
    'Workshop "Work of Art"': [],
    "Repent, O ye Sinners": [],
    "The Reaper's Victims": [],
    "The Last Stab of Hope": [
        VagrantStoryLocationData("CAT - The Last Stab of Hope - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Hallway of Heroes": [],
    "The Beast's Domain": [
        VagrantStoryLocationData("CAT - The Beast's Domain - Lizardman Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("CAT - The Beast's Domain - Lizardman Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    # Abandoned Mine B1
    "Dreamers' Entrance": [],
    "The Crossing": [],
    "Miners' Resting Hall": [VagrantStoryLocationData("AM1 - Miners' Resting Hall - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Conflict and Accord": [],
    "The End of the Line": [],
    "The Earthquake's Mark": [
        VagrantStoryLocationData("AM1 - The Earthquake's Mark - Hyacinth Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("AM1 - The Earthquake's Mark - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Coal Mine Storage": [
        VagrantStoryLocationData("AM1 - Coal Mine Storage - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM1 - Coal Mine Storage - Trap Clear Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM1 - Coal Mine Storage - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "The Suicide King": [],
    "The Battle's Beginning": [
        VagrantStoryLocationData("AM1 - The Battle's Beginning - Wyvern Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "What Lies Ahead?": [
        VagrantStoryLocationData("AM1 - What Lies Ahead? - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "The Fruits of Friendship": [],
    "The Passion of Lovers": [
        VagrantStoryLocationData("AM1 - The Passion of Lovers - Hyacinth Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)
    ],
    "The Hall of Hope": [],
    "The Dark Tunnel": [],
    "Everwant Passage": [
        VagrantStoryLocationData("AM1 - Everwant Passage - Silver Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)
    ],
    "Mining Regrets": [
        VagrantStoryLocationData("AM1 - Mining Regrets - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM1 - Mining Regrets - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Rust in Peace": [VagrantStoryLocationData("AM1 - Rust in Peace - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Smeltry": [VagrantStoryLocationData("AM1 - The Smeltry - Fire Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Clash of Hyaenas": [],
    "Greed Knows No Bounds": [],
    "Live Long and Prosper": [
        VagrantStoryLocationData("AM1 - Live Long and Prosper - Fern Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)
    ],
    "Pray to the Mineral Gods": [
        VagrantStoryLocationData("AM1 - Pray to the Mineral Gods - Fern Sigil Unlock", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS)
    ],
    "Traitor's Parting": [VagrantStoryLocationData("AM1 - Traitor's Parting - Ogre Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Escapeway": [],
    # Abandoned Mine B2
    "Subtellurian Horrors": [],
    "Dining in Darkness": [VagrantStoryLocationData("AM2 - Dining in Darkness - Sky Dragon Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Bandit's Hollow": [VagrantStoryLocationData("AM2 - Bandit's Hollow - Iron Key Unlock", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS)],
    "Delusions of Happiness": [VagrantStoryLocationData("AM2 - Delusions of Happiness - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Work, Then Die": [],
    "The Lunatic Veins": [],
    "Tomb of the Reborn": [
        VagrantStoryLocationData("AM2 - Tomb of the Reborn - Earth Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)
    ],
    "Fool's Gold, Fool's Loss": [
        VagrantStoryLocationData("AM2 - Fool's Gold, Fool's Loss - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Kilroy Was Here": [],
    "A Wager of Noble Gold": [],
    "Lambs to the Slaughter": [
        VagrantStoryLocationData("AM2 - Lambs to the Slaughter - Heal Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "The Ore of Legend": [],
    "Suicidal Desires": [
        VagrantStoryLocationData("AM2 - Suicidal Desires - Death Vapor Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Paralysis Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Terra Thrust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Gust Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Freeze Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Trap Clear Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Suicidal Desires - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Cry of the Beast": [],
    "The Fallen Bricklayer": [],
    "Hall of Contemplation": [
        VagrantStoryLocationData("AM2 - Hall of Contemplation - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Hall of the Empty Sconce": [],
    "Acolyte's Burial Vault": [VagrantStoryLocationData("AM2 - Acolyte's Burial Vault - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "The Abandoned Catspaw": [],
    "Crossing of Blood": [
        VagrantStoryLocationData("AM2 - Crossing of Blood - Holy Light Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Crossing of Blood - Diabolos Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Senses Lost": [
        VagrantStoryLocationData("AM2 - Senses Lost - Eruption Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("AM2 - Senses Lost - Poison Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Desire's Passage": [
        VagrantStoryLocationData("AM2 - Desire's Passage - Cure Panel Floor Trap", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS)
    ],
    "Way of Lost Children": [],
    "Hidden Resources": [VagrantStoryLocationData("AM2 - Hidden Resources - Chest", "Vera Root", VagrantStoryLocationCategory.CHEST)],
    "Treaty Room": [],
    "The Miner's End": [VagrantStoryLocationData("AM2 - The Miner's End - Air Elemental Boss", "Vera Root", VagrantStoryLocationCategory.BOSS)],
    "Gambler's Passage": [],
    "Revelation Shaft": [],
    "Corridor of Shade": [],
    "Credits": [
        VagrantStoryLocationData("Level End: Credits", "Vera Root", VagrantStoryLocationCategory.LEVEL_END),
    ],
}

location_dictionary: Dict[str, VagrantStoryLocationData] = {}  #
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})
