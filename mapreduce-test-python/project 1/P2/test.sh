#!/bin/sh
../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /P2/input/

/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../mapreduce-test-data/shot_logs.csv /P2/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ./mapper1.py -mapper ./mapper1.py -file ./reducer1.py -reducer ./reducer1.py \
-input /P2/input/shot_logs.csv -output /P2/output/ 

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ./mapper2.py -mapper ./mapper2.py -file ./reducer2.py -reducer ./reducer2.py \
-input /P2/output/* -output /P2/output2/

/usr/local/hadoop/bin/hdfs dfs -cat /P2/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/output2/
../../../stop.sh
