import numpy as np # numpy para las operaciones con matrices, en este caso las imagenes 
import cv2 # OpenCV para manipular y visualizar la imagen

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder

def setup_pf(map):
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    map = cv2.imread(map)
    map = cv2.cvtColor(map, cv2.COLOR_BGR2GRAY)
    map = np.uint8(map/255)
    grid = Grid(matrix=map)

    return finder, grid

def pathfind(finder, grid, start, end):
    path, runs = finder.find_path(start, end, grid)

    # Mostramos los resultados
    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))

    com = []
    mov_x = False
    mov_y = False
    for i, coord in enumerate(path):
    # Itero en la lista 'path', siendo 'coord' tuplas de 2 enteros marcando las coordenadas del camino, e 'i' el indice del elemento en la lista
        if coord == path[0]:
            com.append('S') # Si la coordenada es la primera de la lista la marco como el inicio en la nueva lista
        else:
            if coord == path[-1]:
                com.append('E') # Si es la ultima la marco como el fin del camino y salgo del loop
                break
            if coord[0] == path[i-1][0]: # Si la coordenada X del elemento actual es igual a la del anterior sabemos que no nos movemos en el eje x en este paso
                mov_x = False
            else:
                mov_x = True # Sino sabemos que si
            if coord[1] == path[i-1][1]: # Lo mismo para el eje Y
                mov_y = False
            else:
                mov_y = True
            if mov_y and coord[1] > path[i-1][1]: # Si nos movemos en el eje Y, y la coordenada Y del punto actual es mayor a la del anterior, nos movemos hacia abajo en el eje Y ya que el grafico de la lista es positivo hacia abajo
                com.append('D')
            elif mov_y and coord[1] < path[i-1][1]: # Si la condicion opuesta se cumple, nos movemos hacia arriba
                com.append('U')
            elif mov_x and coord[0] < path[i-1][0]: # Si nos movemos en el eje X, y la coordenada X del punto actual es menor a la del anterior, nos movemos hacia la izquierda en el eje X ya que el grafico de la lista es positivo hacia la derecha
                com.append('L') 
            elif mov_x and coord[0] > path[i-1][0]: # Si la condicion opuesta se cumple, nos movemos hacia la derecha
                com.append('R')
    return com

def getPos(pos, dirs, i):
    newPos = pos
    dirs = dirs[0:i]
    for val in dirs:
        if val == 'L':
            newPos[0]-=1
        if val == 'R':
            newPos[0]+=1
        if val == 'U':
            newPos[1]+=1
        if val == 'D':
            newPos[1]-=1  
    return newPos