print('simple assignment')
shoplist=['apple','mange','carrot','banana']
mylist=shoplist
del shoplist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)
print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)