import os.path
file = open
    
if os.path.isfile('y.txt'):
    print('nice.')
    file = open('y.txt' , 'a')
    file.write('took u long enough :/')
    file.close()

else:
    print('HELP')
    file = open('y.txt' , 'w')
    file.write('failed :/')
    file.close()
