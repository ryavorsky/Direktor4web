import shutil
import os
import math

import SocioGraph
import BuildRatings
import BuildTexts

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

    # Build specific graphs for the report
    for graph_id in graph_specs :
        BuildGraphFromSpec(graphData, graph_id, graph_specs[graph_id], subFolder)

    print '\n Building graphs complete'


def BuildGraphFromSpec(graphData, graph_id, graph_spec, subFolder) :

    graph_type = graph_spec.pop()
    questions = graph_spec
    file_name = os.path.join(subFolder, 'graph' + graph_id + '.svg')

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

    # build the graph and the visualization
    G = SocioGraph.MakeGraphFromEdges(edges, file_name)

    # save the graph statistics
    code = 'val' + BuildTexts.encodeNumber(graph_id) + 'links'
    BuildTexts.addMacro(subFolder, code, len(edges))

    # build the rating table
    if  graph_type == 'directed' :
        BuildRatings.computeRating(subFolder, graph_id, G)

