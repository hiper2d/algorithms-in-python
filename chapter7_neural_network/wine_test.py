import csv
from random import shuffle
from typing import List

from chapter7_neural_network.util import normalize_by_feature_scaling

if __name__ == "__main__":
    wine_parameters: List[List[float]] = []
    wine_classifications: List[List[float]] = []
    wine_species: List[int] = []
    with open('wine.data', 'r') as wine_data:
        wines: List = list(csv.reader(wine_data, quting=csv.QUOTE_NONNUMERIC))
        shuffle(wines)
        for wine in wines:
            parameters: List[float] = [float(n) for n in wine[1:14]]
            wine_parameters.append(parameters)
            species: int = int(wine[0])
            if species == 1:
                wine_classifications.append([1.0, 0.0, 0.0])
            elif species == 2:
                wine_classifications.append([0.0, 1.0, 0.0])
            elif species == 3:
                wine_classifications.append([0.0, 0.0, 1.0])
            wine_species.append(species)
    normalize_by_feature_scaling(wine_parameters)

