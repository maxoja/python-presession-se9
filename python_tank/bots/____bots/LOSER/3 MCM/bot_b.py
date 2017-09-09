import pygame
#Manop, Com, Manyou
from core.tank import TankPrototype

class BotB ( TankPrototype ):
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
        #this method will be call at the __init__() function of a super class
        #use this to create and initialize variable you will use in your tank algorithm
        self.current_direction = 'left'
    
    def update( self ) :
        #this method will be called every millisecond
        #code your algorithm here and it will affect your tank action
        self_x, self_y = self.getPosition()

        '''change current_direction when this tank is at the edge of the battle field'''
        if self.isAtEdge(self.current_direction):
            if self.current_direction == 'left':
                self.current_direction = 'right'
            elif self.current_direction == 'right':
                self.current_direction = 'left'
            elif self.current_direction == 'up':
                self.current_direction = 'down'
            elif self.current_direction == 'down':
                self.current_direction = 'up'

        '''then move it to the determined direction'''
        self.move(self.current_direction)

        '''get enemy list from method .getEnemyList()'''
        enemy_list = self.getEnemyList()

        enemy_x = 0
        enemy_y = 0

        if enemy_list:
            for enemy in enemy_list:
                self_x, self_y = self.getPosition()
                enemy_x, enemy_y = enemy.getPosition()
                enemy_direction = enemy.getDirection()

        ally_list = self.getAllyList()

        for ally in ally_list:
            ally_x, ally_y = ally.getPosition()



            if (self_y == enemy_y):
                if self_x < enemy_x:
                    self.current_direction = 'right'
                else:
                    self.current_direction = 'left'
            elif (self_y < enemy_y):
                self.current_direction = 'down'
            else:
                self.current_direction = 'up'


            if self_x == enemy_x and self_x != ally_x:  # if on the same column
                if self_y < enemy_y:
                    self.shoot('down')
                else:
                    self.shoot('up')
            if self_y == enemy_y and self_y != ally_y:  # if on the same row
                if (self_x < enemy_x):
                    self.shoot('right')
                else:
                    self.shoot('left')

    pass
  
