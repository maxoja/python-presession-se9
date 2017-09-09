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
        #this method will be call at the __init__() function of a super class
        #use this to create and initialize variable you will use in your tank algorithm
        self.current_direction = 'left'
    
    def update( self ) :

        if self.isAtEdge(self.current_direction):
            if self.current_direction == 'left':
                self.current_direction = 'right'
            elif self.current_direction == 'right':
                self.current_direction = 'left'



        enemy_list = self.getEnemyList()


        target = None
        targetDistance = None
        for tank in enemy_list:
            if targetDistance == None:
                targetDistance = self.calculateDistance(self, tank)
                target = tank

            elif targetDistance > self.calculateDistance(self, tank):
                targetDistance = self.calculateDistance(self, tank)
                target = tank

        if target != None:
            x_target , y_target = target.getPosition()

            x_me , y_me = self.getPosition()

            if(x_me < x_target):
                self.move('right')

            elif(x_me > x_target):
                self.move('left')

            if (y_me < y_target):
                self.move('down')

            elif (y_me > y_target):
                self.move('up')

            if(x_me - x_target <= 1 and y_me - y_target == 0):
                if (x_me < x_target):
                    self.shoot('right')

                elif (x_me > x_target):
                    self.shoot('left')

            elif (y_me - y_target <= 1 and x_me - x_target == 0):
                if (y_me < y_target):
                    self.shoot('down')

                elif (y_me > y_target):
                    self.shoot('up')



    def calculateDistance(self, tank1, tank2):
        x_tank1, y_tank1 = tank1.getPosition()
        x_tank2, y_tank2 = tank2.getPosition()
        y_dis = abs(y_tank1 - y_tank2)
        x_dis = abs(x_tank1 - y_tank2)
        return (y_dis**2 + x_dis**2)**0.5










