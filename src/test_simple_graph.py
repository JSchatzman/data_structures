"""Test implementation of a simple unweighted directed graph."""

import pytest


@pytest.fixture
def sample_graph():
    """Create testing graph."""
    from simple_graph import Graph
    one_graph = Graph('A')
    empty_graph = Graph()
    new_graph = Graph(['A', 'B', 'C', 'D'])
    return one_graph, empty_graph, new_graph


def test_initialization_of_graph(sample_graph):
    """Test initilaization of an empty graph."""
    assert sample_graph[1].graph == {}


def test_initialization_of_graph_with_one_datapoint(sample_graph):
    """Test initialization of a graph with one data point."""
    assert sample_graph[0].graph == {'A': []}


def test_initialization_of_graph_with_multiple_datapoints(sample_graph):
    """Test graph with multiple data points is initialized."""
    assert sample_graph[2].graph == {'A': [], 'B': [], 'C': [], 'D': []}


def test_add_a_node_adds_node_with_no_connections(sample_graph):
    """Test add_node adds a node to graph with no connections."""
    sample_graph[1].add_node('B')
    assert sample_graph[1].graph == {'B': []}


def test_add_a_node_to_an_initialized_graph(sample_graph):
    """Test node is added to an existing graph."""
    sample_graph[2].add_node('E')
    assert sample_graph[2].graph == {'A': [], 'B': [], 'C': [],
                                     'D': [], 'E': []}


def test_add_existing_node_do_not_duplicate(sample_graph):
    """Test add and existingnode does not duplicate in graph."""
    sample_graph[0].add_node('A')
    assert sample_graph[0].graph == {'A': []}


def test_add_edge_on_existing_nodes(sample_graph):
    """Test connections between existing nodes is created."""
    sample_graph[2].add_edge('A', 'B')
    assert sample_graph[2].graph['A'] == ['B']


def test_add_edge_when_node2_does_not_exist(sample_graph):
    """Test connection between new node2 and existing is made."""
    sample_graph[0].add_edge('A', 'B')
    assert sample_graph[0].graph == {'A': ['B'], 'B': []}


def test_add_edge_when_node1_does_not_exist(sample_graph):
    """Test connection between new node1 and existing node2."""
    sample_graph[0].add_edge('B', 'A')
    assert sample_graph[0].graph == {'A': [], 'B': ['A']}


def test_add_edge_when_node1_and_node2_does_not_exist(sample_graph):
    """Test connection between new node1 and new node2."""
    sample_graph[1].add_edge('A', 'B')
    assert sample_graph[1].graph == {'A': ['B'], 'B': []}


def test_list_of_nodes_is_displayed(sample_graph):
    """Test nodes are displayed in a list."""
    assert sample_graph[0].nodes() == ['A']
    assert sample_graph[1].nodes() == []


def test_list_of_multiple_nodes_is_displayed(sample_graph):
    """Test nodes in a graph of multiple nodes are returned."""
    many_nodes = sample_graph[2].nodes()
    many_nodes.sort()
    assert many_nodes == ['A', 'B', 'C', 'D']
