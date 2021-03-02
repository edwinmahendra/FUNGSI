def prims(n):
    awal=0
    angka=2
    prima=[]
    while awal<n:
        for i in range(2,angka):
            if(angka%i==0):
                break
        else:
            prima.append(angka)
            awal+=1
        angka+=1
    return prima

def gens():
    awal=1
    angka=2
    genap=[]
    while awal<=n:
        if angka % 2==0:
            genap.append(angka)
            awal+=1
        angka+=1
    return genap

def gans(n): 
    awal=0
    angka=1
    ganjil=[]
    while awal<n:
        if angka % 2 != 0:
            ganjil.append(angka)
            awal+=1
        angka+=1
    return ganjil

print('=====MATH IS FUN=====')
print('[1] bil. prima\n[2] bil. genap\n[3] bil. ganjil')
pilihan = input('masukkan pilihan: ')
n=int(input('Masukkan bilangan ke n='))
if pilihan =='1':
    print(prims(n))
elif pilihan == '2':
    print(gens(n))
elif pilihan == '3':
    print(gans(n))
else:
    print('pilihan anda tidak ada')