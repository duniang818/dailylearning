def iter_dfs(G,s):
    S,Q=set(),[]
    Q.append(s)  #s:初始状态，第一个随机搜索的节点
    while Q: #扩展图
        u = Q.pop() #当前搜索的节点
        if u in S:  # S:已经搜索的节点集合
            print("u is in S")
            continue
        S.add(u)
        Q.extend(G[u]) #G[u]: 当前节点的后继节点
        print("u:{},S:{},Q:{}".format(u, S, Q))
        yield u #最后将搜索的节点添加到生成器里面，这里是list生成器。

if __name__ == "__main__":
    a, b, c, d, e, f, g, h, i = range(9)
    G = [{b, c, d, e, f},  # a
         {c, e},           # b
         {d},              # c
         {e},              # d
         {f},              # e
         {c, g, h},        # f
         {f, h},           # g
         {f, g}            # h
         ]
    print(list(iter_dfs(G,a)))       # [0, 5, 7, 6, 2, 3, 4, 1]


'''
    #python实现深度优先搜索是用的栈数据结构（last-in-first-out）后进先出，只能是一边队列的一边可以操作数据，从同一边进出。python中对应的方法为：Stack()，用list实现。
    #python实现宽度优先搜索是用的FIFO队列数据结构（first-in-first-out）先进先出，从队列一边进，但从队列另一边出，可以两边操作数据。python中对应的方法为：
    FIFOQueue()，用deque()双向队列实现。
    #python实现宽度优先搜索是用的堆队列数据结构（。python中对应的方法为：
    PriorityQueue()，用heapq()队列实现。
'''