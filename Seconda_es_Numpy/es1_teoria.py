import numpy as np

data1 = [1, 3, 5, 7, 9, 11]
data1
arr1 = np.array(data1) # array([ 1,  3,  5,  7,  9, 11])
arr1.ndim # 1 dimensione
arr1.shape # (6,) 1 dimensione, 6 elementi
arr1.dtype # dtype('int64')

arr = np.empty((10, 6)) # 10 righe, 6 colonne (10*6 = 60)

for i in range(10):
    arr[i] = i

arr

arr[[2,1,4]]

arr.reshape((5,12)) # 5 righe, 12 colonne (5*12 = 60)

arr.reshape((-1,15)) # -1 indica che numpy deve calcolare il numero di righe

arr.reshape((3,2,10)) # 3 matrici, 2 righe, 10 colonne (3*2*10 = 60)


x = np.array([[2, 4, 6], [6, 8, 10]], np.int32) 
y= x.astype(float) # converte il tipo di dato degli elementi di x in float
#y=array([[ 2.,  4.,  6.],
#      [ 6.,  8., 10.]])



x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

np.concatenate([x,y]) # array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
np.concatenate([x,y],axis=1)    # The axis along which the arrays will be joined. If axis is None, arrays are flattened before use. Default is 0.
# ValueError: axis 1 is out of bounds for array of dimension 1
# Devo fare un reshape
x = x.reshape(1,-1)
y = y.reshape(1,-1)

c=np.concatenate([x,y],axis=1) # array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]])
# la dimensione dell'array c sarà di 2
c.ndim # 2




#+    np.add    Addition (e.g., 1 + 1 = 2)
# -    np.subtract    Subtraction (e.g., 3 - 2 = 1)
# -    np.negative    Unary negation (e.g., -2)
# *    np.multiply    Multiplication (e.g., 2 * 3 = 6)
# /    np.divide    Division (e.g., 3 / 2 = 1.5)
# //    np.floor_divide    Floor division (e.g., 3 // 2 = 1)
# **    np.power    Exponentiation (e.g., 2 ** 3 = 8)
# %    np.mod    Modulus/remainder (e.g., 9 % 4 = 1)

# sin, cos, tan: compute sine, cosine and tangent of angles
# arcsin, arccos, arctan: calculate inverse sine, cosine and tangent
# hypot: calculate hypotenuse of given right triangle
# sinh, cosh, tanh: compute hyperbolic sine, cosine and tangent
# arcsinh, arccosh, arctanh: compute inverse hyperbolic sine, cosine and tangent
# deg2rad: convert degree into radians
# rad2deg: convert radians into degree

a = np.arange(1,11) # array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
np.where(a>5,0,10) # array([10, 10, 10, 10, 10,  0,  0,  0,  0,  0])

bools = np.array([True,True,False,False,True])
bools.any() # True (almeno un True)
bools.all() # False (quindi non tutti True)
bools[:2].all() # True (tutti True)

arrsort = np.random.randn(4,3)
arrsort.sort(0)    # righe ordinate
arrsort.sort(1)    # colonne ordinate

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names) # array(['Bob', 'Joe', 'Will'], dtype='<U4') stampa i valori unici 
# e li ordina in ordine alfabetico (in questo caso) 
#dtype='<U4' indica che il tipo di dato è Unicode di 4 caratteri

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#estraiamo tutti i numeri dispari da arr
arr[arr % 2 == 1] # array([1, 3, 5, 7, 9])