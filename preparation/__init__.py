from preparation import scikit_learn_related


def get_stages():
    return scikit_learn_related.get_stages()


def run(all_data):
    print "Preparation:"
    counter = 1
    for stage in get_stages():
        print "Stage", counter, ":", stage
        counter += 1
        all_data = stage.run(all_data)
    return all_data