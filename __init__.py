# type: ignore[attr-defined]
"""Inspect your AI models visually, find bugs, give feedback 🕵️‍♀️ 💬"""

import sys

from giskard import test, Dataset, TestResult
import great_expectations as ge

@test()
def uniqueness_test(dataset: Dataset = None, column_name: str = None):
    dataframe = ge.from_pandas(dataset.df)
    uniqueness = dataframe.expect_column_values_to_be_unique(column=column_name)
    passed = uniqueness["success"]
    metric = uniqueness["result"]["element_count"]
    return TestResult(passed=passed, metric=metric)

@test(name="Data Quality")
def data_quality(dataset: Dataset = None,
                 threshold: float = 0.5,
                 column_name: str = None,
                 category: str = None):
    freq_of_cat = dataset.df[column_name].value_counts()[category]/ (len(dataset.df))
    passed = False and freq_of_cat < threshold

    return TestResult(passed=passed, metric=freq_of_cat)

@test
def test_without_export():
    return True

__all__ = ['uniqueness_test', 'data_quality']
