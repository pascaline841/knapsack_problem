class Stock:
    def __init__(self, name, price, percent):
        """
        Define a stock
        Args:
            name (int): name of a stock
            price (float): price of a stock
            percent (float): percentage % of a stock afet 2 years
            benefit (float): benefit in $ of a stock after 2 years.
        """
        self.name = name
        self.price = float(price)
        self.percent = float(percent)
        self.benefit = self.price * self.percent / 100
        self.ratio = self.benefit / self.price


def get_stocks(names, prices, percents):
    """Calculate and add the benefit and the ratio of a stock."""
    return [Stock(*args) for args in zip(names, prices, percents)]


def best_stocks(stocks):
    """Order the stocks by the best benefit and only keep the best 20."""
    stocks = sorted(stocks, key=lambda stock: stock.benefit, reverse=True)
    del stocks[20:]
    return stocks
