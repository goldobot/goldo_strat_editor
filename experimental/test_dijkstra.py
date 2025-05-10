import numpy as np

class WPNode:
    def __init__(self,_wp):
        self.x = _wp[0]
        self.y = _wp[1]
        self.ngb_dist = {}
        self.enabled = True
    def __str__(self):
        return "x={} y={} ngb_dist={}".format(self.x, self.y, self.ngb_dist)


class GoldoDijkstra:
    def __init__(self, node_dico, edge_list):
        self.wp_graph = {k:WPNode(node_dico[k]) for k in node_dico.keys()}
        for edge in edge_list:
            wp0 = node_dico[edge[0]]
            wp1 = node_dico[edge[1]]
            delta_x = wp1[0] - wp0[0]
            delta_y = wp1[1] - wp0[1]
            dist = np.sqrt(delta_x*delta_x + delta_y*delta_y)
            self.wp_graph[edge[0]].ngb_dist[edge[1]] = dist
            self.wp_graph[edge[1]].ngb_dist[edge[0]] = dist
        self.keys = self.wp_graph.keys()
        self.reset()

    def reset(self):
        self.dist = {}
        self.prev = {}
        self.sptSet = {}
        for k in self.keys:
            self.dist[k] = 1e9
            self.prev[k] = None
            self.sptSet[k] = False
        self.src = None

    def compute_min_key(self):
        my_min = 1e9
        min_key = None
        for k in self.keys:
            if self.dist[k] < my_min and self.sptSet[k] == False:
                my_min = self.dist[k]
                min_key = k
        return min_key

    def do_dijkstra(self, src):
        self.reset()
        self.dist[src] = 0
        self.src = src
    
        for cout in range(len(self.keys)):
            u = self.compute_min_key()
            self.sptSet[u] = True
            for v in self.wp_graph[u].ngb_dist.keys():
                dist_uv = self.wp_graph[u].ngb_dist[v]
                if not self.wp_graph[v].enabled: dist_uv = 1e7
                if (self.sptSet[v]==False) and (self.dist[v] > self.dist[u] + dist_uv):
                    self.dist[v] = self.dist[u] + dist_uv
                    self.prev[v] = u
    
        return self.dist, self.prev
    
    def get_path(self, dst):
        if self.src==None:
            print ("DEBUG : (self.src==None)")
            return []
        if dst not in self.keys:
            print ("DEBUG : (dst not in self.keys)")
            return []
        wpn_k = dst
        print ("DEBUG : wpn_k = {}".format(wpn_k))
        wpn = self.wp_graph[wpn_k]
        my_path = [(wpn_k,wpn.x,wpn.y)]
        for cout in range(len(self.keys)):
            wpn_k = self.prev[wpn_k]
            print ("DEBUG : wpn_k = {}".format(wpn_k))
            if (wpn_k==None):
                # "src" was found in the previous iteration..
                # FIXME : TODO : check that the "src" node is indeed present in the path!..
                my_path.reverse()
                return my_path
            wpn = self.wp_graph[wpn_k]
            my_path.append((wpn_k,wpn.x,wpn.y))
        # something went wrong!..
        print ("DEBUG : something went wrong!..")
        return []
