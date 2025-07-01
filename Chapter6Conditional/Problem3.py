"""WAP to find out whether  a student is pass
or fail.if it require total 40% and atleast 33% 
in each subject to pass .Assume 3 subject and 
take marks as an input from user 
 """
list=[]

for i in range(3):
    while True:
        marks = int(input(f"Enter the marks of subject {i+1} : "))
        if 0 <= marks <= 100:
            list.append(marks)
            break
        else:
            print("❌ Invalid input. Marks should be between 0 and 100.")


min_marks=all(m>=33 for m in list)
total=sum(list)
pre=(total/300)*100

if(min_marks and pre>=40):
   print("Pass")
else:
    print("Fail")   
        
  