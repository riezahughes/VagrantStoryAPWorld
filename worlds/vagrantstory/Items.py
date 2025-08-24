from enum import IntEnum
from typing import NamedTuple, List, Optional
import random
from BaseClasses import Item, ItemClassification # ItemClassification is used for internal logic, but not directly in MedievilItemData itself.


class VagrantStoryItemCategory(IntEnum):
    FILLER = 0
    GRIMOIRE = 2
    KEYS = 3
    SIGILS = 4
    CHAIN_ABILITY = 5
    DEFENCE_ABILITY = 6 
    TRAP = 7
    SKIP = 8


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
    VagrantStoryItemData("Gil (10)", 0, VagrantStoryItemCategory.FILLER, False),
    VagrantStoryItemData("Gil (20)", 1, VagrantStoryItemCategory.FILLER, False),
    VagrantStoryItemData("Gil (30)", 2, VagrantStoryItemCategory.FILLER, False),
    VagrantStoryItemData("Gil (40)", 3, VagrantStoryItemCategory.FILLER, False),
    VagrantStoryItemData("Gil (50)", 4, VagrantStoryItemCategory.FILLER, False)
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