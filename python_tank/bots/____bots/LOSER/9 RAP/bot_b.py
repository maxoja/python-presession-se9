import pygame

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
        pass
    
    def update( self ) :
        #this method will be called every millisecond
        #code your algorithm here and it will affect your tank action
        
        enemy_list = self.getEnemyList()

        ally_list = self.getAllyList()
            
        for ally in ally_list :
            self_x, self_y = self.getPosition()
            ally_x, ally_y = ally.getPosition()
            friendHP = ally.getHP()
            mana = self.getMP()
            if self_x == ally_x :      
                if ally_y < self_y :   
                    if mana>=60:
                        self.move('up')
                        self.shoot_heal('up')
                        self.shoot_heal('down')
                    
                else :                  
                    if mana>=60:
                        self.move('down')
                        self.shoot_heal('down')
                        self.shoot_heal('up')

            if self_y == ally_y :      
                if ally_x < self_x :   
                    if mana>=60:
                        self.move('left')
                        self.shoot_heal('left')
                        self.shoot_heal('right')
                else :                  
                    if mana>=60:
                        self.move('right')
                        self.shoot_heal('right')
                        self.shoot_heal('left')

            if self_x == ally_x :      
                if ally_y < self_y :   
                    if mana>=60:
                        self.move('up')
                        self.move('up')
                    
                else :                  
                    if mana>=60:
                        self.move('down')
                        self.move('down')
                        
            if self_y == ally_y :      
                if ally_x < self_x :   
                    if mana>=60:
                        self.move('left')
                        self.move('left')
                else :                  
                    if mana>=60:
                        self.move('right')
                        self.move('right')
                    
        for enemy in enemy_list:
            self_x, self_y = self.getPosition()
            enemy_x, enemy_y = enemy.getPosition()

            if self_x == enemy_x:
               if enemy_y < self_y:
                   self.shoot('up')
               else :
                   self.shoot('down')

        for enemy in enemy_list:
            self_x, self_y = self.getPosition()
            enemy_x, enemy_y = enemy.getPosition()

            if self_y == enemy_y:
                if enemy_x > self_x:
                    self.shoot('right')
                else :
                    self.shoot('left')


            if self_x == enemy_x:
               if enemy_y < self_y:
                   self.move('up')
                   self.move('up')
                   
               else :
                   self.move('down')
                   self.move('down')


            if self_y == enemy_y:
                if enemy_x > self_x:
                    self.move('right')
                    self.move('right')
                else :
                    self.move('left')
                    self.move('left')

        

        
                   
                
