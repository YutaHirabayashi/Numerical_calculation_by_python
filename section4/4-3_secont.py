import numpy as np

def f(x):
    y=x-np.cos(x)
    return y

EPSIRON=1E-7

def calc_dval(x_m,x,f):
    d=-f(x)*(x-x_m)/(f(x)-f(x_m))
    return d

def secont(x_0,x_1,f,epsiron,N_max):
    x_m=x_0
    x=x_1
    n=0

    while True:
        d=calc_dval(x_m,x,f)
        if n<N_max:
            x_m=x
            x=x+d
            n=n+1
        else:
            return np.NAN

        if d<=epsiron:
            return x

if __name__ == "__main__":
    #newton法
    x=secont(
        x_0=1,
        x_1=2,
        f=f,
        epsiron=EPSIRON,
        N_max=20
    )

    print(x)