import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here

	# standard
	mean = np.mean(data, axis=0)
	std  = np.std(data, axis=0)
	standardized_data = np.round(((data - mean) / std), 4)

	# normalized
	mn = np.min(data, axis=0)
	mx = np.max(data, axis=0)
	normalized_data = np.round(((data - mn) / (mx - mn)), 4)


	return standardized_data, normalized_data