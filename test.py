import matplotlib.pyplot as plt
N = 5
menMeans = (20, 35, 30, 35, 27)
ind = np.arange(N)

#Creating a figure with some fig size
fig, ax = plt.subplots(figsize = (10,5))
ax.bar(ind,menMeans,width=0.4)
#Now the trick is here.
#plt.text() , you need to give (x,y) location , where you want to put the numbers,
#So here index will give you x pos and data+1 will provide a little gap in y axis.
for index,data in enumerate(menMeans):
    plt.text(x=index , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=20))
plt.tight_layout()
plt.show()