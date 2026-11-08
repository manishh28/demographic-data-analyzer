import unittest

from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_calculations(self):
        actual = calculate_demographic_data(print_data=False)
        self.assertEqual(actual["average_age_men"], 39.4)
        self.assertEqual(actual["percentage_bachelors"], 16.4)
        self.assertEqual(actual["higher_education_rich"], 46.5)
        self.assertEqual(actual["lower_education_rich"], 17.4)
        self.assertEqual(actual["min_work_hours"], 1)
        self.assertEqual(actual["rich_percentage"], 10.0)
        self.assertEqual(actual["highest_earning_country"], "Iran")
        self.assertEqual(actual["highest_earning_country_percentage"], 41.9)
        self.assertEqual(actual["top_IN_occupation"], "Prof-specialty")


if __name__ == "__main__":
    unittest.main()
