import polars as pl
from io import StringIO
from main import (
    cleanData,
    summaryStatistics,
    PiePlot,
    tripleBarPlot,
)  # Replace 'your_module' with the actual name of your module

"""
Test Functions for data processing and visualization functions
"""

def test_summaryStatistics():
    csv_data = """#,School Name,International students (%),International faculty (%),Value for money rank,Career progress rank,Careers service rank
                  1,School A,30,20,10,20,15
                  2,School B,25,30,20,15,10
                  3,School C,20,25,15,10,20
                  4,School D,15,20,30,25,25
                  5,School E,35,40,5,5,5"""

    # Read the CSV data into a Polars DataFrame
    df = pl.read_csv(StringIO(csv_data))

    # Summary statistics function (assuming it works with Polars)
    summary = summaryStatistics(
        df, ["Value for money rank", "Career progress rank", "Careers service rank"]
    )

    # Check if the summary statistics contain the required metrics
    assert (
        summary.filter(pl.col("stat") == "mean").select("Value for money rank").item() == 16.0
    ), "Mean of Value for money rank is incorrect"
    assert (
        summary.filter(pl.col("stat") == "median").select("Value for money rank").item() == 15.0
    ), "Median of Value for money rank is incorrect"
    assert (
        summary.filter(pl.col("stat") == "mean").select("Career progress rank").item() == 15.0
    ), "Mean of Career progress rank is incorrect"
    assert (
        summary.filter(pl.col("stat") == "median").select("Career progress rank").item() == 15.0
    ), "Median of Career progress rank is incorrect"
    assert (
        summary.filter(pl.col("stat") == "mean").select("Careers service rank").item() == 15.0
    ), "Mean of Careers service rank is incorrect"
    assert (
        summary.filter(pl.col("stat") == "median").select("Careers service rank").item() == 15.0
    ), "Median of Careers service rank is incorrect"
