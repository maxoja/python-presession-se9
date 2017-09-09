import pygame

from core.tank import TankPrototype

class BotSampleA ( TankPrototype ):
    #because this bot class is inherited from TankPrototype class
    #this class will derive and obtain all public methods available in TankPrototype
    #the methods available for use listed below
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
    
    def start( self ) :
        self.current_direction = 'left'
        self.stop = False
        #this method will be call at the __init__() function of a super class
        #use this to create and initialize variable you will use in your tank algorithm
        pass
    
    def update( self ) :

        if self.isAtEdge(self.current_direction):
            if self.current_direction == 'left':
                self.current_direction = 'up'
            elif self.current_direction == 'up':
                self.current_direction = 'right'
            elif self.current_direction == 'right':
                self.current_direction = 'down'
            elif self.current_direction == 'down':
                self.current_direction = 'left'
        if not self.stop:
            self.move(self.current_direction)

        if self.isBlocked(self.current_direction):
            if self.current_direction == 'left':
                self.current_direction = 'right'
            elif self.current_direction == 'right':
                self.current_direction = 'left'
            elif self.current_direction == 'up':
                self.current_direction = 'down'
            elif self.current_direction == 'down':
                self.current_direction = 'up'

        enemy_list = self.getEnemyList()

        for enemy in enemy_list:
            self_x, self_y = self.getPosition()
            enemy_x, enemy_y = enemy.getPosition()

            if self_x == enemy_x and not self.allyInWay(self.getAllyList(), "x"):
                self.stop = True
                if enemy_y < self_y:
                    self.shoot('up')
                else:
                    self.shoot('down')
                break

            elif self_y == enemy_y and not self.allyInWay(self.getAllyList(), "y"):
                self.stop = True
                if enemy_x < self_x:
                    self.shoot('left')
                else:
                    self.shoot('right')
                break
            else:
                self.stop = False

    def allyInWay(self, allies, axis):
        if allies == []:
            return False
        if axis == "x":
            return self.getPosition()[0] == allies[0].getPosition()[0]
        if axis == "y":
            return self.getPosition()[1] == allies[0].getPosition()[1]

        #this method will be called every millisecond
        #code your algorithm here and it will affect your tank action
        pass

