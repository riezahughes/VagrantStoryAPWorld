from enum import IntEnum
from typing import Optional, NamedTuple, Dict

from BaseClasses import Location, Region
from .Items import VagrantStoryItem

class VagrantStoryLocationCategory(IntEnum):
    FILLER = 0
    PROGRESSION = 1
    CHEST = 2
    BOSS = 3
    BOSS_PLUS = 4
    GRIMOIRE = 5
    KEYS = 6
    SIGILS = 7
    LEVEL_END = 8

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
    "Wine Cellar": [
        VagrantStoryLocationData("Chest: Wine Cellar - Workers Breakroom", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Wine Cellar - The Reckoning Room", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Wine Cellar - Blackmarket of Wines", "Vera Root", VagrantStoryLocationCategory.CHEST),  
        VagrantStoryLocationData("Chest: Wine Cellar - The Gallows", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Wine Cellar - The Hero's Winehall", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Wine Cellar - The Gallows (Locked)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Minotaur - Wine Cellar", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Dullahan - Wine Cellar", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Minotaur Zombie - Wine Cellar", "Vera Root", VagrantStoryLocationCategory.BOSS),        

    ],
    "Catacombs": [
        VagrantStoryLocationData("Chest: Catacombs - Rodent-Ridden Chamber", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Catacombs - The Lamenting Mother", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Catacombs - Bandits Hideout", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Sanctum": [
        VagrantStoryLocationData("Chest: Sanctum - Alchemists Laboratory", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Golem - Sanctum", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Dragon - Sanctum", "Vera Root", VagrantStoryLocationCategory.BOSS),        

    ],
    "Abandoned Mines B1": [
        VagrantStoryLocationData("Chest: Abandoned Mines B1 - Miners Resting Hall (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Abandoned Mines B1 - Coal Mine Storage", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Abandoned Mines B1 - Rust in Peace (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),     
        VagrantStoryLocationData("Chest: Abandoned Mines B1 - Mining Regrets", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Abandoned Mines B2": [
        VagrantStoryLocationData("Chest: Abandoned Mines B2 - Delusions of Happiness", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Abandoned Mines B2 - Hidden Resources (Locked)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Abandoned Mines B2 - Acolytes Burial Vault", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Abandoned Mines B2 - Suicidal Desires", "Vera Root", VagrantStoryLocationCategory.CHEST),     
        VagrantStoryLocationData("Boss: Wyvern - Abandoned Mines B2", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Fire Elemental - Abandoned Mines B2", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Ogre - Abandoned Mines B2", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Sky Dragon - Abandoned Mines B2", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Limestone Quarry": [
        VagrantStoryLocationData("Chest: Limestone Quarry - Bonds of Friendship", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Limestone Quarry - Stone and Sulsurous Fire", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Limestone Quarry - Excavated Hollow", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Limestone Quarry - Drowned in Fleeting Joy", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Limestone Quarry - Companion in Arms (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),   
        VagrantStoryLocationData("Boss: Water Elemental - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Air Elemental - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Earth Elemental - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Ogre Lord - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Snow Dragon - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Temple of Kiltia": [
        VagrantStoryLocationData("Chest: Temple of Kiltia - The Chapel of Meschaunce", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Last Crusader - Temple of Kiltia", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Minotaur Lord - Temple of Kiltia", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Kali - Temple of Kiltia", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Great Cathedral B1": [
        VagrantStoryLocationData("Boss: Marid - Great Cathedral B1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Ifrit - Great Cathedral B1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Iron Crab - Great Cathedral B1", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "Great Cathedral L1": [
        VagrantStoryLocationData("Chest: The Great Cathedral L1 - Where Darkness Spreads", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: The Great Cathedral L1 - The Flayed Confessional", "Vera Root", VagrantStoryLocationCategory.CHEST),            
        VagrantStoryLocationData("Boss: Arch Dragon - Great Cathedral L1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Djinn - Great Cathedral L1", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Great Cathedral L2": [
        VagrantStoryLocationData("Chest: The Great Cathedral L2 - An Arrow into Darkness", "Vera Root", VagrantStoryLocationCategory.CHEST),   
        VagrantStoryLocationData("Boss: Flame Dragon - Great Cathedral L2", "Vera Root", VagrantStoryLocationCategory.BOSS),        
        VagrantStoryLocationData("Boss: Nightmare - Great Cathedral L2", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Great Cathedral L3": [
            VagrantStoryLocationData("Boss: Dao - Great Cathedral L3", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "Great Cathedral L4": [
        VagrantStoryLocationData("Boss: Guildenstern - Great Cathedral L4", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Guildenstern, Dark Angel - Great Cathedral L4", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Forgotten Pathway": [
        VagrantStoryLocationData("Chest: Forgotten Pathway - The Fallen Knight", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Forgotten Pathway - Awaiting Retribution", "Vera Root", VagrantStoryLocationCategory.CHEST), 
    ],
    "Escapeway": [
        VagrantStoryLocationData("Chest: Escapeway - Where Body and Soul Part (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Escapeway - Buried Alice", "Vera Root", VagrantStoryLocationCategory.CHEST),        
    ],
    "Iron Maiden B1": [
        VagrantStoryLocationData("Chest: Iron Maiden B1 - The Wheel (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B1 - The Judas Cradle", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B1 - The Ducking Stool", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B1 - The Branks (Locked)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Wyvern Knight - Iron Maiden B1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Iron Golem - Iron Maiden B1", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Iron Maiden B2": [
        VagrantStoryLocationData("Chest: Iron Maiden B2 - Lead Sprinkler", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B2 - Squassation", "Vera Root", VagrantStoryLocationCategory.CHEST),        
    ],
    "Iron Maiden B3": [
        VagrantStoryLocationData("Chest: Iron Maiden B3 - Saint Elmos Belt", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B3 - Dunking the Witch", "Vera Root", VagrantStoryLocationCategory.CHEST),        
    ],
    "Undercity West": [
        VagrantStoryLocationData("Chest: Undercity West - The Childrens Hideout", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Undercity West - Larder for a Lean Winter", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Undercity West - The Crumbling Market", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Dark Elemental - Undercity West", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Shadow - Undercity West", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Giant Crab - Undercity West", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Undercity East": [
        VagrantStoryLocationData("Chest: Undercity East - Weapons Not Allowed", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Undercity East - Sale of the Sword", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Undercity East - Catspaw Blackmarket", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Harpy - Undercity East", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Nightstalker - Undercity East", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Neesa and Tieger - Undercity East", "Vera Root", VagrantStoryLocationCategory.BOSS),

    ],
    "The Keep": [
        VagrantStoryLocationData("Chest: The Keep - The Warriors Rest (Locked)", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "City Walls West": [
        VagrantStoryLocationData("Boss: Duane + 2 Crimson Knights - City Walls West", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "City Walls South": [
        VagrantStoryLocationData("Boss: Jan Rosencrantz - City Walls South", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "City Walls East": [],
    "City Walls North": [],
    "Snowfly Forest": [
        VagrantStoryLocationData("Chest: Snowfly Forest - Forest River", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Snowfly Forest - Hewn from Nature", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Earth Dragon - Snowfly Forest", "Vera Root", VagrantStoryLocationCategory.BOSS), 
        VagrantStoryLocationData("Boss: Grissom and Dark Crusader - Snowfly Forest", "Vera Root", VagrantStoryLocationCategory.BOSS),        

    ],
    "Snowfly Forest East": [
        VagrantStoryLocationData("Chest: Snowfly Forest East - Natures Womb", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Damascus Crab NG+ - Snowfly Forest", "Vera Root", VagrantStoryLocationCategory.BOSS),        
    ],
    "Town Center East": [
        VagrantStoryLocationData("Chest: Town Center East - Gharmes Walk (Locked)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Town Center East - The House Gilgitte", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Town Center South": [
        VagrantStoryLocationData("Chest: Town Center South - The House Khazabas (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),
    ],
    "Town Center West": [],

    # Temporary Holder
    "Bosses": [
        # VagrantStoryLocationData("Lich - Boss", "Vera Root", VagrantStoryLocationCategory.BOSS), ?
        VagrantStoryLocationData("Marid and Ifrit - NG+", "Vera Root", VagrantStoryLocationCategory.BOSS),
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