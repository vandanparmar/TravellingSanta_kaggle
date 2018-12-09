from matplotlib import pyplot as plt
import numpy as np
import csv


with open('all/cities.csv','r') as csv_data:
	csv_reader = csv.reader(csv_data, delimiter=',')
	orig_data = list(csv_reader)

# print(orig_data)

def is_prime(n):
	if n % 2 == 0 and n > 2: 
		return False
	return all(n % i for i in range(3, int(np.sqrt(n)) + 1, 2))

def gen_order_list(v,ids):
	## for all ids, then adds on 0 at the beginning and end
	return [0]+[val for _,val in sorted(zip(v,ids))]+[0]

def tot_dist(order):
	##order is a 'correctly' sorted list of ids
	this_xs = xs[order]
	this_ys = ys[order]
	print(this_xs,this_ys)
	d_x = np.diff(this_xs,1)
	d_y = np.diff(this_ys,1)
	this_xs2 = np.power(d_x,2)
	this_ys2 = np.power(d_y,2)
	dists = this_xs2+this_ys2
	## not sure if below should be [1::10] or [0::10]
	penalty = np.sum(0.1*np.multiply(dists[1::10],prime_bools[order[1::10]]))
	dist = np.sum(dists)+penalty
	return (dist,penalty)


ids = np.array(list(map(lambda x:int(x[0]),orig_data[1:])))
xs = np.array(list(map(lambda x:float(x[1]),orig_data[1:])))
ys = np.array(list(map(lambda x:float(x[2]),orig_data[1:])))
print(ids.dtype)
print(xs.dtype)
print(ys.dtype)
no_of_vals = len(ids)
prime_v = np.vectorize(is_prime)
prime_bools = np.array(prime_v(np.arange(no_of_vals)))
print(prime_bools)

test_vals = np.random.rand(no_of_vals-1)
test_vals[[0,-1]] = 0


print(tot_dist(gen_order_list(test_vals,ids)))