unitslength = ['m', 'dm', 'cm', 'mm']

#Getting the number to convert

while True:
    num = float(input("Enter a number to convert (x,0 for int | x,y for float): "))
    break
#Types
uf = input("Unit from (m, dm, cm, mm): ")

#Main calculation here        

if uf == unitslength[0]:
    m = num 
    dm = num * 10
    cm = num * 100
    mm = num * 1000
if uf == unitslength[1]:
    m = num / 10
    dm = num
    cm = num * 10
    mm = num * 100
if uf == unitslength[2]:
    m = num / 100
    dm = num / 10
    cm = num
    mm = num * 10
if uf == unitslength[3]:
    m = num / 1000
    dm = num / 100
    cm = num / 10
    mm = num

#Display the conversion results
print('''Results:
''' + str(num) + ' ' + str(uf) + '''
- ''' + str(m) + ' ' + str(uf) + '''
- ''' + str(dm) + ' ' + str(uf) + '''
- ''' + str(cm) + ' ' + str(uf) + '''
- ''' + str(mm) + ' ' + str(uf))
