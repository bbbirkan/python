import timeit

# Ölçülecek kod bloğu
code_to_test = """
for i in range(9000):
  x = i * i
"""

# Performans testini yap
time = timeit.timeit(code_to_test, number=1000)

# Sonuçları ekrana yaz
print(f"Test sonucu: {time} saniye")