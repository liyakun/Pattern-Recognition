import numpy as np
import scipy, scipy.spatial
import random
import sys
import matplotlib.pyplot as plt

def LIoyds(data, k):
	min_val_X = min(data[0,:])
	min_val_Y = min(data[1,:])
	max_val_X = max(data[0,:])
	max_val_Y = max(data[1,:])
	
	# initialize centers
	centers = np.zeros((k, 2), np.float64 )
	for i in range(k):
		centers[i,0] = random.uniform( min_val_X , max_val_X )
		centers[i,1] = random.uniform( min_val_Y , max_val_Y )

	change = True
	index = np.zeros( len(data[0,:]) )
	index_previous = np.zeros( len(data[0,:]) )

	# loop until there is no change in assignment to clusters
	while change == True:
		
		print "next iteration"

		tree = scipy.spatial.KDTree( centers )
		index = np.zeros( len(data[0,:]) )

		# assign points to clusters/centers
		for i in range( len(data[0,:]) ):
			[ distance , location] = tree.query( data[:,i] )
			index[i] = location

		# if assignment to centers did not change then stop algorithm
		if np.array_equal( index , index_previous ):
			change == False
			break

		index_previous = np.copy( index )

		for i in range(k):
			centers[i,0] = 0.0
			centers[i,1] = 0.0

		# calculate new position of centroid
		for i in range( 0 , k ): # loop over all centers	
			no_of_points_in_cluster = sum((index_previous) == i) # sum number of points assigned to a center	

			for j in range( len( index_previous ) ): # loop over all indexes of points
				if index_previous[j] == i: # if point is assigned to center add it
					centers[i,0] = centers[i,0] + data[0,i]
					centers[i,1] = centers[i,1] + data[1,i]
		
			if no_of_points_in_cluster != 0:
				centers[i,0] = centers[i,0] / float(no_of_points_in_cluster)
				centers[i,1] = centers[i,1] / float(no_of_points_in_cluster)
			else:
				centers[i,0] = 0.0
				centers[i,1] = 0.0

	return index, centers



def plotData(data,indexes,centers):
	plt.title("plot")
	
	bool_idx = (indexes == 0)
	plt.scatter(data[0,bool_idx], data[1,bool_idx], color='red')
	plt.scatter(centers[0,0], centers[0,1], s=100 , color='red', edgecolors='black')

	bool_idx = (indexes == 1)
	plt.scatter(data[0,bool_idx], data[1,bool_idx], color='orange')
	plt.scatter(centers[1,0], centers[1,1], s=100 , color='orange', edgecolors='black')

	bool_idx = (indexes == 2)
	plt.scatter(data[0,bool_idx], data[1,bool_idx], color='green')
	plt.scatter(centers[2,0], centers[2,1], s=100 , color='green', edgecolors='black')

	plt.show()






data = np.loadtxt('resources/data-clustering-1.csv', None, comments='#', delimiter=',')

[indexes, centers] = LIoyds(data , 3)

plotData(data,indexes,centers)