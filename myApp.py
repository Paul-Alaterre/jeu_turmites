import tkinter as tk
from turmites import Turmites

class MyApp(tk.Tk):


    def __init__(self):
        tk.Tk.__init__(self)
        self.__titre = tk.Label(self, text="Choisissez un jeu")
        self.__titre.grid(row=0, column=1)

        #Turmites
        self.__turmites = tk.Frame(self)
        self.__turmites_titre = tk.Label(self.__turmites, text="Turmites")
        self.__turmites_input_lines_titre = tk.Label(self.__turmites, text="Insérer un nombre de colonnes")
        self.__turmites_input_lines = tk.Spinbox(self.__turmites, from_=0, to=10000)
        self.__turmites_input_columns_titre = tk.Label(self.__turmites, text="Insérer un nombre de lignes")
        self.__turmites_input_columns = tk.Spinbox(self.__turmites, from_=0, to=10000)
        self.__turmites_color_choice_titre = tk.Label(self.__turmites, text="Choisissez un nombre de couleur")
        self.__turmites_input_cell_size = tk.Spinbox(self.__turmites, from_=0, to=10000)
        self.__turmites_input_cell_size_titre = tk.Label(self.__turmites, text="Choisissez la taille des 'pixels'")
        self.__turmites_color_var = tk.IntVar()
        self.__turmites_color_var.set("0")
        self.__turmites_color_choice_1 = tk.Radiobutton(self.__turmites, text="2 couleurs", variable=self.__turmites_color_var, value=1)
        self.__turmites_color_choice_2 = tk.Radiobutton(self.__turmites, text="4 couleurs", variable=self.__turmites_color_var, value=2)
        self.__turmites_color_choice_3 = tk.Radiobutton(self.__turmites, text="6 couleurs", variable=self.__turmites_color_var, value=3)
        self.__turmites_button = tk.Button(self.__turmites, text="Start", command=self.turmites)
        self.__turmites.grid(row=1, column=1)
        self.__turmites_titre.pack()
        self.__turmites_input_lines_titre.pack()
        self.__turmites_input_lines.pack()
        self.__turmites_input_columns_titre.pack()
        self.__turmites_input_columns.pack()
        self.__turmites_input_cell_size_titre.pack()
        self.__turmites_input_cell_size.pack()
        self.__turmites_color_choice_titre.pack()
        self.__turmites_color_choice_1.pack()
        self.__turmites_color_choice_2.pack()
        self.__turmites_color_choice_3.pack()
        self.__turmites_button.pack()

        
    def turmites(self):
        root = tk.Toplevel(self, bg = "blue")
        colors = ["blue","white"]
        if self.__turmites_color_var.get() == 2 :
            colors = ["blue","white","green","yellow"]
        elif self.__turmites_color_var.get() == 3:
            colors = ["blue","white","green","yellow","red","purple"]
            
        jeu = Turmites(root, int(self.__turmites_input_lines.get()),int(self.__turmites_input_columns.get()), cell_size= int(self.__turmites_input_cell_size.get()),authorized_colors = colors)
        jeu.reset_turmites()
        jeu.pack()
        tk.Button(root, text="Iteration suivante (pressez la barre espace pour plus de vitesse)", command=jeu.start, bg="white", fg="blue").pack()
        tk.Button(root, text="Ajouter une turmite aléatoirement (pressez 'a' pour plus de vitesse)", command=jeu.add_random_turmite, bg="white", fg="blue").pack()
        root.bind("<space>",jeu.start)
        root.bind("<a>",jeu.add_random_turmite)
        tk.Button(root, text="Quitter", command= root.destroy, bg="white", fg="blue").pack()

            



MyApp().mainloop()
