import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
#% formatter something like '{:06}'
  
X = ['RRC','SDAP','PDCP','RLC','MAC','PHY','NG']
Xticks = [0,1,2,3,4,5,6]
Y = [1.53, 0, 1.0, 5.79, 0.03, 43.64, 30.24]

#fig = plt.figure()  
plt.bar(X, Y, 1, color="blue")  
#plt.bar(XX,YY,1,color="yellow")  #使用不同颜色  
plt.xlabel("X-axis")  #设置X轴Y轴名称  
plt.ylabel("Y-axis")  
plt.title("bar chart")
#使用text显示数值  
for a,b in zip(Xticks,Y):
    plt.text(x = a-0.25 , y = b+0.05 , s=f"{b}" , fontdict=dict(fontsize=10))
    #plt.text(x=a , y = b , s=f"{b}" , fontdict=dict(fontsize=10))
 #plt.text(a, b+0.05, '%.000f' % b, ha='center', va= 'bottom',fontsize=11)  
#for a,b in zip(XX,YY):  
# plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)    
plt.ylim(0,45.00)    #设置Y轴上下限  
plt.show()

