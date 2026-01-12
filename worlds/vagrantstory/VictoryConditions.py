def defeat_guildenstern_dark_angel_victory(self, state):
    return state.can_reach_location("Level Clear: Credits", self.player)
