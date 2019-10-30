PI = 3.14
SIGMA = 15
EXP = 2.72
DIM = 50

gauss_mat = [[0 for j in range(-DIM,DIM+1)] for i in range(-DIM,DIM+1)]
# print(gauss_mat)

def get_mat():
    for i in range(-DIM,DIM+1):
        for j in range(-DIM,DIM+1):
            gauss_mat[i][j] += int(1 / (2*PI*SIGMA**2) * EXP ** (-(i**2 + j**2) / (2*SIGMA**2)) * 50000)

    return gauss_mat

# for i in range(-DIM,DIM+1):
#     for j in range(-DIM,DIM+1):
#         gauss_mat[i][j] += int(1 / (2*PI*SIGMA**2) * EXP ** (-(i**2 + j**2) / (2*SIGMA**2)) * 50000)

# print(gauss_mat)
