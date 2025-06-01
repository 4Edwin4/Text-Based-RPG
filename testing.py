import Combat
import Player
import Bestiary

player = Player.Character('Edwin')
player.char_class('rogue')
player.equipping(weapon='dagger', armor='leather_armor')
monster = Bestiary.Skeleton()
monster.apply('Poison', player)

print(player.name, player.cls, 'total ac', player.ac, 'shield bonus', player.shield_bonus, 'armor bonus',
      player.armor_bonus, 'weapon and dmg range', player.weapon, player.dmg_range)

print(monster.name, 'total ac', monster.ac, 'shield bonus', monster.shield_bonus, 'armor bonus',
      monster.armor_bonus, 'weapon and dmg range', monster.weapon, monster.dmg_range)

Combat.combat_round(player, monster)

