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
    GRIMOIRES = 5
    KEY_UNLOCKS = 6
    SIGIL_UNLOCKS = 7
    ROOD_INVERSE_UNLOCKS = 8
    ABILITY_UNLOCKS = 9
    BREAK_UNLOCKS = 10
    FLOOR_TRAPS = 11
    LEVEL_END = 12

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
            "Prologue",
            "Wine Cellar",
            "Catacombs",
            "Sanctum",
            "Abandoned Mines B1",
            "Abandoned Mines B2",
            "Limestone Quarry",
            "Temple of Kiltia",
            "Great Cathedral B1",
            "Great Cathedral L1",
            "Great Cathedral L2",
            "Great Cathedral L3",
            "Great Cathedral L4",
            "Forgotten Pathway",
            "Escapeway",
            "Iron Maiden B1",
            "Iron Maiden B2",
            "Iron Maiden B3",
            "Undercity West",
            "Undercity East",
            "The Keep",
            "City Walls West",
            "City Walls South",
            "City Walls East",
            "City Walls North",
            "Snowfly Forest",
            "Snowfly Forest East",
            "Town Center West",
            "Town Center East",
            "Town Center South",
            "Credits",
            "Ashley"
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


# VagrantStoryLocationData("Key Unlock: Rood Inverse - To Undercity West", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS), NEED TO FIND WHERE THIS IS USED


location_tables = {
    "Prologue": [
        VagrantStoryLocationData("Boss: Injured Wyvern - Prologue", "Vera Root", VagrantStoryLocationCategory.BOSS),
        # two soldiers at start?

    ],
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
        VagrantStoryLocationData("Sigil Unlock: Chamomile Sigil - Smokebarrel Stair", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Stock Sigil - Reopens The Gallows", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Chest Key - Wine Cellar", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),                
        VagrantStoryLocationData("Floor Trap: Gust - Wine Magnate's Chamber", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Heal - Smokebarrel Stair", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),

    ],
    "Catacombs": [
        VagrantStoryLocationData("Chest: Catacombs - Rodent-Ridden Chamber", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Catacombs - The Lamenting Mother", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Catacombs - Bandits Hideout", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Sigil Unlock: Lily Sigil - The Withered Spring", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),        
        VagrantStoryLocationData("Floor Trap: Cure - Hall of Sworn Revenge", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Freeze - The Weeping Corridor", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),    
    ],
    "Sanctum": [
        VagrantStoryLocationData("Chest: Sanctum - Alchemists Laboratory", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Golem - Sanctum", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Dragon - Sanctum", "Vera Root", VagrantStoryLocationCategory.BOSS),        
        VagrantStoryLocationData("Floor Trap: Heal - Priests Confinement", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),

    ],
    "Abandoned Mines B1": [
        VagrantStoryLocationData("Chest: Abandoned Mines B1 - Miners Resting Hall (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Abandoned Mines B1 - Coal Mine Storage", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Abandoned Mines B1 - Rust in Peace (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),     
        VagrantStoryLocationData("Chest: Abandoned Mines B1 - Mining Regrets", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Sigil Unlock: Fern Sigil - Live Long and Prosper", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Hyacinth Sigil - The Earthquake's Mark", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Silver Key - Abandoned Mines B1", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Floor Trap: Eruption - The Earthquake's Mark", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Poison - Coal Mine Storage", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Trap Clear - Coal Mine Storage", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),

        
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
        VagrantStoryLocationData("Key Unlock: Iron Key - Abandoned Mines B2", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Chest Key - Abandoned Mines B2", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Floor Trap: Cure - Desire's Passage", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
        VagrantStoryLocationData("Floor Trap: ??????? - Senses Lost", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
        VagrantStoryLocationData("Floor Trap: ????????? - Senses Lost", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
        VagrantStoryLocationData("Floor Trap: Diablolos - Crossing of Blood", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
        VagrantStoryLocationData("Floor Trap: Death Vapour - Crossing of Blood", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
        # Suididal Desires down here has shitloads of traps. Need to reach it to see just how many.
        VagrantStoryLocationData("Floor Trap: Trap Clear - Suicidal Desires", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: ???? - Suicidal Desires", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: ??? - Suicidal Desires", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: ?? - Suicidal Desires", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: ? - Suicidal Desires", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Heal - Lambs to the Slaughter", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Trap Clear - Bandits' Hollow", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Heal - Bandits' Hollow", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),

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
        VagrantStoryLocationData("Sigil Unlock: Aster Sigil - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Eulelia Sigil - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Melissa Sigil - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Gold Key 1 - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),  
        VagrantStoryLocationData("Key Unlock: Gold Key 2 - Limestone Quarry", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        # no mention of what this trap is
        VagrantStoryLocationData("Floor Trap: ???? - Atone for Eternity", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Heal - The Dreamers Climb", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Paralyze - The Labourers Bonfire", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
                                           
    ],
    "Temple of Kiltia": [
        VagrantStoryLocationData("Chest: Temple of Kiltia - The Chapel of Meschaunce", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Last Crusader - Temple of Kiltia", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Minotaur Lord - Temple of Kiltia", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Kali - Temple of Kiltia", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Key Unlock: Silver Key - Temple of Kiltia", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),                
        VagrantStoryLocationData("Floor Trap: Heal - The Dark Coast", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Trap Clear - The Dark Coast", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
      
    ],
    "Great Cathedral B1": [
        VagrantStoryLocationData("Boss: Marid - Great Cathedral B1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Ifrit - Great Cathedral B1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Iron Crab - Great Cathedral B1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Floor Trap: Heal - Struggle For the Soul, B1", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
    ],
    "Great Cathedral L1": [
        VagrantStoryLocationData("Chest: The Great Cathedral L1 - Where Darkness Spreads", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: The Great Cathedral L1 - The Flayed Confessional", "Vera Root", VagrantStoryLocationCategory.CHEST),            
        VagrantStoryLocationData("Boss: Arch Dragon - Great Cathedral L1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Djinn - Great Cathedral L1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Sigil Unlock: Laurel Sigil - Great Cathedral L1", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),                
        VagrantStoryLocationData("Floor Trap: Curse - Sin and Punishment, L1", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
        VagrantStoryLocationData("Floor Trap: Eruption - Sin and Punishment, L1", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),                     
    ],
    "Great Cathedral L2": [
        VagrantStoryLocationData("Chest: The Great Cathedral L2 - An Arrow into Darkness", "Vera Root", VagrantStoryLocationCategory.CHEST),   
        VagrantStoryLocationData("Boss: Flame Dragon - Great Cathedral L2", "Vera Root", VagrantStoryLocationCategory.BOSS),        
        VagrantStoryLocationData("Boss: Nightmare - Great Cathedral L2", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Sigil Unlock: Calla Sigil - Great Cathedral L2", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),        
        VagrantStoryLocationData("Sigil Unlock: Acacia Sigil - Great Cathedral L2", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Palm Sigil - Great Cathedral L2", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),                
        VagrantStoryLocationData("Floor Trap: Paralysis - Abasement From Above, L2", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),                     
        VagrantStoryLocationData("Floor Trap: Curse - Abasement From Above, L2", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),                     
        VagrantStoryLocationData("Floor Trap: Poison - Abasement From Above, L2", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),                     

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
        # There are two traps in the orgacle of sins no more but i've no information on what they are
        VagrantStoryLocationData("Floor Trap: ? - The Oracle Sins No More", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: ?? - The Oracle Sins No More", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Escapeway": [
        VagrantStoryLocationData("Chest: Escapeway - Where Body and Soul Part (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Escapeway - Buried Alice", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Key Unlock: Silver Key - Escapeway", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Gold Key - Escapeway", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),   
        # There's an unknown number of traps in this room below. Needs investigated. Just putting 1 here for now.
        VagrantStoryLocationData("Floor Trap: ??? - Blood & The Beast", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Diabolos - Facing Your Illusions", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS) 
        
    ],
    "Iron Maiden B1": [
        VagrantStoryLocationData("Chest: Iron Maiden B1 - The Wheel (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B1 - The Judas Cradle", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B1 - The Ducking Stool", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B1 - The Branks (Locked)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Wyvern Knight - Iron Maiden B1", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Iron Golem - Iron Maiden B1", "Vera Root", VagrantStoryLocationCategory.BOSS),        
        VagrantStoryLocationData("Boss: Wyvern Queen NG+ - Iron Maiden B1", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("Sigil Unlock: Tearose Sigil - Iron Maiden B1", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Chest Key - Iron Maiden B1", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Steel Key - Iron Maiden B1", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Floor Trap: Gust - Heretic's Fork", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Freeze - Heretic's Fork", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Eruption - Blooding", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Death Vapour - Blooding", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
        VagrantStoryLocationData("Floor Trap: Terra Thrust - Burning", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
    ],
    "Iron Maiden B2": [
        VagrantStoryLocationData("Chest: Iron Maiden B2 - Lead Sprinkler", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B2 - Squassation", "Vera Root", VagrantStoryLocationCategory.CHEST),        
        VagrantStoryLocationData("Boss: Dark Dragon NG+ - Iron Maiden B2", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("Boss: Ravana NG+ - Iron Maiden B2", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("Boss: Dragon Zombie NG+ - Iron Maiden B2", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("Boss: Ogre Zombie NG+ - Iron Maiden B2", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("Boss: Death NG+ - Iron Maiden B2", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("Floor Trap: Gust - The Mind Burns", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS), 
        # The Cold's Bridle has 3 unknown traps. Need to reach it to see what they are.
        VagrantStoryLocationData("Floor Trap: ? - The Cold's Bridle ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS), 
        VagrantStoryLocationData("Floor Trap: ?? - The Cold's Bridle ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS), 
        VagrantStoryLocationData("Floor Trap: ??? - The Cold's Bridle ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Paralysis - Lead Sprinkler ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),      
        VagrantStoryLocationData("Floor Trap: Terra Thrust - Squassation ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),     
        VagrantStoryLocationData("Floor Trap: Poison - Squassation ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),    
        # 1 unknown trap in the pendulum room        
        VagrantStoryLocationData("Floor Trap: ??? - Pendulum ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS), 
        # 1 unknown trap in the dragging room
        VagrantStoryLocationData("Floor Trap: ??? - Dragging ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        # 1 unknown trap in the tongue slicer room
        VagrantStoryLocationData("Floor Trap: ??? - Tongue Slicer ", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),                     
    ],
    "Iron Maiden B3": [
        VagrantStoryLocationData("Chest: Iron Maiden B3 - Saint Elmos Belt", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Iron Maiden B3 - Dunking the Witch", "Vera Root", VagrantStoryLocationCategory.CHEST),        
        VagrantStoryLocationData("Boss: Asura NG+ - Iron Maiden B3", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
    ],
    "Undercity West": [
        VagrantStoryLocationData("Chest: Undercity West - The Childrens Hideout", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Undercity West - Larder for a Lean Winter", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Undercity West - The Crumbling Market", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Dark Elemental - Undercity West", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Shadow - Undercity West", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Giant Crab - Undercity West", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Key Unlock: Iron Key - Undercity West", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS), 
        VagrantStoryLocationData("Key Unlock: Silver Key - Undercity West", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Gold Key 1 - Undercity West", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),  
        VagrantStoryLocationData("Key Unlock: Gold Key 2 - Undercity West", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),                   
        VagrantStoryLocationData("Sigil Unlock: Mandrake Sigil - Undercity West", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Cattleya Sigil - Undercity West", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Floor Trap: Gust - Crossroads of Rest", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        # Theres another huge pile of traps in the Crumbling Market. Need to reach it to see how many.
        VagrantStoryLocationData("Floor Trap: ???? - The Crumbling Market", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),    
        VagrantStoryLocationData("Floor Trap: Poison - Salvation for the Mother", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),                               

    ],
    "Undercity East": [
        VagrantStoryLocationData("Chest: Undercity East - Weapons Not Allowed", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Undercity East - Sale of the Sword", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Undercity East - Catspaw Blackmarket", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Harpy - Undercity East", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Nightstalker - Undercity East", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Boss: Neesa and Tieger - Undercity East", "Vera Root", VagrantStoryLocationCategory.BOSS),
        VagrantStoryLocationData("Key Unlock: Iron Key - Undercity East", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),        
        VagrantStoryLocationData("Floor Trap: Gust - The Pirate's Son", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        VagrantStoryLocationData("Floor Trap: Clear Trap - Catspaw Blackmarket", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
        # No idea what this one is either
        VagrantStoryLocationData("Floor Trap: ???? - Catspaw Blackmarket", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),
                        
    ],
    "The Keep": [
        VagrantStoryLocationData("Chest: The Keep - The Warriors Rest (Locked)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Damascus Golem NG+ - The Keep", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("Sigil Unlock: Kalmia Sigil - The Keep", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),        
        VagrantStoryLocationData("Key Unlock: Chest Key - The Keep", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Platinum Key - To Snowfly Forest East", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),        
        VagrantStoryLocationData("Sigil Unlock: Anemone Sigil - The Keep", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Colombine Sigil - The Keep", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Marigold Sigil - The Keep", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Schirra Sigil - The Keep", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Tigertail Sigil - The Keep", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Verbena Sigil - The Keep", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),                       
        VagrantStoryLocationData("Sigil Unlock: Azalea Sigil - The Keep", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),        
    ],
    "City Walls West": [
        VagrantStoryLocationData("Boss: Duane + 2 Crimson Knights - City Walls West", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "City Walls South": [
        VagrantStoryLocationData("Boss: Jan Rosencrantz - City Walls South", "Vera Root", VagrantStoryLocationCategory.BOSS),
    ],
    "City Walls East": [],
    "City Walls North": [
        VagrantStoryLocationData("Key Unlock: Iron Key - City Walls North", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Sigil Unlock: Clematis Sigil - A Welcome Invasion", "Vera Root", VagrantStoryLocationCategory.SIGIL_UNLOCKS),                
    ],
    "Snowfly Forest": [
        VagrantStoryLocationData("Chest: Snowfly Forest - Forest River", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Snowfly Forest - Hewn from Nature", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Earth Dragon - Snowfly Forest", "Vera Root", VagrantStoryLocationCategory.BOSS), 
        VagrantStoryLocationData("Boss: Grissom and Dark Crusader - Snowfly Forest", "Vera Root", VagrantStoryLocationCategory.BOSS),        

    ],
    "Snowfly Forest East": [
        VagrantStoryLocationData("Chest: Snowfly Forest East - Natures Womb", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Boss: Damascus Crab NG+ - Snowfly Forest", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),        
    ],
    "Town Center East": [
        VagrantStoryLocationData("Chest: Town Center East - Gharmes Walk (Locked)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Chest: Town Center East - The House Gilgitte", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Key Unlock: Bronze Key - Town Center East", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Key Unlock: Chest Key - Town Center East", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),                
    ],
    "Town Center South": [
        VagrantStoryLocationData("Chest: Town Center South - The House Khazabas (Magic Lock)", "Vera Root", VagrantStoryLocationCategory.CHEST),
        VagrantStoryLocationData("Key Unlock: Bronze Key - Town Center South", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),        
    ],
    "Town Center West": [
        VagrantStoryLocationData("Boss: Marid and Ifrit NG+", "Vera Root", VagrantStoryLocationCategory.BOSS_PLUS),
        VagrantStoryLocationData("Key Unlock: Crimson Key - To Town Center West", "Vera Root", VagrantStoryLocationCategory.KEY_UNLOCKS),
        VagrantStoryLocationData("Floor Trap: Heal - The Rene Coastroad", "Vera Root", VagrantStoryLocationCategory.FLOOR_TRAPS),        
    ],
    "Credits": [
        VagrantStoryLocationData("Level End: Credits", "Vera Root", VagrantStoryLocationCategory.LEVEL_END),
    ],
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
    ]
}

location_dictionary: Dict[str, VagrantStoryLocationData] = {}#
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})