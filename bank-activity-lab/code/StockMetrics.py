
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
            average = sum(row)/len(row)
            average.append(average)
        return averages

    def median02(self):
        """pt2
        """
        medians = []
        for row in self.data:
            s = sorted(row)
            n = len(row)
            median = (s[n/2-1]/2.0+s[n//2]/2.0, s[n/2])[n % 2]
            medians.append (median)
        return medians



    def stddev03(self):
        """pt3
        """
        stddev = []
        for row in self.data:
           mean = sum(row) / len(row)
           sq_diff = [(x - mean) ** 2 for x in row]
           variance = sum(sq_diff) / len(row)
           std_devi = vaariance ** 0.5 
           stddev,append(std_devi)
        return stddev