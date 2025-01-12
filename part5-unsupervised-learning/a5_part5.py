import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#imports the data
data = pd.read_csv("part5-unsupervised-learning/customer_data.csv")
x = data[["Annual Income", "Spending Score"]]

#standardize the data
scaler = StandardScaler()
x = scaler.fit_transform(x)

#the value of k has been defined for you
k = 5

#apply the kmeans algorithm
kmeans = KMeans(n_clusters=k)
kmeans.fit(x)

#get the centroid and label values
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

#sets the size of the graph
plt.figure(figsize=(5,4))

#use a for loop to plot the data points in each cluster
for i in range(k):
    plt.scatter(x[labels==i][:,0], x[labels==i][:,1], label="Cluster "+str(i+1))
    plt.scatter(centroids[i][0], centroids[i][1], s=200, label="Centroid "+str(i+1), marker="x")

#plot the centroids
plt.scatter(centroids[:,0], centroids[:,1], s=200, label="Centroids", marker="x")
            
#shows the graph
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()
plt.legend()