
try:
    print("Reading the file content:")


    file = open('sample.txt','r')
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    
    print(f"Line 1: {first_line}")
    print(f"Line 2: {second_line}")
    file.close()
    
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found")    
    