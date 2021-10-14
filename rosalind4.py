mesci = 33
potomci = 5

def nekaj(n, k):
    if n < 2:
        return n
    else:
        return nekaj(n-1, k) + nekaj(n-2, k)

print(nekaj(mesci,potomci))
