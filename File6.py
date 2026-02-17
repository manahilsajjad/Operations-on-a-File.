File1=open("Text1.txt","r")
File2=open("Text2.txt","w")
for line in File1.readlines():
   
    if not line.startswith("File"):
        print(line)
        File2.write(line)

File1.close()
File2.close()
                           