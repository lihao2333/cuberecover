import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

fig, ax = plt.subplots()
patches = []
num_polygons = 5
num_sides = 5

polygon = Polygon(((1,0),(1,1),(0,1)),True)
patches.append(polygon)
polygon = Polygon(((4,0),(1,1),(0,1)),True)
patches.append(polygon)
p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=1)

colors = ["#EB70AA","#009911"]
p.set_array(np.array(colors))

ax.add_collection(p)

plt.show()
