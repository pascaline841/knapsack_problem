def total_benefit(selection):
    """Sum of total money earn after buy the purchased_stocks."""
    return sum(stock.benefit for stock in selection)


def total_cost(selection):
    """Total money spend to buy the purchased_stocks =< portofolio."""
    return sum(stock.price for stock in selection)


def brute_force_algorithm(stocks, portfolio):
    """
    Brute force method will find all the possible solutions and return the most valuable
    Space complexity : O(2**n)
    Time complexity : O(2**n)
    Returns:
        Max_benefit, purchased_stocks.
    """
    nb_stock = len(stocks)
    nb_combination = 2 ** nb_stock
    best_combination = []
    for i in range(1, nb_combination):
        binary = bin(i)[2:]
        length_bin = len(binary)
        if length_bin <= nb_stock:
            binary = (nb_stock - length_bin) * "0" + binary
        combination = [stocks[i] for i in range(nb_stock) if binary[i] != "0"]
        if (
            total_benefit(combination) > total_benefit(best_combination)
            and total_cost(combination) <= portfolio
        ):
            best_combination = combination
            purchased_stocks = [stock.name for stock in best_combination]
            max_benefit = total_benefit(best_combination)
            max_cost = total_cost(best_combination)

    return purchased_stocks, max_benefit, max_cost
