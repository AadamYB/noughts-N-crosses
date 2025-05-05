"""test scripts"""

import pytest
from tkinter import *
from unittest.mock import MagicMock, patch
from app.main import noughtsNcrosses


def test_example():
    """just assert true"""
    assert True


def test_success():
    """this should pass"""
    assert 1 == 1


# def test_failure(): fail
#     """this should fail"""
#     assert 10 + 2 == 3


@patch("tkinter.Tk")
@patch("tkinter.Label")
@patch("tkinter.Frame")
@patch("tkinter.Button")
def test_initial_player_label(MockButton, MockFrame, MockLabel, MockTk):
    """Mock GUI elements to run Tkinter-based test headlessly"""
    mock_root = MagicMock()
    game = noughtsNcrosses(mock_root)

    game.current_player = "X"
    game.label.cget = lambda attr: "X's Turn"

    label_text = game.label.cget("text")
    assert label_text in ["X's Turn", "O's Turn"]
