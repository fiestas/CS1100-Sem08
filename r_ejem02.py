# funcion foo con caso base de salida

def foo(s):
    if len(s) == 1:
        print(s)
    else:
        print(s)
        s = s[1:]
        foo(s)

foo('hola mundo')
