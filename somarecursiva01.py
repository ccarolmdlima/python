def somaelem(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + somaelem(l[1:])

l = [2, 0, 1, 5, 7, 8, 6]
resultado = somaelem(l)
print(resultado)
