dic = {
    'Parth' : 80
}

name = input("Enter the student's name: ")

if name in  dic:
    print(f"{name} marks: {dic[name]}")
else:
    print("Student not found.")    