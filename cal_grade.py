#input of marks
m1 = int(input("first marks"))
m2 = int(input("second marks"))
m3 = int(input("third marks"))
m4 = int(input("fouth marks"))

#grade calculation
total = m1+m2+m3+m4
avg =total/4
print(avg)

#condition pass or fail
if (avg>=50):
    print("pass")
else:
    print("fail")
    