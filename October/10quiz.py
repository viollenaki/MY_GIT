from csv import reader
user = reader(open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\users.csv'))

file = list(reader(open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\mbank_short.csv')))
file = file[1:]




users = {}
for i in user:
    if len(i)>0:
        users[i[0]] = i[1]

current = reader(open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\currencies.csv'))
currencies = {}
for i in current:
    if len(i) >0:
        currencies[i[0]] = i[1]

names = set()
for i,j in users.items():
    names.add(j)
# print(users)
# print(names)
# print(currencies)


# def get_history():
#     from datetime import datetime
#     dict = {}
#     for i in file:
#         if len(i)>0:
#             date = str(datetime.fromtimestamp(i[0]))
#             dict[users[i[0]]] =  dict.get(users[i[0]],{date:{ 'receiver': users[i[2]], 'amount': int(i[3]), 'currency': currencies[i[4]]  }})
#     return dict
# print(get_history())

def top_5():
    dict_som ={
'KYRGYZ SOM':1,
'RUSSIAN RUBLE':0.9,
'UNITED STATES DOLLAR':80,
'KAZAKH TENGE':0.2,
'EUROPEAN EURO':90}
    dict_receive= {}
    dict_send = {}
    for i in file:
        if len(i)>0:
            dict_receive[users[i[2]]] = dict_receive.get(users[i[2]],0) + (dict_som[currencies[i[4]]] * int(i[3]))
            dict_send[users[i[1]]] = dict_send.get(users[i[1]],0) + (dict_som[currencies[i[4]]] * int(i[3]))
    sender = sorted([(j,i) for i,j in dict_send.items()])[-5:]
    receiver = sorted([(j,i) for i,j in dict_receive.items()])[-5:]
    return f'{sender} \n{receiver}'

print(top_5())
