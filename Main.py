import numpy as np
import NeuralNetwork as NN

testlayer = NN.LayerDense
values = [2, 5]
testlayer.load_random(3, 4, [2, 5])
testlayer.printNeurons()
