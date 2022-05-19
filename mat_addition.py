X = [[58,45,21],
[29 ,23,22],
[54 ,36,13]]
Y = [[80,25,33],
[12,15,27],
[93,41,12]]
result = [[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for k in result:
    print(k)
