def linear_congruential_method(seed, n):
  a = 150
  b = 777
  m = 2048

  number_series = []
  x = seed
  for _ in range(n):
    x = (a * x + b) % m
    number_series.append(x / m)
  
  return number_series

def print_result(number_series):
  print("\n".join(map(str, number_series)))
  print("\n")

n = 10

print_result(linear_congruential_method(42, n))

print_result(linear_congruential_method(26, n))

print_result(linear_congruential_method(1356, n))