# 1.Make function to find simple interset Use (keyword argument , postional argument , deafult argument)
  #def SI(p,r=5,t):  def SI(r=5,p, t):  this both are wrong
#because You must place all required (non-default) parameters before the default ones.
def SI(p,t,r=5):
    return p * r * t
print("Simple Interest for P=100, T=1 year, default R=5% is:", SI(100, 1)) #Postoinal argument
print("Simple Interest for P=100, T=1 year, R=10% is:", SI(100, 1, 10)) 
print("Simple Interest for P=100, T=7 years, default R=5% is:", SI(p=100, t=7)) #Keyword argument
print("Simple Interest for P=100, T=7 years (keyword arguments in different order), default R=5% is:", SI(t=7, p=100)) 

# 2.Variable-Length Arguments

def total(*numbers):
    print(f"sum of {len(numbers)} numbers is {sum(numbers)}")
total(1, 2, 3, 4) 
total(1, 2, 3, 4,5)
total(1,2,3,4,5,6,7,8,9,10)

# 3.Type Hints to argument

def add(a: int, b: int) -> int:
    return a + b
print(add(10,5))

#  4.**kwargs (Dictionary of keyword arguments)

def show_details(**person):
    for key, value in person.items():
        print(key, ":", value)

show_details(name="Rohan", age=21)
show_details(name="Krishna", age=18)

# 5.Anonymous Function (Lambda) 
SI = lambda p,r,t: p*r*t
print(SI(100,5,1)) 