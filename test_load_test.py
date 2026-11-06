"""
Programmer: Noah Gaido
Course: ENSC 201, Fall 2026
Programming Assignment #5
Version: 1.2
Date: 10/27/2026

Description: Verify stress calculations, boundaries, and loading cycles.
Sources: PA5 Conditionals and Loops assignment; ENSC 201 Coding Standard.
Notes: OpenAI ChatGPT assisted with generating and revising the code
    and unit tests.
"""

import numpy as np

from load_test import calculate_stress, classify_stress, run_load_test


def test_calculate_stress_common():
    """Check stress for a typical applied force.

    Returns:
        None.
    """
    assert calculate_stress(100, 10) == 10.0


def test_calculate_stress_zero_force():
    """Check that zero force produces zero stress.

    Returns:
        None.
    """
    assert calculate_stress(0, 10) == 0.0


def test_calculate_stress_decimal():
    """Check a decimal result using a floating-point comparison.

    Returns:
        None.
    """
    assert np.isclose(calculate_stress(5, 2), 2.5)


def test_classify_stress_safe():
    """Check a stress well below the warning range.

    Returns:
        None.
    """
    assert classify_stress(10, 25) == "SAFE"


def test_classify_stress_zero():
    """Check the zero-stress boundary.

    Returns:
        None.
    """
    assert classify_stress(0, 25) == "SAFE"


def test_classify_stress_below_warning():
    """Check a stress just below the 80% threshold.

    Returns:
        None.
    """
    assert classify_stress(19.99, 25) == "SAFE"


def test_classify_stress_at_warning_threshold():
    """Check that exactly 80% is a warning.

    Returns:
        None.
    """
    assert classify_stress(20, 25) == "WARNING"


def test_classify_stress_warning():
    """Check a stress within the warning range.

    Returns:
        None.
    """
    assert classify_stress(22, 25) == "WARNING"


def test_classify_stress_at_limit():
    """Check that exactly 100% is still a warning.

    Returns:
        None.
    """
    assert classify_stress(25, 25) == "WARNING"


def test_classify_stress_above_limit():
    """Check that stress just above the limit fails.

    Returns:
        None.
    """
    assert classify_stress(25.01, 25) == "FAILURE"


def test_run_load_test_no_failure():
    """Check that all cycles complete without failure.

    Returns:
        None.
    """
    failure_cycle = run_load_test(50, 25, 3, 10, 25)

    assert failure_cycle == 0


def test_run_load_test_first_cycle_failure():
    """Check that first-cycle failure stops further cycles.

    Returns:
        None.
    """
    failure_cycle = run_load_test(300, 100, 5, 10, 25)

    assert failure_cycle == 1


def test_run_load_test_later_failure():
    """Check increasing stress and early failure on cycle three.

    Returns:
        None.
    """
    failure_cycle = run_load_test(100, 100, 5, 10, 25)

    assert failure_cycle == 3


def test_run_load_test_one_cycle_at_limit():
    """Check that one cycle exactly at the limit passes with a warning.

    Returns:
        None.
    """
    failure_cycle = run_load_test(250, 10, 1, 10, 25)

    assert failure_cycle == 0


def test_run_load_test_final_cycle_failure():
    """Check that failure on the final planned cycle is reported.

    Returns:
        None.
    """
    failure_cycle = run_load_test(100, 100, 3, 10, 25)

    assert failure_cycle == 3
