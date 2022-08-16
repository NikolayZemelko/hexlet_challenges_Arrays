def reverse_matrix(matrix):  
  return list(zip(*matrix))

def lane_multiply(lane_a, lane_b):
  return sum(map(lambda x, y: x * y, lane_a, lane_b))

def multiply(a, b):
  
  matrix_b = reverse_matrix(b)[:]
  matrix_a = a[:]
  result = []

  for index_a, x in enumerate(matrix_a):
    result.append([])
    for y in matrix_b:
      result[index_a].append(lane_multiply(x, y))

  return result
