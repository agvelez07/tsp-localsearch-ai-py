import math
import random
import sys
import time
from libic import *
from ic import *



# ------------------
#   Execucao...
# ------------------

w = windowIC(800)

#l = newListIC(20)
#l = readTSP2ListIC("eil51.tsp")
#l = readTSP2ListICOpt("eil51.tsp", "eil51.opt.tour")
l = readTSP2ListIC("berlin52.tsp")
#l = readTSP2ListICOpt("berlin52.tsp", "berlin52.opt.tour")
print(l)
print("Distancia INICIAL:", distCircularIC(l))
#drawIC(l,w)
input("Enter para continuar... ")
print("Optimizing...")

iter = 10000
if len(sys.argv) > 1:
    iter = int(sys.argv[1])

st = time.process_time()
(ci, cf, lopt) = optDistCircularIC(l,iter)
et = time.process_time()
print("CPU time: ", (et - st)*1000, "ms")

drawIC(lopt,w)
print("Distancia", ci, "->", cf)
input("Enter para continuar... ")

