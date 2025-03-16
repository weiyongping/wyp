import itertools as itt

spins = ("up", "down")  # 自旋
def states_O(coordinates,orbits):  # 得到单个空穴在氧上的所有可能状态
    states = []
    for coordinate in coordinates:
        if coordinate[1] == 0:  # 判断氧的轨道: px or py
            orbit = orbits[0]
        else:
            orbit = orbits[1]
        for spin in spins:
            states.append((coordinate,orbit,spin))
    return states  # 以列表的形式输出所有状态，每个状态为一个元组：包含坐标，轨道，自旋

def states_Ni(coordinates,orbits):  # 得到单个空穴在镍上的所有可能状态
    states = []
    for coordinate in coordinates:  # 遍历坐标，轨道，自旋
        for orbit in orbits:
            for spin in spins:
                states.append((coordinate, orbit, spin))
    return states

def main():
    coor1_O = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0)]  # 氧的坐标
    orbit1_O = ["px", "py"]  # 氧的轨道
    coor1_Ni = [(0, 0, 0)]
    orbit1_Ni = ["dx2", "dz2"]

    states1_one = states_O(coor1_O, orbit1_O) + states_Ni(coor1_Ni, orbit1_Ni)  # 单个空穴的所有可能状态
    states1_two = list(itt.combinations(states1_one, 2))  # 2个空穴的所有可能状态
    print(states1_one)
    print(len(states1_one))  # 状态个数
    print(states1_two)
    print(len(states1_two))

    print("*"*50)

    coor2_O = [(0,0,0),(-2, 0, 0), (2, 0, 0), (-1, -1, 0), (-1, 1, 0),(1,-1,0),(1,1,0)]  # 氧的坐标
    orbit2_O = ["px", "py"]  # 氧的轨道
    coor2_Ni = [(-1,0,0),(1,0,0)]
    orbit2_Ni = ["dx2", "dz2"]

    states2_one = states_O(coor2_O, orbit2_O) + states_Ni(coor2_Ni, orbit2_Ni)  # 单个空穴的所有可能状态
    states2_four = list(itt.combinations(states2_one, 4))  # 4个空穴的所有可能状态
    print(states2_one)
    print(len(states2_one))  # 状态个数
    # print(states2_four)
    print(len(states2_four))

if __name__ == "__main__":
    main()


