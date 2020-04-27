import sys
import functools
import os
import mmap
import numpy as np
import matplotlib.pyplot as plt
import gzip
import timeit

time_mmap = []
reads_mmap = []

time_read = []
reads_read = []

time_seqio = []


def _read(file,n_reads):
    ctr = 0
    while ctr < n_reads*4:
        file.readline()


gz = gzip.open(sys.argv[1],"r")

for i in range(4* 5* 10*6):
    t = timeit.Timer(functools.partial(_read,gz,i))
    time_read.append(t)
    reads_read.append(i)

mfd = os.open(sys.argv[1], os.O_RDONLY)
mfile = mmap.mmap(mfd, 0, prot=mmap.PROT_READ)

for i in range(4* 5* 10*4):
    t = timeit.Timer(functools.partial(_read,mfd,i))
    time_mmap.append(t)
    reads_mmap.append(i)

print(time_read)
print(time_mmap)