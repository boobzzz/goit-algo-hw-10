import numpy as np
import scipy.integrate as spi


def f(x):
    return np.sin(x)


def monte_carlo_integration(func, a, b, num_samples):
    samples = np.random.uniform(a, b, num_samples)
    sample_evaluations = func(samples)
    integral_estimate = (b - a) * np.mean(sample_evaluations)
    return integral_estimate


a, b = 0, np.pi
num_samples = 100000

monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)
quad_result, _ = spi.quad(f, a, b)

print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Метод quad: {quad_result}")
