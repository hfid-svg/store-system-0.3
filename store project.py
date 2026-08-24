# store-system-0.3
this is my python project


inv=[ ]
toko={"vandal":50,"shield":30,"potion":10}
uang=100
while True:
    i=input("selamat datang apakah ada yg bisa kami bantu?(ya/tidak)?:")
    if i=="ya":
        print(f"[status saat ini] uang:{uang}$|isi inventory:{inv}")
        print("silahkan pilih menu di bawah ini:")
        print("a.beli barang")
        print("b.jual barang")
        print("c.keluar")
        a=input(":masukkan pilihanmu(a/b/c):")
        if a=="a":
            while True:
                print(f"vandal:{toko["vandal"]}$")
                print(f"shield:{toko["shield"]}$")
                print(f"potion:{toko["potion"]}$")
                print(f"uang anda saat ini:{uang}$")
                item=input("beli apa?(ketik 'keluar' untuk selesai):")
                if item=="keluar":
                    print("tsilahkan datang kembali!")
                    break
                elif item in toko:
                    harga=(toko[item])
                    print(f"harga {item}:{harga}$")
                    pilihan=input(f"apakah anda yakin mau membeli {item}?(ya/tidak):")
                    if pilihan=="ya":
                        if uang>=harga:
                            uang=uang-harga
                            inv.append(item)
                            print(f"{item} telah di tambahkan ke inventory!")
                            print(f"isi inventory saat ini:{inv}")
                        else:
                            print("uang kamu tidak cukup!")
                    elif pilihan=="tidak":
                        print("transaksi di batalkan")
                    else:
                        print("pilihan tidak valid")
                else:
                    print("barang tidak ada di toko!")
            print(f"isi inventory saat ini:{inv}")
        elif a=="b":
            while True:
                jualitem=input("masukkan nama item yg mau anda jual(ketik 'keluar'untuk stop):")
                if jualitem in inv:
                    yakin=input(f"apakah anda yakin ingin menjual{jualitem}(ya/tidak):?")
                    if yakin=="ya":
                        inv.remove(jualitem)
                        uang=uang+toko[jualitem]
                        print(f"isi inventory saat ini:{inv}")
                        print(f"uang:{uang}$")
                    elif yakin=="tidak":
                        print("transaksi dibatalkan")
                    else:
                        print("pilihan tidak valid!")
                elif jualitem=="keluar":
                    print("silahkan datang kembali!")
                    break
                elif jualitem not in inv:
                    print("item tidak ada di inventory!")
        elif a=="c":
            print("terimakasih sudah menggunakan layanan kami:)")
            break
        else:
            print("pilihan tidak valid!")
    elif i=="tidak":
        print("terimakasih sudah menggunakan layanan kami,silahkan datang kembali! :)")
        break
    else:
        print("pilihan tidak valid!")
print("program selesai")
