class Element():

    def __init__(self, char_repr, nb_ligne, nb_colonne):
        self.__char_repr = char_repr
        self.__pos = (nb_ligne, nb_colonne)

    def __repr__(self):
        return self.__char_repr

    def __str__(self):
        return self.__char_repr

    def get_pos(self):
        return self.__pos

    def change_pos(self, ligne, colonne):
        self.__pos = (ligne, colonne)
