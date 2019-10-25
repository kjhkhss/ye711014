x = int(input('玩家第一次摇出的点数:'))
y = int(input('玩家第二次摇出的点数:'))
if x + y == 7 or x + y == 11:
    print('玩家胜利！')
elif x + y == 2 or x + y == 3 or x + y == 12:
    print('庄家胜利！')
else:
    needs_go_on = True
    while needs_go_on:
        print('玩家继续摇骰子！')
        a = x + y
        w = int(input('玩家摇出的点数:'))
        z = int(input('玩家摇出的点数:'))
        if w + z == 7:
            print('庄家胜利！')
            break
        elif w + z == a:
            print('玩家胜利!')
            break
        else:
            needs_go_on = True
