#TODO: Check command
import os
import pytest

def test_command():
    assert os.system('python -c "import paradise"') == 0
    # assert True
