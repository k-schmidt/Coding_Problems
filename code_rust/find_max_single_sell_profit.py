"""
Given a list of stock prices for n days, find the max profit
with a single buy/sell activity.
"""


def find_buy_sell_stock_prices(array):
    if array is None or len(array) < 2:
        return None

    current_buy = array[0]
    global_sell = array[1]
    global_profit = global_sell - current_buy

    current_profit = None

    for i in range(1, len(array)):
        current_profit = array[i] - current_buy

        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = array[i]

        if current_buy > array[i]:
            current_buy = array[i]

    return (global_sell - global_profit), global_sell
