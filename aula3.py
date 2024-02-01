///////////////////ex/////////////////
conjunto = {'maça','laranja', 'melancia', 'caju' }
print(conjunto)

////////////////////exemplo/////////////////////////
conjunto = {letra for letra in 'Infinity' }
lista = []
for letra in 'Infinity':
    lista.append(letra)
    
print(conjunto)
/////////////////////////////////////////
conjunto = {letra for letra in 'Infinity' }
print(conjunto)
////////////////////////////////////
conjunto = {letra for letra in 'Infinity' if letra not in 'aeiou' }
    
print(conjunto)
//////////////////////////////////////////////////
conjunto = {letra for letra in 'Infinity' if letra not in 'aeiou' }

cores = set(['azul', 'verde', 'amarelo'])

print(conjunto)
print(cores)
///////////////////////////////////////////////

cores1 = {'azul', 'verde', 'amarelo'}
cores2 = {'vermelho', 'roxo', 'amarelo', 'verde', 'amarelo', 'salmao'}

#inter = cores1.intersecton(cores2)
cores1.intersection_update(cores2)

print(cores1)
print(cores2)
#print (inter)
//////////////////////////////////////////////
# essa barrinha | significa ou
