def defeat_guildenstern_dark_angel_victory(self, state):
    return state.can_reach_location("Game End: Credits", self.player)
