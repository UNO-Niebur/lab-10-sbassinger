#MapPlot.py
#Name: Scott Bassinger
#Date: 04/13/2026
#Assignment: Lab10

import matplotlib.pyplot as plt

trials = []
reaction_times = []

input_file = open("reaction_time_data.csv", "r")
lines = input_file.readlines()
input_file.close()

for i in range(1, len(lines)):
    line = lines[i].strip()
    if line == "":
        continue
    parts = line.split(",")
    trial = int(parts[0])
    rt = int(parts[1])
    trials.append(trial)
    reaction_times.append(rt)


clean_trials = []
clean_times = []

for i in range(len(trials)):
    if reaction_times[i] >= 100 and reaction_times[i]<= 1000:
        clean_trials.append(trials[i])
        clean_times.append(reaction_times[i])


plt.plot(clean_trials, clean_times, marker="o")

plt.title("Reaction Time Across Trials")
plt.xlabel("Trial Number")
plt.ylabel("Reaction Time (ms)")

plt.savefig("output.png")
print("Graph Saved as output.png")
