import matplotlib.pyplot as plt
import itertools
from datetime import datetime, timedelta
import os

RULENAME = "get_top_barcodes"
SAMPLES = [["HBP_Ape_266_CN","HBP_Ape_266_Putamen"],["HBP_Ape_266_SN","HBP_Ape_267_CN"],["HBP_Ape_268_CN","HBP_Ape_268_Putamen"]]


def read_sec_from_benchmark(benchmark_path):
    benchmark = open(benchmark_path,"r")
    header_line = benchmark.readline()
    benchmark_line = benchmark.readline()
    return float(benchmark_line.split("\t")[0])


def autolabel(rects,ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        sec = timedelta(seconds=int(height))
        ax.annotate('{}'.format(str(sec)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    fontSize=7,
                    ha='center', va='bottom')


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

fig,axs = plt.subplots(3,2)

x = [0,1]

row_ctr = 0
for samples in SAMPLES:
    col_ctr = 0
    for sample in samples:
        rects = axs[row_ctr,col_ctr].bar(x,[b[sample],b_star[sample]],width=0.99)
        axs[row_ctr, col_ctr].set_xticks([0,1])
        axs[row_ctr, col_ctr].set_xticklabels(["get_top-\nbarcodes", "get_top-\nbarcodes*"], horizontalalignment="center",
                                  fontsize=7)
        autolabel(rects,axs[row_ctr, col_ctr])
        col_ctr += 1
    row_ctr += 1


for ax in axs.flat:
    ax.set(xlabel='rule', ylabel='time in seconds')

fig.tight_layout(pad=3.0)

plt.show()