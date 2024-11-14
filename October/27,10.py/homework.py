import csv
with open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\27,10.py\products.csv') as file:
    file = list(csv.reader(file))[1:]
    prods_dict = {}
    for i,j,_ in file:
        prods_dict[i] = j


with open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\27,10.py\clients.csv') as file:
    file = csv.reader(file)
    file = list(file)[1:]
    clients_dict = {}
    for id, name, _,_ in file:
        clients_dict[id] = name

sales = list(csv.reader(open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\27,10.py\sales.csv')))[1:]


with open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\27,10.py\postavchiki.csv') as file:
    file = list(csv.reader(file))[1:]
    distributor_id = {}
    for i,j,_ in file:
        distributor_id[i] = j
# print(distributor_id])

purchase = list(csv.reader(open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\27,10.py\purchase.csv')))[1:]
# print(purchase[0][1])









def wasted_money_and_maxPrice():
    dict = {}
    maxval = float('-inf')
    name = ''
    for i in purchase:
        distr_name = distributor_id[i[1]]
        dict[distr_name] = dict.get(distr_name, 0) + float(i[5])
        if float(i[4]) > maxval:
            maxval = float(i[4])
            name = distributor_id[i[1]]
            prod_name = prods_dict[i[2]]
    return dict,name,maxval,prod_name
# print(wasted_money_and_maxPrice())








def get_max_trade_name():
    client_name = ''
    maxval = float('-inf')
    for i in sales:
        if float(i[5]) > maxval:
            maxval = float(i[5])
            client_name = clients_dict[i[1]]
    return client_name, maxval





# print(get_max_trade_name())
def get_top5_trade():
    dict = {}
    for i in sales:
        name = clients_dict[i[1]]
        if name not in dict:
            dict[name] = [prods_dict[i[2]]]
        else:
            dict[name].append(prods_dict[i[2]])
        
    top5 = sorted([(len(set(arr)),name) for name, arr in dict.items() ])[-5:]
    return top5

print(get_top5_trade())

def get_all_avr():
    dict = {}
    for i in purchase:
        name = distributor_id[i[1]]
        if name not in dict:
            dict[name] = [float(i[5])]
        else:
            dict[name].append(float(i[5]))
    average = [(name, sum(arr)/len(arr)) for name,arr in dict.items()]
    return average
# print(get_all_avr())

with open(r'C:\Users\User\Desktop\GIT AIT Akbar\October\27,10.py\purchase.csv') as file:
    file = list(csv.reader(file))[1:]
    purchase_dict = {}
    for _,_,item,_,price,_ in file:
        purchase_dict[item] = price




def get_max_profit():
    dict = {}
    for i in sales:
        profit = float(i[4]) - float(purchase_dict[i[2]])
        dict[prods_dict[i[2]]] = profit
    name = ''
    maxval = float('-inf')
    for prod_name, profit in dict.items():
        if profit > maxval:
            maxval = profit
            name = prod_name
    return name, maxval
# print(get_max_profit())







def most_trade_client():
    dict = {}
    for i in sales:
        if i[1] not in dict:
            dict[i[1]] = {}
        else:
            dict[i[1]][i[2]] = dict[i[1]].get(i[2], 0) + float(i[3])
    name = ''
    prod = ''
    maxval = float('-inf')
    for k,v in dict.items():
        for key,arr in v.items():
            if arr > maxval:
                maxval = arr
                name = clients_dict[k]
                prod = prods_dict[key]
    return name,prod, maxval
# print(most_trade_client())
