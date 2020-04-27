path_benchmarks = "benchmarks"
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import re
import numpy as np
import csv
onlyfiles = [f for f in listdir(path_benchmarks) if isfile(join(path_benchmarks, f))]

original = {}
fast = {}

fast_regex = re.compile('benchmarks_fast__')
slow_regex = re.compile('benchmarks__')

fast_file_names = list(filter(fast_regex.match,onlyfiles))
slow_file_names = list(filter(slow_regex.match,onlyfiles))

for file_name in fast_file_names:
    fast[file_name] = {}
    iteration_size = re.search('__(.+?)\.',file_name).group(1).split("_")
    size = int(iteration_size[1])
    fast[file_name] = {
        "size": size
    }
    file = open(path_benchmarks+'/'+file_name,"rb")
    line1 = file.readline()
    line2 = file.readline()
    line2_split = line2.decode().split("\t")
    fast[file_name]["sec"] = float(line2_split[0])


for file_name in slow_file_names:
    original[file_name] = {}
    iteration_size = re.search('__(.+?)\.',file_name).group(1).split("_")
    size = int(iteration_size[1])
    original[file_name] = {
        "size": size
    }
    file = open(path_benchmarks+'/'+file_name,"rb")
    line1 = file.readline()
    line2 = file.readline()
    line2_split = line2.decode().split("\t")
    original[file_name]["sec"] = float(line2_split[0])



sizes_fast = []
time_fast = []
time = []
sizes = []
for file_name, data in fast.items():
    sizes_fast.append(data["size"])
    time_fast.append(data["sec"])


for file_name, data in original.items():
    sizes.append(data["size"])
    time.append(data["sec"])


plt.plot(sizes,time,"o",color="black")
plt.plot(sizes_fast, time_fast,'x',color="red")
plt.show()
print(fast)