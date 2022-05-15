#route optimization given a graph matrix

from turtle import shape
import numpy as np
np.set_printoptions(suppress=True, precision=0)

def is_prime(x:int) -> bool:
    if x <= 1:
        return False
    for c in range(2, 1+x//2):
        if x%c == 0:
            return False
    return True

def list_primes(n:int, primes:list = [], last_checked:int = 0) -> list:
    if n == 0:
        out = primes.copy()
        primes.clear()
        return out
    elif n < 0:
        raise Exception("Enter value greater than 0!")

    else:
        if is_prime(last_checked + 1):
            primes.append(last_checked + 1)
            return list_primes(n-1, primes, last_checked+1)
        else:
            return list_primes(n, primes, last_checked + 1)

def primes_up2(x:int, primes:list = []) -> list:
    if x == 0:
        out = primes.copy()
        primes.clear()
        return out
    elif x < 0:
        raise Exception("Enter value greater than 0!")

    else:
        if is_prime(x):
            primes.insert(0, x)
        return primes_up2(x-1, primes)
    
def get_carpan(x:int) -> list:
    temp = x
    divs = []
    pp = primes_up2(x//2)
    while len(pp) != 0:
        if x % pp[0] == 0:
            divs.append(pp[0])
            x = x//pp[0]
        else:
            pp.pop(0)
    if len(divs) == 0 and is_prime(temp):
        divs.append(temp)
    return divs


def sko_matmul(stepn:np.ndarray, step1:np.ndarray, primes:list, rout:np.ndarray):
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
                        for i, v in enumerate(rout[bt, to]):
                            if i == 0:
                                continue
                            else:
                                print(rout[fr, to], v)
                                rout[fr, to].append(v)
                                print(rout[fr, to])

                        # rout[fr, to] = rout[fr, bt] * rout[bt, to]
                        # print(fr+1, to+1, 90*"-")
                        # print(bt+1, "\t", rout[fr, bt], rout[bt, to])

    return dout, rout

def iterate_mat(step:np.ndarray, prs):
    # rout = np.ones(step.shape) * prs
    rout = np.empty((step.shape), dtype=object)
    dout = step.copy()

    for i in range(rout.shape[0]):
        # rout[i,i] = 0
        
        for j in range(rout.shape[1]):
            rout[i,j] = [i+1, j+1]
            if step[i,j] == np.inf:
                rout[i,j] = []

            # if step[i,j] == 0 or step[i,j] == np.inf:
            #     rout[i,j] = 1

    while True:
        dout, rout = sko_matmul(dout, step, prs, rout)

        # print(dout, "\n\n", rout)

        if np.array_equal(dout, sko_matmul(dout, step, prs, rout)[0]):
            return dout, rout

def opt_rut(rout, prs, fr, to):
    pass

def get_simplified_rut(dout:np.ndarray, rout:np.ndarray, rut_row):
    ma = (rut_row==1)

    tempd, tempr = dout[ma, :], rout[ma, :]
    return tempd[:, ma], tempr[:, ma]

def get_ruts(step:np.ndarray, rut:np.ndarray, lng:np.ndarray = [], tow_names = []):
    if len(tow_names) != rut.shape[0]:
        tow_names = [x for x in range(rut.shape[0])]
    if len(lng) != step.shape[0]:
        lng = [1 for x in range(step.shape[0])]

    prs = list_primes(len(lng))

    osd = step*lng

    dout, rout = iterate_mat(osd, prs)

    for tow in range(rut.shape[0]):
        rut_dout, rut_rout = get_simplified_rut(dout, rout, rut[tow, :])
        print(tow_names[tow], rut_mat)