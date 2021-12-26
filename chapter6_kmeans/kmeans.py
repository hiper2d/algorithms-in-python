from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from random import uniform
from statistics import pstdev, mean
from typing import Sequence, List, Generic, TypeVar

from chapter6_kmeans.data_point import DataPoint

Point = TypeVar('Point', bound=DataPoint)


def z_scores(original: Sequence[float]) -> List[float]:
    avg: float = mean(original)
    std: float = pstdev(original)
    if avg == 0:
        return [0] * len(original)
    return [(x - avg) / std for x in original]


class KMeans(Generic[Point]):
    @dataclass
    class Cluster:
        points: List[Point]
        centroid: DataPoint

    @staticmethod
    def _dimension_slice(points: List[DataPoint], dimension: int) -> List[float]:
        return [x.dimensions[dimension] for x in points]

    def __init__(self, k: int, points: List[Point]):
        if k < 1:  # k-means can't do negative or zero clusters
            raise ValueError("k must be greater than 0")
        self._points: List[Point] = points
        self._z_score_normalize()
        self._clusters: List[KMeans.Cluster] = []
        for _ in range(k):
            rand_point: DataPoint = self.random_point()
            cluster: KMeans.Cluster = KMeans.Cluster([], rand_point)
            self._clusters.append(cluster)

    @property
    def _centroids(self) -> List[DataPoint]:
        return [x.centroid for x in self._clusters]

    def run(self, max_iterations: int = 100) -> List[KMeans.Cluster]:
        for iteration in range(max_iterations):
            for c in self._clusters:  # clear all clusters
                c.points.clear()
            self._assign_clusters()
            old_centroids: List[DataPoint] = deepcopy(self._centroids)
            self._recalculate_centroids()
            if old_centroids == self._centroids:  # if centroids haven't changed, we're done
                print(f"Converged after {iteration} iterations")
                return self._clusters
        return self._clusters

    def random_point(self) -> DataPoint:
        rand_dimensions: List[float] = []
        for dimension in range(self._points[0].num_dimensions):
            values: List[float] = self._dimension_slice(self._points, dimension)
            rand_value: float = uniform(min(values), max(values))
            rand_dimensions.append(rand_value)
        return DataPoint(rand_dimensions)

    def _z_score_normalize(self) -> None:
        z_scored: List[List[float]] = [[] for _ in range(len(self._points))]
        for dimension in range(self._points[0].num_dimensions):
            dimension_slice: List[float] = self._dimension_slice(self._points, dimension)
            for index, z_score in enumerate(z_scores(dimension_slice)):
                z_scored[index].append(z_score)
        for i in range(len(self._points)):
            self._points[i].dimensions = tuple(z_scored[i])

    def _assign_clusters(self) -> None:
        for point in self._points:
            closest: DataPoint = min(self._centroids, key=lambda centroid: point.distance(centroid))
            idx: int = self._centroids.index(closest)
            closest_cluster: KMeans.Cluster = self._clusters[idx]
            closest_cluster.points.append(point)

    def _recalculate_centroids(self) -> None:
        for cluster in self._clusters:
            if len(cluster.points) == 0: # keep the same centroid if no points
                continue
            means: List[float] = []
            for dimension in range(cluster.points[0].num_dimensions):
                dimension_slice: List[float] = self._dimension_slice(cluster.points, dimension)
                means.append(mean(dimension_slice))
            cluster.centroid = DataPoint(means)


if __name__ == "__main__":
    point1: DataPoint = DataPoint([2.0, 1.0, 1.0])
    point2: DataPoint = DataPoint([2.0, 2.0, 5.0])
    point3: DataPoint = DataPoint([300.0, 100.5, 200.5])
    kmeans_test: KMeans = KMeans(2, [point1, point2, point3])
    test_clusters: List[KMeans.Cluster] = kmeans_test.run()
    for index, cluster in enumerate(test_clusters):
        print(f"Cluster {index}: {cluster.points}")