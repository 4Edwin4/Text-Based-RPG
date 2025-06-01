import random
import time


def sneak_atk(attacker, target):
    # sneak attack success function
    dmg = 0
    if hasattr(attacker, 'sneak_atk'):
        chance = 5 * attacker.int
        chance_roll = random.randint(1, 100)
        dex_negate = ['FlatFoot']

        # for loop to check if target has a dex negating effect
        for effect in target.active_effects:
            if effect in dex_negate:
                chance = 100
            else:
                continue

        # if not then tries a chance roll
        if chance_roll <= chance:
            dmg = random.randint(1, attacker.sneak_atk)
            print('You managed to strike a vital spot!')
        return dmg

    else:
        return dmg


def dmg_calc(attacker, target, armor):

    # determines combat modifier based on range quality of weapon
    if "range" in attacker.dmg_type:
        atk_mod = attacker.dex
    else:
        atk_mod = attacker.str

    # rolls attack and calculates attack total
    atk_roll = random.randint(1, 20)
    atk_total = atk_roll + attacker.bab + atk_mod

    # function for damage if successful hit equal to or above target ac
    if atk_total >= armor:

        # critical hit logic
        crit_hit = False

        if atk_roll not in attacker.crit_range:
            dmg_roll = random.randint(1, attacker.dmg_range)
        else:
            crit_hit = True
            dmg_roll = 0
            for roll in range(attacker.crit_mod):
                dmg_roll += random.randint(1, attacker.dmg_range)
            print(attacker.name, "'s landed a perilous blow!")

        # strength modifier for melee weapons
        if 'melee' in attacker.dmg_type:
            if crit_hit:
                dmg_roll += attacker.str * attacker.crit_mod
            else:
                dmg_roll += attacker.str

        # sneak damage modifier for those with sneak_atk attribute
        sneak_dmg = sneak_atk(attacker, target)
        dmg_roll += sneak_dmg

        # damage reduction modifier for those with damage reduction
        if hasattr(target, 'dr_value'):
            for vulnerability in target.dr:
                if vulnerability not in attacker.dmg_type:
                    dmg_roll -= target.dr_value
                    dmg_roll = max(0, dmg_roll)
                    print(attacker.name + "'s weapon seems ineffective!")

        target.hp -= dmg_roll
        target.hp = max(0, target.hp)

        print(attacker.name + " Hit's " + target.name + " for " + str(dmg_roll) + " damage with an attack roll of "
              + str(atk_total) + " and their hp is now " + str(target.hp))
        time.sleep(3)

        if target.hp == 0:
            print(target.name + " has been defeated!")
            time.sleep(3)

    else:
        print(attacker.name + " failed to hit " + target.name + " with " + str(atk_total))
        time.sleep(3)


def combat_round(player, monster):
    # initiative roll
    player_init = random.randint(1, 20) + player.dex
    monster_init = random.randint(1, 20) + monster.dex
    print('A ' + monster.name + ' appears! Prepare to fight!')
    time.sleep(3)

    # monster goes first
    if monster_init > player_init:
        print(monster.name, 'moved faster than you!')
        dmg_calc(monster, player, player.ac)
        time.sleep(3)

    # otherwise player goes first
    while player.hp > 0 and monster.hp > 0:
        if player.hp > 0:

            turn_complete = False
            action_list = ['Fight', 'Action', 'Run']

            # choose what player wants to do
            choice = ""
            while choice not in action_list:
                print(action_list)
                choice = input('What would you like to do? ').capitalize()

            # fight option and following damage logic
            if choice == action_list[0]:
                # player status update removes old effects then iterates by 1 and activates
                player.remove_effect()
                player.update_effect()
                if "touch" in player.dmg_type:
                    dmg_calc(player, monster, monster.touch_ac)
                else:
                    dmg_calc(player, monster, monster.ac)
                turn_complete = True

            # opens players special action list and choice logic
            elif choice == action_list[1]:
                action_choice = ""
                while action_choice not in player.actions_list:
                    print(player.actions_list)
                    action_choice = input("What action would you like to use? ").capitalize()

                    if player.actions_list.index(action_choice) + 1 == len(player.actions_list):
                        break
                    elif action_choice == player.actions_list[player.actions_list.index(action_choice)]:

                        # player status update removes old effects then iterates by 1 and activates
                        player.remove_effect()
                        player.update_effect()

                        # player does special action
                        player.apply(action_choice, monster)
                        turn_complete = True
                        time.sleep(3)

            # player chooses to run
            elif action_list.index(choice) + 1 == len(action_list):
                break

        if monster.hp > 0 and turn_complete is True:
            monster.remove_effect()
            monster.update_effect()
            time.sleep(3)
            if "touch" in monster.dmg_type:
                dmg_calc(monster, player, player.touch_ac)
            else:
                dmg_calc(monster, player, player.ac)
