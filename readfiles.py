print("Here is my diary: \n")

f1=open('diary.txt', 'r')
print(f1.read())
f1.close()

print("We're writing to the diary!! \n")
f2=open('diary2.txt', 'w')
f2.write("~Bohemian Rhaphsody - Queen")
f2.close()

