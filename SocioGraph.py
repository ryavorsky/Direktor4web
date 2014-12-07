# The graph object


import math
import os
import BuildTexts

class SocioGraph :

    node = {}

    edge = {}

    type = ""

    def __init__(self, graph_type):
        self.node = {}
        self.edge = {}
        self.type = graph_type

    def nodes(self) :
        return [v for v in self.node]

    def edges(self) :
        res = []
        for edge_id in self.edge :
            res = res+ [[self.edge[edge_id]['source'], self.edge[edge_id]['target']]]
        return res

    def add_node(self, node_name) :
        self.node[node_name] = {}
        self.node[node_name]['id'] = node_name

    def update_node_attr(self, node_name, attr_name, attr_value) :
        self.node[node_name][attr_name] = attr_value

    def add_edge(self, node1, node2) :
        id = node1 + '->' + node2
        self.edge[id] = {}
        self.edge[id]['source'] = node1
        self.edge[id]['target'] = node2

    def update_edge_attr(self, node1, node2, attr_name, attr_value) :
        id = node1 + '->' + node2
        self.edge[id][attr_name] = attr_value

    def in_degree(self, node_id) :
        res = 0
        for edge_id in self.edge:
            if self.edge[edge_id]['target'] == node_id :
                res = res + 1
        return res

    def out_degree(self, node_id) :
        res = 0
        for edge_id in self.edge:
            if self.edge[edge_id]['source'] == node_id :
                res = res + 1
        return res

    def full_degree(self, node_id) :
        return self.in_degree(node_id) + self.out_degree(node_id)


    def has_edge(self, node1, node2) :
        return (self.edges().count([node1,node2]) > 0 )

    def connected(self, node1, node2) :
        return self.has_edge(node1, node2) or self.has_edge(node2, node1)


    def layout(self, mode='circular', width=800 ) :

        N = len(self.nodes()) # number of vertices
        if N == 0 :
            return

        cx, cy = width/2, width/2
        r = width/2 - 40

        i = 0

        # sort nodes to improve the graph view
        nodes_sequence = self.sort_nodes()

        for node in nodes_sequence :
            angle = 2.0*math.pi*i/N - 1
            node_cx = cx + int (r * math.cos(angle))
            node_cy = cy + int (r * math.sin(angle))
            dx = 0 + len(node) * 5
            dy = 5
            fillcolor = '#CCFFDD'
            degree = self.in_degree(node)
            size  = 15 + 1.5*degree
            if size > 30 :
                size = 30
            if node == '1' :
                fillcolor = '#FFFF00'
            node_svg = '<circle cx="'+str(node_cx)+'" cy="'+str(node_cy)
            node_svg = node_svg +'" r="'+str(size)+'" style="stroke:#000000; fill:'+fillcolor+'"/>'
            node_svg = node_svg + '\n<text x="'+str(node_cx-dx)+'" y="'+str(node_cy+dy) + '"'
            node_svg = node_svg + ' font-family="Verdana"  font-size="14"'
            node_svg = node_svg + ' fill="black">'+node+'</text>'
            self.update_node_attr(node, 'cx', node_cx)
            self.update_node_attr(node, 'cy', node_cy)
            self.update_node_attr(node, 'svg', node_svg)
            i = i + 1

        for pair in self.edges() :
            node1, node2 = pair
            x1, y1 = self.node[node1]['cx'], self.node[node1]['cy']
            x2, y2 = self.node[node2]['cx'], self.node[node2]['cy']
            edge_path = '<path stroke="#000000" d="M'+str(x1)+','+str(y1)+' L'+str(x2)+','+str(y2)+'"></path>'
            self.update_edge_attr(node1, node2, 'svg', edge_path)


    def sort_nodes(self) :

        list = self.nodes()
        N = len(list)
        for i in range(0, N-2) :

            best = i + 1

            for j in range(i+2, N) :

                if self.connected(list[i],list[j]) and not self.connected(list[i],list[best]) :
                    best = j

                if self.connected(list[i],list[j]) and self.connected(list[i],list[best]) :
                    if self.full_degree(j) == 1:
                        best = j
                    elif (self.full_degree(best) > 1) and self.full_degree(list[j]) > self.full_degree(list[best]) :
                        best = j

                if not self.connected(list[i],list[j]) and not self.connected(list[i],list[best]) :
                    if  self.full_degree(list[j]) < self.full_degree(list[best]) :
                        best = j

            if best > i+1:
                  list[i+1], list[best] = list[best], list[i+1]

        return list

    def max_degree(self, nodes_list):
        max_node_id = nodes_list[0]
        for node in nodes_list:
            if self.full_degree(node) > self.full_degree(max_node_id) :
                max_node_id = node
        return max_node_id

    def isolated_nodes(self):
        res = []
        for node in self.nodes():
            if self.full_degree(node) == 0:
                res.append(node)
        return res

    def not_isolated_nodes(self):
        res = []
        for node in self.nodes():
            if self.full_degree(node) > 0:
                res.append(node)
        return res

    def make_svg(self, file_name='g.svg', size = 800) :

        f_out = open(file_name, 'w')
        
        header = '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
        header = header + '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'
        header = header + '<svg height="' + str(size) + '" width="' + str(size) + '" version="1.1"'
        header = header + ' xmlns="http://www.w3.org/2000/svg">\n<desc>Socio Graph</desc>\n'
        f_out.write(header)

        res = ''
        for edge_id in self.edge :
            res = res + self.edge[edge_id]['svg'] + '\n'
        for node_id in self.nodes() :
            res = res + self.node[node_id]['svg'] + '\n'

        f_out.write(res)
        f_out.write('</svg>\n')
        f_out.close()


    def javascript_code(self):

        res_n = max([int(n) for n in self.nodes()])
        res_labels = [str(n+1) for n in range(res_n)]
        res_edges = self.edges()

        if self.type != "directed":
            res_labels = self.not_isolated_nodes()
            res_n = len(res_labels)
            for i in range(len(res_edges)) :
                [node0,node1] = res_edges[i]
                node0_index = res_labels.index(node0)+1
                node1_index = res_labels.index(node1)+1
                res_edges[i][0] = str(node0_index)
                res_edges[i][1] = str(node1_index)

        res_size = [ self.full_degree(node) for node in res_labels]
        max_size = max(res_size + [1])
        min_size = min(res_size + [1])  # add 1 to avoid empty list
        res_size = [str(9 + 6*(size-min_size)/max_size) for size in res_size]

        edge_codes = [str(edge[0]) + "-" + str(edge[1]) for edge in res_edges]
        res_spec = str(res_n) + ":" + ",".join(edge_codes)
        return [res_spec, res_labels, res_size]


    def make_dot(self, file_name='g.dot', size = 800) :

        f_out = open(file_name, 'w')
        
        header = 'digraph G {\n overlap="scale"; \n'
        f_out.write(header)

        res = ''
        if (self.type == 'directed') :
            max_degree = max ([self.in_degree(node_id) for node_id in self.nodes()]) + 1.0
        else :
            max_degree = max ([self.full_degree(node_id) for node_id in self.nodes()]) + 1.0

        for node_id in self.nodes() :
            if (self.type == 'directed') :
                degree = self.in_degree(node_id)
            else :
                degree = self.full_degree(node_id)

            size = str(0.7 + 0.7*degree/max_degree)
            if (self.full_degree(node_id) > 0) or (self.type == 'directed'):
                if (node_id == '1') :
                    fillcolor = '#FFFAAA'
                else :
                    fillcolor = '#EEEEEE'
                res = res + node_id + '[shape="circle"; width="' + size + '", fontsize="32", fixedsize=true, style=filled, fillcolor="'+fillcolor+'"];\n'

        for edge_id in self.edge :
            res = res + self.edge[edge_id]['source'] + ' -> ' + self.edge[edge_id]['target'] + '[len="2.7"];\n'

        f_out.write(res)
        f_out.write('}\n')
        f_out.close()



def MakeGraphFromEdges(size, edges, graph_type, file_name) :

    G = SocioGraph(graph_type)

    for n in range(size):
        G.add_node(str(n+1))

    for pair in edges :
        if (pair[0] in G.nodes()) and (pair[1] in G.nodes()):
            G.add_edge(pair[0], pair[1])
        else :
            subFolder = os.path.dirname(file_name)
            BuildTexts.Alert(subFolder, file_name+str(pair))

    G.layout()

    G.make_dot(file_name)

    print 'Ok!\n', 'Nodes :', G.node, '\nEdges :', G.edge

    return G

