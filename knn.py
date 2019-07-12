import numpy as np 
from sklearn.neighbors import KDTree
import pickle
import pandas as pd
# rng = np.random.RandomState(0)
# X = rng.random_sample((10, 23))  
def get_train(json_file):
	df= pd.read_json(json_file)
	return df

def build_kdtree(X, filename):
	tree= KDTree(X, leaf_size=2)
	f= open(filename, "wb")
	pickle.dump(tree, f)
	f.close()
	return tree

def load_tree(filename):
	f= open(filename, 'rb')
	tree= pickle.load(f)
	return tree 

def get_neighbors_idx(kdtree, new_data, k=3):
	#get indicies of the closest neighbors
	dist, ind = kdtree.query(new_data, k)   
	return ind.flatten()

def generate_random(centers_list, n):
	#generate the random data based on the composite scores 
	res= []
	for j in range(n):
		temp= []
		for i in centers_list:
			temp.append(abs(np.random.normal(i, 0.2)))
		res.append(temp)
	return np.array(res)

def predict(neighbors_idx, train_data):
	arr= np.array(train_data)
	classes= train_data[tuple(neighbors_idx), -1]
	pred= np.mean(classes)
	if pred > 0.5:
		return 1
	else:
		return 0

def get_composite(ndarr):
	#expect ndarray of training data
	return np.array([np.mean(ndarr[:, i]) for i in range(len(ndarr[0]))])

def merge_data(twitter_data, n):
	composite_scores= get_composite(twitter_data)
	centers= np.subtract(1, composite_scores)
	fake_data= generate_random(centers, n)
	final= np.concatenate((twitter_data, fake_data))
	return final

def run(new_data, filename, start_data= None, model_trained= False):
	train_data= merge_data(start_data, 5)
	if model_trained:
		tree= load_tree(filename)
	else:
		tree= build_kdtree(train_data, filename)
	idx= get_neighbors_idx(tree, [new_data])
	val= predict(idx, train_data)
	if val == 1:
		return "Accept"
	else:
		return "Reject"

#new stuff
def result_object(filename, pickle_file):
	df= get_train(filename)
	ndarr_train= df.to_numpy()[1:]
	test= df.to_numpy()[0]
	res= run(test, pickle_file, ndarr_train)
	final= df.iloc[0].to_dict()
	final["Predicted Decision"]= res
	return final 

if __name__ == '__main__':
	print(result_object("dataset.json", "final.pickle"))









