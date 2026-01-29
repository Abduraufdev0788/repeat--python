matn = input("matnni kiriitng: ")

if matn.lower() == matn[:: -1].lower():
    print("matn palindrom")
else:
    print("palindorm emas")