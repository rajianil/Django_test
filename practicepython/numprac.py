import numpy as np
digits = np.array([
 [1, 2, 3],
 [4, 5, 6],
  [6, 7, 9]])
print(type(digits))

grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])
print(grades.mean())

temperatures = np.array([
29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
12.6, 49.9, 38.6, 31.3, 9.2, 22.2
]).reshape(2, 2, 3)

print(temperatures)
