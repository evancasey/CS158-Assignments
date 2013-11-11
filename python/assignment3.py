from learning import *
import pdb
import math
import random
import os
import sys
import numpy as np
# import matplotlib.pyplot as plt


def testNeuralNetLearner(data, iterations=1000, learn_rate=0.5, momentum=0.1):

	if data == "xor":
	    ds = DataSet(name='../data/xor')
	    num_input = 4
	    num_output = 4
	    num_hl = 1 # number of hidden layers
	elif data == "semeion":
	    ds = DataSet(name='../data/semeion')
	    num_input = 256
	    num_output = 10
	    num_hl = 1 # number of hidden layers
	 
	 # # create the learner with the matrix
	 # NNlearner = createNeuralNetLearner(m, num_input, num_output, num_hl, iterations, learn_rate, momentum)
	 
	 # test the learner (cross validation)
		 

def createNeuralNetLearner(m, num_input, num_output, num_hl, iterations, learn_rate, momentum):
 	# create a neural net learner

 	# transform the ds to matrix
 	inputs = np.array(ds.examples)
 	
	mx = np.matrix(inputs)

 	# create weights
 	mw = np.random.random((256, 256))
 	

 	# call forward propogation
 	

 	# call backward propogation
 	

 	# update weights
 	# 

def sigmoid(a):
	return 1/(1 + math.pow(math.e, -a))

def forwardProp(N, w):
	""" takes a list of node values and the associated weights"""
	if len(N) != len(w):
		return "error"
	else:
		a = 0
		for i in range(len(N)):
			a += N[i]*w[i]

		nodeValue = sigmoid(a)

		return nodeValue

def _create_weights(m):
	pass


if __name__ == "__main__":

	testNeuralNetLearner("xor",1000,0.5,0.1)

	# some stuff
	# 
	# testNeuralNetLearner()

