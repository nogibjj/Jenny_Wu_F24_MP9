"""
Test goes here

"""

import pandas as pd
import sys
import os

sys.path.append("python_files/main_files")

import congressional_age as lib


def load_dataset(datasource):
    dataframe = pd.read_csv(datasource)
    return dataframe

dataframe = load_dataset("sample_data/data_aging_congress.csv")


def test_get_summary_stats():
    test_desc_stats = lib.get_summary_stats(dataframe, "age_years")
    """test that the summary function will work"""
    assert test_desc_stats is not None


def test_hist_cong_age_plot_creation():
    # Run the function
    lib.hist_cong_age(dataframe, "age_years")
    # Check if the output file exists
    assert os.path.exists(
        "output/congressional_age.png"
    ), "Plot image file was not created."
    # Optionally, remove the file after the test
    os.remove("output/congressional_age.png")


def test_age_dist_50_plot_creation():
    # Run the function
    desc_stats = lib.get_summary_stats(dataframe, "age_years")
    lib.age_dist_50(dataframe, desc_stats)
    # Check if the output file exists
    assert os.path.exists("output/chamber_age.png"), "Plot image file was not created."
    # Optionally, remove the file after the test
    os.remove("output/chamber_age.png")


test_get_summary_stats()
test_hist_cong_age_plot_creation()
test_age_dist_50_plot_creation()
