import sympy as sp


def df(f, x, h=0.001):
    df = sp.limit((f(x + h) - f(x)) / h, h, 0)
    return df


""" output the first derivative of a function by using the limit estimation"""


def d2f(f, x, h=0.001):
    def df1(x):
        ddf = df(f, x, h)
        return ddf

    return df(df1, x, h)


""" output the second derivative of a function by calling df and then using the first derivative as an argument"""


def newton(f, x0, h=0.001):
    x = x0
    count = 0
    while df(f, x, h=0.001) > 0.00001:  # 0.00001 is our stopping value
        x = x - (df(f, x, h=0.001) / d2f(f, x, h=0.001))
        count = count + 1
    if count = 0:
        raise Error 
    return x, count


""" the newton optimization implementation using the equation:
"x_t = x_t-1 - f'(x_t-1)/ f''(x_t-1)" """

f = lambda x: x**4 + 3 * x  # our function to optimize

newton(f, x0=9, h=0.001)
