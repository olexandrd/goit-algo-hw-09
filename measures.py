import timeit
import matplotlib.pyplot as plt

from algorithms import find_coins_greedy, find_min_coins, coins

sum_list = [2**x for x in range(5, 20)]


def timeit_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def timeit_measure(func, *args, **kwargs):
    wrapped = timeit_wrapper(func, *args, **kwargs)
    return timeit.timeit(wrapped, number=10)


def measure(func, sum_list):
    return [timeit_measure(func, sum=sum, coins=coins) for sum in sum_list]


greedy_results = measure(find_coins_greedy, sum_list)
dp_results = measure(find_min_coins, sum_list)


# Build plot
plt.figure(figsize=(8, 6))
plt.plot(sum_list, greedy_results, label="Greedy algorithm")
plt.plot(sum_list, dp_results, label="DP algorithm")
plt.ylabel("Time, s")
plt.yscale("log")
plt.title("Greedy vs DP algorithms")
plt.legend()
plt.grid(True, which="both", ls="--", c="0.5")
plt.show()