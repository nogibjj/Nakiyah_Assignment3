import polars as pl
from io import StringIO
from mylib.lib import (
    readData,
    cleanData,
    summaryStatistics,
    PiePlot,
    tripleBarPlot,
)

"""
Test Functions for data processing and visualization functions
"""

def test_readData():
    data = readData("FT Global Business School MBA Ranking 2024.csv")
    assert isinstance(data, pl.DataFrame), "readData should return a Polars DataFrame"
    assert data.height > 0, "DataFrame should not be empty"

def test_cleanData():
    # Assuming readData is already called
    raw_data = readData("FT Global Business School MBA Ranking 2024.csv")
    cleaned_data = cleanData(raw_data, "#", ["#", "School Name"], 10)
    
    assert isinstance(cleaned_data, pl.DataFrame), "cleanData should return a Polars DataFrame"
    assert all(col in cleaned_data.columns for col in ["#", "School Name"]), "Cleaned DataFrame should include specified columns"
    assert cleaned_data.select(pl.col("#").n_unique()).to_numpy()[0] <= 10, "Number of unique ranks should be limited to requiredrank"

def test_summaryStatistics():
    raw_data = readData("FT Global Business School MBA Ranking 2024.csv")
    stats = summaryStatistics(raw_data, ["Value for money rank", "Salary percentage increase", "Overall satisfaction **"])
    
    assert isinstance(stats, dict), "summaryStatistics should return a dictionary"
    assert all(key in stats for key in ["Value for money rank", "Salary percentage increase", "Overall satisfaction **"]), "Summary stats should contain specified keys"

def test_PiePlot():
    raw_data = readData("FT Global Business School MBA Ranking 2024.csv")
    cleaned_data = cleanData(raw_data, "#", ["#", "School Name", "International students (%)"], 10)
    pie_plot = PiePlot(cleaned_data, "International students (%)", "School Name")
    
    assert pie_plot is not None, "PiePlot should return a plot object"
    # Additional assertions can be added based on the plotting library used

def test_tripleBarPlot():
    raw_data = readData("FT Global Business School MBA Ranking 2024.csv")
    cleaned_data = cleanData(raw_data, "#", ["#", "School Name", "Value for money rank", "Career progress rank", "Careers service rank"], 10)
    bar_chart = tripleBarPlot(cleaned_data, "School Name", ("Value for money rank", "Career progress rank", "Careers service rank"))
    
    assert bar_chart is not None, "tripleBarPlot should return a plot object"
    # Additional assertions can be added based on the plotting library used

# Running tests
if __name__ == "__main__":
    test_readData()
    test_cleanData()
    test_summaryStatistics()
    test_PiePlot()
    test_tripleBarPlot()
    print("All tests passed!")
