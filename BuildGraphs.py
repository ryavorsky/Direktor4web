import shutil
import os
import math

def BuildAllGraphs(subFolder, graphData):
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph61.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph62.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph711.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph712.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph721.svg'))
    shutil.copy2(os.path.join(subFolder,'graph_sample.svg'), os.path.join(subFolder,'graph722.svg'))

class SocioGraph :

    node = {}

    edge = {}

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
        return 1

    def out_degree(self, node_id) :
        return 1

    def layout(self, mode='circular', width=800 ) :

        N = len(self.nodes()) # number of vertices
        if N == 0 :
            return

        cx, cy = width/2, width/2
        r = width/3

        i = 0
        for node in self.nodes() :
            angle = 2.0*math.pi*i/N
            node_cx = cx + int (r * math.cos(angle))
            node_cy = cy + int (r * math.sin(angle))
            node_svg = '<circle cx="'+str(node_cx)+'" cy="'+str(node_cy)+'" r="15" style="stroke:#000000; fill:#AAFFBB"/>'
            node_svg = node_svg + '\n<text x="'+str(node_cx-4)+'" y="'+str(node_cy+5)+'" fill="black">'+node+'</text>'
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



def Try():
    G = SocioGraph()
    edges = G.edges()
    nodes = G.nodes()

    G.add_node('1')
    G.add_node('2')
    G.add_node('3')
    G.add_edge('1','2')
    G.add_edge('1','3')

    G.layout()

    G.make_svg()

    print 'Ok!\n', 'Nodes :', G.node, '\nEdges :', G.edge
    print G.nodes()

