import numpy as np

#行列
a=np.array([[1,2,1,1],[4,5,-2,4],[4,3,-3,1],[2,1,1,3]])
#ベクトル
b=np.array([-1,-7,-12,2])

#解
x=np.zeros((a.shape[0]))

#前進消去
for k in range(0,a.shape[0]-1,1):
    for i in range(k+1,a.shape[0],1):
        alpha=-a[i,k]/a[k,k]
        for j in range(k,a.shape[1],1):
            a[i,j]=a[i,j]+a[k,j]*alpha
        b[i]=b[i]+b[k]*alpha

#後進代入
for k in reversed(range(0,a.shape[0],1)):
    s=0
    for i in range(k+1,a.shape[0],1):
        s+=(a[k,i]*x[i])
    x[k]=(b[k]-s)/a[k,k]

print("=============A==============")
print(a)
print("=============B==============")
print(b)
print("=============X==============")
print(x)
