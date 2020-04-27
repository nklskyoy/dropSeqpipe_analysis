import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
samples = [["255_S4", "254_S3"], ["253_S2", "252_S1"]]

rules_original = ["get_top_barcodes", "MergeBamAlignment","repair_barcodes"]
rules = ["MERGE_AND_REPAIR"]


def read_sec_from_file(path):
    file  = open(path,"r")
    haeder = file.readline()
    benchmarks = file.readline()
    sec = float(benchmarks.split("\t")[0])
    file.close()
    return sec


path_original = os.getcwd()+"/"+os.path.dirname(__file__)+"/original/"
path_accelerate = os.getcwd()+"/"+os.path.dirname(__file__)+"/accelerate/"

print(path_original)
print(path_accelerate)


get_top_barcodes_patch = mpatches.Patch(color='indianred', hatch="+",label='get_top_barcodes')
MergeBamAlignment_patch = mpatches.Patch(color='grey', hatch=".",label="MergeBamAlignment")
repair_barcodes_patch = mpatches.Patch(color='orchid', hatch="\\",label="repair_barcodes")

acc_patch = mpatches.Patch(color='lightblue', hatch="//",label="merge_and_repair")

fig,axs = plt.subplots(2,2)
for i in range(len(samples)):
    for j in range(len(samples[i])):
        sample = samples[i][j]
        sec_acc = [read_sec_from_file(path_accelerate+"MERGE_AND_REPAIR."+sample+".txt"),0,0]

        sec_original = [ read_sec_from_file(path_original+rules_original[r]+"."+sample+".txt")
            for r in range(len(rules_original))]

        sec = np.array([sec_acc,sec_original]).transpose()
        print(sec[0])
        lev1 = axs[i,j].bar([1,2],sec[0],1,color=["lightblue","indianred"])
        lev2 = axs[i,j].bar([1,2],sec[1],1,bottom=sec[0], color=["lightblue","grey"])
        lev3 = axs[i,j].bar([1,2],sec[2],1,bottom=sec[1]+sec[0], color=["lightblue","orchid"])

        lev1[0].set_hatch("\\") # accelerated bar
        lev1[1].set_hatch("+")

        lev2[1].set_hatch(".")     # die oberste bar

        lev3[1].set_hatch("//")



        print(sec[0])
        print(sec[1])

for ax in fig.get_axes():
    ax.label_outer()
    ax.set_xticklabels(["",""])

fig.legend(handles=[get_top_barcodes_patch,MergeBamAlignment_patch,repair_barcodes_patch,acc_patch])

plt.show()