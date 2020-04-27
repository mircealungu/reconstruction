import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

import os


def module_from_path(full_path, folder_prefix=""):
    # extracting a module from a file name
    # e.g. /Users/mircea/Zeeguu-Core/zeeguu_core/model/user.py -> zeeguu_core.model.user

    file_name = full_path[len(folder_prefix):]
    file_name = file_name.replace(os.sep, ".")
    file_name = file_name.replace(".py", "")
    return file_name


assert ("tools.map_article_words" == module_from_path("tools/map_article_words.py"))


def top_level_module(module_name, depth=1):
    # extracts the parent of depth X
    # e.g. top_level_module(zeeguu_core.model.util, 1) -> zeeguu_core
    components = module_name.split(".")
    return ".".join(components[:depth])


top_level_module(module_from_path("zeeguu_core/model/user.py", "/Users/mircea/Zeeguu-Core/"), 2)


def abstracted_to_top_level(G, system_module):
    aG = nx.DiGraph()
    for each in G.edges():
        source = top_level_module(each[0], 2)
        destination = top_level_module(each[1], 2)
        if system_module(source) and system_module(destination):
            aG.add_edge(source, destination)
    return aG


def dependencies_graph(path_to_code):
    files = Path(path_to_code).rglob("*.py")

    G = nx.Graph()

    for file in files:
        m = module_from_path(str(file), path_to_code)
        if m not in G.nodes:
            G.add_node(m)

        for each in imports(str(file)):
            G.add_edge(m, each)

    return G


def full_path(file_name, root_folder):
    return root_folder + "/" + file_name


def extract_import_from_line(line):
    # TODO: think about how to detect imports when
    # they are inside a function / method
    x = re.search("^import (\S+)", line)
    x = re.search("^from (\S+)", line)
    return x.group(1)


import re


def imports(file):
    # extracts all the imported modules from a file
    lines = [line for line in open(file)]

    all_imports = []
    for line in lines:
        try:
            all_imports.append(extract_import_from_line(line))
        except:
            continue

    return all_imports


assert 'sqlalchemy' in (imports('/Users/mircea/Zeeguu-Core/zeeguu_core/model/user.py'))


def draw_graph_with_weights(G, weight_function, figsize=(10, 10)):
    node_weights = [weight_function(each) for each in G.nodes]

    plt.figure(figsize=figsize)
    nx.draw(G,
            with_labels=True,
            node_size=node_weights)
    plt.show()


def draw_graph(G):
    plt.figure(figsize=(10, 6))
    nx.draw(G)
    plt.show()


def system_module(m):
    modules = ['zeeguu_core.bookmark_quality',
               'zeeguu_core.configuration',
               'zeeguu_core.content_recommender',
               'zeeguu_core.content_retriever',
               'zeeguu_core.model',
               'zeeguu_core.language',
               'zeeguu_core.emailer',
               'zeeguu_core.util',
               'zeeguu_core.word_scheduling']
    return m in modules or m == 'tools' or m == 'playground'


if __name__ == "__main__":
    directed = dependencies_graph('/Users/mircea/Zeeguu-Core/')
    directedAbstracted = abstracted_to_top_level(directed, system_module)

    draw_graph(directedAbstracted)
