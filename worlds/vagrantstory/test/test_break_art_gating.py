from BaseClasses import CollectionState
from Fill import distribute_items_restrictive
from test.bases import WorldTestBase
from worlds.AutoWorld import call_all

from ..Items import BLADE_GROUP_BY_TYPE, gate_blade_names
from ..Rules import _BREAK_ART_WEAPON_GROUPS


class _GatingBase:
    game = "Vagrant Story"

    def test_gate_blades_cover_every_type_and_are_in_pool(self) -> None:
        gate = gate_blade_names(self.world.options)
        self.assertEqual(len(gate), len(BLADE_GROUP_BY_TYPE))
        pool = {item.name for item in self.multiworld.itempool} | {item.name for item in self.multiworld.precollected_items[1]}
        for blade in gate:
            self.assertIn(blade, pool)

    def test_break_arts_need_matching_blade(self) -> None:
        for weapon, group in _BREAK_ART_WEAPON_GROUPS.items():
            loc = self.multiworld.get_location(f"Break Art {weapon} Level 1", 1)
            state = self.multiworld.get_all_state(False)
            for name in self.world.item_name_groups[group]:
                state.prog_items[1].pop(name, None)
            self.assertFalse(loc.can_reach(state), f"{loc.name} reachable without any {group}")

    def test_gate_blades_placed_early(self) -> None:
        call_all(self.multiworld, "pre_fill")
        distribute_items_restrictive(self.multiworld)
        spheres = list(self.multiworld.get_spheres())
        gate = set(gate_blade_names(self.world.options))
        early = set()
        for sphere in spheres[:4]:
            for loc in sphere:
                if loc.item and loc.item.player == 1 and loc.item.name in gate:
                    early.add(loc.item.name)
        self.assertEqual(early, gate, f"gate blades not all within first 4 spheres: missing {gate - early}")


class TestVanilla(_GatingBase, WorldTestBase):
    game = "Vagrant Story"
    run_default_tests = False
    options = {"progression_option": 0}


class TestVanillaHeavy(_GatingBase, WorldTestBase):
    game = "Vagrant Story"
    run_default_tests = False
    options = {"progression_option": 0, "item_drop_option": 1}


class TestOpenWorkOfArt(_GatingBase, WorldTestBase):
    game = "Vagrant Story"
    run_default_tests = False
    options = {"progression_option": 1, "open_world_option": 5}


class TestOpenKeanes(_GatingBase, WorldTestBase):
    game = "Vagrant Story"
    run_default_tests = False
    options = {"progression_option": 1, "open_world_option": 4, "item_drop_option": 1}
