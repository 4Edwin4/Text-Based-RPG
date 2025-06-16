from asyncio import shield

import Combat
import Player
import Bestiary
from Bestiary import Skeleton

player = Player.Character('Edwin')
player.char_class('fighter')
player.equipping(weapon='short_spear', armor='leather_armor', shield='wood_shield')
monster = Bestiary.Skeleton()

print('skeleton ac is', monster.ac)

print(player.name, player.cls, 'total ac', player.ac, 'shield bonus', player.shield_bonus, 'armor bonus',
      player.armor_bonus, 'weapon and dmg range', player.weapon, player.dmg_range)

print(player.active_effects)

Combat.combat_round(player, monster)