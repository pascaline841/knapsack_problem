import math


def greedy_algorithm(stocks, portfolio):
    """
    Function that will choose the best stock.ratio to buy in order to have the best profits.
    Space complexity : O(n)
    Time complexity : O(n)
    Args:
        stocks(list): list of the 20 best stocks from the csv file
        portfolio (float): maximum value to invest $.
    """
    purchased_stocks = []
    total_cost = 0
    max_benefit = 0
    stocks = sorted(stocks, key=lambda stock: stock.ratio)
    while stocks:
        stock = stocks.pop()
        if stock.price + total_cost <= portfolio:
            purchased_stocks.append(stock.name)
            total_cost += stock.price
            max_benefit += stock.benefit
    print(
        f"\nGREEDY ALGORITHM\nTotal cost : {total_cost} $\n"
        f"Max profit : {max_benefit} $\n Purchased stocks : {purchased_stocks}"
    )


def dynamic_algorithm(stocks, portfolio):
    """
    Solve the "knapsack" problem by finding the most valuable solution.
    Space complexity : O(n)
    Time complexity : O(n)
    """

    w = portfolio
    total_cost = 0
    n = len(stocks)
    purchased_stocks = []
    matrice = [[0 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, w + 1):
            best_price = math.trunc(stocks[i - 1].price)
            if best_price <= w:
                matrice[i][w] = max(
                    stocks[i - 1].benefit + matrice[i - 1][w - best_price],
                    matrice[i - 1][w],
                )
            else:
                matrice[i][w] = matrice[i - 1][w]
    while n > 1:
        stock = stocks[n - 1]
        w = math.trunc(w)
        if matrice[n][w] == matrice[n - 1][w - math.trunc(stock.price)] + stock.benefit:
            purchased_stocks.append(stock.name)
            w -= stock.price
            total_cost += stock.price
        n -= 1
    max_benefit = matrice[-1][-1]

    print(
        f"\nDYNAMIC ALGORITHM\nTotal cost : {total_cost} $\n"
        f"Max benefit : {max_benefit} $\nPurchased stocks : {purchased_stocks} "
    )
