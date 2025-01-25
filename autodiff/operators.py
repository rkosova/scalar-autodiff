class Negative:
    def __init__(self):
        self.name = 'neg'

    def __call__(self, a):
        return Negative.forward(a)

    @staticmethod
    def forward(a):
        return -a
    
    @staticmethod
    def backward(*args):
        return tuple([-1])


class Add:
    def __init__(self):
        self.name = 'add'
    
    def __call__(self, a, b):
        return Add.forward(a, b)

    @staticmethod
    def forward(a, b):
        return a + b
    
    @staticmethod
    def backward(*args):
        return 1, 1
    

class Subtract:
    def __init__(self,):
        self.name = 'sub'

    def __call__(self, a, b):
        return Subtract.forward(a, b)

    @staticmethod
    def forward(a, b):
        return a - b
    
    @staticmethod
    def backward(*args):
        return 1, -1
    

class Multiply:
    def __init__(self):
        self.name = 'mult'

    def __call__(self, a, b):
        return Multiply.forward(a, b)
    
    @staticmethod
    def forward(a, b):
        return a * b
    
    @staticmethod
    def backward(*args):
        return args[1], args[0]


class Divide:
    def __init__(self):
        self.name = 'div'

    def __call__(self, a, b):
        return Divide.forward(a, b)
    
    @staticmethod
    def forward(a, b):
        return a * 1/b
    
    @staticmethod
    def backward(*args):
        return 1/args[1], -args[0]/(args[1]**2)
    