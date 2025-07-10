'''
https://yottagin.com/?p=1822
'''

from collections import deque

class Graph():
    def __init__(self):
        """ ノードのつながりを辞書型で表現する """
        self.adjacency_dict = {}
    
    def add_vertex(self, v):
        """ ノードを追加する """
        self.adjacency_dict[v] = []
    def add_edge(self, v1, v2):
        """ ノード同士をつなぐ。"""
        # 無向グラフの場合は双方向。もし有向グラフなら片側のみ。
        self.adjacency_dict[v1].append(v2)
        self.adjacency_dict[v2].append(v1)
    def next_vertices(self, v):
        """ 隣接したノードを返す """
        return self.adjacency_dict[v]
    def remove_edge(self, v1, v2):
        """ ノード同士のつながりを削除する。"""
        self.adjacency_dict[v1].remove(v2)
        self.adjacency_dict[v2].remove(v1)
    def remove_vertex(self,v):
        """ ノードを削除する。"""
        while self.adjacency_dict[v] != []:
            adjacent_vertex = self.adjacency_dict[v][-1]
            self.remove_edge(v, adjacent_vertex)
        del self.adjacency_dict[v]
    
    def __str__(self):
        return self.adjacency_dict.__str__()

    
# make a graph
graph = Graph()
for i in range(1, 4+1):
    graph.add_vertex(i)
for v1, v2 in [[1,2], [2,3], [3,4], [4,2]]:
    graph.add_edge(v1, v2)

    
def bfs():
    visited = [False]*(4+1)
    visited[1] = True
    q = deque()
    q.append(1)
    print(1)

    while q:
        v_now = q.popleft()
        print(f'next vertices: {graph.next_vertices(v_now)}')
        for v_next in graph.next_vertices(v_now):
            if visited[v_next] == 0:
                print(v_next)
                visited[v_next] = True
                q.append(v_next)
    print(visited[1:])

def recursive_dfs():
    def dfs(node):
        if visited[node]:
            return

        visited[node] = True
        print(node)
        for v in graph.next_vertices(node):
            dfs(v)

    visited = [False]*(4+1)
    dfs(1)
    print(visited[1:])


def main():
    print('BFS: ')
    bfs()
    print('\nDFS')
    recursive_dfs()

if __name__ == '__main__':
    main()
