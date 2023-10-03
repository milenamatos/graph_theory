import matplotlib.pyplot as plt

def find_dividers(num):
  dividers = []
  for i in range(1, num + 1):
    if num % i == 0:
      dividers.append(i)

  return dividers

numbers = list(range(1, 501))
results = [None] * 500

for num in numbers:
  num_list = find_dividers(num)
  results[num-1] = len(num_list)
  print(f"Divisores de {num}: {num_list}")

plt.bar(numbers, results)
plt.xlabel('Número')
plt.ylabel('Quantidade de divisores')
plt.title('Número de Divisores de 1 a 500')
plt.show()