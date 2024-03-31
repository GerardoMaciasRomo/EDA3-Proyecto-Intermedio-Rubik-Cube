import numpy as np


class RubikCube:
    """Esta clase solo nos sirve para crear un prototipo de cubo lleno
    y de tamaño standard"""

    def create_cube(self):
        """Regresa un cubo con caras armadas"""

        cube = np.zeros((54))
        cube[9:18] = 1
        cube[18:27] = 2
        cube[27:36] = 3
        cube[36:45] = 4
        cube[45:54] = 5
        cube = np.reshape(cube, (6, 3, 3))

        return cube

    def create_cube_with_given_list(self, lista):
        """Esta función debería transformar un arreglo lineal dado en un cubo
        y regresar ese cubo"""
        cube = np.reshape(lista, (6, 3, 3))
        return cube

    def create_list_with_given_cube(self, cube):
        """Esta función convierte el cubo  a una lista plana y regresar esa lista"""
        lista = np.reshape(cube, (54))
        return lista


class Movements:
    """Dentro de esta clase Movements(), se encuentran los códigos de los doce
    movimientos principales  del puzzle de Rubik 3x3, me en cuentro aún revisando
    el correcto funcionamiento de cada una de las implementaciones"""

    def __init__(self, cube):
        """El único parámetro necesario para esta clase es un cubo que debe ser dado"""
        self.cube = cube

    def u(self):
        """Implementación del movimiento U en el cubo"""
        # Rotar Top sobre su propio eje a la Izquierda
        sub_top = self.cube[4]
        rotated_top = np.rot90(sub_top, k=-1)
        self.cube[4] = rotated_top
        # Rotar a la izquierda las primeras filas de las primras cuatro caras
        cero = self.cube[0, 0].copy()
        one = self.cube[1, 0].copy()
        two = self.cube[2, 0].copy()
        three = self.cube[3, 0].copy()
        self.cube[3, 0] = cero
        self.cube[2, 0] = three
        self.cube[1, 0] = two
        self.cube[0, 0] = one

    def u_prima(self):
        """Implementación del movimiento U' en el cubo"""
        # Rotar Top sobre su propio eje a la derecha
        sub_top = self.cube[4]
        rotated_top = np.rot90(sub_top, k=1)
        self.cube[4] = rotated_top
        # Rotar a la derecha las primeras filas de las primeras cuatro caras
        cero = self.cube[0, 0].copy()
        one = self.cube[1, 0].copy()
        two = self.cube[2, 0].copy()
        three = self.cube[3, 0].copy()
        self.cube[1, 0] = cero
        self.cube[2, 0] = one
        self.cube[3, 0] = two
        self.cube[0, 0] = three

    def d(self):
        """Implementación del movimiento D en el cubo"""
        # Rotar Down sobre su propio eje a la Izquierda
        sub_down = self.cube[5]
        rotated_down = np.rot90(sub_down, k=-1)
        self.cube[5] = rotated_down
        # Rotar a la izquierda las ultimas filas de las primras cuatro caras
        cero = self.cube[0, 2].copy()
        one = self.cube[1, 2].copy()
        two = self.cube[2, 2].copy()
        three = self.cube[3, 2].copy()
        self.cube[3, 2] = cero
        self.cube[2, 2] = three
        self.cube[1, 2] = two
        self.cube[0, 2] = one

    def d_prima(self):
        """Implementación del movimiento D' en el cubo"""
        sub_down = self.cube[5]
        rotated_down = np.rot90(sub_down, k=1)
        self.cube[5] = rotated_down
        # Rotar a la derecha las últimas filas de las primeras cuatro caras
        cero = self.cube[0, 2].copy()
        one = self.cube[1, 2].copy()
        two = self.cube[2, 2].copy()
        three = self.cube[3, 2].copy()
        self.cube[1, 2] = cero
        self.cube[2, 2] = one
        self.cube[3, 2] = two
        self.cube[0, 2] = three

    def f(self):
        """Implementación del movimiento F en el cubo"""
        sub_front = self.cube[0]
        rotated_front = np.rot90(sub_front, k=-1)
        self.cube[0] = rotated_front
        one = self.cube[1, :, 0].copy()
        four = self.cube[4, 2].copy()
        five = self.cube[5, 2].copy()
        three = self.cube[3, :, 2].copy()
        self.cube[1, :, 0] = four
        self.cube[5, 2] = one
        five = np.flip(five)
        self.cube[3, :, 2] = five
        three = np.flip(three)
        self.cube[4, 2] = three

    def f_prima(self):
        """Implementación del movimiento F' en el cubo"""
        sub_front = self.cube[0]
        rotated_front = np.rot90(sub_front, k=1)
        self.cube[0] = rotated_front
        one = self.cube[1, :, 0].copy()
        four = self.cube[4, 2].copy()
        five = self.cube[5, 2].copy()
        three = self.cube[3, :, 2].copy()
        self.cube[4, 2] = one
        four = np.flip(four)
        self.cube[3, :, 2] = four
        three = np.flip(three)
        self.cube[5, 2] = three
        self.cube[1, :, 0] = five

    def b(self):
        """Implementación del movimiento B en el cubo"""
        sub_back = self.cube[2]
        rotated_back = np.rot90(sub_back, k=-1)
        self.cube[2] = rotated_back
        four = self.cube[4, 0].copy()
        one = self.cube[1, :, 2].copy()
        three = self.cube[3, :, 0].copy()
        five = self.cube[5, 0].copy()
        four = np.flip(four)
        self.cube[3, :, 0] = four
        self.cube[4, 0] = one
        self.cube[1, :, 2] = five
        three = np.flip(three)
        self.cube[5, 0] = three

    def b_prima(self):
        """Implementación del movimiento B' en el cubo"""
        sub_back = self.cube[2]
        rotated_back = np.rot90(sub_back, k=1)
        self.cube[2] = rotated_back
        four = self.cube[4, 0].copy()
        one = self.cube[1, :, 2].copy()
        three = self.cube[3, :, 0].copy()
        five = self.cube[5, 0].copy()
        self.cube[1, :, 2] = four
        self.cube[5, 0] = one
        five = np.flip(five)
        self.cube[3, :, 0] = five
        three = np.flip(three)
        self.cube[4, 0] = three

    def r(self):
        """Implementación del movimiento R en el cubo"""
        index_column = 2
        cero = self.cube[0, :, index_column].copy()
        four = self.cube[4, :, index_column].copy()
        two = self.cube[2, :, 0].copy()
        five = self.cube[5, :, 0].copy()
        five = np.flip(five)
        four = np.flip(four)
        self.cube[0, :, index_column] = five
        self.cube[4, :, index_column] = cero
        self.cube[2, :, 0] = four
        self.cube[5, :, 0] = two
        sub_right = self.cube[1]
        rotated_right = np.rot90(sub_right, k=-1)
        self.cube[1] = rotated_right

    def r_prima(self):
        """Implementación del movimiento R' en el cubo"""
        sub_right = self.cube[1]
        rotated_right = np.rot90(sub_right, k=1)
        self.cube[1] = rotated_right
        index_column = 2
        cero = self.cube[0, :, index_column].copy()
        four = self.cube[4, :, index_column].copy()
        two = self.cube[2, :, 0].copy()
        five = self.cube[5, :, 0].copy()
        two = np.flip(two)
        cero = np.flip(cero)
        self.cube[0, :, index_column] = four
        self.cube[4, :, index_column] = two
        self.cube[2, :, 0] = five
        self.cube[5, :, 0] = cero

    def l(self):
        """Implementación del movimiento L en el cubo"""
        sub_left = self.cube[3]
        rotated_left = np.rot90(sub_left, k=-1)
        self.cube[3] = rotated_left
        index_column = 0
        cero = self.cube[0, :, index_column].copy()
        four = self.cube[4, :, index_column].copy()
        two = self.cube[2, :, 2].copy()
        five = self.cube[5, :, 2].copy()
        five = np.flip(five)
        four = np.flip(four)
        self.cube[0, :, index_column] = five
        self.cube[4, :, index_column] = cero
        self.cube[2, :, 2] = four
        self.cube[5, :, 2] = two

    def l_prima(self):
        """Implementación del movimiento L' en el cubo"""
        sub_left = self.cube[3]
        rotated_left = np.rot90(sub_left, k=1)
        self.cube[3] = rotated_left
        index_column = 0
        cero = self.cube[0, :, index_column]
        four = self.cube[4, :, index_column]
        two = self.cube[2, :, index_column]
        five = self.cube[5, :, index_column]
        self.cube[0, :, index_column] = four
        self.cube[4, :, index_column] = two
        self.cube[2, :, index_column] = five
        self.cube[5, :, index_column] = cero

    def print_cube(self):
        """Esta función solo imprime el cubo"""
        print(self.cube)

    def return_cube(self):
        """Devuelve el cubo"""
        return self.cube

    def ravel(self):
        return self.cube.ravel()


class RubikSolver(RubikCube, Movements):
    def __init__(self, cube):
        self.cube = cube

    def random_suffle(self):
        """Esta función debe permitir revolver el cubo con una serie de movimientos al azar"""
        pass

    def lista_suffle(self):
        """Esta función debe revolver el cubo según el array que le sesa dado"""
        pass

    def Best_First_Search(self, goal, heuristic):
        """Esta función debe de resolver el cubo de rubik ccon el allgoritmo de Best First Search"""
        self.goal = goal
        self.heuristic = heuristic

    def Breadth_First_Search(self, goal, heuristic):
        """Esta función debe de resolver el cubo de rubik con el algoritmo de Breadth First Search"""
        self.goal = goal
        self.heuristic = heuristic

    def A_Star(self, goal, heuristic):
        """Esta función debe resolver el cubo de rubik con el algorito de A Estrella"""
        self.goal = goal
        self.heuristic = heuristic

    def Surprise(self, goal, heuristic):
        """Esta función debe resolver el cubo de rubik con un algorimo de nuestra autoría ( No tengo ni idea de que vamos a hacer en esta parte)"""
        self.goal = goal
        self.heuristic = heuristic
        # Se me ocurre que podemos poner dijkstra


"""Bienvenido a la sección de Testeo del código """
# help(RubikCube)
# help(Movements)
cubo = RubikCube()
lista = []
for i in range(54):
    lista.append(i)
cubo = cubo.create_cube_with_given_list(lista)
movimientos = Movements(cubo)
movimientos.print_cube()
print("------------------------------")
# movimientos.u()
# movimientos.print_cube()
# print("------------------------------")
# movimientos.u_prima()
# movimientos.print_cube()
"""Definitivamente U y U' funcionan al 100%"""
# movimientos.d()
# movimientos.print_cube()
# print("------------------------------")
# movimientos.d_prima()
# movimientos.print_cube()
"""Definitivamente D y D' funcionan al 100 %"""
# movimientos.r()
# movimientos.print_cube()
# print("--------------------------")
# movimientos.r()
# movimientos.r()
# movimientos.r()
# movimientos.print_cube()
"""Definitivamente R funciona  al 100%"""
# movimientos.r_prima()
# movimientos.print_cube()
# print("--------------------------")
# movimientos.r_prima()
# movimientos.r_prima()
# movimientos.r_prima()
# movimientos.print_cube()
"""Definitivamente R' funciona al 100%"""
# movimientos.l()
# movimientos.print_cube()
# print("--------------------------")
# movimientos.l()
# movimientos.l()
# movimientos.l()
# movimientos.print_cube()
"""Definitivamente L funciona al 100%"""
# movimientos.l_prima()
# movimientos.print_cube()
# print("--------------------------")
# movimientos.l_prima()
# movimientos.l_prima()
# movimientos.l_prima()
# movimientos.print_cube()
"""Definitivamente L' funciona al 100%"""
# movimientos.f()
# movimientos.print_cube()
# print("--------------------------")
# movimientos.f()
# movimientos.f()
# movimientos.f()
# movimientos.print_cube()
"""Definitivamente F funciona al 100% """
# movimientos.f_prima()
# movimientos.print_cube()
# print("--------------------------")
# movimientos.f_prima()
# movimientos.f_prima()
# movimientos.f_prima()
# movimientos.print_cube()
"""Definitivamente F' funciona al 100%"""
# movimientos.b()
# movimientos.print_cube()
# print("--------------------------")
# movimientos.b()
# movimientos.b()
# movimientos.b()
# movimientos.print_cube()
"""Definitivamente B funciona al 100%"""
# movimientos.b_prima()
# movimientos.print_cube()
# print("--------------------------")
# movimientos.b_prima()
# movimientos.b_prima()
# movimientos.b_prima()
# movimientos.print_cube()
"""Definitivamnte B' funciona al 100%"""
"""Ahora probaré la funcionalidad general del cubo """
"""Final Test Case"""
movimientos.r()
movimientos.r_prima()
print("r-------------------------------")
movimientos.print_cube()
# movimientos.l()
# movimientos.l_prima()
# print("l-------------------------------")
# movimientos.print_cube()
movimientos.u()
movimientos.u_prima()
print("u-------------------------------")
movimientos.print_cube()
movimientos.d()
movimientos.d_prima()
print("d-------------------------------")
movimientos.print_cube()
movimientos.f()
movimientos.f_prima()
print("f-------------------------------")
movimientos.print_cube()
movimientos.b()
movimientos.b_prima()
print("b-------------------------------")
movimientos.print_cube()

ravel = movimientos.ravel()
print(ravel)
"""Test Case 1"""
# movimientos.r()
# movimientos.r_prima()
# ravel = movimientos.ravel()
# print(ravel)
"""Test Case 2"""
# movimientos.r()
# movimientos.r_prima()
# ravel = movimientos.ravel()
# print(ravel)
"""Test Case 3"""
# movimientos.f()
# movimientos.f_prima()
# ravel = movimientos.ravel()
# print(ravel)
"""Test Case 4"""
# movimientos.d()
# movimientos.d_prima()
# ravel = movimientos.ravel()
# print(ravel)
"""Test Case 5"""
# movimientos.u()
# movimientos.u_prima()
# ravel = movimientos.ravel()
# print(ravel)
"""Test Case 6"""
# movimientos.b()
# movimientos.b_prima()
# ravel = movimientos.ravel()
# print(ravel)
"""Según Los casos pruebas hay un error en L y/o L' """
