def all_routes_to_dest ( n : int , connections : list [list[int]] , begin : int , end : int ) -> bool :
    
    dicti = {start: [] for start, desti in connections}
    for start, desti in connections:
        dicti[start].append(desti)
    
#     print(dicti)
    abc, visit = set(), set()
    #we iterate through each node and each vertex in graph only once.
    def dfs(vertex):
        # 3 base cases
        if vertex not in dicti: # end node with no leaves, not present as key in dicti
            return vertex == end
        if vertex in abc: 
            return False
        if vertex in visit:
            return True

        abc.add(vertex)
        for node in dicti[vertex]:
            if not dfs(node):
                return False
        abc.remove(vertex)
        visit.add(vertex)
        return True

    return dfs(begin)