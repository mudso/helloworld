#this is mt shoping list
shoplist=['apple','mange','carrot','bana']
print('i have',len(shoplist),'things to purchase')

print('these items are;',end=' ')
for item in shoplist:
    print(item,end=' ')
print('\ni also have to but rice')
shoplist.append('rice')
print('my shopping list is now',shoplist)

print('i will sort my list now')
shoplist.sort()
print('sorter shopping list is',shoplist)

print('the first item i will buy is',shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('i bought the',olditem)
print('my shopping list is now',shoplist)