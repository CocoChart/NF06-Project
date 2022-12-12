import ctypes

_sum = ctypes.CDLL("../tests.dll")

final = 0  
final2 = ctypes.c_int(final)
nombre1 = 5
nombre2 = 4
#ctypes.c_int(variable) permet de créer un entier 
#_sum.sum(nombre1,nombre2, ctypes.pointer(final2)) ##ctypes.pointer(final2) permet de récupérer l'adresse de final2 ; correspond au & en C
#print("final :", final2.value )

'''
final = [0,0]
id_final = id(final)
hex_final = hex(id(final))
##p= create_string_buffer(3)
print("id_final", id_final, hex_final)
final = _sum.sum(nombre1,nombre2, tab)
'''

liste = [1,2,3,4]
array = ctypes.c_int * 4
listeparam = ctypes.c_int(1) #array(*liste)
_sum.liste(ctypes.pointer(listeparam))    
#print(listeparam)

