# file_obj = open("sample.txt",'w')
# string = """Hi hello 
# this is rajkumar
# Todays topic is file handling"""
# file_obj.write(string)
# file_obj.close()

## opening a file in write mode
file_obj = open("sample.txt",'w')
strings_list = ["Welcome to file handling \n","This is write Operations\n"]
file_obj.writelines(strings_list)
file_obj.close()

## Opening a file in reading mode
# try:
#     file_obj = open("test.txt",'r')
#     data = file_obj.read()
    
# except Exception as e:
#     print(f"Something Wrong : {e}")

# else:
#     print(data)

## Opening file with using 'with' keyword
try:
    with open('sample.txt','r') as file:
        data = file.read()
    
except Exception as e:
    print(f"Something Wrong : {e}")

else:
    print(data)
