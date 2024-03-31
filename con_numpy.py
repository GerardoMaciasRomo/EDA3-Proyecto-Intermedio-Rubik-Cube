# Querido Pichón, esta página no sirve para absolutamente nada dentro del código
# Solamente me está sirviendo para aprender a usar una librería numpy
# De antemano, gracias por tu comprensión y paciencia.

import numpy as np

cube = np.zeros((6, 3, 3))
print(cube)
arreglo = []
for i in range(54):
    arreglo.append(i + 1)
print(arreglo)
np.array(arreglo)
reshaped = np.reshape(arreglo, (6, 3, 3))
print(reshaped)
reshaped2 = np.reshape(reshaped, (54))
print(reshaped2)
reshaped2.ravel()
reshaped2[:9] = 0
reshaped2[9:18] = 1
reshaped2[18:27] = 2
reshaped2[27:36] = 3
reshaped2[36:45] = 4

reshaped3 = np.reshape(reshaped2, (6, 3, 3))
print(reshaped3[5])
down = reshaped3[5]
rotated_down = np.rot90(down, k=1)
print(rotated_down)
reshaped3[5] = rotated_down
print(reshaped3)
rotative_faces = reshaped3[[0, 1, 2, 3]]
rotated_faces = np.roll(rotative_faces, 1, axis=0)
reshaped3[[0, 1, 2, 3]] = rotated_faces
print(rotated_faces)
print(reshaped3)
print("-------------------------")
cero = reshaped3[0, 0]
one = reshaped3[1, 0]
two = reshaped3[2, 0]
three = reshaped3[3, 0]


print(cero, one, two, three)
reshaped3[1, 0] = cero
reshaped3[2, 0] = one
reshaped3[3, 0] = two
reshaped3[0, 0] = three
print(cero, one, two, three)
print(reshaped3)
cero = reshaped3[0, 0]
one = reshaped3[1, 0]
two = reshaped3[2, 0]
three = reshaped3[3, 0]
print("-----------------------------")
index_column = 2
column = reshaped[5, :, index_column]
print(column)
reshaped3[5, :, index_column] = [0, 1, 2]
print(reshaped3)
print("-------------------------------")
sub_right = reshaped3[1]
rotated_right = np.rot90(sub_right, k=-1)
reshaped3[1] = rotated_right
print(reshaped3)
print("--------------------------")
reshaped3[0, :, 0] = [2, 4, 6]
reshaped[0, :, 2] = [5, 7, 9]
print(reshaped3[0])
sub_front = reshaped3[0]
rotated_front = np.rot90(sub_front, k=-1)
reshaped3[0] = rotated_front
print(reshaped3[0])
print("-------------------------------")


class CuboPedorro:
    def __init__(self, caras, colores):
        self.caras = caras
        self.colores = colores

    def __str__(self):
        return f"Cubo Pedorro de {self.caras} caras"


cubo = CuboPedorro(6, "Arcoiris")
print(cubo)
