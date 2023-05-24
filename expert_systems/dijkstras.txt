// Dijkstras
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void dijkstras(vector<pair<int,int>> adj[],int s,vector<int>&distance){
    // min heap
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    distance[s] = 0;

    pq.push({0,s}); // {distance ,node}

    while(!pq.empty()){
        pair<int,int> temp = pq.top();
        pq.pop();

        int dist = temp.first;
        int node = temp.second;

        for(auto i:adj[node]){
            int edgeWeight = i.second;
            int adjNode = i.first;

            if(dist + edgeWeight < distance[adjNode]){
                pq.push({dist+edgeWeight,adjNode});
                distance[adjNode] = dist+edgeWeight;
            }
        }
    }
}

int main(){
    int v, e;
    cout << "Enter number of vertices : ";
    cin >> v;

    cout << "Enter number of edges : ";
    cin >> e;

    vector<pair<int, int>> adjList[v];

    for (int i = 0; i < e; i++){
        int u, v, w;
        cin >> u >> v >> w;
        adjList[u].push_back({v, w});
        adjList[v].push_back({u, w});
    }

    vector<int> distance(v,INT_MAX);
    int s;
    cout<<"Enter Source Node : ";
    cin>>s;

    dijkstras(adjList,s,distance);

    for(int i = 0; i<distance.size(); i++){
        cout<<"Minimum distance from Source "<<s<<" to node "<<i<<" is : "<<distance[i]<<endl;
    }

    return 0;
}