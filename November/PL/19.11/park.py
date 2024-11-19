from time import sleep
arr = []
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ':
    arr.append(i)
mainword = 'Hello world'
second = ''
for i in arr:
    for j in mainword:
        print(j)
        sleep(0.05)
        if i == j:
            second += j
