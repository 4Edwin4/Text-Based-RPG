import Equipment
import Effects


class Monster:
    def __init__(self):
        # ## weapon
        self.weapon = "Unarmed"
        self.dmg_range = 4
        self.crit_mod = 2
        self.crit_range = [20]
        self.dmg_type = "Bludgeoning"
        # ## armor
        self.ac = 10
        self.touch_ac = 10
        self.natarmor_bonus = 0
        self.shield_name = None
        self.shield_bonus = 0
        self.armor_name = None
        self.armor_bonus = 0
        # ## Stats
        self.bab = 0
        self.fort_save = 0
        self.ref_save = 0
        self.will_save = 0
        self.hp = 0
        self.max_hp = self.hp
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wix = 0
        self.cha = 0
        self.active_effects = {}

    def ac_calc(self):
        self.ac = 10 + self.shield_bonus + self.armor_bonus + self.natarmor_bonus + self.dex

    def touch_ac_calc(self):
        self.touch_ac = 10 + self.dex

    def equipping(self, shield="", armor="", weapon=""):
        equipment = [shield, armor, weapon]
        for item in equipment:
            if item in dir(Equipment):
                getattr(Equipment, item)(self)
            else:
                continue
        self.ac_calc()

    def apply(self, effect="", target=""):
        effect = effect
        target = target
        for name in dir(Effects):
            if name == effect:
                target.active_effects.update({effect: 0})

    def update_effect(self):
        for effect in self.active_effects:
            for name in dir(Effects):
                if name == effect:
                    effect_page = getattr(Effects, effect)
                    if self.active_effects[effect] < effect_page.duration:
                        self.active_effects[effect] += 1
                        effect_page.active(self)
                else:
                    continue

    def remove_effect(self):
        for effect in list(self.active_effects.keys()):
            effect_page = getattr(Effects, effect)
            if self.active_effects[effect] >= effect_page.duration:
                print(self.name + ' no longer has the ' + effect_page.name + ' condition!')
                del self.active_effects[effect]
                self.ac_calc()
                self.touch_ac_calc()


class Gnoll(Monster):
    def __init__(self):
        Monster.__init__(self)
        self.natarmor_bonus = 1
        self.name = "Gnoll"
        self.hp = 11
        self.bab = 1
        self.str = 2
        self.con = 1
        self.ac_calc()
        self.equipping(shield='wood_shield', weapon='short_spear', armor='leather_armor')


class Skeleton(Monster):
    def __init__(self):
        Monster.__init__(self)
        self.name = 'Skeleton'
        self.natarmor_bonus = 2
        self.hp = 4
        self.str = 2
        self.dex = 2
        self.dr_value = 5
        self.dr = ['Bludgeoning']
        self.ac_calc()
        self.equipping(weapon='claw', armor='leather_armor')
