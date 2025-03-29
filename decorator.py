
def smart(func):
    def inner(a,b):
        if a<b:
          a,b = b,a
          return
        elif b == 0:
          print("indivisible by o")
          return
        else:
          print("error")
        return func(a,b)
    return inner
          
@smart
def div(a,b):
    print(a/b)

div(0,2)
#please try this out