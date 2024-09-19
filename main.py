from mylib.lib import (
    readData,
    cleanData,
    summaryStatistics,
    PiePlot,
    tripleBarPlot,
)

Data = "FT Global Business School MBA Ranking 2024.csv"
ReadData = readData(Data)


ColumnsWantedForSummaryStats = [
    "Value for money rank",
    "Salary percentage increase",
    "Overall satisfaction **",
]
SummaryStatistics = summaryStatistics(ReadData, ColumnsWantedForSummaryStats)
print(SummaryStatistics)


ColumnsForDataset = [
    "#",
    "School Name",
    "International students (%)",
    "International faculty (%)",
    "Value for money rank",
    "Career progress rank",
    "Careers service rank",
]
Rank = "#"  # Column for sorting
requiredrank = 10
PctIntlStudents = "International students (%)"
PctIntlFaculty = "International faculty (%)"
SchoolName = "School Name"
RankNames = "Value for money rank", "Career progress rank", "Careers service rank"

CleanData = cleanData(ReadData, Rank, ColumnsForDataset, requiredrank)
piePlotStudents = PiePlot(CleanData, PctIntlStudents, SchoolName)
piePlotFaculty = PiePlot(CleanData, PctIntlFaculty, SchoolName)
BarChart = tripleBarPlot(CleanData, SchoolName, RankNames)
