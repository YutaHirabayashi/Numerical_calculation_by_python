
#誤差評価に関するTaylor展開を用いた解説
#https://qiita.com/Ren112358/items/f2c0bbc90810c040a2e5

import numpy as np

#f(x)の定義
def f(x):
    y=np.power(x,5.0)-5.0*np.power(x,3.0)+4.0*x
    return y

#精度の定義
EPSIRON=1E-10

#二分法
def bisection(a,b,f,epsiron):
    x_min=a
    x_max=b
    while(x_max-x_min>epsiron):
        c=(x_min+x_max)/2
        y1=f(x_min)
        y2=f(c)
        if y1*y2<0:
            x_max=c
        else:
            x_min=c
    return c

#範囲[a,b]の、aとbを返す
def search_range(range_x_min,range_x_max,n,f):
    h=(range_x_max-range_x_min)/n
    for b in np.arange(range_x_min+h,range_x_max,h):
        a=b-h
        y1=f(a)
        y2=f(b)
        if y1*y2<0:
            return a,b

    return np.NAN, np.NAN

#main
if __name__ == "__main__":
    #範囲[a,b]を決定
    a,b=search_range(
        range_x_min=-3,
        range_x_max=3,
        n=10,
        f=f
    )

    if np.isnan(a) or np.isnan(b):
        print("中間値に解が存在しません")
        exit()

    #二分法を実施して解を求める
    x=bisection(
        a=a,
        b=b,
        f=f,
        epsiron=EPSIRON
    )

    print(x)