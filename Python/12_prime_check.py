num = 7
flag = True
for i in range(2, num):
    if num % i == 0:
        flag = False
if flag:
    print('Prime')
else:
    print('Not Prime')