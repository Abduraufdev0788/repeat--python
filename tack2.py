son1 = int(input("son1 ni kiriting: "))
son2 = int(input("son2 ni kiriting: "))
son3 = int(input("son3 ni kiriting: "))

if son1 > son2 and son1 > son3 :
    if son2 > son3 :
        print(f"eng kattasi {son1},\n ortachasi {son2}, eng kichigi {son3}")
    else:
        print(f"eng kattasi {son1},\n ortachasi {son3}, eng kichigi {son2}")
elif son2 > son1 and son2 > son3:
    if son1 > son3:
        print(f"eng kattasi {son2},\n ortachasi {son1}, eng kichigi {son3}")
    else:
        print(f"eng kattasi {son2},\n ortachasi {son3}, eng kichigi {son2}")

elif son3 > son1 and son3 > son2 :
    if son1 > son3:
        print(f"eng kattasi {son3},\n ortachasi {son1}, eng kichigi {son2}")
    else:
        print(f"eng kattasi {son3},\n ortachasi {son2}, eng kichigi {son1}")

else:
    print("barcha sonlar teng")