from leitura import read_csv_file

def hashtable(columns):
  hash_table = {}
  for row in columns:
      for col in row:
          hash_table[row[0]] = row[1]
  return hash_table
        
columns = read_csv_file()

result = hashtable(columns)

cidade = input("Digite o nome de uma cidade: ")

if cidade in result:
  print("O CEP da cidade de {} é do cep {}".format(cidade,result[cidade]))
else:
  print("Cidade não encontrada.")

# print(result['Caseara'])
# print(result['Cachoeirinha'])
# print(result['Frederico Westphalen'])
# print(result['Constantina'])

