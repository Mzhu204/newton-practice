import sympy as sp

def df(f, x, h=0.001):
    df = sp.limit((f(x+h)- f(x))/h, h, 0)
    return df

def d2f(f, x, h=0.001):
    def df1(x):
        ddf= df(f, x, h)
        return ddf
    return df(df1, x, h)


def newton(f, x0, h=0.001):
    x=x0
    count = 0
    while df(f, x, h=0.001) > 0.00001:
        x= x-(df(f, x, h=0.001)/d2f(f, x, h=0.001))
        count = count+1
    return x, count

f= lambda x: x**4+ 3*x

newton(f, x0=9, h=0.001)