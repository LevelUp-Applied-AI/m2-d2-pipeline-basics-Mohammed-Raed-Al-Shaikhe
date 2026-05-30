"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    
    series = pd.Series([1, 2, np.nan, 4])
    
    cleaned = clean_column(series)

    # check no NaN values remain
    assert cleaned.isna().sum() == 0

    # check NaN replaced with correct median
    median_value = series.median()
    assert cleaned.iloc[2] == median_value




def test_compute_revenue():

    quantity = pd.Series([2, 3, 4])
    price = pd.Series([10, 5, 8])

    revenue = compute_revenue(quantity, price)

    expected = pd.Series([20, 15, 32])

    assert revenue.equals(expected)
