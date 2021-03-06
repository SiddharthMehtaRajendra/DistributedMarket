${SPARK_HOME}/bin/spark-submit \
--master yarn \
--deploy-mode client \
--queue default \
--num-executors 2 \
--executor-memory 2G \
--conf spark.eventLog.enabled=true \
--conf spark.eventLog.dir=hdfs://master:9000/shared/log/ \
--conf spark.ui.enabled=true \
--conf spark.ui.port=4040 \
--archives hdfs:///user/root/mnist/input/data/mnist.zip#mnist \
hdfs:///user/root/mnist/input/code/mnist_data_setup.py \
--output mnist/output \
--format csv