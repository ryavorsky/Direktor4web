import shutil
import os
import math

import SocioGraph
import BuildRatings
import BuildTexts

graph_sequence = ['61','62','711','712','721','722','731']

graph_specs = {
                '61' : [4,8, 'directed'], 
                '62' : [4,8, 'pairs'   ], 
                '711': [5,7, 'directed'], 
                '712': [5,7, 'pairs'   ], 
                '721': [3,6, 'directed'], 
                '722': [3,6, 'pairs'   ],
                '731': [0, 'directed']
                }


def BuildAllGraphs(subFolder, graphData):

    all_graphs = []

    # Build specific graphs for the report
    for graph_id in graph_sequence :
        G = BuildGraphFromSpec(graphData, graph_id, graph_specs[graph_id], subFolder)
        all_graphs.append(G)

    # Add graph descriptions for JavaScript

    js_specs = []
    js_labels = []
    js_size = []

    for G in all_graphs:
        [spec, labels, sizes] = G.javascript_code()
        js_specs.append(spec)
        labels_str = '["' + '","'.join(labels) + '"]'
        js_labels.append(labels_str)
        size_str = '[' + ','.join(sizes) + ']'
        js_size.append(size_str)

    js_specs_str = '["' + '",\n    "'.join(js_specs) + '"\n]'
    js_labels_str = '[' + ',\n    '.join(js_labels) + '\n]'
    js_size_str = '[' + ',\n    '.join(js_size) + '\n]'

    jsFileName = os.path.join(subFolder,'JavaScript','GraphSpecs.js')
    jsFile = open(jsFileName,'a')
    jsFile.write('\ngraph_specs = ' + js_specs_str + ';\n')
    jsFile.write('\ngraph_nodes_labels = ' + js_labels_str + ';\n')
    jsFile.write('\ngraph_nodes_size = ' + js_size_str + ';\n')
    jsFile.close()


    print '\n Building graphs complete'


def BuildGraphFromSpec(graphData, graph_id, graph_spec, subFolder) :

    graph_type = graph_spec.pop()
    questions = graph_spec
    size = len(graphData)
    file_name = os.path.join(subFolder, 'SVG', 'graph' + graph_id + '.dot')

    edges = []
    dict = {}

    for nodeData in graphData:

        [id, local_id, name, age, edgeGroups] = nodeData
        dict[id] = local_id

    # compute all edges
    for nodeData in graphData:

        [id, local_id, name, age, edgeGroups] = nodeData
        for question in questions:
            targets = edgeGroups[question-1]
            for target in targets:
                edges = edges + [[local_id, dict.get(target,'0')]]

    # compute symmetric edges (pairs of eges)
    if  graph_type == 'pairs' :
        sym_edges = []
        for edge in edges :
            reverse = [edge[1],edge[0]]
            if edges.count(reverse) > 0 :
                sym_edges = sym_edges + [edge]

        edges = sym_edges

    # remove duplicates
    edges = removeDuplicates(edges)

    # build the graph and the visualization
    G = SocioGraph.MakeGraphFromEdges(size, edges, graph_type, file_name)


    # save the graph statistics
    code = 'val' + BuildTexts.encodeNumber(graph_id) + 'links'

    if graph_type == 'pairs' :
        links = len(edges) / 2
    else :
        links = len(edges)

    BuildTexts.addMacro(subFolder, code, links)

    # build the rating table
    if  graph_type == 'directed' :
        BuildRatings.computeRating(subFolder, graph_id, G)

    return G

def removeDuplicates(lst) :

    res = []
    for e in lst:
        if res.count(e) == 0 :
            res.append(e)
    return res