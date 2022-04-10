# utility functions


def is_feature_in_osm_tags(features, osm_tags):
    is_in = False
    for feature in features:
        if feature.split("=")[0] in osm_tags:
            if osm_tags[feature.split("=")[0]] == feature.split("=")[1]:
                is_in = True
                break
    return is_in
