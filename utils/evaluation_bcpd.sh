#!/bin/bash
# Loop

# save image
for bag in 0
do
    for pct in 45
    do
        for trial in 0
        do
            for alg in bcpd
            do
                terminator -e "cd ~/catkin_ws && source devel/setup.bash && roslaunch bcpd-dlo-tracking bcpd_tracker.launch bag_file:=$bag" &
                first_teminal=$!
                terminator -e "cd ~/catkin_ws && source devel/setup.bash && roslaunch trackdlo evaluation.launch alg:=$alg bag_file:=$bag trial:=$trial pct_occlusion:=$pct save_images:=true --wait" &
                second_teminal=$!
                sleep 70
                rosnode kill -a
                killall -9 rosmaster
            done
        done
    done
done

# save image
for bag in 1 2
do
    for pct in 0
    do
        for trial in 0
        do
            for alg in bcpd
            do
                terminator -e "cd ~/catkin_ws && source devel/setup.bash && roslaunch bcpd-dlo-tracking bcpd_tracker.launch bag_file:=$bag" &
                first_teminal=$!
                terminator -e "cd ~/catkin_ws && source devel/setup.bash && roslaunch trackdlo evaluation.launch alg:=$alg bag_file:=$bag trial:=$trial pct_occlusion:=$pct save_images:=true --wait" &
                second_teminal=$!
                sleep 50
                rosnode kill -a
                killall -9 rosmaster
            done
        done
    done
done

for bag in 0
do
    for pct in 45
    do
        for trial in 1 2 3 4 5 6 7 8 9
        do
            for alg in bcpd
            do
                terminator -e "cd ~/catkin_ws && source devel/setup.bash && roslaunch bcpd-dlo-tracking bcpd_tracker.launch bag_file:=$bag" &
                first_teminal=$!
                terminator -e "cd ~/catkin_ws && source devel/setup.bash && roslaunch trackdlo evaluation.launch alg:=$alg bag_file:=$bag trial:=$trial pct_occlusion:=$pct --wait" &
                second_teminal=$!
                sleep 70
                rosnode kill -a
                killall -9 rosmaster
            done
        done
    done
done

for bag in 1 2
do
    for pct in 0
    do
        for trial in 1 2 3 4 5 6 7 8 9
        do
            for alg in bcpd
            do
                terminator -e "cd ~/catkin_ws && source devel/setup.bash && roslaunch bcpd-dlo-tracking bcpd_tracker.launch bag_file:=$bag" &
                first_teminal=$!
                terminator -e "cd ~/catkin_ws && source devel/setup.bash && roslaunch trackdlo evaluation.launch alg:=$alg bag_file:=$bag trial:=$trial pct_occlusion:=$pct --wait" &
                second_teminal=$!
                sleep 50
                rosnode kill -a
                killall -9 rosmaster
            done
        done
    done
done
