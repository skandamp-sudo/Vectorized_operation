import numpy as np
import timeit


size = 1000000
arr1 = np.random.rand(size)
arr2 = np.random.rand(size)

def vectorized_operation():
    return arr1 * arr2


execution_time = timeit.timeit(vectorized_operation, number=10) 
average_time = execution_time / 10 

print("Average time taken for vectorized operation:", average_time, "seconds")
