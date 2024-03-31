import numpy as np


class Hola:
    def create_cube(self):

        self.cube = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(6)]

        for i in range(6):
            print("Cara", i + 1)
            for j in range(3):
                for k in range(3):
                    if i == 0:
                        self.cube[i][j][k] = 1
                    elif i == 1:
                        self.cube[i][j][k] = 2
                    elif i == 2:
                        self.cube[i][j][k] = 3
                    elif i == 3:
                        self.cube[i][j][k] = 4
                    elif i == 4:
                        self.cube[i][j][k] = 5
                    else:
                        self.cube[i][j][k] = 6
                    print(self.cube[i][j][k], end=" ")
                print()
            print()
        # Hasta aquí voy a pasar al código
        print(self.cube)
        print(self.cube[1][0])
        return self.cube

    def u_prima(self, cube):
        self.cube = cube

        auxiliar1 = cube[0][0]
        auxiliar2 = cube[1][0]
        auxiliar3 = cube[2][0]
        auxiliar4 = cube[3][0]

        cube[0][0] = auxiliar4
        cube[1][0] = auxiliar1
        cube[2][0] = auxiliar2
        cube[3][0] = auxiliar3

        print(cube[0])
        print(cube[1])
        print(cube[2])
        print(cube[3])

        cube[4] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(cube[4])
        for i in range(3):
            for j in range(3):
                new_i = j
                new_j = 2 - i
                cube[4][new_i][new_j] = cube[4][i][j]
        print(cube[4])


hola = Hola()
cubillo = hola.create_cube()
hola.u_prima(cubillo)
print("-----------------------------------------------")
