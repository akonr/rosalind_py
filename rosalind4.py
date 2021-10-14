mesci = 33
potomci = 5

# def rabbit_recursive(n,k):
#     if n < 2:
#         return n
#     else:
#         return rabbit_recursive(n-1, k) + rabbit_recursive(n-2, k)*k
#
#
# print(rabbit_recursive(mesci,potomci))


def nekaj(n, k):
    if n < 2:
        return n
    else:
        return nekaj(n-1, k) + nekaj(n-2, k)

print(nekaj(mesci,potomci))
