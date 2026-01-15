from planetAlpha import PlanetAlpha
from element import Element

class Turmite(Element):


    def __init__(self, pos_x, pos_y, direction, ruleset):
        Element.__init__(self,"\U0001FAB2", pos_x, pos_y)
        self.__direction = direction
        self.__ruleset = ruleset

    def get_direction(self):
        return self.__direction
        
    def get_ruleset(self):
        return self.__ruleset

    def turn_right(self):
        if self.__direction == PlanetAlpha.SOUTH:
            self.__direction = PlanetAlpha.WEST
        elif self.__direction == PlanetAlpha.WEST:
            self.__direction = PlanetAlpha.NORTH
        elif self.__direction == PlanetAlpha.NORTH:
            self.__direction = PlanetAlpha.EAST
        else :
            self.__direction = PlanetAlpha.SOUTH


    def turn_left(self):
        if self.__direction == PlanetAlpha.SOUTH:
            self.__direction = PlanetAlpha.EAST
        elif self.__direction == PlanetAlpha.EAST:
            self.__direction = PlanetAlpha.NORTH
        elif self.__direction == PlanetAlpha.NORTH:
            self.__direction = PlanetAlpha.WEST
        else :
            self.__direction = PlanetAlpha.SOUTH


