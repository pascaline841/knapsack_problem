import csv

import time

import stock

import bruteforce

import optimized


def get_data(path):
    """
    Function to obtain datas of stocks in a csv document.
    Args:
        path (str): path to the document.
    """
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]
    return data


def get_stocks_csv():
    request = input(
        "What dataset of stocks would you like to analyzed ?\n "
        "- dataset1\n - dataset2\n - dataset_test\n\n"
    )
    path = f"csv files\{request}.csv"
    data = get_data(path)
    names = data["name"]
    prices = data["price"]
    percents = data["profit"]
    return stock.get_stocks(names, prices, percents)


def main():
    """Run the program with csv file."""
    print("\n                     Algo Invest&Trade\n")
    portfolio = 500
    stocks = get_stocks_csv()

    # ALGO GLOUTON
    start_time = time.time()
    optimized.greedy_algorithm(stocks, portfolio)
    print(f"Time of excecution : {(time.time() - start_time)} secondes.")

    # ALGO DYNAMIQUE
    start_time = time.time()
    optimized.dynamic_algorithm(stocks, portfolio)
    print(f"Time of excecution : {(time.time() - start_time)} secondes.")

    # ALGO FORCE BRUTE
    start_time = time.time()
    print("\nBRUTE FORCE ALGORITHM")
    stocks = stock.best_stocks(stocks)
    result = bruteforce.brute_force_algorithm(stocks, portfolio)
    print(
        f"Total cost : {result[2]} $\nMax benefit : {result[1]} $\n"
        f"Purchased stocks : {result[0]}\n"
        f"Time of excecution : {(time.time() - start_time)} secondes."
    )


if __name__ == "__main__":
    main()
