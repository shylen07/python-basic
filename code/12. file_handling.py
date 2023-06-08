# Title: File Handling
# Created by Devender Singh

with open('file.txt', 'w') as f:
    f.write("Hello, file!")

with open('file.txt', 'r') as f:
    content = f.read()
    print("File Content:", content)
