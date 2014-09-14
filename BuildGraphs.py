import shutil
import os
import math
import SocioGraph

graph_specs = {
                '61':[4,8, 'directed'], 
                '62':[4,8, 'pairs'], 
                '711':[5,7, 'directed'], 
                '712':[5,7, 'pairs'], 
                '721':[3,6, 'directed'], 
                '722':[3,6, 'pairs']
                }


def BuildAllGraphs(subFolder, graphData):

    # Build specific graphs for the report
    for graph_id in graph_specs :
        file_name = os.path.join(subFolder, 'graph' + graph_id + '.svg')
        BuildSpecGraph(graphData, graph_specs[graph_id], subFolder, file_name)

    print '\n Building graphs complete'


def BuildSpecGraph(graphData, graph_spec, subFolder, file_name) :

    graph_type = graph_spec.pop()
    questions = graph_spec

    edges = []
    dict = {}

    for nodeData in graphData:

        [id, local_id, name, age, edgeGroups] = nodeData
        dict[id] = local_id

    for nodeData in graphData:

        [id, local_id, name, age, edgeGroups] = nodeData
        for question in questions:
            targets = edgeGroups[question-1]
            for target in targets:
                edges = edges + [[local_id, dict.get(target,'0')]]

    sym_edges = []
    for pair in edges :
        reverse = [pair[1],pair[0]]
        if pair[0] < pair[1] and edges.count(reverse) > 0 :
            sym_edges = sym_edges + [pair]

    if  graph_type == 'pairs' :
        edges = sym_edges

    G = SocioGraph.MakeGraphFromEdges(edges, file_name)



