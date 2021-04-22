import unittest
import main

class StockTests_DisneyStyle(unittest.TestCase):

    def test_is_capitlized_or_alphacharacter(self):
        self.assertEqual(main.tickerSymboltoUpper("DIS"), "DIS")
        self.assertEqual(main.tickerSymboltoUpper("dis"), "DIS")
        self.assertEqual(main.tickerSymbolcheckLength("Disney"), True)
        self.assertEqual(main.tickerSymbolcheckLength("f"), True)
        self.assertEqual(main.tickerSymbolcheckLength(""), False)
        self.assertEqual(main.tickerSymbolcheckLength("Splash Mountain"), False)
        self.assertEqual(main.tickerSymbolAlpha("belle"), True)
        self.assertEqual(main.tickerSymbolAlpha("1"), False)
        self.assertEqual(main.tickerSymbolAlpha("#"), False)

    def test_is_charttype(self):
        self.assertEqual(main.isChartCorrect(1), False)
        self.assertEqual(main.isChartCorrect(2), False)
        self.assertEqual(main.isChartCorrect(3), True)

    def test_is_timeseries(self):
        self.assertEqual(main.isTimeCorrect(1), False)
        self.assertEqual(main.isTimeCorrect(2), False)
        self.assertEqual(main.isTimeCorrect(3), False)
        self.assertEqual(main.isTimeCorrect(4), False)
        self.assertEqual(main.isTimeCorrect(-1), True)
        self.assertEqual(main.isTimeCorrect(10), True)

    def test_is_startdate(self):
        self.assertEqual(main.validate("2021-04-22"), True)
        self.assertEqual(main.validate("1955-07-17"), True)
        self.assertEqual(main.validate("21-04-25"), False)
        self.assertEqual(main.validate("1965-8-01"), False)
        self.assertEqual(main.validate("2007-04-7"), False)
        self.assertEqual(main.validate("75-1-15"), False)

if __name__ == "__main__":
    unittest.main()
