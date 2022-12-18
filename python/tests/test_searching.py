import pytest
from binary_search import binary_search
from breadth_first_search import breadth_first
from dijkstra_algo import dijkstra_alogrithm


def test_selection_1():
    # Gather
    test_data = {
        "input": [2, 3, 5, 1, 4],
        "value": 5,
        "output": 2
    }

    # Act
    response = binary_search(test_data["input"], test_data["value"])

    # Asset
    assert response == test_data["output"]


@pytest.mark.parametrize(
    "input_arr, value, output_index",
    [
        (list(range(100)), 0, 0),
        (list(range(100)), 99, 99),
        (list(range(1, 100)), 50, 49),
        (list(range(1, 100)), 25, 24),
        (list(range(0, 100, 2)), 25, None),
        (list(range(0, 10, 3)), 8, None)
    ]
)
def test_selection_2(input_arr, value, output_index):
    # Act
    response = binary_search(input_arr, value)

    # Assert
    assert response == output_index


def test_selection_3(test_validator):
    """Search for the first friend a specified node that is Nigerian for"""

    # Gather
    graph = {
        "aminu": [{"id": "sos", "country_code": "GER"}, {"id": "chisom", "country_code": "USA"}],
        "sos": [{"id": "alison", "country_code": "NLD"}],
        "chisom": [{"id": "tawa", "country_code": "NGA"}, {"id": "promise", "country_code": "BLG"}],
        "tawa": [{"id": "aminu", "country_code": "NGA"}],
        "alison": [],
        "promise": []
    }
    selection_key = "country_code"
    selection_criterion = "NGA"

    # Act
    person = breadth_first(graph, "aminu", test_validator,
                           selection_key, selection_criterion)

    # Assert
    assert person["id"] == "tawa"


def test_selection_4(test_validator):
    """Search for the first friend a specified node that is Nigerian for"""

    # Gather
    graph = {
        "aminu": [{"id": "sos", "country_code": "GER"}, {"id": "chisom", "country_code": "USA"}],
        "sos": [{"id": "alison", "country_code": "NLD"}],
        "chisom": [{"id": "tawa", "country_code": "NGA"}, {"id": "promise", "country_code": "BLG"}],
        "tawa": [{"id": "aminu", "country_code": "NGA"}],
        "alison": [],
        "promise": []
    }
    selection_key = "country_code"
    selection_criterion = "NGA"

    # Act
    person = breadth_first(graph, "mary", test_validator,
                           selection_key, selection_criterion)

    # Assert
    assert person == None


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
def test_selection_5(graph, start, finish, output_cost, output_parent):
    """Search for the Shortest weigthed path between start and finish"""

    # Act
    output = dijkstra_alogrithm(graph, start, finish)

    # Assert
    assert output["cost"][finish] == output_cost
    assert output["parent"][finish] == output_parent
