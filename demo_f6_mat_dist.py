import route_opt as ropt
import numpy as np

tow_names = ["4018", "4019", "4027", "4028", "4029", "4032", "4035", "4697", "CAMÇ", "SBZÇ"]

#which tow performs milkruns to which segments
rut = np.array([[0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
                [0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
                [0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1],
                [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0]])

#length of each segment
lng = np.array([[17444], [59930], [8545], [24432], [24800], [56130], [36290],
                [21690], [24985], [5431], [39357], [21930], [29139], [67253], 
                [120540], [120540], [12540], [17945], [17934], [16993], [17082], 
                [18038], [17570], [17625], [19190], [20470], [38600], [17517], 
                [18260], [8916], [8670], [10410], [12569], [1], [1]])

mat = np.zeros([35, 35]) + np.inf

#indicates which road segment is attached to which segments
att = [(1, 17),
       (17, 1),
       
       (2, 18),
       (2, 1),
       (18, 1),
       (18, 2),
       (1, 2),
       (1, 18),

       (0, 3),
       (0, 2),
       (2, 3),
       (2, 0),
       (3, 0),
       (3, 2),

       (3, 19),
       (19, 3),

       (5, 21),
       (5, 17),
       (21, 17),

       (18, 5),
       (18, 22),
       (6, 5),
       (6, 22),

       (19, 6),
       (19, 23),
       (7, 6),
       (7, 23),

       (20, 7),
       (26, 7),
      #  (26, 20),

       (32, 21),

       (21, 8),
       (21, 24),
       (8, 24),
       
       (9, 25),
       
       (22, 9),
       (22, 10),
       (10, 9),

       (10, 23),

       (24, 11),
       (24, 27),
       
       (11, 12),

       (12, 13),
       (25, 13),

       (13, 26),
       (28, 26),

       (27, 33),
       (27, 14),
       (27, 29),
       
       (14, 28),
       (30, 28),
       
       (29, 15),
       (31, 15),
       (29, 31),

       (15, 30),
       (15, 32),
       (32, 30),
       
       (32, 34),
       (34, 32),

       (31, 16),

       (16, 32)
       ]

for i in range(mat.shape[0]):
    mat[i,i] = 0
    # mat[i,i] = 0.5

for i,j in att:
    mat[i,j] = 1

primes = ropt.list_primes(len(lng))

one_step_dist = mat * lng

res = ropt.iterate_mat(one_step_dist, primes)