from .lib import Gradation


def plot_gradation(gradation):
    for i in range(0, 10):
        pass


data = (
    (0, 0.005, 1),
    (0.005, 0.01, 2),
    (0.01, 0.05, 4),
    (0.05, 0.1, 8),
    (0.1, 0.5, 4),
    (0.5, 2, 2),
)

gradation = Gradation()
for i in data:
    gradation.set(*i)
