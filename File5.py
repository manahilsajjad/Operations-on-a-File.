file_read=open("Text1.txt","r")
print(file_read.read())
file_read.close()


file_write=open("Text1.txt","w")
file_write.write("File in write mode..")
file_write.write("\n Whats your name?")
file_write.close()

file_append=open("Text1.txt","a")
file_append.write("\n File in append mode.")
file_append.close()
