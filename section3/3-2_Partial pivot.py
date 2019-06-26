
import numpy as np
import sys

eposilon=sys.float_info.epsilon

a=np.array([[2,4,1,-3],[-1,-2,2,4],[4,2,-3,5],[5,-4,-3,1]]).astype(float)
b=np.array([0,10,2,6]).astype(float)

x=np.zeros((4))

for k in range(0,a.shape[0]-1,1):
    #a[i,k]の中で最大インデックスを求める(k<=i<=N)
    i_max=np.argmax(np.fabs(a[k::,k]))+k
    
    #if a[imax,k]<epsiron->quit
    #else a[imax]とa[k]、b[imax]とb[k]を入れ替える
    if np.fabs(a[i_max,k])<eposilon:
        print("a is not regular")
        exit()
    
    #listで交換するとうまくいかないので注意（ミュータブルだから）
    for n in range(0,a.shape[0],1):
        a[k,n],a[i_max,n]=a[i_max,n],a[k,n]
    b[k],b[i_max]=b[i_max],b[k]

    #前進消去
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