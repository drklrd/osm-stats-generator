# define class for stats
class OSMStats:
    def __init__(self, user) -> None:
        self.user = user
        self.stats = {}

    # function to print the stats
    def show_stats(self):
        for stat in self.stats:
            actions = ["created", "modified"]
            for action in actions:
                print(
                    "{variable} ({action}): {value}".format(
                        variable=stat,
                        action=action,
                        value=str(len(self.stats[stat][action])),
                    )
                )

    # function to get stats
    def get_current_stats(self):
        return self.stats

    # function to update stats
    def update_stats(self, updated_stats):
        self.stats = updated_stats
