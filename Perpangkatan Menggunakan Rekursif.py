print("===== Perpangkatan Menggunakan Rekursif =====")

def Perpangkatan():
    print("\nIni merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    nilai = input("Masukkan Angka = ")
    
    if(nilai == ''):

        print("Program Selesai")
        print()
        return 0
        
    else :
        p = int(input("Masukkan Pangkatnya = "))
        int(nilai)
        h = int(nilai)**int(p)
        
        print("Hasilnya adalah = ",h)
        
        Perpangkatan()
        
    return h

nilai = 0
Perpangkatan()