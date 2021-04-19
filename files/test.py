f=open("test.txt",'w')
f.write("hello world\n")
f.write("Hii how are you\n")
f.write("My name is ravi")
f.close()

f=open("test.txt",'a')
f.write("\nhgfhghdzf")
f.close()

f=open("test.txt",'r')
print(f.read())
f.close()
 
# print(f.readable())
# f.close()

f=open("myfile.txt",'a')
f.write("hfdhfhd\n")
f.write("hfueiei")
f.close()

with open("rk.txt","w")as f:
    f.write("hello ravi")


