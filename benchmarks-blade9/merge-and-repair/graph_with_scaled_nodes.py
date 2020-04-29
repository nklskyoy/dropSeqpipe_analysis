import csv
import re


COL_SLOW = [255,0,0]
COL_FAST = [255,255,255]

MIN_WIDTH = 3
MAX_WIDTH = 8

rules = {}

with open('benchmarks_blade9.merge-and-repair.csv', 'r') as csvfile:
    line = csvfile.readline()   #header
    line = csvfile.readline()
    while line:
        parsed_line = line.split(",")
        line = csvfile.readline()
        rules[parsed_line[1]] = {}
        rules[parsed_line[1]]["time"] = float(parsed_line[4])
        rules[parsed_line[1]]["meanload"] = float(parsed_line[5])


max_time = 0
max_load = 0
min_time = 1000000
min_load = 1000000

max_time_rule =""

for rule_name, rule_benchmarks in rules.items():
    if max_load < rule_benchmarks["meanload"]:
        max_load =  rule_benchmarks["meanload"]
    if max_time < rule_benchmarks["time"]:
        max_time = rule_benchmarks["time"]
        max_time_rule = rule_name


    if min_load > rule_benchmarks["meanload"]:
        min_load =   rule_benchmarks["meanload"]
    if min_time > rule_benchmarks["time"]:
        min_time = rule_benchmarks["time"]
print(rules)

print("MAX time: ", rule_name)

with open('rulegrph_scaled.dot',"w") as rulegraph_scaled:
    with open('rulegraph.dot',"r") as rulegraph:
        for line in rulegraph:
            found = False
            for rule_name, rule_benchmarks in rules.items():
                is_node_for_role = re.findall("label = \""+rule_name + "\"",line)
                if (is_node_for_role):
                    found = True
                    scale_load = (rule_benchmarks["meanload"]-min_load)/(max_load - min_load)
                    scale_time = (rule_benchmarks["time"]-min_time)/(max_time - min_time)

                    color = [0,0,0]
                    for i in range(len(COL_FAST)):
                        color[i] = COL_FAST[i] + (COL_SLOW[i] - COL_FAST[i])*scale_time

                    color_rgb = "#"

                    for i in range(len(color)):
                        h = str(hex(int(color[i])))[2:].upper()
                        # if h is 0, append 0
                        if len(h) == 1:
                            h+="0"

                        color_rgb+=h


                    width = MIN_WIDTH + (MAX_WIDTH - MIN_WIDTH)*scale_load
                    line_pre = line[:-3]
                    line_new = line_pre + ", width=\"" +  str(int(width)) + "\", fillcolor=\"" + color_rgb +"\"];\n"
                    rulegraph_scaled.write(line_new)
            if not found:
                rulegraph_scaled.write(line)


