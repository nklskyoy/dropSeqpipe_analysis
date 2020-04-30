import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

plt.style.use('ggplot')


def parse_table(table):
    line1 = table.readline()
    R1 = []
    R2 = []

    while line1:
        samplename = line1.split("\t")[0]
        line2 = table.readline().split("\t")
        size_R1 = float(line2[0].split("G")[0])
        line3 = table.readline().split("\t")
        size_R2 = float(line3[0].split("G")[0])
        R1.append(size_R1)
        R2.append(size_R2)
        line4 = table.readline()   # empty line
        line1 = table.readline()

    return R1,R2


path1 = os.getcwd()+"/"+os.path.dirname(__file__)+"ds1/samples.txt"
path2 = os.getcwd()+"/"+os.path.dirname(__file__)+"ds2/samples.txt"

table1 = open(path1,"r")
table2 = open(path2, "r")


R1_1,R2_1 = parse_table(table1)
R1_2,R2_2 = parse_table(table2)

x = [R1_1,R2_1,R1_2,R2_2]

fig,ax = plt.subplots(1,1)

labels = ["D1.R1","D1.R2","D2.R1","D2.R2"]

bplot = ax.boxplot(x)
plt.boxplot(x)

ax.set_xticks([1,2,3,4])
ax.set_xticklabels(labels)

ax.set(xlabel='', ylabel='size in GB')

plt.show()


