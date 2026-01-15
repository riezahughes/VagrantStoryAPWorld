# world/dc2/__init__.py
from typing import Dict, Set, List

from BaseClasses import MultiWorld, Region, Item, Entrance, Tutorial, ItemClassification, CollectionState
from Options import Toggle

from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import set_rule, add_rule, add_item_rule

from .Items import VagrantStoryItem, VagrantStoryItemCategory, item_dictionary, key_item_names, item_descriptions, BuildItemPool
from .Locations import VagrantStoryLocation, VagrantStoryLocationCategory, VagrantStoryLocationData, location_tables, location_dictionary
from .Options import VagrantStoryOption, GoalOptions
from .VictoryConditions import defeat_guildenstern_dark_angel_victory
from .rooms import all_minor_regions


class VagrantStoryWeb(WebWorld):
    bug_report_page = ""
    theme = "stone"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Vagrant Story randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["RiezaHughes"],
    )

    tutorials = [setup_en]


class VagrantStoryWorld(World):
    """
    Vagrant Story is a game about an amnesiac 007 chasing after the ladies with some risky business
    """

    game: str = "Vagrant Story"
    explicit_indirect_conditions = False
    options_dataclass = VagrantStoryOption
    options: VagrantStoryOption
    topology_present: bool = True
    web = VagrantStoryWeb()
    data_version = 0
    base_id = 1230000
    enabled_location_categories: Set[VagrantStoryLocationCategory]
    required_client_version = (0, 5, 0)
    item_name_to_id = VagrantStoryItem.get_name_to_id()
    location_name_to_id = VagrantStoryLocation.get_name_to_id()
    item_name_groups = {}
    item_descriptions = item_descriptions

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.locked_items = []
        self.locked_locations = []
        self.main_path_locations = []
        self.enabled_location_categories = set()

    def generate_early(self):
        self.enabled_location_categories.add(VagrantStoryLocationCategory.FILLER)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.PROGRESSION)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.CHEST)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.BOSS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.BOSS_PLUS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.BOSS_UNLOCKS_PLUS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.GRIMOIRES)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.KEY_UNLOCKS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.SIGIL_UNLOCKS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.ROOD_INVERSE_UNLOCKS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.ABILITY_UNLOCKS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.BREAK_UNLOCKS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.FLOOR_TRAPS)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.PUZZLE_CLEAR)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.ROOM_ENTERED)
        self.enabled_location_categories.add(VagrantStoryLocationCategory.GAME_END)

    def create_regions(self):
        # Create Regions
        regions: Dict[str, Region] = {}

        regions["Menu"] = self.create_region("Menu", [])
        regions["Prologue"] = self.create_region("Prologue", location_tables["Prologue"])
        regions["Ashley"] = self.create_region("Ashley", location_tables["Ashley"])
        regions["Credits"] = self.create_region("Credits", location_tables["Credits"])

        # a new region is created for every minor region
        regions.update({region_name: self.create_region(region_name, location_tables[region_name]) for region_name in all_minor_regions})

        def create_connection(from_region: str, to_region: str):
            connection = Entrance(self.player, f"{from_region} -> {to_region}", regions[from_region])
            regions[from_region].exits.append(connection)
            connection.connect(regions[to_region])

        def create_room_connections(from_region: str, to_region: str, connection_name: str):
            connection = Entrance(self.player, connection_name, regions[from_region])
            regions[from_region].exits.append(connection)
            connection.connect(regions[to_region])

        # loop hell for the fucking hundreds of regions
        for region_name, data in all_minor_regions.items():
            exit_targets = [ex[0] for ex in data["exits"]]
            used_counts = {}

            for exit_target in data["exits"]:
                if exit_target in all_minor_regions:
                    if exit_targets.count(exit_target) > 1:
                        count = used_counts.get(exit_target, 1)
                        name = f"{region_name} -> {exit_target} ({count})"
                        used_counts[exit_target] = count + 1
                    else:
                        name = f"{region_name} -> {exit_target}"
                    create_room_connections(region_name, exit_target, name)

        create_connection("Menu", "Ashley")
        create_connection("Menu", "Prologue")
        create_connection("Prologue", "Entrance to Darkness")
        create_connection("Dome", "Credits")

    # For each region, add the associated locations retrieved from the corresponding location_table
    def create_region(self, region_name, location_table) -> Region:
        new_region = Region(region_name, self.player, self.multiworld)
        print(new_region.name, len(location_table))
        for location in location_table:
            if location.category in self.enabled_location_categories:
                new_location = VagrantStoryLocation(
                    self.player,
                    location.name,
                    location.category,
                    location.default_item,
                    self.location_name_to_id[location.name],
                    new_region,
                )
            else:
                event_item = self.create_item(location.default_item)
                new_location = VagrantStoryLocation(self.player, location.name, location.category, location.default_item, None, new_region)
                event_item.code = None
                # Cast the item to the correct type
                if isinstance(event_item, VagrantStoryItem):
                    new_location.place_locked_item(event_item)
            # Uncomment to print all locations
            # print(f"{self.location_name_to_id[location.name]}: {location.name}")
            new_region.locations.append(new_location)

        self.multiworld.regions.append(new_region)
        return new_region

    def create_items(self):
        randomized_location_count = 0
        for location in self.multiworld.get_locations(self.player):
            if not location.locked and location.address is not None:
                randomized_location_count += 1

        print(f"Requesting itempool size for randomized locations: {randomized_location_count}")

        # Call BuildItemPool to get a list of item NAMES (strings)
        item_names_to_add = BuildItemPool(randomized_location_count, self.options)

        generated_items: List[Item] = []
        for item_name in item_names_to_add:
            new_item = self.create_item(item_name)
            generated_items.append(new_item)

        print(f"Created item pool size: {len(generated_items)}")

        # Add the generated VagrantStoryItem objects to the multiworld's item pool
        self.multiworld.itempool.extend(generated_items)

    def create_item(self, name: str) -> Item:
        item_data = item_dictionary.get(name)

        if not item_data:
            # Fallback for unknown items. This indicates a data inconsistency.
            print(f"Warning: Attempted to create unknown item: {name}. Falling back to filler.")
            return VagrantStoryItem(name, ItemClassification.filler, None, self.player)

        # Determine the Archipelago ItemClassification based on VagrantStoryItemData.
        item_classification: ItemClassification

        if item_data.progression or item_data.category == VagrantStoryItemCategory.KEYS or item_data.category == VagrantStoryItemCategory.SIGILS:
            item_classification = ItemClassification.progression
        elif (
            item_data.category == VagrantStoryItemCategory.GRIMOIRE
            or item_data.category == VagrantStoryItemCategory.CHAIN_ABILITY
            or item_data.category == VagrantStoryItemCategory.DEFENCE_ABILITY
        ):
            item_classification = ItemClassification.useful
        else:  # Default for FILLER or other categories not explicitly useful/progression
            item_classification = ItemClassification.filler

        return VagrantStoryItem(name, item_classification, VagrantStoryItem.get_name_to_id()[name], self.player)

    def get_filler_item_name(self) -> str:
        return "Gil (50)"  # this clearly needs looked into

    def set_rules(self) -> None:
        for region in self.multiworld.get_regions(self.player):
            for location in region.locations:
                set_rule(location, lambda state: True)

        if self.options.goal.value == GoalOptions.DEFEAT_ANGEL:
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location("Game End: Credits", self.player)

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {}

        name_to_vagrant_story_code = {item.name: item.v_code for item in item_dictionary.values()}
        # Create the mandatory lists to generate the player's output file
        items_id = []
        items_address = []
        locations_id = []
        locations_address = []
        locations_target = []
        for location in self.multiworld.get_filled_locations():
            if location.item is not None:
                if location.item.player == self.player:
                    # we are the receiver of the item
                    items_id.append(location.item.code)
                    items_address.append(name_to_vagrant_story_code[location.item.name])

            if location.player == self.player:
                # we are the sender of the location check
                locations_address.append(item_dictionary[location_dictionary[location.name].default_item].v_code)
                locations_id.append(location.address)
                if location.item is not None:
                    if location.item.player == self.player:
                        locations_target.append(name_to_vagrant_story_code[location.item.name])
                    else:
                        locations_target.append(0)

        slot_data = {
            "options": {
                "guaranteed_items": self.options.guaranteed_items.value,
                "goal": self.options.goal.value,
                "deathlink": self.options.deathlink.value,
                "include_new_game_plus": self.options.include_new_game_plus.value,
                "include_puzzle_mode_checks": self.options.include_puzzle_mode_checks,
                "include_mid_boss_checks": self.options.include_mid_boss_checks.value,
                "progression_option": self.options.progression_option.value,
            },
            "seed": self.multiworld.seed_name,  # to verify the server's multiworld
            "slot": self.multiworld.player_name[self.player],  # to connect to server
            "base_id": self.base_id,  # to merge location and items lists
            "locationsId": locations_id,
            "locationsAddress": locations_address,
            "locationsTarget": locations_target,
            "itemsId": items_id,
            "itemsAddress": items_address,
        }

        return slot_data
