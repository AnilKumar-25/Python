lis=['Rocky','Surya','Rolex','Vikram']
print('------------------------------------------------------------\n')
print('    ***** WELLCOME TO STUDENT MANAGEMENT SYSTEM *****\n')
print('------------------------------------------------------------')
while True:
    print('\nPlease choose any one option:')
    print('1.To view students list')
    print('2.To add new student')
    print('3.To remove student')
    print('4.To search student')
    print('5.To exit\n')
    num=int(input('Enter your choice:'))
    if num==1:
        for i in range(len(lis)):
            print(lis[i])
    elif num==2:
        new=input('Enter new name:')
        lis.append(new)
    elif num==3:
        r=input('Enter name:')
        if r in lis:
            lis.remove(r)
            print('Student has been removed')
        else:
            print('Name not found')
    elif num==4:
        f=input('Enter name to search:')
        if f in lis:
            print('Name found..')
        else:
            print('Nmae not found..')
    elif num==5:
        exit()
    else:
        print('Wrong input')
    c=input('\nDo you want to continue(y/n):')
    print('_____________________________')
    if c=='y' or c=='Y':
        continue
    elif c=='n' or c=='N':
        break
    else:
        print('Wrong output')
        









