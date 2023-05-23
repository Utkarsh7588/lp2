def kruskal_mst(edges,n):
    edges.sort(key=lambda e:e[2])
    parent=list(range(n))
    rank=[0]*n
    mst=[]

    def find(u):
        if parent[u]!=u:
            parent[u]=find(parent[u])
        return parent[u]

    def union(u,v):
        u_root,v_root=find(u),find(v)

        if u_root==v_root:
            return
        if rank[u_root]>rank[v_root]:
            parent[v_root]=u_root    
        else:
            parent[u_root]=v_root
            if rank[u_root]==rank[v_root]:
                rank[v_root]+=1

    for u,v,w in edges:
        if find(u)!=find(v):
            union(u,v)
            mst.append((u,v,w))
        if len(mst)==n-1:
            break
            


