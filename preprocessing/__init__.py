from preprocessing import missing_value_handling, feature_transformation, feature_selection


def get_stages():
    return missing_value_handling.get_stages() + feature_transformation.get_stages() + feature_selection.get_stages()


def run_stages(all_data, stages):
    print "Preprocessing:"
    counter = 1
    for stage in stages:
        print "Stage", counter, ":", stage
        counter += 1
        all_data = stage.run(all_data)
    return all_data


def run(all_data):
    return run_stages(all_data, get_stages())