from functools import reduce
from typing import List, Callable, TypeVar

from chapter7_neural_network.layer import Layer
from chapter7_neural_network.util import sigmoid, derivative_sigmoid

T = TypeVar('T')


class Network:
    def __init__(self, layer_structure: List[int], learning_rate: float,
                 activation_function: Callable[[float], float] = sigmoid,
                 activation_function_derivative: Callable[[float], float] = derivative_sigmoid) -> None:
        if len(layer_structure) < 3:
            raise ValueError('The layer structure must have at least 3 layers (1 input, 1 hidden, 1 output)')
        self.layers: List[Layer] = []
        # input layer
        input_layer: Layer = Layer(None, layer_structure[0], learning_rate, activation_function,
                                   activation_function_derivative)
        self.layers.append(input_layer)
        # hidden layers and output layer
        for previous, num_neurons in enumerate(layer_structure[1::]):
            next_layer: Layer = Layer(self.layers[previous], num_neurons, learning_rate=learning_rate,
                                      activation_function=activation_function,
                                      derivative_activation_function=activation_function_derivative)
            self.layers.append(next_layer)

    # Pushes input data to the first layer, then output from the first
    # as input to the second, second to the third, etc.
    def outputs(self, input: List[float]) -> List[float]:
        return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input)

    # Figures out each neuron's changes based on the errors of the output
    # versus the expected output
    def backpropagate(self, expected: List[float]) -> None:
        pass
