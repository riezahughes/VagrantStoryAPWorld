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
    NAMED_WEAPON = 10
    BLADE_PARTS = 11
    GRIP_PARTS = 12
    SHIELD_PARTS = 13
    ARMOUR = 14
    TRAP = 15
    SKIP = 16


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
    VagrantStoryItemData("Crimson Pain Chain Ability", 117, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Dulling Impact Chain Ability", 118, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Gain Life Chain Ability", 119, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Gain Magic Chain Ability", 120, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Heavy Shot Chain Ability", 121, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Instill Chain Ability", 122, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Mind Ache Chain Ability", 123, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Mind Assault Chain Ability", 124, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Numbing Claw Chain Ability", 125, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Paralysis Pulse Chain Ability", 126, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Phantom Pain Chain Ability", 127, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Raging Ache Chain Ability", 128, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Snake Venom Chain Ability", 129, VagrantStoryItemCategory.CHAIN_ABILITY, False),
    VagrantStoryItemData("Temper Chain Ability", 130, VagrantStoryItemCategory.CHAIN_ABILITY, False),

    # Defence Abilities
    VagrantStoryItemData("Absorb Damage Defence Ability", 131, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Absorb Magic Defence Ability", 132, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Aqua Ward Defence Ability", 133, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Demonscale Defence Ability", 134, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Fireproof Defence Ability", 135, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Impact Guard Defence Ability", 136, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Phantom Shield Defence Ability", 137, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Reflect Damage Defence Ability", 138, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Reflect Magic Defence Ability", 139, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Shadow Guard Defence Ability", 140, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Siphon Soul Defence Ability", 141, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Terra Ward Defence Ability", 142, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Ward Defence Ability", 143, VagrantStoryItemCategory.DEFENCE_ABILITY, False),
    VagrantStoryItemData("Windbreak Defence Ability", 144, VagrantStoryItemCategory.DEFENCE_ABILITY, False),


    # Break Arts
    VagrantStoryItemData("Mistral Edge Break Art", 145, VagrantStoryItemCategory.BREAK_ARTS, False), # Axe and Mace
    VagrantStoryItemData("Glacial Gale Break Art", 146, VagrantStoryItemCategory.BREAK_ARTS, False), # Axe and Mace
    VagrantStoryItemData("Killer Mantis Break Art", 147, VagrantStoryItemCategory.BREAK_ARTS, False), # Axe and Mace
    VagrantStoryItemData("Black Nebula Break Art", 148, VagrantStoryItemCategory.BREAK_ARTS, False), # Axe and Mace
    VagrantStoryItemData("Lotus Palm Break Art", 149, VagrantStoryItemCategory.BREAK_ARTS, False), # Bare Hands
    VagrantStoryItemData("Vertigo Break Art", 150, VagrantStoryItemCategory.BREAK_ARTS, False), # Bare Hands
    VagrantStoryItemData("Vermillion Aura Break Art", 151, VagrantStoryItemCategory.BREAK_ARTS, False), # Bare Hands
    VagrantStoryItemData("Retribution Break Art", 152, VagrantStoryItemCategory.BREAK_ARTS, False), # Bare Hands
    VagrantStoryItemData("Brimstone Hail Break Art", 153, VagrantStoryItemCategory.BREAK_ARTS, False), # Crossbow
    VagrantStoryItemData("Heaven's Scorn Break Art", 154, VagrantStoryItemCategory.BREAK_ARTS, False), # Crossbow
    VagrantStoryItemData("Death Wail Break Art", 155, VagrantStoryItemCategory.BREAK_ARTS, False), # Crossbow
    VagrantStoryItemData("Sanctus Flare Break Art", 156, VagrantStoryItemCategory.BREAK_ARTS, False), # Crossbow
    VagrantStoryItemData("Whistle Sting Break Art", 157, VagrantStoryItemCategory.BREAK_ARTS, False), # Dagger
    VagrantStoryItemData("Shadowweave Break Art", 158, VagrantStoryItemCategory.BREAK_ARTS, False), # Dagger
    VagrantStoryItemData("Double Fang Break Art", 159, VagrantStoryItemCategory.BREAK_ARTS, False), # Dagger
    VagrantStoryItemData("Wyrm Scorn Break Art", 160, VagrantStoryItemCategory.BREAK_ARTS, False), # Dagger
    VagrantStoryItemData("Bear Claw Break Art", 161, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Axe
    VagrantStoryItemData("Accursed Umbra Break Art", 162, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Axe
    VagrantStoryItemData("Iron Ripper Break Art", 163, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Axe
    VagrantStoryItemData("Emetic Bomb Break Art", 164, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Axe
    VagrantStoryItemData("Sunder Break Art", 165, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Sword
    VagrantStoryItemData("Thunderwave Break Art", 166, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Sword
    VagrantStoryItemData("Swallow Slash Break Art", 167, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Sword
    VagrantStoryItemData("Advent Sign Break Art", 168, VagrantStoryItemCategory.BREAK_ARTS, False), # Great Sword
    VagrantStoryItemData("Bonecrusher Break Art", 169, VagrantStoryItemCategory.BREAK_ARTS, False), # Heavy Mace
    VagrantStoryItemData("Quickshock Break Art", 170, VagrantStoryItemCategory.BREAK_ARTS, False), # Heavy Mace
    VagrantStoryItemData("Ignis Wheel Break Art", 171, VagrantStoryItemCategory.BREAK_ARTS, False), # Heavy Mace
    VagrantStoryItemData("Hex Flux Break Art", 172, VagrantStoryItemCategory.BREAK_ARTS, False), # Heavy Mace
    VagrantStoryItemData("Ruination Break Art", 173, VagrantStoryItemCategory.BREAK_ARTS, False), # Polearm
    VagrantStoryItemData("Scythe Wind Break Art", 174, VagrantStoryItemCategory.BREAK_ARTS, False), # Polearm
    VagrantStoryItemData("Giga Tempest Break Art", 175, VagrantStoryItemCategory.BREAK_ARTS, False), # Polearm
    VagrantStoryItemData("Spiral Scourge Break Art", 176, VagrantStoryItemCategory.BREAK_ARTS, False), # Polearm
    VagrantStoryItemData("Sirocco Break Art", 177, VagrantStoryItemCategory.BREAK_ARTS, False), # Staff
    VagrantStoryItemData("Riskbreak Break Art", 178, VagrantStoryItemCategory.BREAK_ARTS, False), # Staff
    VagrantStoryItemData("Gravis Aether Break Art", 179, VagrantStoryItemCategory.BREAK_ARTS, False), # Staff
    VagrantStoryItemData("Trinity Pulse Break Art", 180, VagrantStoryItemCategory.BREAK_ARTS, False), # Staff
    VagrantStoryItemData("Rending Gale Break Art", 181, VagrantStoryItemCategory.BREAK_ARTS, False), # Sword
    VagrantStoryItemData("Vile Scar Break Art", 182, VagrantStoryItemCategory.BREAK_ARTS, False), # Sword
    VagrantStoryItemData("Cherry Ronde Break Art", 183, VagrantStoryItemCategory.BREAK_ARTS, False), # Sword
    VagrantStoryItemData("Papillon Reel Break Art", 184, VagrantStoryItemCategory.BREAK_ARTS, False), # Sword

    # Unique Named Weapons
    VagrantStoryItemData("Fandango", 185, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Tovarisch", 187, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Seventh Heaven", 188, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Rusty Nail", 189, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Pink Squirrel", 190, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Shandy Gaff", 191, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Soul Kiss", 192, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Bosom Cleaver", 193, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Stinger", 194, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("White Cargo", 195, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Balin's Revenge", 196, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Sweet Death", 197, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Corpse Reviver", 198, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Sweet Sorrow", 199, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Eviscerator", 200, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Affinity", 201, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Dog's Nose", 202, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Pirate's Mate", 203, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Klondike", 204, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Ribsplitter", 205, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Mojito", 206, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Matador", 207, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Death Sentence", 208, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("White Lady", 209, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Angel Face", 210, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Frost Maiden", 211, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("White Rose", 212, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Bellini", 213, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Balalaika", 214, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Bull Shot", 215, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Sonora", 216, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Red Viking", 217, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Angel Lance", 218, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Magnolia Frau", 219, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Shillelagh", 220, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Czarine", 221, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Pussyfoot", 222, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Angel Kiss", 223, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Diki Diki", 224, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Blackthorn", 225, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Fallen Angel", 226, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Excalibur", 227, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Brionac", 228, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Isolde", 229, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Mjolnir", 230, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Pinaka", 231, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Sarnga", 232, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Izanagi", 233, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Dainslaif", 234, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Ascalon", 235, VagrantStoryItemCategory.NAMED_WEAPON, False),
    VagrantStoryItemData("Angel Wing", 236, VagrantStoryItemCategory.NAMED_WEAPON, False),

    # Blade Parts

    VagrantStoryItemData("Battle Knife", 257, VagrantStoryItemCategory.BLADE_PARTS, False, ), # Daggers
    VagrantStoryItemData("Scramasax", 258, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Dirk", 259, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Throwing Knife", 260, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Kudi", 261, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Cinquedea", 262, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Kris", 263, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Hatchet", 264, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Khukuri", 265, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Baselard", 266, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Stiletto", 267, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Jamadhar", 268, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Spatha", 269, VagrantStoryItemCategory.BLADE_PARTS, False, ), # Swords
    VagrantStoryItemData("Scimitar", 270, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Rapier", 271, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Short Sword", 272, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Firangi", 273, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Shamshir", 274, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Falchion", 275, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Shotel", 276, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Khora", 277, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Khopesh", 278, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Wakizashi", 279, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Rhomphaia", 280, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Broad Sword", 281, VagrantStoryItemCategory.BLADE_PARTS, False, ), # Great Swords
    VagrantStoryItemData("Norse Sword", 282, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Katana", 283, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Executioner", 284, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Claymore", 285, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Schiavona", 286, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Bastard Sword", 287, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Nodachi", 288, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Rune Blade", 289, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Holy Win", 290, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Hand Axe", 291, VagrantStoryItemCategory.BLADE_PARTS, False, ), # Axes and Maces
    VagrantStoryItemData("Goblin Club", 292, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Battle Axe", 293, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Spiked Club", 294, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Francisca", 295, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Ball Mace", 296, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Tabarzin", 297, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Footman's Mace", 298, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Chamkaq", 299, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Morning Star", 300, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Tabar", 301, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("War Hammer", 302, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Bullova", 303, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Bec de Corbin", 304, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Crescent", 305, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("War Maul", 306, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Guisarme", 307, VagrantStoryItemCategory.BLADE_PARTS, False, ), # Great Axes
    VagrantStoryItemData("Large Crescent", 308, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Sabre Halberd", 309, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Balbriggan", 310, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Double Blade", 311, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Halberd", 312, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Wizard Staff", 313, VagrantStoryItemCategory.BLADE_PARTS, False, ), # Staves
    VagrantStoryItemData("Clergy Rod", 314, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Summoner Baton", 315, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Shamanic Staff", 316, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Bishop's Crosier", 317, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Sage Cane", 318, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Langdebeve", 319, VagrantStoryItemCategory.BLADE_PARTS, False, ), # Heavy Maces
    VagrantStoryItemData("Sabre Mace", 320, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Footman's Mace", 321, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Gloomwing", 322, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Mjolnir", 323, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Hand of Light", 324, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Griever", 325, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Destroyer", 326, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Spear", 327, VagrantStoryItemCategory.BLADE_PARTS, False, ), # Polearms
    VagrantStoryItemData("Glaive", 328, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Scorpion", 329, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Corcesca", 330, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Trident", 331, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Awl Pike", 332, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Boar Spear", 333, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Fauchard", 334, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Voulge", 335, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Pole Axe", 336, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Bardysh", 337, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Brandestoc", 338, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Gastraph Bow", 339, VagrantStoryItemCategory.BLADE_PARTS, False, ), # crossbows
    VagrantStoryItemData("Light Crossbow", 340, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Target Bow", 341, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Windlass", 342, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Cranequin", 343, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Lug Crossbow", 344, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Siege Bow", 345, VagrantStoryItemCategory.BLADE_PARTS, False, ),
    VagrantStoryItemData("Arbalest", 346, VagrantStoryItemCategory.BLADE_PARTS, False, ),

    # Grip Parts

    VagrantStoryItemData("Short Hilt", 347, VagrantStoryItemCategory.GRIP_PARTS, False), # Daggers, Swords and GreatSwords
    VagrantStoryItemData("Swept Hilt", 348, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Cross Guard", 349, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Knuckle Guard", 350, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Counter Guard", 351, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Side Ring", 352, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Power Palm", 353, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Murderer's Hilt", 354, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Spiral Hilt", 355, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Wooden Grip", 356, VagrantStoryItemCategory.GRIP_PARTS, False), # Axes, Maces and Staves
    VagrantStoryItemData("Sand Face", 357, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Grimoire Grip", 358, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Czekan Type", 359, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Sarissa Grip", 360, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Heavy Grip", 361, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Gendarme", 362, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Runkasyle", 363, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Bhuj Type", 364, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Elephant", 365, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Wooden Pole", 366, VagrantStoryItemCategory.GRIP_PARTS, False), # Polearms
    VagrantStoryItemData("Spiculum Pole", 367, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Winged Pole", 368, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Ahlspies", 369, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Framea Pole", 370, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Spiral Pole", 371, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Simple Bolt", 372, VagrantStoryItemCategory.GRIP_PARTS, False), # CrossBow
    VagrantStoryItemData("Steel Bolt", 373, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Stone Bullet", 374, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Javelin Bolt", 375, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Falarica Bolt", 376, VagrantStoryItemCategory.GRIP_PARTS, False),
    VagrantStoryItemData("Sonic Bullet", 377, VagrantStoryItemCategory.GRIP_PARTS, False),


    # Shield Parts

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