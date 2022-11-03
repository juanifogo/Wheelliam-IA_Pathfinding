from Pathfinding import *
from Detector import *
import requests

url = "http://localhost:5000/test"
finder, grid = setup_pf("example_map_binary.png")
detector = setup_detector("C:/Users/46756494/Documents/wheelliam/model")
START_POS = 0
END_POS = 0
curr_pos = START_POS
dirs = pathfind(finder, grid, START_POS, END_POS)
while not curr_pos == END_POS:
    # codigo de conseguir coords
    collision = False
    cam = 0
    if(collision):
        im_path = runDetector(detector, cam)
        im = open(im_path, "rb")
        data = {"file": im}
        r = requests.post(url, files=data)
        if (im):
            pass
            #bocina()
        else:
            pass
            #esquivar() # se modifica curr_pos
            dirs = pathfind(finder, grid, curr_pos, END_POS)
