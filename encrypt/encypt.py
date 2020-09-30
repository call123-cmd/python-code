def Encrypt(filename,key):
    file = open(filename,"rb")
    data = file.read()
    file.close()

    data =bytearray(data)
    for index,value in enumerate(data):
        data[index]= value ^ key

    file = open("CC-"+filename,"wb")
    file.write(data)
    file.close()


key = int(input("ask for a key between 1-255"))
filename = input("please enter a filename")

Encrypt(filename,key)