import pytest
from pylenium.driver import Pylenium
from Pages.Herokuapp import Herokuapp

@pytest.fixture
def herokuapp(py: Pylenium):
    _herokuapp = Herokuapp(py)
    
    return _herokuapp