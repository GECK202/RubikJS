from re import X
from solver.rubic import cube_t, rotateCube
from solver.top import solvTop, solvTop2
from solver.midl import solvMidl
from solver.bottom import solvBottom, solvBottom2
from itertools import permutations
from time import time


def restrictSolv(solv):
	dir = {	"U U'":"", "U U2":"U'", "U U":"U2", "U' U'":"U2", "U' U2":"U", "U' U":"", "U2 U":"U'", "U2 U2":"", "U2 U'":"U",
			"D D'":"", "D D2":"D'", "D D":"D2", "D' D'":"D2", "D' D2":"D", "D' D":"", "D2 D'":"D", "D2 D2":"", "D2 D":"D'",
			"F F'":"", "F F2":"F'", "F F":"F2", "F' F'":"F2", "F' F2":"F", "F' F":"", "F2 F'":"F", "F2 F2":"", "F2 F":"F'",
			"B B'":"", "B B2":"B'", "B B":"B2", "B' B'":"B2", "B' B2":"B", "B' B":"", "B2 B'":"B", "B2 B2":"", "B2 B":"B'",
			"L L'":"", "L L2":"L'", "L L":"L2", "L' L'":"L2", "L' L2":"L", "L' L":"", "L2 L'":"L", "L2 L2":"", "L2 L":"L'",
			"R R'":"", "R R2":"R'", "R R":"R2", "R' R'":"R2", "R' R2":"R", "R' R":"", "R2 R'":"R", "R2 R2":"", "R2 R":"R'",
			"  ":" "}
	flag = True
	while flag == True:
		newSolv = solv
		for k, v in dir.items():
			newSolv = newSolv.replace(k, v)
		if newSolv == solv:
			flag = False
		solv = newSolv
	return solv.strip()

def solver3(a):
	cube = cube_t()
	rotateCube(cube, a.upper())
	len_des = 100000
	solv_ret = ''
	start = time()
	for top_edg in  permutations([4,5,6,7], 4):
		for top_con in  permutations([4,5,6,7], 4):
			for midl_edg in  permutations([0,1,2,3], 4):
				for bottom_con in  permutations([0,1,2,3], 4):
					cube_x = cube.copyCube()
					try:
						solv = restrictSolv(solvTop(cube_x,top_edg,top_con).strip()+" "+solvMidl(cube_x,midl_edg).strip()+" "+solvBottom(cube_x,bottom_con).strip()).strip()
						x = solv.count(' ')
					except:
						continue
					if x < len_des:
						print(f'find more less solv with len {x} for time from start {time()-start} sec')
						len_des = x
						solv_ret = solv
	print(f'all time for find solvers is {time()-start} sec')
	return solv_ret						

def solver2(a):
	cube = cube_t()
	rotateCube(cube, a.upper())
	solv = restrictSolv(solvTop2(cube).strip()+" "+solvBottom2(cube).strip()).strip()
	print(solv)
