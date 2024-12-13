from bfs_graph import *

def test_get_unvis_related_input_out_of_range():
    g = SimpleGraph(3)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)

    assert g._get_unvisited_related(3) is None


def test_get_unvis_related_doesnt_exist():
    g = SimpleGraph(3)

    g.AddVertex(0)
    g.AddVertex(1)

    assert g._get_unvisited_related(2) is None


def test_get_unvis_related_none():
    g = SimpleGraph(3)
    g.AddVertex(0)
    g.AddVertex(1)
    assert g._get_unvisited_related(None) is None

def test_get_unvis_related_0_related():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    assert g._get_unvisited_related(3) == []

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_1_related():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)

    assert g._get_unvisited_related(3) == [0]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_few_related():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)
    g.AddEdge(3, 2)

    assert g._get_unvisited_related(3) == [0, 2]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == [2]

    g.vertex[2].Hit = True

    assert g._get_unvisited_related(3) == []


# Not full graph

def test_get_unvis_related_0_related_not_full():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    assert g._get_unvisited_related(3) == []

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_1_related_not_full():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)

    assert g._get_unvisited_related(3) == [0]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_few_related_not_full():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)
    g.AddEdge(3, 2)

    assert g._get_unvisited_related(3) == [0, 2]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == [2]

    g.vertex[2].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_loops():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 3)

    assert g._get_unvisited_related(3) == [3]

    g.AddEdge(3, 3)

    assert g._get_unvisited_related(3) == [3]

    g.vertex[3].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_few_edges():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)
    g.AddEdge(0, 3)
    g.AddEdge(3, 0)
    g.AddEdge(0, 3)

    assert g._get_unvisited_related(3) == [0]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


# Test BFS

def test_bfs_indexes_out_of_range():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    assert g.BreadthFirstSearch(0, 4) is None
    assert g.BreadthFirstSearch(4, 0) is None
    assert g.BreadthFirstSearch(4, 7) is None


def test_bfs_same_verticies():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    assert g.BreadthFirstSearch(0, 0) == []

    g.AddEdge(0, 0)

    assert g.BreadthFirstSearch(0, 0) == []


def test_bfs_wrong_type():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    assert g.BreadthFirstSearch('0', 1) is None
    assert g.BreadthFirstSearch(0, '1') is None
    assert g.BreadthFirstSearch(None, None) is None


def test_bfs_are_hits_false():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 3)
    g.AddEdge(4, 1)
    g.AddEdge(4, 5)

    verticies = g.vertex

    g.BreadthFirstSearch(0, 5)

    for v in verticies:
        assert v.Hit is False

    g.BreadthFirstSearch(1, 2)

    for v in verticies:
        assert v.Hit is False

    g.BreadthFirstSearch(4, 4)

    for v in verticies:
        assert v.Hit is False


def test_bfs_simple():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 5)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[2],
        g.vertex[3],
        g.vertex[4],
        g.vertex[5]
    ]

def test_bfs_loops():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 5)

    g.AddEdge(0, 0)
    g.AddEdge(0, 0)

    g.AddEdge(1, 1)
    g.AddEdge(1, 1)

    g.AddEdge(2, 2)
    g.AddEdge(2, 2)

    g.AddEdge(3, 3)
    g.AddEdge(3, 3)

    g.AddEdge(4, 4)
    g.AddEdge(4, 4)

    g.AddEdge(5, 5)
    g.AddEdge(5, 5)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[2],
        g.vertex[3],
        g.vertex[4],
        g.vertex[5]
    ]


def test_bfs_cycles_1():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 5)

    g.AddEdge(1, 0)
    g.AddEdge(2, 0)
    g.AddEdge(3, 0)
    g.AddEdge(4, 0)

    res = g.BreadthFirstSearch(0, 5)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[4],
        g.vertex[5]
    ]


def test_bfs_cycles_2():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 1)
    g.AddEdge(3, 5)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[2],
        g.vertex[3],
        g.vertex[5]
    ]


def test_bfs_multiple_edges_cycles_loops():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(3, 4)
    g.AddEdge(4, 1)
    g.AddEdge(4, 1)
    g.AddEdge(3, 5)
    g.AddEdge(3, 5)
    g.AddEdge(4, 5)
    g.AddEdge(4, 5)

    g.AddEdge(5, 5)
    g.AddEdge(4, 4)
    g.AddEdge(2, 2)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[5]
    ]


def test_bfs_multiple_edges_cycles_loops_not_full():
    g = SimpleGraph(10)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(3, 4)
    g.AddEdge(4, 1)
    g.AddEdge(4, 1)
    g.AddEdge(3, 5)
    g.AddEdge(3, 5)
    g.AddEdge(4, 5)
    g.AddEdge(4, 5)

    g.AddEdge(5, 5)
    g.AddEdge(4, 4)
    g.AddEdge(2, 2)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[5]
    ]


def test_bfs_multiple_edges_cycles_loops_not_full():
    g = SimpleGraph(10)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(3, 4)
    g.AddEdge(4, 1)
    g.AddEdge(4, 1)
    g.AddEdge(3, 5)
    g.AddEdge(3, 5)
    g.AddEdge(4, 5)
    g.AddEdge(4, 5)

    g.AddEdge(5, 5)
    g.AddEdge(4, 4)
    g.AddEdge(2, 2)

    g.AddVertex(6)
    g.AddVertex(7)
    g.AddVertex(8)
    g.AddVertex(9)

    g.AddEdge(6, 7)
    g.AddEdge(8, 9)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[5]
    ]

    assert g.BreadthFirstSearch(0, 7) == []
    assert g.BreadthFirstSearch(6, 9) == []

    g.AddEdge(7, 8)

    assert g.BreadthFirstSearch(6, 9) == [
        g.vertex[6],
        g.vertex[7],
        g.vertex[8],
        g.vertex[9]
    ]