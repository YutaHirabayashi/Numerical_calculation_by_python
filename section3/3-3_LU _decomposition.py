#参考資料
# https://www.cspp.cc.u-tokyo.ac.jp/hanawa/class/spc2016s/sp20160614-2.pdf


import numpy as np
import sys

epsilon=sys.float_info.epsilon

a=np.array([[2,4,1,-3],[-1,-2,2,4],[4,2,-3,5],[5,-4,-3,1]]).astype(float)
b=np.array([0,10,2,6]).astype(float)

x=np.zeros((4))

#一時ベクトル
y=np.zeros((4))

#L(下三角)とU(上三角)は1つの4*4で表現可能（メモリ節約）->aに上書きする

#pは置換行列なのでp[i]=j（j行とi行を置換,ただしi<k）という形式の1次元配列で保持する
p=np.zeros((4))

for k in range(0,a.shape[0]-1,1):
    #a[i,k]の中で最大インデックスを求める（k<=i<=N)
    i_max=np.argmax(np.fabs(a[k::,k]))+k

    if np.fabs(a[i_max,k])<epsilon:
        print("a is not regular")
        exit()

    #pに保存
    p[k]=i_max

    #交換
    for n in range(0,a.shape[0],1):
        a[k,n],a[i_max,n]=a[i_max,n],a[k,n]

    #前進消去
    for i in range(k+1,a.shape[0],1):
        alpha=-a[i,k]/a[k,k]
        
        #L行列(三角行列の逆行列なので-がつく)
        a[i,k]=-alpha

        #U行列
        for j in range(k+1,a.shape[1],1):
            a[i,j]=a[i,j]+a[k,j]*alpha

#LU行列はbに寄らず計算できる
print("=============LU==============")
print(a)
print("=============P===============")
print(p)


for k in range(0,a.shape[0]-1,1):
    #bの交換(Pを作用させることに相当)
    b[k],b[(int)(p[k])]=b[(int)(p[k])],b[k]


for k in range(0,a.shape[0],1):
    #前進代入
    s=b[k]
    for i in range(0,k,1):
        s-=(a[k,i]*y[i])
    y[k]=s #Lの対角成分は1

#後進代入
for k in reversed(range(0,a.shape[0],1)):
    s=y[k]
    for i in range(k+1,a.shape[0],1):
        s-=(a[k,i])*x[i]
    x[k]=s/a[k,k]

print("===========B===================")
print(b)

print("===========Y===================")
print(y)    

print("===========X===================")
print(x)    
    
