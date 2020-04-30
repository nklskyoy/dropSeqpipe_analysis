import matplotlib.pyplot as plt
import itertools
import os

RULENAME = "MergeBamAlignment"
SAMPLES = [["252_S1","253_S2"],["254_S3","255_S4"]]

def read_sec_from_benchmark(benchmark_path):
    benchmark = open(benchmark_path,"r")
    header_line = benchmark.readline()
    benchmark_line = benchmark.readline()
    return float(benchmark_line.split("\t")[0])


path = os.getcwd()+"/"+os.path.dirname(__file__)+"original/"
path_star = os.getcwd()+"/"+os.path.dirname(__file__)+"run1/"

b = {}
b_star = {}

for sample in list(itertools.chain.from_iterable(SAMPLES)):
    path_sample = path + RULENAME + "." + sample + ".txt"
    path_sample_star = path_star + "benchmark." + sample + ".txt"
    b[sample] = read_sec_from_benchmark(path_sample)
    b_star[sample] = read_sec_from_benchmark(path_sample_star)


plt.style.use('ggplot')

fig,axs = plt.subplots(2,2)

x = [0,1]

row_ctr = 0
for samples in SAMPLES:
    col_ctr = 0
    for sample in samples:
        axs[row_ctr,col_ctr].bar(x,[b["252_S1"],b_star["252_S1"]],width=0.99)
        axs[row_ctr, col_ctr].set_xticks([0,1])
        axs[row_ctr, col_ctr].set_xticklabels(["Merge-\nBamAlignment", "Merge-\nBamAlignment*"], horizontalalignment="center",
                                  fontsize=7)
        col_ctr += 1
    row_ctr += 1


for ax in axs.flat:
    ax.set(xlabel='rule', ylabel='time in seconds')

fig.tight_layout(pad=3.0)

plt.show()