import polars as pl
from io import StringIO
from main import (
    cleanData,
    summaryStatistics,
    PiePlot,
)

"""
Test Functions for data processing and visualization functions using Polars
"""

# Test summaryStatistics
def test_summaryStatistics():
    csv_data = """#,School Name,International students (%),International faculty (%),Value for money rank,Career progress rank,Careers service rank
                  1,School A,30,20,10,20,15
                  2,School B,25,30,20,15,10
                  3,School C,20,25,15,10,20
                  4,School D,15,20,30,25,25
                  5,School E,35,40,5,5,5"""

    df = pl.read_csv(StringIO(csv_data))

    summary, meanVal, medianVal = summaryStatistics(
        df, ["Value for money rank", "Career progress rank", "Careers service rank"]
    )

    # Check if the summary statistics contain the required metrics
    assert (
        medianVal["Value for money rank"][0] == 16.0
    ), "Median Value for money rank is incorrect"
    assert (
        medianVal["Career progress rank"][0] == 15.0
    ), "Median Value for progress rank is incorrect"
    assert (
        medianVal["Careers service rank"][0] == 15.0
    ), "Median Value for service rank is incorrect"

    assert (
        meanVal["Value for money rank"][0] == 15.0
    ), "Mean of Value for money rank is incorrect"
    assert (
        meanVal["Career progress rank"][0] == 15.0
    ), "Mean of Value for progress rank is incorrect"
    assert (
        meanVal["Careers service rank"][0] == 15.0
    ), "Mean of Value for service rank is incorrect"


# Test cleanData
def test_cleanData():
    csv_data = """#,School Name,International students (%),International faculty (%),Value for money rank,Career progress rank,Careers service rank
                  1,School A,30,20,10,20,15
                  2,School B,25,30,20,15,10
                  3,School C,20,25,15,10,20
                  4,School D,15,20,30,25,25
                  5,School E,35,40,5,5,5"""

    df = pl.read_csv(StringIO(csv_data))

    Columns = [
        "#",
        "School Name",
        "International students (%)",
        "International faculty (%)",
        "Value for money rank",
        "Career progress rank",
        "Careers service rank",
    ]
    CleanedData = cleanData(df, "#", Columns, 3)

    # Check if the cleaned DataFrame has the correct number of rows
    assert CleanedData.height == 3, "Number of rows in cleaned data is incorrect"
    assert all(col in CleanedData.columns for col in Columns), "Column filtering failed"


# Test PiePlot
def test_PiePlot():
    csv_data = """#,School Name,International students (%),International faculty (%),Value for money rank,Career progress rank,Careers service rank
                  1,School A,30,20,10,20,15
                  2,School B,25,30,20,15,10
                  3,School C,20,25,15,10,20
                  4,School D,15,20,30,25,25
                  5,School E,35,40,5,5,5"""

    df = pl.read_csv(StringIO(csv_data))
    try:
        PiePlot(df, "International students (%)", "School Name")
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Pie plot failed: {e}")

    assert plot_success, "Pie plot generation failed"
