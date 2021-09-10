
from posix import listdir 
import numpy as np
import loadUtils
from loader import Loader

model = Loader("FanA", "Conf203", 60)
print(model.buildMatrix())
