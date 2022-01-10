#write pgm for each conversion

#list to tuple
#list to set
#list to dict   
#tuple to list
#tuple to set
#tuple to dict
#set to list
#set to tuple
#set to dict

#list to tuple
a=[1,2,"python",4,5,6,5]
b=tuple(a)
print(b)

#list to set
a=[1,2,"python",4,5,6,5]
#print(a)
b=set(a)
print(b)

#list to dict
a=[1,2,3,4]
b=['python',10,100,200]
c=dict(zip(a, b))
print(c)

#tuple to list
a=(1,2,"python",4,5,6,5)
#print(a)
b=list(a)
print(b)

#tuple to set
a=(1,2,"python",4,5,6,5)
b=set(a)
print(b)

#tuple to dict
a=(1,2,"python",4,5,6,5)
b=('python',10,100,200)
c=dict(zip(a,b))
print(c)

#set to list
a={1,2,"python",4,5,6,5}
b=list(a)
print(b)

#set to tuple
a={1,2,"python",4,5,6,5}
b=tuple(a)
print(a)

#set to dict
a={1,2,"python",4,5,6,5}
b={'python',10,100,200}
c=dict(zip(a,b))
print(c)





