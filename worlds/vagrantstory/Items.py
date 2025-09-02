from enum import IntEnum
from typing import NamedTuple, List, Optional
import random
from BaseClasses import Item, ItemClassification # ItemClassification is used for internal logic, but not directly in MedievilItemData itself.


class VagrantStoryItemCategory(IntEnum):
    FILLER = 0
    RECOVERY = 1
    PERM_STAT_BOOST = 2
    TEMP_STAT_BOOST = 3
    GRIMOIRE = 4
    KEYS = 5
    SIGILS = 6
    CHAIN_ABILITY = 7
    DEFENCE_ABILITY = 8
    BREAK_ARTS = 9
    TRAP = 10
    SKIP = 11


class VagrantStoryItemData(NamedTuple):
    name: str
    v_code: Optional[int] # Changed to Optional[int] for flexibility with None
    category: VagrantStoryItemCategory
    progression: bool # Added 'progression' field to the raw data


class VagrantStoryItem(Item):
    game: str = "Vagrant Story"
    category:VagrantStoryItemCategory
    v_code: Optional[int] # Make m_code an instance attribute for MedievilItem

    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int):
        super().__init__(name, classification, code, player)
        # The 'advancement' attribute is automatically handled by the parent Item class
        # if ItemClassification.progression is passed to its constructor.
        # You can explicitly set it here for clarity if you prefer, but BaseClasses.Item does this.
        # self.advancement = classification == ItemClassification.progression

        # Store game-specific data directly on the item instance
        item_data = item_dictionary.get(name)
        if item_data:
            self.v_code = item_data.v_code
            self.category = item_data.category
        else:
            self.v_code = None
            self.category = VagrantStoryItemCategory.FILLER # Fallback for unknown items


    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 9901000 
        # Create a dictionary mapping item names to their unique Archipelago IDs.
        return {item_data.name: (base_id + item_data.v_code) 
                for item_data in _all_items if item_data.v_code is not None}


key_item_names = {

}


_all_items: List[VagrantStoryItemData] = [

    # Recovery Items
    VagrantStoryItemData("Cure Root",1, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Cure Bulb",2, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Cure Tonic",3, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Cure Potion",4, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Mana Root",5, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Mana Bulb",6, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Mana Tonic",7, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Mana Potion",8, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Vera Root",9, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Vera Bulb",10, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Vera Tonic",11, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Vera Potion",12, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Acolyte's Nostrum", 13, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Saint's Nostrum", 14, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Alchemist's Reagent", 15, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Sorcerer's Reagent", 16, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Yggdrasil's Tears", 17, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Faerie Chortle", 18, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Spirit Orison", 19, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Angelic Paean", 20, VagrantStoryItemCategory.RECOVERY, False),
    VagrantStoryItemData("Panacea", 21, VagrantStoryItemCategory.RECOVERY, False),

    # Permanent Buffs
    VagrantStoryItemData("Elixir of Queens", 22, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Elixir of Mages", 23, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Elixir of Kings", 24, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Elixir of Sages", 25, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Elixir of Dragoon", 26, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Audentia", 27, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Virtus", 28, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Valens", 29, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Prudens", 30, VagrantStoryItemCategory.PERM_STAT_BOOST, False),
    VagrantStoryItemData("Volare", 31, VagrantStoryItemCategory.PERM_STAT_BOOST, False),

    # Temporary Stat Boosts
    VagrantStoryItemData("Snowfly Draught", 31, VagrantStoryItemCategory.TEMP_STAT_BOOST, False), # Technically a dispel, but this works.
    VagrantStoryItemData("Faerie Wing", 32, VagrantStoryItemCategory.TEMP_STAT_BOOST, False),
    VagrantStoryItemData("Eye of Argo", 33, VagrantStoryItemCategory.TEMP_STAT_BOOST, False),

    # Grimoires
    VagrantStoryItemData("Grimoire Guerir", 34, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Mollese", 35, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Antidote", 36, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Benir", 37, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Purifier", 38, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Vie", 39, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Sylphe", 40, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Salamandre", 41, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Gnome", 42, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Undine", 43, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Parebrise", 44, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Ignifuge", 45, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Rempart", 46, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Barrer", 47, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Zephyr", 48, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Teslae", 49, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Incendie", 50, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Terre", 51, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Glace", 52, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Lux", 53, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Patire", 54, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Exsorcer", 55, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Banish", 56, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Demolir", 57, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Foudre", 58, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Flamme", 59, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Gaea", 60, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Avalanche", 61, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Radius", 62, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Meteore", 63, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Egout", 64, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Deamance", 65, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Intensite", 66, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Debile", 67, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Eclairer", 68, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Naugeux", 69, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Agilite", 70, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Tardif", 71, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Ameliore", 72, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Deteriorer", 73, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Annuler", 74, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Paralysie", 75, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Venin", 76, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Fleau", 77, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Muet", 78, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Halte", 79, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Dissiper", 80, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Clef", 81, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Visible", 82, VagrantStoryItemCategory.GRIMOIRE, False),
    VagrantStoryItemData("Grimoire Analysis", 83, VagrantStoryItemCategory.GRIMOIRE, False),

    # Keys
    VagrantStoryItemData("Bronze Key", 84, VagrantStoryItemCategory.KEYS, True),
    VagrantStoryItemData("Chest Key", 85, VagrantStoryItemCategory.KEYS, True),
    VagrantStoryItemData("Crimson Key", 86, VagrantStoryItemCategory.KEYS, True),
    VagrantStoryItemData("Gold Key", 87, VagrantStoryItemCategory.KEYS, True),
    VagrantStoryItemData("Iron Key", 88, VagrantStoryItemCategory.KEYS, True),
    VagrantStoryItemData("Platinum Key", 89, VagrantStoryItemCategory.KEYS, True),
    VagrantStoryItemData("Rood Inverse", 90, VagrantStoryItemCategory.KEYS, True),
    VagrantStoryItemData("Silver Key", 91, VagrantStoryItemCategory.KEYS, True),
    VagrantStoryItemData("Steel Key", 92, VagrantStoryItemCategory.KEYS, True),

    # Sigils
    VagrantStoryItemData("Acacia Sigil", 93, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Anemone Sigil", 94, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Aster Sigil", 95, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Azalea Sigil", 96, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Calla Sigil", 97, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Cattleya Sigil", 98, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Chamomile Sigil", 99, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Clematis Sigil", 100, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Columbine Sigil", 101, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Eulalia Sigil", 102, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Fern Sigil", 103, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Hyacith Sigil", 104, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Kalmia Sigil", 105, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Laurel Sigil", 106, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Lily Sigil", 107, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Mandrake Sigil", 108, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Marigold Sigil", 109, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Melissa Sigil", 110, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Palm Sigil", 111, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Schirra Sigil", 112, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Stock Sigil", 113, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Tearose Sigil", 114, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Tigertail Sigil", 115, VagrantStoryItemCategory.SIGILS, True),
    VagrantStoryItemData("Verbana Sigil", 116, VagrantStoryItemCategory.SIGILS, True),

    # Chain Abilities
    VagrantStoryItemData("Crimson Pain Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Dulling Impact Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Gain Life Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Gain Magic Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Heavy Shot Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Instill Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Mind Ache Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Mind Assault Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Numbing Claw Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Paralysis Pulse Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Phantom Pain Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Raging Ache Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Snake Venom Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Temper Chain Ability", 0, VagrantStoryItemCategory.CHAIN_ABILITY, False),

    # Defence Abilities
    VagrantStoryItemData("Absorb Damage Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Absorb Magic Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Aqua Ward Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Demonscale Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Fireproof Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Impact Guard Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Phantom Shield Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Reflect Damage Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Reflect Magic Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Shadow Guard Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Siphon Soul Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Terra Ward Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Ward Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Windbreak Defence Ability", 0, VagrantStoryItemCategory.DEFENCE_ABILITY, False),


    # Break Arts
    VagrantStoryItemData("Mistral Edge Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Axe and Mace
    VagrantStoryItemData("Glacial Gale Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Axe and Mace
    VagrantStoryItemData("Killer Mantis Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Axe and Mace
    VagrantStoryItemData("Black Nebula Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Axe and Mace
    VagrantStoryItemData("Lotus Palm Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Bare Hands
    VagrantStoryItemData("Vertigo Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Bare Hands
    VagrantStoryItemData("Vermillion Aura Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Bare Hands
    VagrantStoryItemData("Retribution Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Bare Hands
    VagrantStoryItemData("Brimstone Hail Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Crossbow
    VagrantStoryItemData("Heaven's Scorn Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Crossbow
    VagrantStoryItemData("Death Wail Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Crossbow
    VagrantStoryItemData("Sanctus Flare Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Crossbow
    VagrantStoryItemData("Whistle Sting Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Dagger
    VagrantStoryItemData("Shadowweave Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Dagger
    VagrantStoryItemData("Double Fang Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Dagger
    VagrantStoryItemData("Wyrm Scorn Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Dagger
    VagrantStoryItemData("Bear Claw Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Axe
    VagrantStoryItemData("Accursed Umbra Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Axe
    VagrantStoryItemData("Iron Ripper Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Axe
    VagrantStoryItemData("Emetic Bomb Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Axe
    VagrantStoryItemData("Sunder Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Sword
    VagrantStoryItemData("Thunderwave Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Sword
    VagrantStoryItemData("Swallow Slash Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Sword
    VagrantStoryItemData("Advent Sign Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Sword
    VagrantStoryItemData("Bonecrusher Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Heavy Mace
    VagrantStoryItemData("Quickshock Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Heavy Mace
    VagrantStoryItemData("Ignis Wheel Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Heavy Mace
    VagrantStoryItemData("Hex Flux Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Heavy Mace
    VagrantStoryItemData("Ruination Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Polearm
    VagrantStoryItemData("Scythe Wind Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Polearm
    VagrantStoryItemData("Giga Tempest Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Polearm
    VagrantStoryItemData("Spiral Scourge Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Polearm
    VagrantStoryItemData("Sirocco Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Staff
    VagrantStoryItemData("Riskbreak Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Staff
    VagrantStoryItemData("Gravis Aether Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Staff
    VagrantStoryItemData("Trinity Pulse Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Staff
    VagrantStoryItemData("Rending Gale Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Sword
    VagrantStoryItemData("Vile Scar Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Sword
    VagrantStoryItemData("Cherry Ronde Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Sword
    VagrantStoryItemData("Papillon Reel Break Art", 0, VagrantStoryItemCategory.BREAK_ARTS, False), # Sword

]
# Convert raw list of tuples into MedievilItemData NamedTuple instances
# _all_items = [VagrantStoryItemData(row[0], row[1], row[2], row[3]) for row in _all_items]


item_descriptions = {
    # Optional: Add detailed descriptions for items here
    # "Gold (50)": "A small pouch of gold coins."
}

# Create a dictionary for quick lookup of item data by name
item_dictionary: dict[str, VagrantStoryItemData] = {item_data.name: item_data for item_data in _all_items}


def BuildItemPool(count: int, options) -> List[str]:
    """
    Generates a list of item names to be used for the item pool.
    This function does NOT create Archipelago Item objects; it only provides their names.
    The actual Item objects are created in MedievilWorld.create_items.

    Args:
        count (int): The total number of item names to generate.
        options: The options object from the Archipelago multiworld, used for guaranteed items.

    Returns:
        List[str]: A shuffled list of item names.
    """
    item_pool_names: List[str] = []
    
    # Add any guaranteed items specified in the options first
    if hasattr(options, "guaranteed_items") and options.guaranteed_items.value:
        for item_name in options.guaranteed_items.value:
            if item_name in item_dictionary:
                item_pool_names.append(item_name)
            else:
                print(f"Warning: Guaranteed item '{item_name}' not found in item_dictionary. Skipping.")
                
    # this needs adjusted for VS
    progression_and_weapon_items = [
        item_data.name for item_data in _all_items
        if item_data.progression or item_data.category == VagrantStoryItemCategory.GRIMOIRE
    ]
    
    for item_name in progression_and_weapon_items:
        if item_name not in item_pool_names and len(item_pool_names) < count:
                item_pool_names.append(item_name)
    
    # Populate the rest of the pool with random filler items
    filler_item_names = [item_data.name for item_data in _all_items 
                         if item_data.category == VagrantStoryItemCategory.FILLER or item_data.category == VagrantStoryItemCategory.TRAP]
    

    for _ in range(count - len(item_pool_names)):
        if filler_item_names:
            item_name_to_add = random.choice(filler_item_names)
            item_pool_names.append(item_name_to_add)
        else:
            print("Warning: Ran out of filler items for Medievil. Duplicating from all available items.")
            # Fallback: if no specific filler items left, pick from any available item
            item_pool_names.append(random.choice(list(item_dictionary.keys())))

    random.shuffle(item_pool_names) # Shuffle the final list of item names
    return item_pool_names