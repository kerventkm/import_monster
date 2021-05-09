# -*- coding: utf-8 -*-
import builtins
import math

import scipy

import numpy
import pytest
from import_monster import methods_importer


class Test_method_importer:
    """
    This test case is testing 'method_importer' function from package 'import_monster'
    Method has to check if any of module contains callable object with name method_name and return list of such objects
    """

    def test_method_importer(self):
        """ Testing that methods_importer returns list modules contains callable object with given name """
        assert methods_importer("sum", [math, builtins, scipy, numpy]) == [
            "builtins",
            "scipy",
            "numpy",
        ]

    @pytest.mark.parametrize(
        "test_case,expected_result",
        [
            (("add", [math, builtins, scipy, numpy]), ["scipy", "numpy"]),
            (("exponent", [builtins, scipy, numpy]), []),
            # It will give error because correct is ['math', 'scipy']
            (("pi", [math, builtins, scipy]), ["math"]),
        ],
    )
    def test_multiple(self, test_case, expected_result):
        assert list(methods_importer(*test_case)) == expected_result

    def test_fail(self):
        with pytest.raises(TypeError):
            methods_importer(1, 100)
