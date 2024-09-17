
while True :
    a = input('введите целое :')
    if a.isdigit() != 1 :
        print('не число')
        break
    if int(a) % 2 == 0 :
        print('число чётное')
        continue
        print('я не попадаю в цикл')
    else :
        print('число нечётное')
print('я за циклом')
