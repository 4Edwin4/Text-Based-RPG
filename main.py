# 2025-06-01
# Rogue has full sneak attack with feint
# Fighter now has shield bash which applies stun effect.
# Need to work out stun mechanics.
# bestiary initialized. When pulling monster for use run the equipping method inside bestiary for standard gear
# and inside main to add non-standard gear.

from Player import Character
from Bestiary import *
import Combat

player = Character(input("What is your name adventurer? "))
monster = Skeleton()

while not player.cls:
    player.char_class(input("""Do you fight with shield and weapon in hand as a 'fighter'?
Perhaps you use the environment and the enemies own weaknesses against themselves as a 'rogue'?
Might you be a 'wizard' who studies and commands the fabric of the material plane through magic? """).lower())

print(player.name, player.cls, player.ac, player.shield_bonus)

print("""Wait where is your gear!?
You can't enter the training yard without a way to defend yourself!
Here take this """, end='')

if player.cls == 'Fighter':
    print("""short spear and wood shield. It has some range and you can use a shield for extra protection.
You'll also need some armor to protect your body from monster attacks.
They are a bit old but they still work. You really didn't bring anything with you!""")
    player.equipping(weapon='short_spear', shield='wood_shield', armor='hide_armor')
elif player.cls == 'Rogue':
    print("""dagger. It is light, fast, and easier to hit vital targets on monsters with this.
You need to get close to use it though. You'll need some light armor to move around quick.
This set of leather armor should do the trick. Also, its quiet so it'll help you sneak when you have too.
You really didn't bring anything with you!""")
    player.equipping(weapon='dagger', armor='leather_armor')
elif player.cls == 'Wizard':
    print("""old grimoire I have. It doesn't do me any real good. I was never good at magic.
This one though has a simple air blast. You magical types don't really use armor so you tend to be more
vulnerable than most but can you can hit more frequently. You really didn't bring anything with you!""")
    player.equipping(weapon='air_tome')
print(player.name, player.cls, 'total ac', player.ac, 'shield bonus', player.shield_bonus, 'armor bonus',
      player.armor_bonus, 'weapon and dmg range', player.weapon, player.dmg_range)

Combat.combat_round(player, monster)
print('end combat')


