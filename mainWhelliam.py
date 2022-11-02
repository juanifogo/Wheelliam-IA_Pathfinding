from Pathfinding import *
from Detector import *

finder, grid = setup_pf("example_map_binary.png")

# codigo de conseguir coords
START_POS = 0
END_POS = 0


dirs = pathfind(finder, grid, START_POS, END_POS)