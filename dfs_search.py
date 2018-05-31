# 迭代深入深度优先
def iter_dfs(g, s):
    searched, q = set(), []
    q.append(s)     # s:初始状态，第一个随机搜索的节点
    while q:    # 扩展图
        u = q.pop()     # 当前搜索的节点
        if u in searched:  # S:已经搜索的节点集合
            continue
        searched.add(u)
        q.extend(g[u])  # G[u]: 当前节点的后继节点
        yield u     # 最后将搜索的节点添加到生成器里面，这里是list生成器。


# 递归深度优先
def rec_dfs(g, s, searched=None):
    if searched is None:
        searched = set()  # 初始化为一个集合
    searched.add(s)     # 初始化第一个搜索的节点
    for u in G[s]:  # 从当前搜索节点的后继节点（待搜索的扩展图节点列表）中取一个节点。 从左到右取出
        if u in searched:   # 如果已经是搜索过的集合中的节点，则跳过
            continue
        rec_dfs(g, u, searched)
    return searched

# 宽度优先搜索
def bfs(g, s):
    import collections
    p, q = {s: None}, collections.deque([s])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v in p:
                continue
            p[v] = u
            q.append(v)
    return p


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
    print(list(iter_dfs(G, a)))       # [0, 5, 7, 6, 2, 3, 4, 1]
    print(rec_dfs(G, a))
    print(bfs(G, a))

'''
    #python实现深度优先搜索是用的栈数据结构（last-in-first-out）后进先出，只能是一边队列的一边可以操作数据，从同一边进出。python中对应的方法为：Stack()，用list实现。
    #python实现宽度优先搜索是用的FIFO队列数据结构（first-in-first-out）先进先出，从队列一边进，但从队列另一边出，可以两边操作数据。python中对应的方法为：
    FIFOQueue()，用deque()双向队列实现。
    #python实现宽度优先搜索是用的堆队列数据结构（。python中对应的方法为：
    PriorityQueue()，用heapq()队列实现。
'''