# def arbitrary(x,y,z,a,b):                        #key word arguement
#     print("it is a",a)
# arbitrary(x="book",y="pen",z="notebook",a="colourpen",b="its") 

# def arbitrary(*x):     #arbitrary arguements
#     print(x)
# arbitrary(2,4,6,8,12) 

# def arbitrary_arg(x):
#     print("it is a",x)
# arbitrary_arg(x="book")   #key word arguement

#arbitrary key word arguements()
# def arbitrary(**x):
#     print(x["name"])
# arbitrary(name="anu",age=60)   

#default arguements
# def default_parameter(x="krishna"):
#     print("my name is",x)
# default_parameter("gopika")    

# default_parameter()

# def arbitrary(x,y):
#     pass
#     print(10+6)

# def x(*x):
#     print(sum(x))
# x(1,2,3,4,5,6)
# def odd_no(*x):
#     # n=0
#     for i in x:
#         if i%2!=0:
#             print(i)
# # y=int(input("no."))
# odd_no(1,3,7,8,4)   
# def x(*y):
#     s=0
#     for i in y:
#         s=s+i
#     print(s)
# x(1,2,3,4,5,6)
# x(1,2)

# def x(**y):
#    print(y["a"])
# x(a=1,b=60)

# def x(*y):
#     for i in y:
#         if i%2==0:
#            print(i)
# x(1,2,3,4,6,8)
# def x(*y):
#     for i in y:
#         print(i)
# x("and","or","was")   
# def x(**y):
#     print(y["age"])
# x(name="anu",age=90)
# def x(*y,**z):
#     print(y)
#     print(z)
# x(1,2,3,age=40,aadhar=123456)
# def default(x=90):
#     print(x)
# default("b")
# default("c")
# default("a")  
# default(2) 
# default()    
    