import numpy as np

#修正コレスキー分解を行う （A=L^t D L）：Dは対角成分のみ
#行列zに書く（対角成分：D、下三角部分：L）

a=np.array(
    [
        [2.0,-1.0,0.0,0.0],
        [-1.0,3.0,-1.0,0.0],
        [0.0,-1.0,3.0,-1.0],
        [0.0,0.0,-1.0,2.0]
    ]
)

b=np.array([4.0,-10.0,15.0,-11.0])

#修正コレスキー分解
z=np.zeros((a.shape))

for i in range(0,a.shape[0]):
    for j in range(0,i):
        s=0
        for k in range(0,j):
            s+=(z[i,k]*z[k,k]*z[j,k])
        z[i,j]=(a[i,j]-s)/z[j,j]
    s=0
    for k in range(0,i):
        s+=(z[i,k]*z[i,k]*z[k,k])
    z[i,i]=a[i,i]-s


#修正コレスキー分解の結果を利用して、方程式をとく
#LDy=b
y=np.zeros((b.shape))
for i in range(0,a.shape[0]):
    s=0
    for j in range(0,i):
        s+=(z[j,j]*z[i,j]*y[j])    
    y[i]=(b[i]-s)/z[i,i]

#Ltx=y
x=np.zeros((b.shape))
for i in reversed(range(0,a.shape[0])):
    s=0
    for j in range(i+1,a.shape[0]):
        s+=(z[j,i]*x[j])
    x[i]=y[i]-s

print("===========Z===================")
print(z)    

print("===========Y===================")
print(y)    
print("===========X===================")
print(x)    