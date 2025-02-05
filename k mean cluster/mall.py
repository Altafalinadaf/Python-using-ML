import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the dataset
dataset=pd.read_csv('C:/Users/altaf/Downloads/Mall_Customers.csv')
print(dataset.isnull().sum())
print(dataset.shape)
print(dataset.describe)
print(dataset.head(5))


# Segregate & Zipping Dataset

X= dataset['Annual Income (k$)'].values
Y = dataset['Spending Score (1-100)'].values
x=np.array(list(zip(X,Y)))

from sklearn.cluster import KMeans
wcss=[]
for i in range (1,11):
    km=KMeans(n_clusters=i,random_state=0)
    km.fit(x)
    wcss.append(km.inertia_)
plt.plot(range(1,11),wcss,color='red',marker='8')
plt.title('Optimal K values')
plt.xlabel("number of cluster")
plt.ylabel("WCSS")

# fitting the kmeans to the dataset with k=4
model=KMeans(n_clusters=5,random_state=0)
y_means=model.fit_predict(x)
plt.show()
"""### Visualizing the clusters for k=4

Cluster 1: Customers with medium income and low spend

Cluster 2: Customers with high income and medium to high spend

Cluster 3: Customers with low income

Cluster 4: Customers with medium income but high spend
"""
#mtp.scatter, i.e., x[y_predict == 0, 0] containing the x value for the showing the matrix of features values,
# and the y_means is ranging from 0 to 1
plt.scatter(x[y_means==0,0],x[y_means==0,1],s=50, c='brown',label='1')
plt.scatter(x[y_means==1,0],x[y_means==1,1],s=50, c='blue',label='2')
plt.scatter(x[y_means==2,0],x[y_means==2,1],s=50, c='green',label='3')
plt.scatter(x[y_means==3,0],x[y_means==3,1],s=50, c='cyan',label='4')
plt.scatter(x[y_means==4,0],x[y_means==4,1],s=50, c='yellow',label='5')
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1],s=100,marker='s', c='red', label='Centroids')
plt.title('Mall Spending Analysis')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
