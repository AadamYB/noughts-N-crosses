"""test scripts"""

import pytest


def test_exxample():
    """just assert true"""
    assert True


def test_success():
    """this should pass"""
    assert 1 == 1


def test_failure():
    """ this should fail """
    assert 1 + 1 == 3
