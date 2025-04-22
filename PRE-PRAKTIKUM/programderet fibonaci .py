# Program Python untuk deret Fibonacci klasik
jumlah = int(input("Masukkan jumlah deret Fibonacci: "))

a, b = 1, 1
fibonacci = []

for _ in range(jumlah):
    fibonacci.append(a)
    a, b = b, a + b

print("Output:", ",".join(map(str, fibonacci)))