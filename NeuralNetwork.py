import numpy as np
import ActivationFunctions as af
import random


class Neuron:
    def __init__(self, bias: float, weights: list[float]) -> None:
        self.bias = bias
        self.weights = weights

    def getBias(self) -> float:
        return self.bias

    def getWeights(self) -> list[float]:
        return self.weights


class LayerDense:
    def __init__(self) -> None:
        self.Neurons = [Neuron]

    def load_random(self, n_neurons: int, n_neurons_layerbefore: int, range_values: list[int]):
        for i in range(n_neurons):
            bias = np.random.uniform(range_values[0], range_values[1])
            weights = np.random.uniform(
                range_values[0], range_values[1], n_neurons_layerbefore)
            print(bias)
            print(weights)
            self.Neurons.append(Neuron(bias, weights))

    def printNeurons(self):
        for n in self.Neurons:
            print("Neuron: Bias: {}, Weights: {}".format(n.getBias, n.getWeights))


class NeuralNetwork:

    def __init__(self) -> None:
        pass

    def load_xml(self, path: str):
        self.path = path

    def load_random(self, n_inputs: int, n_neur):
        pass


print(np.random.uniform(2, 5))
testlayer = LayerDense()
testlayer.load_random(3, 4, [2, 5])
testlayer.printNeurons()
