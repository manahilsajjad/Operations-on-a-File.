file=open("Text1.txt","r")
print(file.read())
file.close()

file=open("Text1.txt","r")
print(file.read(9))
file.close()
file=open("Text1.txt","a")
file.write("\n Hi i am Manhil Sajjad")
file.close()

