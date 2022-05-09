x=100
def raj():
    x=150
def suraj():
    global x
    x=200
print("before calling suraj ", x)
suraj()
print("after calling suraj ", x)
raj()
print(x)
