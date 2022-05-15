#route optimization given a graph matrix

import numpy as np
np.set_printoptions(suppress=True, precision=0)

# def is_prime(x:int) -> bool:
# 	if x <= 1:
# 		return False
# 	for c in range(2, 1+x//2):
# 		if x%c == 0:
# 			return False
# 	return True

# def list_primes(n:int, primes:list = [], last_checked:int = 0) -> list:
# 	if n == 0:
# 		out = primes.copy()
# 		primes.clear()
# 		return out
# 	elif n < 0:
# 		raise Exception("Enter value greater than 0!")

# 	else:
# 		if is_prime(last_checked + 1):
# 			primes.append(last_checked + 1)
# 			return list_primes(n-1, primes, last_checked+1)
# 		else:
# 			return list_primes(n, primes, last_checked + 1)

# def primes_up2(x:int, primes:list = []) -> list:
# 	if x == 0:
# 		out = primes.copy()
# 		primes.clear()
# 		return out
# 	elif x < 0:
# 		raise Exception("Enter value greater than 0!")

# 	else:
# 		if is_prime(x):
# 			primes.insert(0, x)
# 		return primes_up2(x-1, primes)
	
# def get_carpan(x:int) -> list:
# 	temp = x
# 	divs = []
# 	pp = primes_up2(x//2)
# 	while len(pp) != 0:
# 		if x % pp[0] == 0:
# 			divs.append(pp[0])
# 			x = x//pp[0]
# 		else:
# 			pp.pop(0)
# 	if len(divs) == 0 and is_prime(temp):
# 		divs.append(temp)
# 	return divs





def sko_matmul(stepn:np.ndarray, step1:np.ndarray, rout:np.ndarray, vert_names:list):
	print("\n")
	assert step1.shape[1] == stepn.shape[0]
	c_ax = step1.shape[1]
	dout = np.zeros(stepn.shape) + np.inf

	for fr in range(c_ax):
		for to in range(c_ax):
			for bt in range(c_ax):
				if bt == to or bt == fr:
					continue
			
				else:
					comp = [dout[fr, to], 
							stepn[fr, to], 
							stepn[fr, bt] + step1[bt, to]]

					k = np.argmin(comp)

					dout[fr, to] = comp[k]

					if k == 2:
						rout[fr, to] = rout[fr, bt].copy()
						rout[fr, to].append(rout[bt, to][-1])
								
						# rout[fr, to] = rout[fr, bt] * rout[bt, to]
						# print(vert_names[fr], vert_names[to], 90*"-")
						# print(vert_names[bt], "\t", rout[fr, bt], rout[bt, to])

	return dout, rout

def iterate_mat(step:np.ndarray, vert_names:list):
	# rout = np.ones(step.shape) * prs
	rout = np.empty((step.shape), dtype=object)
	dout = step.copy()

	for i in range(rout.shape[0]):
		# rout[i,i] = 0
				
		for j in range(rout.shape[1]):
			rout[i,j] = [vert_names[i], vert_names[j]]

			# if step[i,j] == 0 or step[i,j] == np.inf:
			#     rout[i,j] = 1

	while True:
		dout, rout = sko_matmul(dout, step, rout, vert_names)

		print(dout, "\n\n", rout)

		if np.array_equal(dout, sko_matmul(dout, step, rout, vert_names)[0]):
			return dout, rout

def vert_set(rut_rout):
	vertices = set()
	for i in range(rut_rout.shape[0]):
		for j in range(rut_rout.shape[1]):
			for v in rut_rout[i,j]:
				vertices.add(v)
	
	return vertices	

def get_simplified_rut(dout:np.ndarray, rout:np.ndarray, rut_row):
	ma = (rut_row==1)

	tempd, tempr = dout[ma, :], rout[ma, :]
	return tempd[:, ma], tempr[:, ma]

def get_ruts(step:np.ndarray, rut:np.ndarray, lng:np.ndarray = [], tow_names = [], vert_names = []):
	if len(tow_names) != rut.shape[0]:
		tow_names = [x for x in range(rut.shape[0])]
	if len(lng) != step.shape[0]:
		lng = [1 for x in range(step.shape[0])]
	if len(vert_names) != step.shape[0]:
		vert_names = [x for x in range(step.shape[0])]

	assert step.shape[1] == rut.shape[1]
	
	osd = step*lng

	dout, rout = iterate_mat(osd, vert_names)

	res = {}

	for tow in range(rut.shape[0]):
		rut_dout, rut_rout = get_simplified_rut(dout, rout, rut[tow, :])
		tow_vert_set = vert_set(rut_rout)
		tow_name = tow_names[tow]
		print("tow:", tow_name, "\n", tow_vert_set)
		res[tow_name] = tow_vert_set

	return res, rout, dout