import tkinter as tk
import random as rd
from planetAlpha import PlanetAlpha
from planetTk import PlanetTk
from turmite import Turmite

class Turmites(PlanetTk):

    nb_iterations = 0
    nb_turmites = 0
    liste = []

    def __init__(self, root, lattitude_cells_count, longitude_cells_count, authorized_colors = ["white", "black"], cell_size = 20, **kw):
        PlanetTk.__init__(self, root, "Turmites", lattitude_cells_count, longitude_cells_count, {Turmite}, background_color = "blue", foreground_color = "white", gridlines_color="black", cell_size = cell_size, **kw)
        self.__authorized_colors = authorized_colors
        self.__affiche_nb_iterations = tk.Label(root, text="",bg="blue",fg="white")
        self.__affiche_nb_iterations.pack()
        self.__affiche_nb_turmites = tk.Label(root, text="",bg="blue",fg="white")
        self.__affiche_nb_turmites.pack()
        

    def reset_turmites(self):
        Turmites.liste = []
        Turmites.nb_iterations = 0
        Turmites.nb_turmites = 0

    def add_turmite(self, turmite):
        Turmites.liste.append(turmite)

    def add_random_turmite(self, event=None):
        rule = ""
        for _ in range (len(self.__authorized_colors)):
            rule += rd.choice(["0","1"])
            direction = rd.choice([PlanetAlpha.WEST, PlanetAlpha.SOUTH, PlanetAlpha.NORTH, PlanetAlpha.EAST])
            x = rd.randint(0,self.get_lines_count()-1)
            y = rd.randint(0,self.get_columns_count()-1)
        Turmites.liste.append(Turmite(x,y,direction,rule))
        Turmites.nb_turmites+=1
        self.__affiche_nb_turmites["text"] = "Nombre de turmites : "+str(Turmites.nb_turmites)


    def start(self, event=None, nb_iterations=1):
        dic_orientation = {PlanetAlpha.WEST: 0, PlanetAlpha.EAST: 180, PlanetAlpha.SOUTH: -90, PlanetAlpha.NORTH: 90}
        for turmite in Turmites.liste:
            self.itemconfigure(f"t_{turmite.get_pos()[0]}_{turmite.get_pos()[1]}", text=str(turmite))
            self.itemconfigure(f"t_{turmite.get_pos()[0]}_{turmite.get_pos()[1]}",angle=dic_orientation[turmite.get_direction()])
        
        for _ in range(nb_iterations):
            for turmite in Turmites.liste:
                if turmite.get_pos()[0] !=0 and turmite.get_pos()[1] !=0 and turmite.get_pos()[0] != self.get_lines_count()-1 and turmite.get_pos()[1] != self.get_columns_count()-1:
                    color = self.itemcget(f"c_{turmite.get_pos()[0]}_{turmite.get_pos()[1]}","fill") 
                    for i in range(len(self.__authorized_colors)):
                        if self.__authorized_colors[i] == color:
                            if turmite.get_ruleset()[i] == "0":
                                turmite.turn_left()
                            else :
                                turmite.turn_right()
                            if i == len(self.__authorized_colors)-1:
                                self.itemconfigure(f"c_{turmite.get_pos()[0]}_{turmite.get_pos()[1]}", fill=self.__authorized_colors[0])
                            else : self.itemconfigure(f"c_{turmite.get_pos()[0]}_{turmite.get_pos()[1]}", fill=self.__authorized_colors[i+1])
                    self.die(self.get_cell_number_from_coordinates(turmite.get_pos()[0],turmite.get_pos()[1]))
                    self.born(self.get_cell_number_from_coordinates(turmite.get_pos()[0]+turmite.get_direction()[0], turmite.get_pos()[1]+turmite.get_direction()[1]),str(turmite))
                    self.itemconfigure(f"t_{turmite.get_pos()[0]+turmite.get_direction()[0]}_{turmite.get_pos()[1]+turmite.get_direction()[1]}",angle=dic_orientation[turmite.get_direction()])
                    turmite.change_pos(turmite.get_pos()[0]+turmite.get_direction()[0],turmite.get_pos()[1]+turmite.get_direction()[1])
            print(turmite.get_direction())
        Turmites.nb_iterations+=1
        self.__affiche_nb_iterations["text"] = "Nombre d'itérations : "+str(Turmites.nb_iterations)
            

