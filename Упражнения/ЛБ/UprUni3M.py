def func(dumi):
    kusa = min(dumi, key=len)
    dulga = max(dumi, key=len)
    return  kusa, dulga


spisak = ["obo", "mom", "huba", "krast", "frast"]
rezultat = func(spisak)
print(rezultat)

