# The graph object


import math


class SocioGraph :

    node = {}

    edge = {}

    def __init__(self):
        self.node = {}
        self.edge = {}

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

    def layout(self, mode='circular', width=800 ) :

        N = len(self.nodes()) # number of vertices
        if N == 0 :
            return

        cx, cy = width/2, width/2
        r = width/2 - 40

        i = 0
        for node in self.nodes() :
            angle = 2.0*math.pi*i/N
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


    def make_svg(self, file_name='c:\\Tmp\\Try\\g.svg', size = 800) :

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


def MakeGraphFromEdges(edges, file_name) :

    G = SocioGraph()

    for pair in edges :
        G.add_node(pair[0])
        G.add_node(pair[1])

    for pair in edges :
        G.add_edge(pair[0], pair[1])

    G.layout()

    G.make_svg(file_name)

    print 'Ok!\n', 'Nodes :', G.node, '\nEdges :', G.edge

    return G

