
#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /lab2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/lab2/mapper.py -mapper ../../mapreduce-test-python/lab2/mapper.py 0-1\
-file ../../mapreduce-test-python/lab2/reducer.py -reducer ../../mapreduce-test-python/lab2/reducer.py \
-input /lab2/input/access.log -output /lab2/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/lab2/mapper2.py -mapper ../../mapreduce-test-python/lab2/mapper2.py \
-file ../../mapreduce-test-python/lab2/reducer2.py -reducer ../../mapreduce-test-python/lab2/reducer2.py \
-input /lab2/output/* -output /lab2/output2/

/usr/local/hadoop/bin/hdfs dfs -cat /lab2/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output2/
../../stop.sh
