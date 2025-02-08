import numpy as np
import matplotlib.pyplot as plt
img1=input('Enter Input Image File Name=')
data1=plt.imread(img1)
shape1=data1.shape
r,c,d=shape1[0],shape1[1],shape1[2]
print('r=',r,' c=',c,' d=',d)
data2=data1[0:r//2,0:c,0:d]
data3=data1[r//2+1:r,0:c,0:d]
rows=3
columns=1
fig=plt.figure(figsize=(5,5))
fig.add_subplot(rows,columns,1)
plt.imshow(data1)
plt.axis('off')
plt.title('Original Image')
fig.add_subplot(rows,columns,2)
plt.imshow(data2)
plt.axis('off')
plt.title('Upper Half of Image1')
fig.add_subplot(rows,columns,3)
plt.imshow(data3)
plt.axis('off')
plt.title('Lower Half of Image1')
plt.show()
