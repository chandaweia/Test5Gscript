#https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh

import matplotlib.pyplot as plt
import numpy as np
N = 5
menMeans = (20.0, 35.115, 30, 35, 27)
ind = np.arange(N)

y = [1.53, 0, 1.0, 5.79, 0.03, 43.64, 30.24]
x = ['RRC','SDAP','PDCP','RLC','MAC','PHY','NG']
xarr=[1,2,3,4,5,6,7]

#Creating a figure with some fig size
fig, ax = plt.subplots(figsize = (10,5))
ax.bar(xarr,y,width=0.4)
#Now the trick is here.
#plt.text() , you need to give (x,y) location , where you want to put the numbers,
#So here index will give you x pos and data+1 will provide a little gap in y axis.
for index,data in enumerate(y):
    plt.text(x=index , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=20))
plt.tight_layout()
plt.show()
