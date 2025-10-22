import numpy as np

arr = np.array(20)
print("\n",arr)
print(type(arr))
print("Shape:", arr.shape)      
print("Size:", arr.size)          
print("Data Type:", arr.dtype) 
print("Dim",arr.ndim)

arr = np.array([1, 2, 3])
print("\n",arr)
print(type(arr))
print("Shape:", arr.shape)      
print("Size:", arr.size)          
print("Data Type:", arr.dtype) 
print("Dim",arr.ndim)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\n",arr)
print(type(arr))
print("Shape:", arr.shape)      
print("Size:", arr.size)          
print("Data Type:", arr.dtype) 
print("Dim",arr.ndim)

arr = np.array([[[1, 2, 3], [4, 5, 6],[1, 2, 3]]])
print("\n",arr)
print(type(arr))
print("Shape:", arr.shape)      
print("Size:", arr.size)          
print("Data Type:", arr.dtype) 
print("Dim",arr.ndim)

arr = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [1, 2, 3]],
     [[1, 2, 3],
     [4, 5, 6],
     [1, 2, 3]]
    ])
print("Shape:", arr.shape)      
