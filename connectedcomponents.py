import pandas as pd
from queue import Queue

data = pd.read_json(r'contacts.json')

df = pd.read_csv('adjlist.csv')


def printframe(index):
    print("Contacts ", data['Contacts'][index], "Email ", data['Email'][index], "OrderId ", data['OrderId'][index], "Phone ", data['Phone'][index])


def checksingle(id, email, orderid, phone):
    emailcount = 0
    orderidcount = 0
    phonecount = 0
    if email != '':
        for i in data['Email']:
            if i == email:
                # print("email")
                emailcount += 1

    if orderid != '':
        for i in data['OrderId']:
            if i == orderid:
                # print("Order")
                orderidcount += 1

    if phone != '':
        for i in data['Phone']:
            if i == phone:
                # print("phone")
                phonecount += 1

    if emailcount > 1 or orderidcount > 1 or phonecount > 1:
        print("Wrong ans")
        print(id)

#
printframe(16)
# printframe(2458)
# printframe(98519)
# printframe(115061)
# printframe(140081)
# printframe(165605)
# printframe(476346)
# checksingle('0', '', '', '8888238873')

ansread = pd.read_csv('ans.csv')
index = 0
for i in ansread['ticket_trace/contact']:
    totest = str(i)
    notsingle = False
    for c in totest:
        if c == '-':
            notsingle = True
    if notsingle == False:
        checksingle(index, data['Email'][index], data['OrderId'][index], data['Phone'][index])
    index += 1
    print(index)



# adjlist = []
# for i in df['connectedcomponents']:
#     toappend = []
#     for val in i[1:len(i) - 1].split(', '):
#         if val != '':
#             toappend.append(int(val))
#     adjlist.append(toappend)
#
# allpeople = []
#
# def findconnectedcomponents(adjlist, allpeople):
#     visited = [False for ind in range(len(adjlist))]
#
#     for i in range(len(adjlist)):
#         q = Queue()
#         component = []
#         if visited[i] == False:
#             visited[i] = True
#             component.append(i)
#             q.put(i)
#             while q.empty() == False:
#                 top = q.get()
#                 for j in range(len(adjlist[top])):
#                     if visited[adjlist[top][j]] == True:
#                         continue
#                     else:
#                         visited[adjlist[top][j]] = True
#                         component.append(adjlist[top][j])
#                         q.put(adjlist[top][j])
#
#             allpeople.append(component)
#
# findconnectedcomponents(adjlist, allpeople)
#
# # print(allpeople)
#
# def comparestrings(one, two):
#     if len(one) != len(two):
#         return False
#
#     for i in range(len(one)):
#         if one[i] != two[i]:
#             return False
#     print(one)
#     print(two)
#     return True
#
#
# def column_manipulatino(columnframe):
#     all = []
#     for i in range(len(list(columnframe))):
#         all.append([i, columnframe[i]])
#
#     all.sort(key=lambda x: x[1])
#
#     uni = []
#     for i in columnframe.unique():
#          uni.append(i)
#
#     uni.sort()
#     arrayofsets = []
#     i = 0
#     while i < len(columnframe) and all[i][1] == '':
#         i += 1
#     index = i
#     tocompare = 1
#     while index < len(all):
#          setemail = set()
#          while index < len(all) and all[index][1] == uni[tocompare]:
#              # print("Start")
#              # print(all[index][1])
#              # print(uni[tocompare])
#              # print("end")
#              setemail.add(all[index][0])
#              index += 1
#
#          tocompare += 1
#          if len(setemail) > 1:
#              arrayofsets.append(setemail)
#
#     max = 0
#     for i in arrayofsets:
#         if (len(i) > max):
#             max = len(i)
#         # print(len(i))
#
#     print("Biggest, ", max)
#     # print(arrayofsets)
#     print("size ", len(arrayofsets))
#     return arrayofsets
#
#
# setsofpeople = column_manipulatino(data['Phone']) + column_manipulatino(data['Email']) + column_manipulatino(data['OrderId'])
#
# allsetsofpeople = []
# for i in range(len(allpeople)):
#     setofonepersonids = setsofpeople[allpeople[i][0]]
#     for j in range(1, len(allpeople[i])):
#         if len(setofonepersonids & setsofpeople[allpeople[i][j]]) == 0:
#             print("False")
#         setofonepersonids = setofonepersonids | setsofpeople[allpeople[i][j]]
#
#     allsetsofpeople.append(setofonepersonids)
#
#
# ans = {'ticket_id': [i for i in range(500000)], 'ticket_trace/contact': [[] for i in range(500000)]}
#
# for i in range(len(allsetsofpeople)):
#     idlist = []
#     sumticket = 0
#     for j in allsetsofpeople[i]:
#         idlist.append(j)
#         sumticket += data['Contacts'].values[j]
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
#         idstring += str(data['Contacts'].values[i])
#         ans['ticket_trace/contact'][i] = idstring
#
# ansdf = pd.DataFrame(ans, columns=['ticket_id', 'ticket_trace/contact'])
# ansdf.to_csv(r'ans.csv', index = False)
# print(ansdf)
