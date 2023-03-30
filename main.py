from arbol import arbol_binario, arbol_nario

def buscar(arbol, elemento_buscado):
    '''
    Función que retorna True si el elemento está en el árbol, False de lo contrario
    '''
    if arbol.elemento is None:
        return False
    elif arbol.elemento == elemento_buscado:
        return True
    else:
        for hijo in arbol.hijos:
            if buscar(hijo, elemento_buscado) is True:
                return True
        return False



def contar_elementos(arbol):
    '''
    Función que cuenta el número de elementos en el árbol
    '''
    if arbol.elemento is None:
        return 0
    else:
        contador=1
        for hijo in arbol.hijos:
            contador+=contar_elementos(hijo)
            
        return contador
            

def altura(arbol):
    '''
    Función que calcula la altura del árbol
    '''
    arcos=[]
    
    if arbol.hijos == []:
        return 0
    else:
        for hijo in arbol.hijos:
            arcos.append(altura(hijo))
            
    return max(arcos) + 1

if __name__=='__main__':
    arbol = arbol_nario()
    arbol.agregar_elemento(None, 1)
    arbol.agregar_elemento(1,2)
    arbol.agregar_elemento(1,3)
    arbol.agregar_elemento(1,4)
    
    arbol.agregar_elemento(2,5)
    arbol.agregar_elemento(2,6)
    
    arbol.agregar_elemento(5,11)
    
    arbol.agregar_elemento(3,7)
    arbol.agregar_elemento(3,8)
    arbol.agregar_elemento(3,9)
    
    arbol.agregar_elemento(4,10)
    print(arbol)
    
    print(altura(arbol))
    
    


