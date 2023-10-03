def muncul_sekali (angka):
    list_angka = [int(char) for char in angka]

    frekuensi = {}
    for n in list_angka:
        if n in frekuensi:
            frekuensi[n] += 1
        else:
            frekuensi[n] = 1
    angka_unik = [n for n, freq in frekuensi.items() if freq == 1]

    return angka_unik

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]