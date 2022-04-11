# utility functions

from config import variables_to_count


def update_stats_with_change(change_type, entity, stats):
    for variable in variables_to_count:
        if is_feature_in_osm_tags(
            features=variables_to_count[variable], osm_tags=entity.tags
        ):
            if not variable in stats:
                stats[variable] = {
                    "created": [],
                    "modified": [],
                    "deleted": [],
                }
            stats[variable][change_type].append(
                {
                    "id": entity.attribs["id"],
                    "timestamp": entity.attribs["timestamp"],
                    "tags": entity.tags,
                }
            )
    return stats


def is_feature_in_osm_tags(features, osm_tags):
    is_in = False
    for feature in features:
        if feature.split("=")[0] in osm_tags:
            if osm_tags[feature.split("=")[0]] == feature.split("=")[1]:
                is_in = True
                break
    return is_in
