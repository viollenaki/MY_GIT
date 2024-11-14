from csv import reader, writer
balance = open('balance.csv', 'w')
file = reader(open(r'C:\Users\User\Desktop\ait progs\csv\22.10\users.csv'))

table = list(reader(open(r'C:\Users\User\Desktop\ait progs\csv\22.10\mbank_short.csv')))
table = table[1:]

users = {}
for i in file:
    if len(i)>0:
        users[i[0]] = i[1]

file = reader(open(r'C:\Users\User\Desktop\ait progs\csv\22.10\currencies.csv'))
currencies = {}
for i in file:
    if len(i) >0:
        currencies[i[0]] = i[1]
# print(currencies)

names = []
for i,j in users.items():
    names.append(j)
print(users)
print(names)


def get_from_to(from_id,to_id):
    dict = {}
    if from_id not in names or to_id not in names:
        return 'andai kishi jok'
    for i in table:
        if len(i)>0:
            if users[i[1]] == from_id:
                if users[i[2]] == to_id:
                    if i[4] not in dict:
                        dict[i[4]] = int(i[3])
                    else:
                        dict[i[4]] += int(i[3])
    print(from_id,'  -> ', to_id,'\n')
    for key,val in dict.items():
        print(f' {currencies[key]  }   {val}')  
    return ''

def dollar_pol():
    spisok =[]
    for i in table:
        if len(i)>0:
            if currencies[i[4]] == 'UNITED STATES DOLLAR':  
                if users[i[1]] not in spisok:
                    spisok.append(users[i[1]])
    return spisok

def get_sender_spisok(to_user):
    spisok = {}
    for i in table:
        if len(i) > 0:
            if users[i[2]] == to_user: 
                spisok[users[i[1]]] = spisok.get(users[i[1]],0) +1
    return spisok


def get_total_profit():
    dict = {}
    for i in table:
        if len(i)>0:
            dict[currencies[i[4]]] = dict.get(currencies[i[4]],0) + int(i[3])
    total_text = 0
    dict_som ={
'KYRGYZ SOM':1,
'RUSSIAN RUBLE':0.9,
'UNITED STATES DOLLAR':80,
'KAZAKH TENGE':0.2,
'EUROPEAN EURO':90}
    for i,j in dict.items():
        total_text += dict_som[i]*j
    return total_text/1000
print(get_total_profit())




