import timeit
import matplotlib.pyplot as plt

from algorithms import find_coins_greedy, find_min_coins, coins

sum_list = [3 + 2**x for x in range(5, 24)]


def execution_time(method, sum: int, coints: list):
    setup_code = f"from algorithms import {method.__name__}"
    execution_code = f"{method.__name__}({sum}, {coints})"
    execution_time = timeit.timeit(
        execution_code, setup=setup_code, globals=globals(), number=10
    )
    return execution_time


greedy_results = [execution_time(find_coins_greedy, sum, coins) for sum in sum_list]
dp_results = [execution_time(find_min_coins, sum, coins) for sum in sum_list]


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
