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
        input_layer: Layer = Layer(None, layer_structure[0], learning_rate, activation_function,
                                   activation_function_derivative)
        self.layers.append(input_layer)
        # for previous, num_neurons in enumerate(layer_structure[1::]):


