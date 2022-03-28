def garis():
    print("------------------------------")


def sort_asc(array):
    array = sorted(array)
    return(array)


def sort_dsc(array):
   array = sorted(array, reverse = True)
   return(array)


def rata_rata(angka):
   return sum(angka) / len(angka)



garis()
print("Masukan tiga buah nilai")
nilai_a =  int(input("Nilai A : "))
nilai_b =  int(input("Nilai B : "))
nilai_c =  int(input("Nilai C : "))
angka = [nilai_a, nilai_b, nilai_c,]
garis()


print("HASIL AKHIR")
print("Urutan Nilai Ascending : ",(sort_asc(angka)))
print("Urutan Nilai Descending : ",(sort_dsc(angka)))


print("Nilai MAX :", max(angka))


print("Nilai MIN :", min(angka))


print("NILAI RATA RATA :", round(rata_rata(angka)))

print()






