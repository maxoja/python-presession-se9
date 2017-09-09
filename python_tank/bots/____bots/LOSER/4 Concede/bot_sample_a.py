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
    isAtEdge(direction)    check if at edge of battle field
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
        pass

    def update( self ) :
        #this method will be called every millisecond
        #code your algorithm here and it will affect your tank actionm
        self.getHP()
        self.getMP()
        
        allies_list = self.getAllyList()
        
        enemy_list = self.getEnemyList()

        if allies_list:
            ally = allies_list[0]
            ally_x, ally_y = ally.getPosition()
        else :
            ally_x, ally_y = 0
            
        

        for enemy in enemy_list:
            self_x, self_y = self.getPosition()
            enemy_x, enemy_y = enemy.getPosition()

            if self_x != enemy_x:
                if self_x < enemy_x:
                    self.move('right')
                else:
                    self.move('left')

            if self_y != enemy_y:
                if self_y > enemy_y:
                    self.move('up')
                else:
                    self.move('down')

            if self_x == enemy_x:

                if self_y < enemy_y:
                    self.shoot ('down')
                else:
                    self.shoot('up')


            if self_y == enemy_y:

                if self_x < enemy_x:
                     self.shoot('right')
                else:
                    self.shoot('left')


        pass

