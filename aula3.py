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
#uniun eh uniao
frutas =set ([])
frutas.add ('maca')
frutas.add ('banana')
frutas.add ('uva')
frutas.add ('laranja')
frutas.add ('morango')
print (frutas)

#ou usa update para juntar mais de um de vez
////////////////////////////////////////////////////////
frutas = {'maca', 'banana' , 'uva', 'laranja' ,'morango'}

print ('banana' in frutas)
print (frutas.intersection({'banana'}))
//////////////////////////////////////////////////////////////
frutas_vermelhas = set([])

frutas_vermelhas.update({'morango' ,'cereja', 'framboesa'  })
print (frutas_vermelhas)
///////////////////////////////////////////////////////////
frutas_vermelhas = {'morango' ,'cereja', 'framboesa'  }


frutas_vermelhas.remove('cereja')
print (frutas_vermelhas)
//////////////////////////////////////////////
a = {1,3,5,7,9}
b = {2,4,6,8}

print (a.union(b))
/////////////////////////////////////////////////////
a = {1,3,5,7,9}
b = {4,5,6,7,8,9}

print (a.intersection(b))
//////////////////////////////////////////////////
a = [1,2,3,4,5]
b = [99,88,77,66,4]

resposta = set(a).union(b)
print(resposta)
/////////////////dicionario/////////////////////////
pessoa = {
    'nome': 'ane', 'cargo': 'aluno', 'escola' : 'infinity'
}
print (pessoa)
print(pessoa['nome'])
print(pessoa['escola'])
///////////////////JEITOS/////////////////////////////////////////
pessoa = {
    'nome': 'ane', 'cargo': 'aluno', 'escola' : 'infinity'
}

compras = dict ([('alimento', 'feijao'),('limpeza' , 'agua sanitaria'),
                 ('vesturario', 'meia')])
print (pessoa)
print(pessoa['nome'])
print(pessoa['escola'])
print (compras)
////////////////////////////////SO EXEMPLO///////////////////////////////////
alunos = {
    f'chave {num}' : f'valor {num}' for num in range (6)
    }

print (alunos)
////////////////////////////////////////////////////

pessoal = {
    'professor': 'xavier',
    'gerente' : 'maria',
    'monitor' : 'pedro'}

print (pessoal['gerente'])
print (pessoal.get('monitor'))
///////////////////////////////////////////////
pessoas1 = {
    'maria': 20,
    'pedro' : 15,
    'xavier' : 40
    }

print (pessoas1['maria'])
