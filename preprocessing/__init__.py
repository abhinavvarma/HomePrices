from preprocessing import missing_value_handling, feature_transformation


def get_stages():
    return missing_value_handling.get_stages() + feature_transformation.get_stages()


def run_stages(all_data, stages):
    for stage in stages:
        print "Preprocessing: Stage:", stage
        all_data = stage().run(all_data)
    return all_data


def run(all_data):
    return run_stages(all_data, get_stages())