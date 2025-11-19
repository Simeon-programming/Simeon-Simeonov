def func():
    dumi = input("Въведете думи разделени с интервали").split()
    if all(dumi.isalpha() for dumi in dumi):
        print("Tова са вашите думи: ")
    else:
        print("Моля въведете само думи!")
