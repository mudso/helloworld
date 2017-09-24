import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# Find the ids that send out page rank - we only are interested
# in pages in the SCC that have in and out links
cur.execute('''SELECT DISTINCT from_id FROM Links''')
from_ids = list()
for row in cur:
    from_ids.append(row[0])
#DISTINCT返回Links的fromid唯一不同值

# Find the ids that receive page rank
to_ids = list()
links = list()
cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
for row in cur:
    from_id = row[0]
    to_id = row[1]
    if from_id == to_id : continue#组合里网页自己跳自己的不要
    if from_id not in from_ids : continue#这个为什么要加
    if to_id not in from_ids : continue#没有跳回的不要
    links.append(row)#处理过的保存到links里
    if to_id not in to_ids : to_ids.append(to_id)
#links的要求比较严格
# Get latest page ranks for strongly connected component
prev_ranks = dict()
for node in from_ids:
    cur.execute('''SELECT new_rank FROM Pages WHERE id = ?''', (node, ))#id的newrank
    row = cur.fetchone()
    prev_ranks[node] = row[0]#构成id-newrank
#处理多少次
sval = input('How many iterations:')
many = 1
if ( len(sval) > 0 ) : many = int(sval)

# Sanity check数据处理前的检查
if len(prev_ranks) < 1 :
    print("Nothing to page rank.  Check data.")
    quit()

# Lets do Page Rank in memory so it is really fast
for i in range(many):
    #处理次数
    # print prev_ranks.items()[:5]
    next_ranks = dict();
    total = 0.0
    for (node, old_rank) in list(prev_ranks.items()):
        total = total + old_rank
        #总计有多少个网页的ranks加在一起
        next_ranks[node] = 0.0
    # print total

    # Find the number of outbound links and sent the page rank down each
    for (node, old_rank) in list(prev_ranks.items()):
        # print node, old_rank
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != node : continue
            #Pages的idpre_ranks和处理过的links的比较，
           #  print '   ',from_id,to_id
            if to_id not in to_ids: continue
            #是否存在不匹配需要处理
            give_ids.append(to_id)
        if ( len(give_ids) < 1 ) : continue
        amount = old_rank / len(give_ids)
        #第一次1.0/（指向多少个网站）
        # print node, old_rank,amount, give_ids

        for id in give_ids:
            next_ranks[id] = next_ranks[id] + amount

    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank#总值
    evap = (total - newtot) / len(next_ranks)#平均变化

    # print newtot, evap
    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap#新值加平均变化

    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank#最新值

    # Compute the per-page average change from old rank to new rank
    # As indication of convergence of the algorithm
    totdiff = 0
    for (node, old_rank) in list(prev_ranks.items()):
        new_rank = next_ranks[node]
        diff = abs(old_rank-new_rank)#绝对值旧－新
        totdiff = totdiff + diff#累加

    avediff = totdiff / len(prev_ranks)
    print(i+1, avediff)

    # rotate
    prev_ranks = next_ranks

# Put the final ranks back into the database
print(list(next_ranks.items())[:5])
cur.execute('''UPDATE Pages SET old_rank=new_rank''')#old存到新
for (id, new_rank) in list(next_ranks.items()) :
    cur.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, id))
conn.commit()
cur.close()

