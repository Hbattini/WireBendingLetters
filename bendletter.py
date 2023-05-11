import os

def appendfiles(file_arr):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'alphabets')
    os.chdir(filepath)
    if all([os.path.isfile(f+".txt") for f in file_arr]):
        print("all the files exist in the path")
        print(file_arr)
        with open(os.path.join(dirname,"wordbend.diw"), "a") as write_file_ptr:
            for file in file_arr:
            #file_ptr = open(file+".txt", "r")
                print(file)
                with open(file.upper()+".txt", 'r') as file_ptr:
                    write_file_ptr.write(file_ptr.read())
                    write_file_ptr.write('\n')
                    print(file+" is written to the main file")
    else:
        print("all the files do not exist in the directory")



    
user_input=input('Enter a string: ')

if(user_input.isalpha()):
    char_arr=list(user_input[::-1])
    appendfiles(char_arr)
        
else:
    print('please enter strings with alphabets. Do not include numbers of special characters')



