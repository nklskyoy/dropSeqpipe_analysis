import os
import matplotlib.pyplot as plt

samples = [["255_S4", "254_S3"], ["253_S2", "252_S1"]]

rules_original = ["get_top_barcodes", "MergeBamAlignment","repair_barcodes"]
rules = ["MERGE_AND_REPAIR"]


def read_sec_from_file(path):
    file  = open(path,"r")
    haeder = file.readline()
    benchmarks = file.readline()
    sec = benchmarks.split("\t")[0]
    file.close()
    return sec


path_original = os.getcwd()+"/original/"
path_accelerate = os.getcwd()+"/accelerate/"

print(path_original)
print(path_accelerate)

fig,axs = plt.subplots(2,2)
for i in range(len(samples)):
    for j in range(len(samples[i])):
        sample = samples[i][j]
        sec_acc = read_sec_from_file(path_accelerate+"MERGE_AND_REPAIR."+sample+".txt")

        sec_original = [ read_sec_from_file(path_original+rules_original[r]+"."+sample+".txt")
            for r in range(len(rules_original))]

        print(sec_original)