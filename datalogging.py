import datetime
#from datetime import date
#from datetime import datetime
now = str(datetime.date.today())
extension = ".txt"
filename = now + extension
f = open(filename,'w+')
f = open(filename,"a")
lst = []
z=1
while z==1:
    name = input('Name:')
# dft - done for today    
    if name == 'dft':
        f.close()
        exit()
    else:
        phone = input('Ph. no. :')
        place = input('Place:')
        temp = input('Body Temp')
        time = str(datetime.datetime.now())
        lst.append(name)
        lst.append(phone)
        lst.append(place)
        lst.append(temp)
        lst.append(time)
        f.write(str(lst)+'\n')
        lst.clear()
      
        
    
