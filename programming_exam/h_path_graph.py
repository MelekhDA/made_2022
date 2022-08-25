from sys import setrecursionlimit
from collections import Counter
import threading


def dfs(vertex_v, colors, current_color, adjacency_list):
    colors[vertex_v] = current_color
    for vertex_u in adjacency_list[vertex_v]:
        if colors[vertex_u] == DEFAULT_COLOR:
            dfs(vertex_u, colors, current_color, adjacency_list)


def main():
    N, M = map(int, input().split())
    colors = [DEFAULT_COLOR for _ in range(N)]

    adjacency_list = [[] for _ in range(N)]
    for _ in range(M):
        vertex_v, vertex_u = map(int, input().split())
        vertex_v, vertex_u = vertex_v - 1, vertex_u - 1
        adjacency_list[vertex_v].append(vertex_u)
        adjacency_list[vertex_u].append(vertex_v)

    current_color = 0
    for vertex_v in range(N):
        if colors[vertex_v] == DEFAULT_COLOR:
            current_color += 1
            dfs(vertex_v, colors, current_color, adjacency_list)

    counter = Counter(colors)
    print(sum(n_edge ** 2 for n_edge in counter.values()))


DEFAULT_COLOR = 0
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
