import polars as pl
import matplotlib.pyplot as plt
import numpy as np

"""
Functions library (Polars version)
"""
# Function 1
def readData(df):
    return pl.read_csv(df, encoding="ISO-8859-1")

# Function 2
def summaryStatistics(df, Col):
    df = df[Col]
    SumStats = df.describe()
    Median = df.median()
    Mean = df.mean()
    return SumStats, Median, Mean

# Function 3
def cleanData(df, ColToSort, Columns, RanksRequired):
    df = df.with_columns(pl.col(ColToSort))
    df1 = df.sort(by=ColToSort)
    df1 = df1.select(Columns).head(RanksRequired)
    
    return df1

def PiePlot(df, col, labels_col):
    data = df.select([col, labels_col]).drop_nulls()
    data = data.sort(col, descending=True)
    values = data[col].to_numpy()
    labels = data[labels_col].to_list()
    
    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title(f"Breakdown of {col} by School", pad=40)
    plt.axis("equal")
    plt.show()
    
    return "Pie Chart displayed"

def tripleBarPlot(df, Col, RankCols):
    num_ranks = len(RankCols)
    universities = df.select(Col).to_series().to_list()  # Convert column to list of universities
    barWidth = 1 / (num_ranks + 1)
    r = np.arange(len(universities))

    for i, rank_col in enumerate(RankCols):
        # Select the rank column and convert to list
        ranks = df.select(rank_col).to_series().to_list()
        plt.bar(
            r + i * barWidth,
            ranks,
            width=barWidth,
            edgecolor="grey",
            label=rank_col,
        )

    plt.xlabel("Universities", fontweight="bold")
    plt.ylabel("Rank")
    plt.title("University Rank Comparison")
    plt.xticks(
        r + (num_ranks / 2 - 0.5) * barWidth, universities, rotation=45, ha="right"
    )
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()
    return "Chart"