import random
from symbolicdiff import Node
from symbolicdiff.optimizers import GradientDescent
import numpy as np
import matplotlib.pyplot as plt

true_w = 2.4
true_b = 0.5
x = np.random.uniform(size=100)
data = true_w * x + true_b + np.random.normal(0, 0.1, size=100)

w = Node(1.0, 'w')
b = Node(1.0, 'b')

optimizer = GradientDescent([w, b], learning_rate=0.05)

for _ in range(5):
    for i in range(x.shape[0]):
        pred = w * x[i] + b
        loss = (pred - data[i]) * (pred - data[i])
        loss.backward()
        optimizer.step()

pred_x = np.array([(w * x[i] + b).value for i in range(x.shape[0])])

plt.scatter(x, data, label='data')
plt.plot(x, pred_x, label='prediction')
plt.legend()
plt.show()
print(f"w={w.value}, b={b.value}")
