fileName = "file.txt"
accessMode = "w"
myFile = open(fileName, accessMode)
myFile.write("Opens a file for reading only in binary.\n")
myFile.write("The file pointer is placed.\n")
myFile.write("This is the default mode")

try:
    name = input("파일 이름을 입력하세요 : ")+".txt"
    accessMode = "r"
    myFile=open(name, accessMode)
    line = myFile.readline()
    c = 0
    while line != "" :
        c += 1
        print(f"{c}: {line}")
        line = myFile.readline()
except :
    print("파일 이름이 잘못되었습니다.")
    myFile.close()