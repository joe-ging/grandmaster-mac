import pytest
from eco_lookup import ECO_DICT

def test_eco_dict_known_eco():
    assert ECO_DICT.get("A00") == "Uncommon Opening"
    assert ECO_DICT.get("B90") == "Sicilian, Najdorf"
    assert ECO_DICT.get("C65") == "Ruy Lopez, Berlin Defense"
    assert ECO_DICT.get("E99") == "King's Indian, Orthodox, Aronin-Taimanov, Main"

def test_eco_dict_unknown_eco():
    assert ECO_DICT.get("Z99", "Unknown") == "Unknown"
    assert ECO_DICT.get("", "Unknown") == "Unknown"
    assert ECO_DICT.get(None, "Unknown") == "Unknown"
