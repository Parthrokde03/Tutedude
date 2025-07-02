try:
    write = input("Enter text to write to the file: ")

    wfile = open('output.txt','w')
    file_write = wfile.write(write + "\n")
    print("Data successfully witten to output.txt.\n")
    wfile.close()

    additional = input("Enter additional text to write append: ")

    afile = open('output.txt', 'a')
    file_append = afile.write(additional)
    print("Data successfully appended.\n")
    afile.close()

    print("Final content of output.txt:")
    rfile = open('output.txt' , 'r')
    file_read1 = rfile.readline().strip()
    file_read2 = rfile.readline().strip()
    print(file_read1)
    print(file_read2)
    rfile.close()
    
except FileNotFoundError:
    print("Error: File not found.")