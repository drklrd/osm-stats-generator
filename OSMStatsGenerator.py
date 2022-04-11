import sys

from osmdiff import OSMChange
from OSMStats import OSMStats
from utils import update_stats_with_change


def main(user):
    osm_changes = OSMChange(file="data/changes.osc")
    stats_collector = OSMStats(user)

    # handle osm creation changes
    for n in osm_changes.create:
        if n.tags and n.attribs["user"] == user:
            updated_stats = update_stats_with_change(
                change_type="created",
                entity=n,
                stats=stats_collector.get_current_stats(),
            )
            stats_collector.update_stats(updated_stats)

    # handle osm modification changes.
    for n in osm_changes.modify:
        if n.tags and n.attribs["user"] == user:
            updated_stats = update_stats_with_change(
                change_type="modified",
                entity=n,
                stats=stats_collector.get_current_stats(),
            )
            stats_collector.update_stats(updated_stats)

    # handle osm deletion changes. TO DO!
    # for n in o.delete:
    # add code to handle deletion here

    # print stats at the end
    stats_collector.show_stats()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python osm_stats.py '<osmusername>'")
        sys.exit(-1)

    exit(main(sys.argv[1]))
