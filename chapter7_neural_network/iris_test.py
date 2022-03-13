import csv
from random import shuffle
from typing import List

from chapter7_neural_network.util import normalize_by_feature_scaling

if __name__ == "__main__":
    iris_parameters: List[List[float]] = []
    iris_classification: List[List[float]] = []
    iris_species: List[str] = []
    with open('iris.csv', mode='r') as iris_file:
        irises: List = list(csv.reader(iris_file))
        shuffle(irises)
        for iris in irises:
            parameters: List[float] = [float(n) for n in iris[0:4]]
            iris_parameters.append(parameters)
            species: str = iris[4]
            if species == 'Iris-setosa':
                iris_classification.append([1.0, 0.0, 0.0])
            elif species == 'Iris-versicolor':
                iris_classification.append([0.0, 1.0, 0.0])
            else:
                iris_classification.append([0.0, 0.0, 1.0])
            iris_species.append(species)
    normalize_by_feature_scaling(iris_parameters)
