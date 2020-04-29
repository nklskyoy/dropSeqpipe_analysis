import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

cdict = [(0, "#FFFFFF"),(1, "#FF0000")]
cmap_name = 'my_list'
nbins = 100


cm = LinearSegmentedColormap.from_list(
    cmap_name, cdict)


fig=plt.figure(figsize=(0.5,32))



ax=fig.add_subplot(111)
ax.axis([0,20,-50,3215.311975])
norm = mpl.colors.Normalize(vmin=0, vmax=32)
cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cm,
                                orientation='vertical',
                                norm=norm,
                                ticks=[0.183175,32],
                                )

plt.subplots_adjust(left=0.4, right=0.8)
plt.show()