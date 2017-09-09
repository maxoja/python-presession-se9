import pygame
import time

from core.tank import TankPrototype


class BotB(TankPrototype):
    # because this bot class is inherited from TankPrototype class
    # this class will derive and obtain all public methods available in TankPrototype
    # the methods available for use listed below
    '''
    getHP()                get current HP
    getMP()                get current MP
    getName()              get name
    getPosition()          get x, y position
    getAllyList()          get a list of friendly tanks
    getEnemyList()         get a list of enemy tanks
    isMoving()             check if moving( can't change direction while moving )
    isDead()               check if the tank is dead or not
    isAtEdge(direction)    check if at edge of bettle field
    isBlocked(direction)   check if stuck with other tanks
    getDirection()         get heading direction ( also moving direction if is moving )
    isAlly(another_bot)    check if another_bot is an alliance or not
    getTeamColor()         get current team color
    readyToMove()          check if ready to move ( also check cooldown and mana cost )
    readyToShoot()         check if ready to shoot ( also check cooldown and mana cost )
    readyToHeal()          check if ready to heal ( also check cooldown and mana cost )
    move(direction)        move forward in the specified direction ('left' 'right' 'up' 'down')
    shoot(direction)       fire a bullet in the specified direction ('left' 'right' 'up' 'down') : cost 10 mana
    shoot_heal(direction)  fire a potion in the specified direction ('left' 'right' 'up' 'down') : cost 20 mana
    '''

    def start(self):
        # this method will be call at the __init__() function of a super class
        # use this to create and initialize variable you will use in your tank algorithm
        self.current_direction = 'left'
        self.iswaiting = False
        self.a = 0

    def update(self):
        # this method will be called every millisecond
        # code your algorithm here and it will affect your tank action

        '''change current_direction when this tank is at the edge of the battle field'''
        ally_list = self.getAllyList()
        enemy_list = self.getEnemyList()
        hasfriend = (len(ally_list) != 0)
        if (hasfriend == True):
            ally = ally_list[0]

            ally_x, ally_y = ally.getPosition()
            me_x, me_y = self.getPosition()

            if me_x < ally_x:
                self.move('left')
            else:
                self.move('right')

            if me_x < 5:
                self.move('left')

            else:
                self.move('right')
        for enemy in enemy_list:
            self_x, self_y = self.getPosition()
            enemy_x, enemy_y = enemy.getPosition()

            if (self_x == enemy_x or abs(self_x - enemy_x) < 1):  # if on the same column
                if enemy_y < self_y:  # enemy is located above
                    self.shoot('up')
                else:  # enemy is located below
                    self.shoot('down')

            if (self_y == enemy_y or abs(self_y - enemy_y) < 1) and (self_y == enemy_y):  # if on the same column
                if enemy_x < self_x:  # enemy is located above
                    self.shoot('left')
                else:  # enemy is located belows
                    self.shoot('right')

            if (time.time() - self.a >= 0.65 and self.iswaiting == False):
                if (self_y == enemy_y):
                    if (self.iswaiting == False):
                        self.a = time.time()
                        self.iswaiting == True

                    if (self_y < 5):
                        self.move('down')
                        self.iswaiting = False

                    elif (self_y > 5):
                        self.move('up')
                        self.iswaiting = False


                else:
                    if (self_y < enemy_y):
                        self.move('down')
                        self.iswaiting = False
                    else:
                        self.move('up')
                        self.iswaiting = False




