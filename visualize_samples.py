import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


#the big data set with 52-base barcodes
table_1 = open("table_data_1.txt","r")

#the "small" data set
table_2 = open("table2.txt", "r")

fig, (ax1, ax2) = plt.subplots(1,2)


offset = 0.52
width = 1
step  =5
i = step

darkkhaki_patch = mpatches.Patch(color='darkkhaki', label='R1')
lightseagreen_patch = mpatches.Patch(color="lightseagreen", label='R2')

##############################################
## table1
##############################################

x = []
y = []
colors = []
tick_label = []
x_tick = []

sum_r1 =0
sum_r2 = 0

line1 = table_1.readline()

while line1:
    samplename = line1.split("\t")[0]
    line2 = table_1.readline().split("\t")
    size_R1 = float(line2[0].split("G")[0])
    line3 = table_1.readline().split("\t")
    size_R2 = float(line3[0].split("G")[0])

    x.append(i-offset)
    x.append(i+offset)
    y.append(size_R1)
    y.append(size_R2)
    colors.append("darkkhaki")
    colors.append("lightseagreen")
    tick_label.append("")
    line4 = table_1.readline()

    sum_r1+=size_R1
    sum_r2+=size_R2

    line1 = table_1.readline()
    x_tick.append(i)
    i += step

y_tick = [1,2,3,4,5,6,7]
y_label = "size in gigabytes"

print("rable1: sumR1:", sum_r1, "; sumR2:", sum_r2)


ax1.set_xticks(x_tick)
ax1.set_xticklabels(tick_label,fontsize=7,rotation=90)
ax1.set_ylabel(y_label)
ax1.bar(x,y,width,color=colors)
ax1.legend(handles=[darkkhaki_patch,lightseagreen_patch])


##############################################
## table2
##############################################


x = []
y = []
colors = []
tick_label = []
x_tick = []

sum_r1 = 0
sum_r2 = 0

line1 = table_2.readline()

while line1:
    samplename = line1.split("\t")[0]
    line2 = table_2.readline().split("\t")
    size_R1 = float(line2[0].split("G")[0])
    line3 = table_2.readline().split("\t")
    size_R2 = float(line3[0].split("G")[0])

    x.append(i-offset)
    x.append(i+offset)
    y.append(size_R1)
    y.append(size_R2)
    colors.append("darkkhaki")
    colors.append("lightseagreen")
    tick_label.append("")
    line4 = table_2.readline()

    sum_r1+=size_R1
    sum_r2+=size_R2

    line1 = table_2.readline()
    x_tick.append(i)
    i += step

y_tick = [1,2,3,4,5,6,7]
y_label = "size in gigabytes"


ax2.set_xticks(x_tick)
ax2.set_xticklabels(tick_label,fontsize=7,rotation=90)
ax2.bar(x,y,width,color=colors)
ax2.legend(handles=[darkkhaki_patch,lightseagreen_patch])

print("Table2: sumR1:", sum_r1, "; sumR2:", sum_r2)


#plt.xticlabels(tick_label)
plt.show()