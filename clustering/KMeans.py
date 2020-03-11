import sys
import re
from pyspark import SparkContext
from pyspark import SparkConf
from helper import *

if __name__ == "__main__":
  if len(sys.argv) != 5:
    print >> sys.stderr, "Usage: K-Means <input_path> <output_path> <k> <distance>"
    exit(-1)

  sconf = SparkConf().setAppName("KMeans Spark").set("spark.ui.port","4141")
  sc = SparkContext(conf=sconf)

  input_path = sys.argv[1]
  output_path = sys.argv[2]
  k = int(sys.argv[3])
  method = sys.argv[4]

  if k <= 0:
    print >> sys.stderr, "K must be greater than 0"
    exit(-1)

  if method != "Euclidean" and method != "GreatCircle":
    print >> sys.stderr, "Distance Method should be Euclidean or GreatCircle"
    exit(-1)

  data = sc.textFile(input_path).map(lambda line: line.split(",")).map(lambda x: (float(x[0]), float(x[1]))).persist()
  center = data.takeSample(False, k, 2019)
  centerChange = float("INF")

  print("##### K-Means Algorithm Start #####")

  iteration = 0
  while centerChange > 1e-2:
    cluster = data.map(lambda x: (closestPoint(x, center, method), (x[0], x[1], 1)))
    # count = cluster.countByKey()
    newCenter = cluster.reduceByKey(addPoints).map(lambda (index, (lat, long, count)): (index, (lat/count, long/count)))
    distances = newCenter.map(lambda (index, cur): Euclidean(cur, center[index]))
    # if method == "Euclidean":
    #  distances = newCenter.map(lambda (index, cur): Euclidean(cur, center[index]))
    #else:
    #  distances = newCenter.map(lambda (index, cur): GreatCircle(cur, center[index]))
    centerChange = distances.sum()
    center = newCenter.map(lambda (index, cur): cur).collect()

    if iteration % 5 == 0:
	    print("Iteration: " + str(iteration) + " Center Change: " + str(centerChange))
    iteration += 1

    

  print("##### K-Means Algorithm Finished #####")

  outputData = cluster.map(lambda (index, (lat, long, c)): str(index) + "," + str(lat) + "," + str(long))
  outputData.saveAsTextFile(output_path+"/data")
  outputCenter = newCenter.map(lambda (index, (lat, long)): str(index) + "," + str(lat) + "," + str(long))
  outputCenter.saveAsTextFile(output_path+"/center")

 
    

  

