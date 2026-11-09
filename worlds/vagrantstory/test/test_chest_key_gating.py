from test.bases import WorldTestBase

CHEST_KEY_LOCATIONS = [
    "WC - The Gallows - Chest",
    "AM2 - Hidden Resources - Chest",
    "AM2 - Hidden Resources - Chest - Grimoire Mollesse",
    "IM1 - The Branks - Chest",
    "KEP - The Warrior's Rest - Chest",
]


class _ChestKeyBase:
    game = "Vagrant Story"

    def test_chests_need_chest_key(self) -> None:
        for name in CHEST_KEY_LOCATIONS:
            loc = self.multiworld.get_location(name, 1)
            state = self.multiworld.get_all_state(False)
            state.prog_items[1].pop("Chest Key", None)
            self.assertFalse(loc.can_reach(state), f"{name} reachable without the Chest Key")

    def test_chests_reachable_with_chest_key(self) -> None:
        for name in CHEST_KEY_LOCATIONS:
            loc = self.multiworld.get_location(name, 1)
            state = self.multiworld.get_all_state(False)
            self.assertTrue(state.has("Chest Key", 1), "Chest Key missing from the pool")
            self.assertTrue(loc.can_reach(state), f"{name} unreachable even with everything")

    def test_other_chests_not_gated_by_chest_key(self) -> None:
        loc = self.multiworld.get_location("WC - The Reckoning Room - Chest", 1)
        state = self.multiworld.get_all_state(False)
        state.prog_items[1].pop("Chest Key", None)
        self.assertTrue(loc.can_reach(state))


class TestChestKeyVanilla(_ChestKeyBase, WorldTestBase):
    game = "Vagrant Story"
    run_default_tests = False
    options = {"progression_option": 0}


class TestChestKeyOpen(_ChestKeyBase, WorldTestBase):
    game = "Vagrant Story"
    run_default_tests = False
    options = {"progression_option": 1, "open_world_option": 0}
