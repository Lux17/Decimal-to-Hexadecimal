# menampilkan teks
print("\n======= Aplikasi Konversi Bilangan Desimal ke Bilangan Hexadecimal =====")
#menginput angka desimal
desimal=int(input("\nMasukan Angka Desimal: "))
# menampilkan bilangan desimal
print("\nBilangan Desimal :"+str(desimal))
#menampilkan angka hexa merubah desimal ke hexa dan menghilangkan "0x	"
print ("Bilangan Hexadecimal Dari " + str(desimal) +
        " Adalah : " + hex(desimal).lstrip("0x").rstrip("L"))

# Nama : Lucky saputra
# Nim : 200511086
