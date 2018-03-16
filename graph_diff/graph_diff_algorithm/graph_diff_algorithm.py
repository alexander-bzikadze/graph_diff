from abc import ABC, abstractmethod

from graph_diff.graph import GraphWithRepetitiveNodesWithRoot
from .graph_map import GraphMap


class GraphDiffAlgorithm(ABC):
    """Graph difference algorithm interface"""

    @abstractmethod
    def construct_diff(self,
                       graph1: GraphWithRepetitiveNodesWithRoot,
                       graph2: GraphWithRepetitiveNodesWithRoot) -> GraphMap: pass