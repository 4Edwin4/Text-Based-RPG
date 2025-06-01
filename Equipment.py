# ## Weapons melee
def claw(self):
    self.weapon = 'Claw'
    self.dmg_range = 4
    self.crit_mod = 2
    self.crit_range = [20]
    self.dmg_type = ['melee', 'Bludgeoning', 'Slash']


def dagger(self):
    self.weapon = 'Dagger'
    self.dmg_range = 4
    self.crit_mod = 2
    self.crit_range = [19, 20]
    self.dmg_type = ['melee', 'Pierce', 'Slash']


def short_spear(self):
    self.weapon = "Short Spear"
    self.dmg_range = 6
    self.crit_mod = 2
    self.crit_range = [20]
    self.dmg_type = ['melee', 'Pierce']


def unarmed(self):
    self.weapon = "Unarmed"
    self.dmg_range = 4
    self.crit_mod = 2
    self.dmg_type = ['melee', 'Bludgeoning']


# ## Weapons Ranged
def air_tome(self):
    self.weapon = "Air Tome"
    self.dmg_range = 3
    self.crt_mod = 2
    self.dmg_type = ['range', 'touch', 'Bludgeoning']


# ## Shields
def wood_shield(self):
    self.shield_name = "Wood Shield"
    self.shield_bonus = 1


# ## Armor
def hide_armor(self):
    self.armor_name = "Hide Armor"
    self.armor_bonus = 4


def leather_armor(self):
    self.armor_name = "Leather Armor"
    self.armor_bonus = 2



