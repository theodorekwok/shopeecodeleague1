import pandas as pd
from numba import jit

df = pd.read_json(r'contacts.json')

allsetsofpeople = []


def comparestrings(one, two):
    if len(one) != len(two):
        return False

    for i in range(len(one)):
        if one[i] != two[i]:
            return False
    print(one)
    print(two)
    return True


def column_manipulatino(columnframe):
    all = []
    for i in range(len(list(columnframe))):
        all.append([i, columnframe[i]])

    all.sort(key=lambda x: x[1])

    uni = []
    for i in columnframe.unique():
         uni.append(i)

    uni.sort()
    arrayofsets = []
    i = 0
    while i < len(columnframe) and all[i][1] == '':
        i += 1
    index = i
    tocompare = 1
    while index < len(all):
         setemail = set()
         while index < len(all) and all[index][1] == uni[tocompare]:
             # print("Start")
             # print(all[index][1])
             # print(uni[tocompare])
             # print("end")
             setemail.add(all[index][0])
             index += 1

         tocompare += 1
         if len(setemail) > 1:
             arrayofsets.append(setemail)

    max = 0
    for i in arrayofsets:
        if (len(i) > max):
            max = len(i)
        # print(len(i))

    print("Biggest, ", max)
    # print(arrayofsets)
    print("size ", len(arrayofsets))
    return arrayofsets


allsetsofpeople = column_manipulatino(df['Phone']) + column_manipulatino(df['Email']) + column_manipulatino(df['OrderId'])


# print(sorted(allsetsofpeople))
def createadjlist(allsetsofpeople):
    adjlist = [[] for i in range(len(allsetsofpeople))]
    for i in range(len(allsetsofpeople)):
        for j in range(i + 1, len(allsetsofpeople)):
            if len(allsetsofpeople[i] & allsetsofpeople[j]) > 0:
                adjlist[i].append(j)
                adjlist[j].append(i)
        print(i)

    return adjlist

adj = createadjlist(allsetsofpeople)

df = {'index': [i for i in range(len(adj))], 'connectedcomponents': []}

for i in range(len(adj)):
    df['connectedcomponents'].append(adj[i])

ansdf = pd.DataFrame(df, columns=['index', 'connectedcomponents'])
ansdf.to_csv(r'adjlist.csv', index = False)
print(ansdf)

# ans = {'ticket_id': [i for i in range(500000)], 'ticket_trace/contact': [[] for i in range(500000)]}
#
# for i in range(len(allsetsofpeople)):
#     idlist = []
#     sumticket = 0
#     for j in allsetsofpeople[i]:
#         idlist.append(j)
#         sumticket += df['Contacts'].values[j]
#     idlist.sort()
#     idstring = ''
#     for id in idlist:
#         idstring += str(id)
#         idstring += '-'
#     idstring = idstring[:-1]
#     idstring += ', '
#     idstring += str(sumticket)
#     for id in idlist:
#         ans['ticket_trace/contact'][id] = idstring
#
# for i in range(len(ans['ticket_trace/contact'])):
#     if ans['ticket_trace/contact'][i] == []:
#         idstring = str(i)
#         idstring += ', '
#         idstring += str(df['Contacts'].values[i])
#         ans['ticket_trace/contact'][i] = idstring
#
# ansdf = pd.DataFrame(ans, columns=['ticket_id', 'ticket_trace/contact'])
# ansdf.to_csv(r'ans.csv', index = False)
# print(ansdf)

