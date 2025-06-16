def fighter(self):
    self.cls = 'Fighter'
    self.bab = 1
    self.fort_sav = 2
    self.ref_sav = 0
    self.will_sav = 0
    self.str += 3
    self.con += 2
    self.wis += 1
    self.hp = 10 + self.con
    self.max_hp = self.hp
    self.actions_list.insert(0, 'Shield bash')

def rogue(self):
    self.cls = 'Rogue'
    self.bab = 0
    self.fort_sav = 0
    self.ref_sav = 2
    self.will_sav = 0
    self.dex += 3
    self.int += 2
    self.con += 1
    self.hp = 8 + self.con
    self.max_hp = self.hp
    self.sneak_atk = 6
    self.actions_list.insert(0, 'Feint')


def wizard(self):
    self.cls = 'Wizard'
    self.bab = 0
    self.fort_sav = 0
    self.ref_sav = 0
    self.will_sav = 2
    self.int += 3
    self.dex += 2
    self.con += 1
    self.hp = 6 + self.con
    self.max_hp = self.hp