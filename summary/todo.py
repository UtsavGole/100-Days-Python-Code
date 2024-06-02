def user_confirmation():
    userConfig=input('Do you have something to do Today (Y/N): ').lower()
    return userConfig

todos=[]

# Function to write on a txt file

def write_File(towrite):
   with open('summary/todos.txt','w') as writefile:
        for i in towrite:
            writefile.writelines(i)
        writefile.close()

#Function  to read txt file
        
def read_File():
    with open('summary/todos.txt','r') as readfile:
        todos=readfile.readlines()
        readfile.close()
    return todos


while True:
    user_input=input('Do you want to add, show or exit: ')

    if 'add' in user_input:
        read_File()

        todo=user_input[4:]+'\n'
        todos.append(todo)

        write_File(todos)

    elif 'show' in user_input:
        todos=read_File()

        for i,j in enumerate(todos):
            output=f"{i+1}.{j}"
            print(output.strip('\n'))

    elif 'edit' in user_input:

        todos=read_File()
            
        toedit=int(input('Enter the S.N of task to edit: '))-1

        new_task=input('Enter the name of edited task: ')+'\n'

        todos[toedit]=new_task

        write_File(todos)

    elif 'complete' in user_input:

        todos=read_File()

        tocomplete=user_input[9:]+'\n'
        todos.remove(tocomplete)

        write_File(todos)

    elif 'exit':
        break

    else:
        print("Wrong Command!!!!")

print('-------------------------------------')

print('Thank you !!!!!')