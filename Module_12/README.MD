###### Old task ###############
import numpy as np 

#task 1 
data = np.arange(10,51,2)
print(data)
#Bonus 
data = np.linspace(0,1,20)
print(data)

#task 2 
data = np.random.randint(1,100,25)
data = data.reshape(5,5)
# yaha 2 matrix kaha hai jinka dot kru??
print(data)

#task 3
data = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
print(np.sin(data))
print(np.cos(data))

#task 4
data = np.arange(0,24)
data = data.reshape(2,3,4)
print(data.ndim)

#task 5
data = np.random.randint(1,10,20)
print(data)
print(np.unique(data))
print(np.where(data%2==0,0,data))

########### new Task #################
#Task 1 
data = np.random.randint(1,6,6).reshape(3,2)
print(data)
Tdata = data.T 
print(Tdata)
print(data @ Tdata)

#Task 2
data = np.random.randint(1,100,16).reshape(4,4)
print(data)
print(np.sum(data,axis=1))

#Task 3
data = np.random.randint(10,50,15)
print(data)
print(np.where(data>30,100,data))
print(np.argmax(data))

#Task 4 
m1 = np.random.randint(1,100,4).reshape(2,2)
m2 = np.random.randint(1,100,4).reshape(2,2)
print(np.vstack((m1,m2)))
print(np.hstack((m1,m2)))

#Task 5
data = np.random.randint(1,100,9).reshape(3,3)
print(np.std(data))
print(data.flatten())
print(np.eye(10)*10)


