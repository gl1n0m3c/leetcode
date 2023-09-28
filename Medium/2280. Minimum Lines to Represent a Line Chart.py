# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/description/

def minimumLines(stockPrices):
    if len(stockPrices) <= 1:
        return 0
    stockPrices.sort()
    start_day       = stockPrices[0][0]
    start_equal     = stockPrices[0][1]
    previous_day    = stockPrices[1][0]
    previous_equal  = stockPrices[1][1]
    number_of_lines = 1
    delta = ((previous_equal - start_equal), (previous_day - start_day))
    for i in range(2, len(stockPrices)):
        day   = stockPrices[i][0]
        equal = stockPrices[i][1]
        new_delta = ((equal - previous_equal), (day - previous_day))
        if delta[0]*new_delta[1] != delta[1]*new_delta[0]:
            number_of_lines += 1
            delta = new_delta
        previous_day   = day
        previous_equal = equal
    return number_of_lines