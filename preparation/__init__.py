from preparation import scikit_learn_related


def get_stages():
    return scikit_learn_related.get_stages()


def run(all_data):
    for stage in get_stages():
        print "Preparation: Stage:", stage
        all_data = stage().run(all_data)
    return all_data