import numpy as np

#f(x)=0の左辺の定義
def f(x):
    y=x-np.cos(x)
    return y

def df(x):
    y=1+np.sin(x)
    return y

#補正量の下限
EPSIRON=1E-7

#newton法（全体）
def newton_method(x_0,f,df,epsiron,N_max):
    x=x_0
    n=0

    while(np.fabs(-f(x)/df(x))>epsiron):
        if n<N_max:
            x=x-f(x)/df(x)
            n=n+1
        else:
            return np.NAN
    return x

if __name__ == "__main__":
    #newton法
    x=newton_method(
        x_0=3,
        f=f,
        df=df,
        epsiron=EPSIRON,
        N_max=10
    )

    print(x)