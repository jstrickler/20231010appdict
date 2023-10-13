


def add_run(klass):

    def run(self):
        print("running")

    setattr(klass, "run", run)

    return klass