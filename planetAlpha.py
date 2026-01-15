import random
from grid import Grid

class PlanetAlpha(Grid):
    WEST = (0,-1)
    EAST = (0,1)
    NORTH = (-1,0)
    SOUTH = (1,0)
    NORTH_EAST = (-1,1)
    SOUTH_EAST = (1,1)
    NORTH_WEST = (-1,-1)
    SOUTH_WEST = (1,-1)
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = {NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST}
    
    def __init__(self, name, latitude_cells_count, longitude_cells_count, ground):
        grid_init = [[ground for _ in range(longitude_cells_count)] for _ in range(latitude_cells_count)]
        Grid.__init__(self, grid_init)
        self.__name = name
        self.__ground = ground


    def get_random_free_place(self):
        l = Grid.get_same_value_cell_numbers(self, self.__ground)
        if l !=[]:
            ind = random.randint(0,len(l)-1)
            return l[ind]
        return -1
  
    def get_name(self):
        return self.__name

    def get_ground(self):
        return self.__ground

    def born(self, cell_number, element):
        Grid.set_cell(self, cell_number, element)
        
    def die(self, cell_number):
        Grid.set_cell(self, cell_number, self.get_ground())
        
    def __repr__(self):
        print(f"{self.__name} ({self.get_lines_count() *self.get_columns_count()-self.get_count(self.__ground)} habitant(s)")
        return Grid.get_grid_str(self, separator='\t')
