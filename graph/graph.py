# -*- coding: utf-8 -*-

from collections import defaultdict

class graph():
    
    def __init__(self,edges):
        '''
        Generate an undirected graph

        Parameters
        ----------
        edges : List
            List of edges

        Returns
        -------
        None.

        '''
        self.graph = defaultdict(list)        
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            
    def add_node(self, node):
        '''
        Adds a node to the graph

        Parameters
        ----------
        node : TYPE
            A node to be added to the graph

        Returns
        -------
        None.

        '''
        if node in self.graph:
            pass
        else:
            self.graph[node] = []
    
    def add_edge(self, edge):
        '''
        Adds an edge to the graph

        Parameters
        ----------
        edge : 
            An edge to be added to the graph

        Returns
        -------
        None.

        '''
        if edge[0] in self.graph:
            if edge[1] in self.graph[edge[0]]:
                pass
        else:
            self.graph[edge[0]].append(edge[1])
            
    def __iter__(self):
        '''
        Returns all the nodes of the graph

        Returns
        -------
        List
            Nodes of graph instance

        '''
        return self.graph.keys()
    
    def __getitem__(self, node):
        '''
        Returns adjacent nodes to the given node

        Parameters
        ----------
        node : 
            A node in the graph

        Returns
        -------
        List of adjacent nodes to the given node

        '''
        return self.graph[node]
    
    def __contains__(self, node):
        if node in self.graph:
            return True
        else:
            return False
        
    def BFS(self, s):
        '''
        Returns a list containing node and distance of node from given node 
        calculated using BFS

        Parameters
        ----------
        s : 
            A node

        Returns
        -------
        bfs_output : 
            node and distance pair of all the other nodes in graph from s

        '''
        bfs_output = []
        distance = {s: 0}
 
        visited = [False] * (max(self.graph) + 1)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            s = queue.pop(0)
            bfs_output.append((s, distance[s]))

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    distance[i] = distance[s] + 1
                    visited[i] = True
        return bfs_output
            
            
    def distance(self, start, goal):
        '''
        Returns distance between start and goal node

        Parameters
        ----------
        start : 
            Node 
        goal : 
            Node

        Returns
        -------
        Int
            Distance

        '''

        visited = []

        queue = [[start]]
        if start == goal:
            return 0
     
        while queue:

            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = self.graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == goal:
                        return len(new_path) - 1
                visited.append(node)
     
        return "Connecting path does not exist"
                
                
