#route optimization given a graph matrix

import numpy as np
np.set_printoptions(suppress=True, precision=0)

def sko_matmul(stepn:np.ndarray, step1:np.ndarray, rout:np.ndarray):
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

	return dout, rout

def iterate_mat(step:np.ndarray, vert_names:list = []):
	if len(vert_names) != step.shape[0]:
		vert_names = [x for x in range(step.shape[0])]

	rout = np.empty((step.shape), dtype=object)
	dout = step.copy()

	for i in range(rout.shape[0]):
		for j in range(rout.shape[1]):
			rout[i,j] = [vert_names[i], vert_names[j]]

	while True:
		dout, rout = sko_matmul(dout, step, rout)

		print(dout, "\n\n", rout)

		if np.array_equal(dout, sko_matmul(dout, step, rout)[0]):
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