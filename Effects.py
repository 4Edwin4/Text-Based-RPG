class FlatFoot:
    duration = 1
    name = 'Flat Foot'

    def active(self):
        print(self.name + ' is flat footed. They dont seem to move as well!')
        self.ac -= self.dex
        self.touch_ac -= self.dex


class Daze:
    duration = 1

    def active(self):
        print("I'm dazed for " + str(Daze.duration) + " turns!")


class Poison:
    duration = 2
    name = 'Poison'

    def active(self):
        print("Poison", self.active_effects)
        print(self.name, "feels the poison taking some of their life!")
        self.hp -= 1


class Stun:
    duration = 1
    name = 'Stun'

    def active(self):
        print(self.name + " is stupefied. They might not be able to act this turn!")
