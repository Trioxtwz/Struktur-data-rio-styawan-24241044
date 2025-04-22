jumlah_deret = int(input("Masukkan jumlah deret: "))
bilangan_genap = []
for i in range(1, jumlah_deret + 1):
    bilangan_genap.append(i * 2)
print("Output:", ",".join(map(str, bilangan_genap)))