import pygame

from core.tank import TankPrototype

class BotSampleB ( TankPrototype ):
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
        self.shoot('right')



    def update( self ) :
        #this method will be called every millisecond
        #code your algorithm here and it will affect your tank action
        '''change current_direction when this tank is at the edge of the battle field'''
        #self.current_direction = 'left'

        self.move(self.current_direction)
        self.shoot('right')

        if self.isBlocked(self.current_direction):
            #self.isBlocked(self.current_direction)
            if self.current_direction == 'right':
                self.current_direction = 'left'
            elif self.current_direction == 'left':
                self.current_direction = 'right'
            elif self.current_direction == 'up':
                self.current_direction = 'down'
            elif self.current_direction == 'down':
                self.current_direction = 'up'

        if self.isAtEdge(self.current_direction):
            if self.current_direction == 'left':
                self.current_direction = 'up'
            elif self.current_direction == 'up':
                self.current_direction = 'down'
            elif self.current_direction == 'right':
                self.current_direction = 'left'
            elif self.current_direction == 'down':
                self.current_direction = 'right'

        if (self.isAtEdge == 'right' or 'left'):
            self.shoot('up')

        '''
        if (self.current_direction == 'up' or 'down'):
            self.shoot('left')
        else :
            self.shoot('down')
        '''
        '''
        if enemy_list[1].isDead():
            if enemy_list[1].isDead == 'True':
                self.shoot('right')
            elif enemy_list[1].isDead == 'False':
                self.shoot('left')
        '''



        '''then move it to the determined direction'''
        enemy_list = self.getEnemyList()
        ally_list = self.getAllyList()


        '''
       # then we check for any enemy locate in the same column and shoot it
        for ally in ally_list:
            self_x, self_y = self.getPosition()
            ally_x, ally_y = ally.getPosition()

            if  == ally_y:  # if on the same column
                    self.shoot('left')
                    #self.shoot('up')
            else:
                    self.shoot('left')
        '''

