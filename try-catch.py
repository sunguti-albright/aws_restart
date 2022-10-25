try:
    f=open('diary3.txt')
except:
    print("This file is not there")
else:
    print(f.read())
    f.close()