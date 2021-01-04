import numpy as np

'''
creating a virtual environment

python3 -m venv env
source env/bin/activate
'''

mylist = [4,2,5,2,6,7,3,6]
print(mylist)

#convert python list to numpy array
numpyarr = np.array(mylist)

print(numpyarr)

numparr2 = np.array([[1.2,2.2,3.3], [4.4,5.2,6.6], [7.2,8.5,9.3], [53.23,23.5,4.4]])
print(numparr2)

#total number of elements present
print(numparr2.size)

#checking the datatype
print(numparr2.dtype)

#returns the shape of the array eg. 2 X 4
print(numparr2.shape)

#returns the number of dimensions or the array e.g 2D, 3D, etc. 
print(numparr2.ndim)

#returns type of the object
print(type(numparr2))

#===================================================================================================
print("===========================================================================")

#Creating Basic NumPy Arrays

myarr = np.array([[5,3,5], [23,45,2], [6,68,875]])
print(myarr)

#arange() creates a series of continuous integers

myarr2 = np.arange(10) # from 0 to 9
# myarr2 = np.arange(1,11) #from 1 to 10
print(myarr2)

#creates n-dim array of zeros
myarr3 = np.zeros(10)
print(myarr3)

#creates n-dim array of ones
myarr4 = np.ones(4)
print(myarr4)

#linspace generates n values from a to be

myarr5 = np.linspace(start = 10, stop = 20, num = 4)
print(myarr5)

#===================================================================================================
print("===========================================================================")

#Array Methods and Array Shaping

arr1 = np.array([1,2,3,4,5])
print(arr1)

#adding an element
arr1 = np.append(arr1, 6)
print(arr1)

mylist = [43,5,23,65]
mylist = np.append(mylist, 345)
print(type(mylist))

#removing an element
print(mylist)
mylist = np.delete(mylist, 1)
print(mylist)

#sorting an array
mylist = np.sort(mylist)
print(mylist)

reshapearr = np.arange(24)
print(reshapearr)

reshapearr = np.reshape(reshapearr, (8,3))
print(reshapearr)

reshapearr = np.reshape(reshapearr, (12, 2))
print(reshapearr)

#===================================================================================================
print("===========================================================================")
print("Indexing and Slicing")
print('--------------------')

#Indexing and Slicing

#positive indexing
iarr = np.array([5,2,7,34,8,5,3,76])
print(iarr)
print(iarr[4])

iarr = np.reshape(iarr, (4,2))
print(iarr)
#indexing a matrix
print(iarr[3,1])

#slicing while indexing
print(iarr[1:4, 1])

#can also try negative indexing.

#striding is jumping over values eg. every 2nd element while indexing --> [2:8:2]

myarrp = np.arange(25)
myarrp = np.reshape(myarrp, (5,5))
print(myarrp)

print(myarrp[::3, ::2])

