from __future__ import annotations
from functools import reduce
from typing import List, Callable, TypeVar, Tuple

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
        last_layer_idx = len(self.layers) - 1
        self.layers[last_layer_idx].calculate_deltas_for_output_layer(expected)
        for l in range(last_layer_idx - 1, 0, -1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])

    # backpropagate() doesn't actually change any weight
    # this function uses the deltas calculated by backpropagate() toa actually make changes to the wights
    def update_weights(self) -> None:
        for layer in self.layers[1:]: # skip input layer
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w] = neuron.weights[w] + \
                                        neuron.learning_rate * layer.previous_layer.output_cache[w] * neuron.delta

    # train() uses the result of outputs() run over many inputs and compares against expected
    # to feed backpropagate() and update_weights()
    def train(self, inputs: List[List[float]], expected: List[List[float]]) -> None:
        for location, xs in enumerate(inputs):
            ys: List[float] = expected[location]
            outs: List[float] = self.outputs(xs)
            self.backpropagate(ys)
            self.update_weights()

    def validate(self, inputs: List[List[float]], expected: List[T],
                 interpret_output: Callable[[List[float]], T]) -> Tuple[int, int, float]:
        correct: int = 0
        for input, expected in zip(inputs, expected):
            result: T = interpret_output(self.outputs(input))
            if result == expected:
                correct += 1
        percentage: float = correct / len(inputs)
        return correct, len(inputs), percentage
