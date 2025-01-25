import secrets
from .operators import *


class Node:
    def __init__(self, value, name, parents=[], operation=None, requires_grad=False, gradient=0):
        self.value = value
        self.name = name

        self.parents = parents
        self.operation = operation
        self.requires_grad = requires_grad
        self.gradient = gradient 
    
    def backward(self, propegated_gradient=1): # defaults to 1 so when we call it on the leaf it autosets its gradient to 1
        self.gradient += propegated_gradient
        if len(self.parents) != 0:
            parents_grad = self.operation.backward(*[p.value for p in self.parents])
            for i, p in enumerate(self.parents):
                p.backward(self.gradient * parents_grad[i]) # chain rule
    
    def __repr__(self):
        return f"{self.name}={self.value}"
    
    def __neg__(self):
        return Node(-self.value, f"-({self.name})", parents=[self], operation=Negative())

    def __add__(self, var2):
        if not isinstance(var2, Node):
            var2 = Node(var2, secrets.token_hex(5)) # random name for now, will probably check graph for naming later
        return Node(self.value + var2.value, f"{self.name}+{var2.name}", parents=[self, var2], operation=Add())
    
    def __radd__(self, var1):
        if not isinstance(var1, Node):
            var1 = Node(var1, secrets.token_hex(5))
        return Node(var1.value + self.value, f"{var1.name}+{self.name}", parents=[var1, self], operation=Add())
    
    def __sub__(self, var2):
        if not isinstance(var2, Node):
            var2 = Node(var2, secrets.token_hex(5))
        return Node(self.value - var2.value, f"{self.name}-{var2.name}", parents=[self, var2], operation=Subtract())

    def __rsub__(self, var1):
        if not isinstance(var1, Node):
            var1 = Node(var1, secrets.token_hex(5))
        return Node(var1.value - self.value, f"{var1.name}-{self.name}", parents=[var1, self], operation=Subtract())

    def __mul__(self, var2):
        if not isinstance(var2, Node):
            var2 = Node(var2, secrets.token_hex(5))
        return Node(self.value * var2.value, f"{self.name}*{var2.name}", parents=[self, var2], operation=Multiply())

    def __rmul__(self, var1):
        if not isinstance(var1, Node):
            var1 = Node(var1, secrets.token_hex(5))
        return Node(var1.value * self.value, f"{var1.name}*{self.name}", parents=[var1, self], operation=Multiply())
    
    def __truediv__(self, var2):
        if not isinstance(var2, Node):
            var2 = Node(var2, secrets.token_hex(5))
        return Node(self.value / var2.value, f"{self.name}/{var2.name}", parents=[self, var2], operation=Divide())

    def __rtruediv__(self, var1):
        if not isinstance(var1, Node):
            var1 = Node(var1, secrets.token_hex(5))
        return Node(var1.value / self.value, f"{var1.name}/{self.name}", parents=[var1, self], operation=Divide())
    
