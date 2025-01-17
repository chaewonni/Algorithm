def solution(n, costs):
    # Union-Find에 사용할 parent 배열 초기화
    parent = [i for i in range(n)]
    
    # Find 연산: 부모를 찾는 함수
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]
    
    # Union 연산: 두 집합을 합치는 함수
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            
    costs.sort(key=lambda x: x[2])
    
    # 최소 비용 계산
    answer = 0
    for u, v, cost in costs:
        # 두 정점이 같은 집합에 속하지 않을 때만 간선을 추가
        if find(u) != find(v):
            union(u, v)
            answer += cost
    
    return answer
