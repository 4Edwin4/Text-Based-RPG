import Classes
import Equipment
import Effects


class Character:
    def __init__(self, name):
        self.name = name
        self.cls = None
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
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.active_effects = {}
        self.actions_list = ['Return']

    def char_class(self, title):
        for name in dir(Classes):
            if name == title:
                getattr(Classes, title)(self)

    def equipping(self, shield="", armor="", weapon=""):
        equipment = [shield, armor, weapon]
        for item in equipment:
            if item in dir(Equipment):
                getattr(Equipment, item)(self)
            else:
                continue
        self.ac_calc()

    def ac_calc(self):
        self.ac = 10 + self.shield_bonus + self.armor_bonus + self.natarmor_bonus + self.dex

    def touch_ac_calc(self):
        self.touch_ac = 10 + self.dex

    def apply(self, effect="", target=""):
        action2effect = {'Feint': 'FlatFoot'}
        target = target

        for name in dir(Effects):
            if effect == name:
                target.active_effect.update({effect: 0})
            elif name == action2effect[effect]:
                target.active_effects.update({action2effect[effect]: 0})
                print(self.name + " has applied " + action2effect[effect] + " to " + target.name)

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
