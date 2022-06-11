from re import X
from solver.rubic import cube_t, rotateCube
from solver.top import solvTop, solvTop2
from solver.midl import solvMidl
from solver.bottom import solvBottom, solvBottom2
from itertools import combinations


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
	for solvTop_comb_edg in  combinations([4,5,6,7], 4):
		for solvTop_comb_con in  combinations([4,5,6,7], 4):
			for solvMidl_comb_con in  combinations([0,1,2,3], 4):
				for solvBottom_comb_con in  combinations([0,1,2,3], 4):
					cube_x = cube.copy()
					solv = restrictSolv(solvTop(cube_x,solvTop_comb_edg,solvTop_comb_con).strip()+" "+solvMidl(cube_x,solvMidl_comb_con).strip()+" "+solvBottom(cube_x,solvBottom_comb_con).strip()).strip()
					x = solv.count(' ')
					if x < len_des:
						len_des = x
						solv_ret = solv
	return solv_ret						

def solver2(a):
	cube = cube_t()
	rotateCube(cube, a.upper())
	solv = restrictSolv(solvTop2(cube).strip()+" "+solvBottom2(cube).strip()).strip()
	print(solv)
