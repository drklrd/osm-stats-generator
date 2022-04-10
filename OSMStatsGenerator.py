import sys
from osmdiff import OSMChange

from config import variables_to_count
from utils import is_feature_in_osm_tags

# define class for stats generator
class OSMStatsGenerator:
    def __init__(self, user) -> None:
        self.user = user
        self.stats = {}

    # function to print the stats
    def show_stats(self):
        for stat in self.stats:
            print(
                "{variable}: {value}".format(
                    variable=stat, value=str(len(self.stats[stat]))
                )
            )


def main(user):
    o = OSMChange(file="data/changes.osc")
    stats_collector = OSMStatsGenerator(user)

    # handle osm creation changes
    for n in o.create:
        if n.tags and n.attribs["user"] == user:
            for variable in variables_to_count:
                if is_feature_in_osm_tags(
                    features=variables_to_count[variable], osm_tags=n.tags
                ):
                    if not variable in stats_collector.stats:
                        stats_collector.stats[variable] = []
                    stats_collector.stats[variable].append(
                        {
                            "id": n.attribs["id"],
                            "timestamp": n.attribs["timestamp"],
                            "tags": n.tags,
                        }
                    )

    # print stats at the end
    stats_collector.show_stats()

    # handle osm modification changes. TO DO!
    # for n in o.modify:
    #     # add code to handle modification here

    # handle osm deletion changes. TO DO!
    # for n in o.delete:
    #     # add code to handle deletion here


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python osm_stats.py '<osmusername>'")
        sys.exit(-1)

    exit(main(sys.argv[1]))
