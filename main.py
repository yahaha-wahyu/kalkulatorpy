import random

angka_random = random.randint(1, 10)
tebak=0

while tebak != angka_random:
    tebak = int(input("tebak angka antara 1 sampai 10: "))
    if tebak < angka_random:
        print("coba lagi, angka terlalu rendah!")
    elif tebak > angka_random:
        print("coba lagi, angka terlalu tinggi!")
print(f"selamat, anda berhasil menebak angka {angka_random} dengan benar!")