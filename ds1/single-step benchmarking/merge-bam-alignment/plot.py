import matplotlib.pyplot as plt
import matplotlib.dates as md

plt.style.use('ggplot')
b = {
    "252_S1":1363.8853,
    "253_S2":1267.8662,
    "254_S3":1044.3471,
    "255_S4":919.5227
}

b_star = {
    "252_S1": 1489.0851,
    "253_S2": 1364.0728,
    "254_S3": 969.9974,
    "255_S4": 729.1544
}

fig,axs = plt.subplots(2,2)

x = [0,1]
rects = axs[0,0].bar(x,[b["252_S1"],b_star["252_S1"]],width=0.99)
axs[0,0].set_xticks([0,1])
axs[0,0].set_xticklabels(["Merge-\nBamAlignment","Merge-\nBamAlignment*"],horizontalalignment="center",fontsize=7)

axs[0,1].bar(x,[b["253_S2"],b_star["253_S2"]],width=0.99)
axs[0,1].set_xticks([0,1])
axs[0,1].set_xticklabels(["Merge-\nBamAlignment","Merge-\nBamAlignment*"],horizontalalignment="center",fontsize=7)

axs[1,0].bar(x,[b["254_S3"],b_star["254_S3"]],width=0.99)
axs[1,0].set_xticks([0,1])
axs[1,0].set_xticklabels(["Merge-\nBamAlignment","Merge-\nBamAlignment*"],horizontalalignment="center",fontsize=7)

axs[1,1].bar(x,[b["255_S4"],b_star["255_S4"]],width=0.99)
axs[1,1].set_xticks([0,1])
axs[1,1].set_xticklabels(["Merge-\nBamAlignment","Merge-\nBamAlignment*"],horizontalalignment="center",fontsize=7)

for ax in axs.flat:
    ax.set(xlabel='rule', ylabel='time in seconds')

fig.tight_layout(pad=3.0)

plt.show()