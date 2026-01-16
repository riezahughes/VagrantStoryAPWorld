from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState, Iterable


def has_key_required(self, location: str, state: CollectionState):
    return state.has("Cleared: " + location, self.player)


def has_sigil_required(self, item, state: CollectionState):
    return state.has(item, self.player)


def has_rood_inverse(self, state):
    return state.has("Rood Inverse", self.player)


def is_boss_defeated(self, boss: str, state: CollectionState):  # can used later
    return state.has("Boss: " + boss, self.player, 1)


def set_vanilla_progression(self):
    # Bronze Key
    set_rule(self.get_entrance("Shasras Hill Park -> Hall to a New World"), lambda state: has_key_required(self, "Bronze Key", state))

    # Crimson Key
    set_rule(self.get_entrance("Rue Vermillion -> Students of Death"), lambda state: has_key_required(self, "Crimson Key", state))

    # Gold Key
    set_rule(self.get_entrance("Corner of Prayers -> Salvation for the Mother"), lambda state: has_key_required(self, "Gold Key", state))
    set_rule(self.get_entrance("Salvation for the Mother -> Corner of Prayers"), lambda state: has_key_required(self, "Gold Key", state))
    set_rule(self.get_entrance("The Body Fragile Yields -> Salvation for the Mother"), lambda state: has_key_required(self, "Gold Key", state))
    set_rule(self.get_entrance("The Soldier's Bedding -> Stair to the Sinners"), lambda state: has_key_required(self, "Gold Key", state))
    set_rule(self.get_entrance("The Timely Dew of Sleep -> Companions in Arms"), lambda state: has_key_required(self, "Gold Key", state))
    set_rule(self.get_entrance("Shelter From the Quake -> Buried Alive"), lambda state: has_key_required(self, "Gold Key", state))

    # Iron Key
    set_rule(self.get_entrance("Noble Gold and Silk -> A Knight Sells his Sword"), lambda state: has_key_required(self, "Iron Key", state))
    set_rule(self.get_entrance("The Sunless Way -> Dark Abhors Light"), lambda state: has_key_required(self, "Iron Key", state))
    set_rule(self.get_entrance("Remembering Days of Yore -> Larder for a Lean Winter"), lambda state: has_key_required(self, "Iron Key", state))
    set_rule(self.get_entrance("From Squire to Knight -> Traces of Invasion Past"), lambda state: has_key_required(self, "Iron Key", state))

    # Platinum Key
    set_rule(self.get_entrance("Impalement -> Knotting"), lambda state: has_key_required(self, "Platinum Key", state))

    # Silver Key
    set_rule(self.get_entrance("Sewer of Ravenous Rats -> Beggars of the Mouthharp"), lambda state: has_key_required(self, "Silver Key", state))
    set_rule(self.get_entrance("The Washing-Woman's Way -> Nameless Dark Oblivion"), lambda state: has_key_required(self, "Silver Key", state))
    set_rule(self.get_entrance("Those who Drink the Dark -> Ants Prepare for Winter"), lambda state: has_key_required(self, "Silver Key", state))
    set_rule(self.get_entrance("The Resentful Ones -> Those who Fear the Light"), lambda state: has_key_required(self, "Silver Key", state))
    set_rule(self.get_entrance("The Auction Block -> Ascension"), lambda state: has_key_required(self, "Silver Key", state))
    set_rule(self.get_entrance("Everwant Passage -> Mining Regrets"), lambda state: has_key_required(self, "Silver Key", state))
    set_rule(self.get_entrance("Shelter From the Quake -> Movement of Fear"), lambda state: has_key_required(self, "Silver Key", state))

    # Steel Key
    set_rule(self.get_entrance("Hanging -> Impalement"), lambda state: has_key_required(self, "Steel Key", state))

    set_rule(self.get_entrance("The Hall of Broken Vows -> The Melodics of Madness"), lambda state: has_sigil_required(self, "Acacia Sigil", state))
    set_rule(self.get_entrance("Urge the Boy On -> Time Trial (Earth Dragon)"), lambda state: has_sigil_required(self, "Anemone Sigil", state))
    set_rule(self.get_entrance("Dream of the Holy Land -> The Ore Road"), lambda state: has_sigil_required(self, "Aster Sigil", state))
    set_rule(
        self.get_entrance("Wiping Blood from Blades -> Time Trial (Death + Ogre Zombie)"),
        lambda state: has_sigil_required(self, "Azalea Sigil", state),
    )
    set_rule(self.get_entrance("The Heretics' Story (Lower) -> Hopes of the Idealist"), lambda state: has_sigil_required(self, "Calla Sigil", state))
    set_rule(self.get_entrance("Rue Crimnade -> Workshop 'Junction Point'"), lambda state: has_sigil_required(self, "Cattleya Sigil", state))
    set_rule(self.get_entrance("Smokebarrel Stair -> Room of Cheap Red Wine"), lambda state: has_sigil_required(self, "Chamomile Sigil", state))
    set_rule(self.get_entrance("From Boy to Hero -> A Welcome Invasion"), lambda state: has_sigil_required(self, "Clematis Sigil", state))
    set_rule(self.get_entrance("A Storm of Arrows -> Time Trial (Dragon)"), lambda state: has_sigil_required(self, "Columbine Sigil", state))
    set_rule(self.get_entrance("The Dreamer's Climb -> Sinner's Sustenence"), lambda state: has_sigil_required(self, "Eulelia Sigil", state))
    set_rule(self.get_entrance("Live Long and Prosper -> Pray to the Mineral Gods"), lambda state: has_sigil_required(self, "Fern Sigil", state))
    set_rule(self.get_entrance("The Earthquake's Mark -> The Passion of Lovers"), lambda state: has_sigil_required(self, "Hyacinth Sigil", state))
    set_rule(self.get_entrance("A Storm of Arrows -> Time Trial (Minotaur)"), lambda state: has_sigil_required(self, "Kalmia Sigil", state))
    set_rule(self.get_entrance("The Poisoned Chapel -> A Light in the Dark"), lambda state: has_sigil_required(self, "Laurel Sigil", state))
    set_rule(self.get_entrance("The Withered Spring -> Prisoners' Niche"), lambda state: has_sigil_required(self, "Lily Sigil", state))
    set_rule(self.get_entrance("Rue Aliano -> The House Khazabas"), lambda state: has_sigil_required(self, "Mandrake Sigil", state))
    set_rule(
        self.get_entrance("A Taste of the Spoils -> Time Trial (Damascus Crab)"), lambda state: has_sigil_required(self, "Marigold Sigil", state)
    )
    set_rule(self.get_entrance("The Laborer's Bonfire -> Torture Without End"), lambda state: has_sigil_required(self, "Melissa Sigil", state))
    set_rule(self.get_entrance("The Melodics of Madness -> What Ails You, Kills You"), lambda state: has_sigil_required(self, "Palm Sigil", state))
    set_rule(
        self.get_entrance("A Taste of the Spoils -> Time Trial (Damascus Golem)"), lambda state: has_sigil_required(self, "Schirra Sigil", state)
    )
    set_rule(self.get_entrance("The Cauldron -> Wooden Horse"), lambda state: has_sigil_required(self, "Tearose Sigil", state))
    set_rule(self.get_entrance("Wiping Blood from Blades -> Time Trial (Asura)"), lambda state: has_sigil_required(self, "Tigertail Sigil", state))
    set_rule(self.get_entrance("Urge the Boy On -> Time Trial (Snow Dragon)"), lambda state: has_sigil_required(self, "Verbena Sigil", state))


def set_new_game_plus_rules(self, state):
    set_rule(self.get_entrance("Glacialdra Kirk Ruins -> Path to the Greengrocer"), lambda state: has_rood_inverse(self, state))
    set_rule(self.get_entrance("Corner of the Wretched -> Crossroads of Rest"), lambda state: has_rood_inverse(self, state))
    set_rule(self.get_entrance("Path to the Greengrocer -> Glacialdra Kirk Ruins"), lambda state: has_rood_inverse(self, state))
    set_rule(self.get_entrance("Train and Grow Strong -> Steady the Boar-Spears"), lambda state: has_rood_inverse(self, state))
