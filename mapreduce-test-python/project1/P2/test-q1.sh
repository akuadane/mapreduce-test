#!/bin/sh
../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /P2/input/

/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../mapreduce-test-data/shot_logs.csv /P2/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ./q1/mapper1.py -mapper ./q1/mapper1.py -file ./q1/reducer1.py -reducer ./q1/reducer1.py \
-input /P2/input/shot_logs.csv -output /P2/output/ 

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ./q1/mapper2.py -mapper ./q1/mapper2.py -file ./q1/reducer2.py -reducer ./q1/reducer2.py \
-input /P2/output/* -output /P2/output2/

/usr/local/hadoop/bin/hdfs dfs -cat /P2/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output2/
../../../stop.sh
