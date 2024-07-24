import numpy as np
import timeit

# Generate two large arrays
size = 1000000
arr1 = np.random.rand(size)
arr2 = np.random.rand(size)

# Define the vectorized operation (element-wise multiplication)
def vectorized_operation():
    return arr1 * arr2

# Measure the execution time using timeit
execution_time = timeit.timeit(vectorized_operation, number=10)  # Run 10 iterations
average_time = execution_time / 10  # Calculate average time per operation

print("Average time taken for vectorized operation:", average_time, "seconds")
