from enum import IntEnum
from typing import Optional, NamedTuple, Dict

from BaseClasses import Location, Region
from .Items import VagrantStoryItem

class VagrantStoryLocationCategory(IntEnum):
    FILLER = 0
    PROGRESSION = 1
    BOSS = 2
    GRIMOIRE = 3
    KEYS = 4
    SIGILS = 5
    LEVEL_END = 6

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
            parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)
        self.default_item_name = default_item_name
        self.category = category
        self.name = name

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 99250000
        region_offset = 1000        
        table_order = [
            "Map",
        ]

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

location_tables = {
    "Wine Cellar": [],
    "Catacombs": [],
    "Sanctum": [],
    "Abandoned Mines B1": [],
    "Abandoned Mines B2": [],
    "Limestone Quarry": [],
    "Temple of Kiltia": [],
    "Great Cathedral B1": [],
    "Great Cathedral L1": [],
    "Great Cathedral L2": [],
    "Great Cathedral L3": [],
    "Great Cathedral L4": [],
    "Forgotten Pathway": [],
    "Escapeway": [],
    "Iron Maiden B1": [],
    "Iron Maiden B2": [],
    "Iron Maiden B3": [],
    "Undercity West": [],
    "Undercity East": [],
    "The Keep": [],
    "City Walls West": [],
    "City Walls South": [],
    "City Walls East": [],
    "City Walls North": [],
    "Snowfly Forest": [],
    "Snowfly Forest East": [],
    "Town Center West": [],

    # Temporary Holder
    "Bosses": [
        VagrantStoryLocationData("Minotaur - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Dullahan - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Golem - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Dragon - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Duane + 2 Crimson Knights - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Wyvern - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Fire Elemental - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Ogre - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Giant Crab - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Earth Dragon - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Father Grissom and Dark Crusader - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Jan Rosencrantz - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Dark Elemental - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Shadow - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Wyvern Knight - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Iron Golem - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Harpy - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Lich - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Nightstalker - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Lady Neesa and Sir Tieger - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Minotaur Zombie - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Water Elemental - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Air Elemental - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Earth Elemental - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Ogre Lord - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Snow Dragon - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Last Crusader - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Minotaur Lord - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Kali - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Marid - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Ifrit - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Iron Crab - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Djinn - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Flame Dragon - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Arch Dragon - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Dao - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Nightmare - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Romeo Guildenstern Part 1 - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Romeo Guildenstern, Dark Angel - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Marid and Ifrit - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Damascus Crab - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Damascus Golem - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Wyvern Queen - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Dark Dragon - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Ravana - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Dragon Zombie - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Ogre Zombie - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Death - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Asura - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),

    ],
}

location_dictionary: Dict[str, VagrantStoryLocationData] = {}
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})