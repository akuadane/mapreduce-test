#!/bin/sh
../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /P2/input/

/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../mapreduce-test-data/shot_logs.csv /P2/input/

python ./q2/starter.py

/usr/local/hadoop/bin/hdfs dfs -cat /P2/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output2/
../../../stop.sh