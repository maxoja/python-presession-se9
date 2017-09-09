import pygame

from core.tank import TankPrototype

class BotSampleB ( TankPrototype ):
    def start( self ) :
        self_x, self_y = self.getPosition()
        if self_y > 5:
            self.current_direction = 'down'
        else:
            self.current_direction = 'up'

    def update( self ) :
        if self.isAtEdge(self.current_direction) or self.isBlocked(self.getDirection()):
            if self.current_direction == 'up':
                self.current_direction = 'left'
            elif self.current_direction == 'left':
                self.current_direction = 'right'
            elif self.current_direction == 'right':
                self.current_direction = 'left'
            elif self.current_direction == 'down':
                self.current_direction = 'left'

        self.move(self.current_direction)

        enemy_list = self.getEnemyList()

        #Shooting
        ally_list = self.getAllyList()
        for ally in ally_list:
            ally_x, ally_y = ally.getPosition()
            for enemy in enemy_list:
                self_x, self_y = self.getPosition()
                enemy_x, enemy_y = enemy.getPosition()

                if self_x == enemy_x and self_x != ally_x:  # if on the same column
                    if enemy_y < self_y:  # enemy is located above
                        self.shoot('up')
                    else:  # enemy is located below
                        self.shoot('down')
                if self_y == enemy_y and self_y != ally_y:
                    if enemy_x < self_y:    # enemy is located left
                        self.shoot('left')
                    else:
                        self.shoot('right')

        #Heal
        for ally in ally_list:
            ally_HP = ally.getHP()
            ally_x, ally_y = ally.getPosition()

            if ally_HP < 40 and ally_y == self_y:
                if ally_x < self_x and self.readyToHeal():
                    self.shoot_heal('left')
                elif ally_x > self_x and self.readyToHeal():
                    self.shoot_heal('right')
  
