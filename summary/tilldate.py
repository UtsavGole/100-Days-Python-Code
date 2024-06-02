def user_confirmation():
    userConfig=input('Do you have something to do Today (Y/N): ')
    return userConfig



todos=[]

while user_confirmation() == 'yes':
    todo=input('Please add your task for a DAY: ')
    todos.append(todo)
    file=open('test.txt','w')
    file.writelines(todos)
    file.close()

fileread=open('test.txt','r')
print(fileread.readlines())
   

print('Thank you')
print(todos)


abcd='add apple'
print(abcd[3:])


