from __future__ import annotations

from random import random
from typing import Optional, List, Callable

from chapter7_neural_network.neuron import Neuron
from chapter7_neural_network.util import dot_product


class Layer:
    def __init__(self, previous_layer: Optional[Layer], num_neurons: int, learning_rate: float,
                 activation_function: Callable[[float], float],
                 derivative_activation_function: Callable[[float], float]) -> None:
        self.previous_layer: Optional[Layer] = previous_layer
        self.neurons: List[Neuron] = []
        for i in range(num_neurons):
            if self.previous_layer is None:
                random_weights: List[float] = []
            else:
                random_weights = [random() for _ in range(len(previous_layer.neurons))]
            neuron: Neuron = Neuron(random_weights, learning_rate, activation_function, derivative_activation_function)
            self.neurons.append(neuron)
            self.output_cache: List[float] = [0.0] * len(self.neurons)

    def outputs(self, inputs: List[float]) -> List[float]:
        if self.previous_layer is None:
            self.output_cache = inputs
        else:
            self.output_cache = [neuron.output(inputs) for neuron in self.neurons]
        return self.output_cache

    def calculate_deltas_for_output_layer(self, expected: List[float]) -> None:
        for n in range(len(self.neurons)):
            self.neurons[n].delta = self.neurons[n].derivative_activation_function(self.neurons[n].output_cache) * \
                (expected[n] - self.neurons[n].output_cache)

    def calculate_deltas_for_hidden_layer(self, next_layer: Layer) -> None:
        for index, neuron in enumerate(self.neurons):
            next_weights: List[float] = [n.weights[index] for n in next_layer.neurons]
            next_deltas: List[float] = [n.delta for n in next_layer.neurons]
            sum_wights_and_deltas: float = dot_product(next_weights, next_deltas)
            neuron.delta = neuron.derivative_activation_function(neuron.output_cache) * sum_wights_and_deltas
