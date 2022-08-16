def rotate_to_90deg_ccw(matrix):

    matrix_t = list(zip(*matrix[::-1]))
    matrix_t2 = list(zip(*matrix_t[::-1]))
    matrix_t3 = list(zip(*matrix_t2[::-1]))
    return matrix_t3


def snail_path(matrix):
    matrix_path = []

    while matrix:
        matrix_path.extend(matrix[0])
        matrix.pop(0)
        matrix = rotate_to_90deg_ccw(matrix)

    return matrix_path
