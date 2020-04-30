import matplotlib.pyplot as plt
import matplotlib.dates as md

plt.style.use('ggplot')
b = {
    "HBP_Ape_266_CN":63426.6755,
    "HBP_Ape_266_SN":17324.4382,
    "HBP_Ape_267_CN":147460.4074,
    "HBP_Ape_268_CN":52247.8957
}

b_star = {
    "HBP_Ape_266_CN":1242.4088,
    "HBP_Ape_266_SN":342.6047,
    "HBP_Ape_267_CN":3664.9562,
    "HBP_Ape_268_CN":1024.4064
}

fig,axs = plt.subplots(2,2)

x = [0,1]
rects = axs[0,0].bar(x,[b["HBP_Ape_266_CN"],b_star["HBP_Ape_266_CN"]],width=0.99)
axs[0,0].set_xticks([0,1])
axs[0,0].set_xticklabels(["get_top\n_barcodes","get_top\n_barcodes*"],horizontalalignment="center",fontsize=7)

axs[0,1].bar(x,[b["HBP_Ape_266_SN"],b_star["HBP_Ape_266_SN"]],width=0.99)
axs[0,1].set_xticks([0,1])
axs[0,1].set_xticklabels(["get_top\n_barcodes","get_top\n_barcodes*"],horizontalalignment="center",fontsize=7)

axs[1,0].bar(x,[b["HBP_Ape_267_CN"],b_star["HBP_Ape_267_CN"]],width=0.99)
axs[1,0].set_xticks([0,1])
axs[1,0].set_xticklabels(["get_top\n_barcodes","get_top\n_barcodes*"],horizontalalignment="center",fontsize=7)

axs[1,1].bar(x,[b["HBP_Ape_268_CN"],b_star["HBP_Ape_268_CN"]],width=0.99)
axs[1,1].set_xticks([0,1])
axs[1,1].set_xticklabels(["get_top\n_barcodes","get_top\n_barcodes*"],horizontalalignment="center",fontsize=7)

for ax in axs.flat:
    ax.set(xlabel='rule', ylabel='time in seconds')

fig.tight_layout(pad=3.0)

plt.show()