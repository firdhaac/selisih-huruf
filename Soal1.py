print("==========Program Selisih Antar Huruf==========")

Jumlah_Kata = int(input("Masukkan Jumlah Kata: "))
a = 1 
b = []

while a <= Jumlah_Kata:
    c = input(f"Masukkan Kata {a}: ")
    b.append(c)
    a += 1
    
for d in b:
    print("Hasil: ")
    for i in range(len(d)):
        if i == len(d)-1:
            break
        else :
            Selisih_Huruf = (ord(d[i]) - ord(d[i+1]))
            
            if ord(d[i]) < ord(d[i+1]):
                print(d[i], "Kurang dari", d[i+1], "Selisihnya adalah", abs(Selisih_Huruf))
            else:
                print(d[i], "Lebih dari", d[i+1], "Selisihnya adalah", abs(Selisih_Huruf))