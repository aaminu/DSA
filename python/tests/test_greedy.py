from greedy_algos.dijkstra_algo import dijkstra_alogrithm
import pytest


########################## Dijkstra Alogrithm #########################

@pytest.mark.parametrize(
    "graph, start, finish, output_cost, output_parent",
    [
        (
            {
                "start": {"A": 6, "B": 2},
                "A": {"finish": 1},
                "B": {"finish": 5, "A": 3, "F": 1},
                "F": {"finish": 1},
                "finish": {}
            },
            "start",
            "finish",
            4,
            "F"
        ),
        (
            {
                "start": {"A": 5, "B": 2},
                "A": {"C": 4, "D": 2},
                "B": {"A": 8, "D": 7},
                "C": {"finish": 3, "D": 6},
                "D": {"finish": 1},
                "finish": {}
            },
            "start",
            "finish",
            8,
            "D"
        ),
        (
            {
                "start": {"A": 10},
                "A": {"B": 20},
                "B": {"C": 1, "finish": 30},
                "C": {"A": 1},
                "finish": {}
            },
            "start",
            "finish",
            60,
            "B"
        ),
        (
            {
                "start": {"A": 2, "B": 2},
                "A": {"finish": 2, "C": 2},
                "B": {"A": 2},
                "C": {"finish": 2, "B": -1, },
                "finish": {}
            },
            "start",
            "finish",
            4,
            "A"
        )

    ]
)
def test_dijkstra_alogrithm(graph, start, finish, output_cost, output_parent):
    """Search for the Shortest weigthed path between start and finish"""

    # Act
    output = dijkstra_alogrithm(graph, start, finish)

    # Assert
    assert output["cost"][finish] == output_cost
    assert output["parent"][finish] == output_parent
