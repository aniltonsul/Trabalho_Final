from leitura import read_csv_file

def jump_search(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        
        if prev >= n:
            return -1
    
    while arr[prev] < x:
        prev += 1
        
        if prev == min(step, n):
            return -1
    
    if arr[prev] == x:
        return prev
    
    return -1

def hashtable(columns):
    hash_table = {}
    for row in columns:
        for col in row:
            hash_table[row[0]] = row[1]
    return hash_table

columns = read_csv_file()

result = hashtable(columns)

cidade = input("Digite o nome de uma cidade: ")

encontrado = False
for key, value in result.items():
    if key.lower() == cidade.lower():
        print("O CEP da cidade de {} é {}".format(key, value))
        encontrado = True
        break

if not encontrado:
    print("Cidade não encontrada.")