import tkinter as tk
from planetAlpha import PlanetAlpha


class PlanetTk(PlanetAlpha,tk.Canvas):

    def __init__(self, root, name, lattitude_cells_count, longitude_cells_count, authorized_classes, background_color = "black", foreground_color = "white", gridlines_color = "blue", cell_size = 40, gutter_size = 0, margin_size = 0, show_content = True, show_grid_lines = True, **kw):
        PlanetAlpha.__init__(self, name, lattitude_cells_count, longitude_cells_count, "")
        self.__cell_size = cell_size
        self.__gutter_size = gutter_size
        self.__margin_size = margin_size
        self.__root = root
        self.__show_content = show_content
        self.__show_grid_lines = show_grid_lines
        self.__authorized_classes = authorized_classes
        self.__background_color = background_color
        self.__foreground_color = foreground_color
        self.__gridlines_color = gridlines_color
        kw['width'] = cell_size * lattitude_cells_count + 2 * margin_size + (lattitude_cells_count - 1) * gutter_size
        kw['height'] = cell_size * longitude_cells_count + 2 * margin_size + (longitude_cells_count - 1) * gutter_size
        tk.Canvas.__init__(self, root, bg=background_color, **kw)
        for cell_number in range(self.get_lines_count() * self.get_columns_count()):
            i, j = self.get_coordinates_from_cell_number(cell_number)
            y = j * (cell_size + gutter_size) + margin_size
            x = i * (cell_size + gutter_size) + margin_size
            self.create_rectangle(x, y, x + cell_size, y + cell_size, fill=foreground_color, tags=(f'c_{i}_{j}', f'c_{cell_number}'), width= show_grid_lines, outline = gridlines_color)
            self.create_text(x + cell_size // 2, y + cell_size // 2, text="", font=('Arial', cell_size // 2, 'bold'), angle=0, tags=(f't_{i}_{j}', f't_{cell_number}'))

    def get_root(self):
        return self.__root

    def get_foreground_color(self):
        return self.__background_color

    def get_background_color(self):
        return self.__background_color

    def born(self, cell_number, element):
        PlanetAlpha.born(self, cell_number, element)
        self.itemconfigure(f't_{cell_number}', text=element)

    def die(self, cell_number):
        PlanetAlpha.die(self, cell_number)
        self.itemconfigure(f't_{cell_number}', text=str(""))


    def born_randomly(self, element):
        a = self.get_random_free_place()
        self.born(a, element)
    
    def populate(self, class_names_count):
        for i in class_names_count:
            for j in range(class_names_count[i]):
                self.born_randomly(i)


    def move_element(self, cell_number, new_cell_number):
        self.born(new_cell_number, self.get_cell(cell_number))
        self.die(cell_number)
        
    ''' 
    def get_classes_cell_number(self):
        dic = {}
        for i in self.__authorized_classes :
            dic.update({str(i()):0})
        dic.update({str(Ground()):0})
        print(self.get_cell(1))
        taille = self.get_columns_count()*self.get_lines_count()
        for j in range(taille):
            dic[str(self.get_cell(j))]+=1
        return(dic)
    '''
    
    def __repr__(self):
        PlanetAlpha.__repr__(self)
