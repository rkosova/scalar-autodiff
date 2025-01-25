from . import Node
from typing import List

class GradientDescent:
    def __init__(self, parameters: List[Node], learning_rate=0.01):
        self.parameters = parameters
        self.learning_rate = learning_rate
    
    def step(self):
        for p in self.parameters:
            p.value -= self.learning_rate * p.gradient
            p.gradient = 0



