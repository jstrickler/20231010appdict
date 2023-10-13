

class Wombat:
    def ID(self):
        print("I am a wombat")

    def __call__(self):
        print("I am really a wombat instance!")

w = Wombat()
w.ID()
w()
