﻿from app import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 5) == 5
