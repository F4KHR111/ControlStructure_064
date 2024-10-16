#3 Write a PYTHON program to print Fibonacci series up to n!
# menampilkan pesan "Masukkan nilai n: " di layar dan menunggu pengguna untuk memasukkan nilai
n = int(input("Masukkan nilai n: "))

a, b = 0, 1 # dua variabel, a dan b, diberikan nilai secara bersamaan dalam satu baris kode.
hasil = [] # Baris ini mendeklarasikan sebuah list kosong bernama hasil
9
for i in range(n): # Baris ini  mengulang suatu blok kode beberapa kali, dengan i sebagai variabel iterasi yang nilainya akan berubah setiap kali loop dijalankan.
    hasil.append(a)
    a, b = b, a + b

#untuk menampilkan string "Deret Fibonacci hingga", diikuti oleh nilai n,dan list hasil yang berisi angka-angka.
print("Deret Fibonacci hingga", n, ":", hasil)