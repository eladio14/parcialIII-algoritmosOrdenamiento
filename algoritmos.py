#MERGE SORT
"""
La función merge_sort recibe una lista arr. Si la longitud de la lista es menor o igual a 1, simplemente devuelve la lista ya que está ordenada.
De lo contrario, encuentra el punto medio mid de la lista y crea dos sublistas: left con los elementos antes del medio y right con los elementos desde el medio hasta el final.
Luego llama recursivamente a merge_sort en ambas sublistas y las fusiona utilizando la función merge.
La función merge toma dos listas ordenadas left y right, y las combina en una nueva lista ordenada.
"""
def merge_sort(arr):
    if len(arr) <=  1:
        return arr
    mid = len(arr) //  2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index =  0
    right_index =  0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index +=  1
        else:
            merged.append(right[right_index])
            right_index +=  1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

#QUICK SORT
"""
La función quick_sort toma una lista arr junto con índices low y high. Si la longitud de la lista es 1, ya está ordenada y la devuelve.
Si low es menor que high, realiza una partición usando la función partition, que organiza los elementos alrededor de un pivote y devuelve su posición.
Luego, quick_sort se llama recursivamente en las dos subpartes de la lista (antes y después del pivote).
"""
def partition(arr, low, high):
    i = (low -  1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i +  1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i +  1)

def quick_sort(arr, low, high):
    if len(arr) ==  1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


#HEAP SORT
""" 
La función heapify se utiliza para convertir una sublista de arr en un montículo máximo, comenzando desde el índice i.
La función heapSort construye un montículo a partir de toda la lista y luego extrae el elemento más grande (raíz del montículo) repetidamente, colocándolo al final de la lista y reconstruyendo el montículo sin ese elemento.
 """
def heapify(arr, n, i):
    largest = i
    _l =  2 * i +  1
    r =  2 * i +  2

    if _l < n and arr[i] < arr[_l]:
        largest = _l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n //  2 -  1, -1, -1):
        heapify(arr, n, i)

    for i in range(n -  1,  0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i,  0)

#SHELL SORT
"""
La función shell_sort toma una lista lista y aplica el algoritmo de ordenamiento de shell, que mejora el ordenamiento de inserción al permitir el intercambio de elementos que están lejos el uno del otro.
Comienza con un "hueco" inicial que se reduce a medida que el algoritmo progresa.
Para cada hueco, compara el elemento actual con el elemento que está a distancia del hueco y si es menor, los intercambia.
Este proceso continúa hasta que el hueco llega a 1, momento en el cual la lista estará ordenada.
"""

def shell_sort(lista):
  
  gap = len(lista) // 2

  while gap > 0:

    for i in range(gap, len(lista)):
      valor_actual = lista[i]
      j = i
      while j >= gap and lista[j - gap] > valor_actual:
        lista[j] = lista[j - gap]
        j -= gap
      lista[j] = valor_actual
    
    gap //= 2

  return lista
