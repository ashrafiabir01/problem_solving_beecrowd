while True :
    try :
        a,b =map(int, input().split())
        if (a<b):
            print('Crescente')
        elif (a==b):
            break
        else :
            
            print('Decrescente')
    except:
        break