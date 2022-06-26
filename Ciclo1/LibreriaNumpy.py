
import numpy as np
import pandas as pd

#arreglos con numpy
arr = np.array([1,2,3])
arrayListas = np.array([(1,2,3),(4,5,6)])

print("dimension del array arr {} ".format(arr.ndim))
print("dimension del array arraylistas {} ".format(arrayListas.ndim))
print("forma del array arr {} ".format(arr.shape))
print("forma del array arraylistas {} ".format(arrayListas.shape))
print("tamaño del array arr {} ".format(arr.size))
print("tamaño del array arraylistas {} ".format(arrayListas.size))
print("tipo del array arr {} ".format(arr.dtype))
print("tipo del array arraylistas {} ".format(arrayListas.dtype))
print("tamaño de items del array arr {} ".format(arr.itemsize))
print("tamaño de items del array arraylistas {} ".format(arrayListas.itemsize))


#pandas