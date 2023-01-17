from graph_algos.breadth_first_search import breadth_first


########################## Breadth First #########################

def test_breadth_first_1(test_validator):
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


def test_breadth_first_2(test_validator):
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
