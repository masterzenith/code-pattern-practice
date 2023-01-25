"""
Given the weights and profits of 'N' items, we are asked to put these items in a knapsack with a capacity 'C'. The goal
is to get the maximum profit out of the knapsack items. Each item can only selected once, as we don't have multiple
quantities of any item.
Let's take Merry's example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights
and profits of the fruits:
Items: {Apple, Orange, Banana, Melon}
Weights: {2, 3, 1, 4}
Profits: {4, 5, 3, 7}
Knapsack capacity: 5
Let's try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:
Apple + Orange(total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit
This shows that Banana + Melon is the best combination as it gives us the maximum profit, and the total weight does not
exceed the capacity.

Time: Since our memoization array dp[profits.length][capacity+1] stores the results for all subproblems, we can
        conclude that we will not have more than N*C sub problems (where 'N' is the number of items and 'C' is the
        knapsack capacity). This means that our time complexity will be O(N*C).
Space: The above algorithm will use O(N*C) space for the memoization array. Other than that, we will use O(N) space for
        the recursion call-stack. So the total space complexity will be O(N*C + N), which is asymptotically equivalent
        to O(N*C)
"""


def solve_knapsack(profits, weights, capacity):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return solve_knapsack_rec(dp, profits, weights, capacity, 0)


def solve_knapsack_rec(dp, profits, weights, capacity, current_idx):
    # base checks
    if capacity <= 0 or current_idx >= len(profits):
        return 0

    # If we have already solved a similar problem, return the result from memory
    if dp[current_idx][capacity] != -1:
        return dp[current_idx][capacity]

    # recursive call after choosing the element at the current_idx
    # if the weight of the element at current_idx exceeds the capacity, we shouldn't process this
    profit1 = 0
    if weights[current_idx] <= capacity:
        profit1 = profits[current_idx] + \
                  solve_knapsack_rec(dp, profits, weights, capacity - weights[current_idx], current_idx + 1)

    # recursive call after excluding the element at the current_idx
    profit2 = solve_knapsack_rec(dp, profits, weights, capacity, current_idx + 1)
    dp[current_idx][capacity] = max(profit1, profit2)
    return dp[current_idx][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


if __name__ == "__main__":
    main()
