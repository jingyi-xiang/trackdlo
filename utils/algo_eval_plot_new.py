import matplotlib.pyplot as plt
import pandas as pd
import os
from os.path import dirname, abspath, join
import numpy as np
from labellines import labelLines

plt.rcParams.update({'font.size': 13})  # legend and axis font size
titleSize = 22
labelSize = 18
figsize = (10, 5)

algorithms = ['trackdlo', 'cdcpd2_no_gripper', 'cdcpd2', 'cdcpd', 'bcpd']
bags = ['stationary','perpendicular_motion', 'parallel_motion']
# titles = ['Avg. Error Over 30s vs. $\%$ Occlusion, Stationary DLO', 'Tracking Error vs. Time for Perpendicular Motion', 'Tracking Error vs. Time for Parallel Motion']
titles = ['Stationary', 'Perpendicular Motion', 'Parallel Motion']
duration_frames = [375, 197, 240]
duration_times = [34.1-8, 18.4-5, 22.7-6.5]
pcts = [0, 10, 20, 30, 40, 50]

# bags = ['stationary','perpendicular_motion']
algorithms_plot = {'trackdlo': 'TrackDLO',
                    'bcpd': 'TrackDLO\n+ GBCPD',
                    'cdcpd': 'CDCPD',
                    'cdcpd2': 'CDCPD2',
                    'cdcpd2_no_gripper': 'CDCPD2\nw/o gripper'}
colors = ['red', 'deepskyblue', 'orange', 'b', 'midnightblue']
markers = ['o', 'X', '^', 's', 'v']

###################### PLOT TIME VS. FRAME ERROR ######################
window_size = 10
dir = join(dirname(dirname(abspath(__file__))), "data")

for n, bag in enumerate(bags):
    if bag=='stationary':
        for pct in [45]:
            plt.figure(figsize=figsize)
            ax = plt.gca()
            for i, algorithm in enumerate(algorithms):
                data = []
                for trial in range(0,10):
                    file_path = f'{dir}/dlo_tracking/algo_comparison/{algorithm}/{bag}/{algorithm}_{trial}_{pct}_{bag}_error.txt'
                    with open(file_path, 'r') as file:
                        content = file.readlines()
                        error = []
                        for line in content:
                            row = line.split()
                            error.append(float(row[1])*1000)
                    
                    data.append(error[:duration_frames[n]])
                mean_data_array = np.asarray(data,dtype=object).mean(axis=0)

                average_smoothed_error = pd.Series(list(mean_data_array)).rolling(window_size).mean()
                std_smoothed_error = pd.Series(list(mean_data_array)).rolling(window_size).std()
                time = np.asarray(average_smoothed_error.index/duration_frames[n]) * duration_times[n] - 0.5

                minus_one_std = average_smoothed_error - std_smoothed_error
                minus_one_std[minus_one_std<0] = 0 # set negative std to 0 so that frame error is always positive
                plus_one_std = average_smoothed_error + std_smoothed_error

                ax.plot(time,average_smoothed_error.values, label=f'{algorithms_plot[algorithm]}', alpha=1.0, color=colors[i], marker=markers[i], markevery=30, markersize=12)
                ax.fill_between(time, minus_one_std.values, plus_one_std.values, alpha=0.2, color=colors[i])

            # labelLines(ax.get_lines(), align=False, zorder=2.5, fontsize=20)
            plt.title(titles[n], fontsize=titleSize)
            plt.xlabel('Time (s)', fontsize=labelSize)
            plt.ylabel('Frame Error (mm)', fontsize=labelSize)

            plt.xlim(0, 26)
            plt.axvspan(5, 26, facecolor='darkslateblue', alpha=0.2)

            plt.ylim(0, 47)
            plt.tight_layout()
            
            #get handles and labels
            handles, labels = plt.gca().get_legend_handles_labels()

            #specify order of items in legend
            order = [4, 0, 2, 1, 3]

            #add legend to plot
            plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])

            plt.savefig(f'{dir}/eval_frame_error_{bag}.png')
            plt.close()

    else:
        for pct in pcts[:1]:
            plt.figure(figsize=figsize)
            ax = plt.gca()
            for i, algorithm in enumerate(algorithms):
                data = []
                for trial in range(0,10):
                    file_path = f'{dir}/dlo_tracking/algo_comparison/{algorithm}/{bag}/{algorithm}_{trial}_{pct}_{bag}_error.txt'
                    with open(file_path, 'r') as file:
                        content = file.readlines()
                        error = []
                        for line in content:
                            row = line.split()
                            error.append(float(row[1])*1000)
                    
                    data.append(error[:duration_frames[n]])
                mean_data_array = np.asarray(data,dtype=object).mean(axis=0)

                average_smoothed_error = pd.Series(list(mean_data_array)).rolling(window_size).mean()
                std_smoothed_error = pd.Series(list(mean_data_array)).rolling(window_size).std()
                time = np.asarray(average_smoothed_error.index/duration_frames[n]) * duration_times[n] - 0.5

                minus_one_std = average_smoothed_error - std_smoothed_error
                minus_one_std[minus_one_std<0] = 0 # set negative std to 0 so that frame error is always positive
                plus_one_std = average_smoothed_error + std_smoothed_error

                ax.plot(time,average_smoothed_error.values, label=f'{algorithms_plot[algorithm]}', alpha=1.0, color=colors[i], marker=markers[i], markevery=30, markersize=12)
                ax.fill_between(time, minus_one_std.values, plus_one_std.values, alpha=0.2, color=colors[i])

            # labelLines(ax.get_lines(), align=False, zorder=2.5, fontsize=20)
            plt.title(titles[n], fontsize=titleSize)
            plt.xlabel('Time (s)', fontsize=labelSize)
            plt.ylabel('Frame Error (mm)', fontsize=labelSize)

            if bag == "perpendicular_motion":
                plt.xlim(0, 13)
                plt.axvspan(2.55, 14, facecolor='slategray', alpha=0.2)

            if bag == "parallel_motion":
                plt.xlim(0, 16)
                plt.axvspan(3.5, 10, facecolor='darkslateblue', alpha=0.2)
                plt.axvspan(10, 16, facecolor='slategray', alpha=0.2)

            plt.ylim(0, 47)
            plt.tight_layout()
            
            #get handles and labels
            handles, labels = plt.gca().get_legend_handles_labels()

            #specify order of items in legend
            order = [4, 0, 2, 1, 3]

            #add legend to plot
            plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])

            plt.savefig(f'{dir}/eval_frame_error_{bag}.png')
            plt.close()