"""test scripts"""

import pytest
from tkinter import *
from app import noughtsNcrosses


def test_example():
    """just assert true"""
    assert True


def test_success():
    """this should pass"""
    assert 1 == 1

def test_initial_player_label():
    root = Tk()
    root.withdraw()  # Prevents the game window from showing during test
    game = noughtsNcrosses(root)

    label_text = game.label.cget("text")
    assert label_text in ["X's Turn", "O's Turn"]
    root.destroy()

# def test_failure():
#     """this should fail"""
#     assert 1 + 1 == 3
