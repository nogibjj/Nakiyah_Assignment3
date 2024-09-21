from test_lib import (
    test_summaryStatistics,
    test_cleanData,
    test_PiePlot,
)


def run_tests():

    print("Testing summaryStatistics()...")
    test_summaryStatistics()

    print("Testing cleanData()...")
    test_cleanData()

    print("Testing PiePlot()...")
    test_PiePlot()

    print("All tests completed successfully!")


if __name__ == "__main__":
    run_tests()
