''' EJERCI8CIO 1 '''
'''A'''
b= [4 , 'palabra' , [0 , 1] , 9.6 , False]

verificar= [9.6 , 0 , False , [0,1] , 4.0 , 'p']

for i in b:
    if i in verificar:
        print(i, 'pertenece a su lista')
    else:
        print(i, 'no pertenece a su lista')

'''B'''
for i in b: 
    if i == [0,1]:
        print(b.index(i))