import pandas as pd
from unittest import TestCase
from unittest.mock import MagicMock
from utils.prepare_data import DataPreparation

class TestDataPreparation(TestCase):
    def test_remove_outliers_no_outliers(self):
        df = pd.DataFrame({'Trip Duration': [10, 20, 30]})
        expected_output = df.copy()
        data_prep = DataPreparation()
        output = data_prep.remove_outliers(df)
        pd.testing.assert_frame_equal(output, expected_output)

    def test_remove_outliers_with_outliers(self):
        df = pd.DataFrame({'Trip Duration': [10, 20, 1000]})
        expected_output = pd.DataFrame({'Trip Duration': [10, 20]})
        data_prep = DataPreparation()
        output = data_prep.remove_outliers(df)
        pd.testing.assert_frame_equal(output, expected_output)

    def test_remove_outliers_with_multiple_outliers(self):
        df = pd.DataFrame({'Trip Duration': [10, 20, 1000, 10000]})
        expected_output = pd.DataFrame({'Trip Duration': [10, 20]})
        data_prep = DataPreparation()
        output = data_prep.remove_outliers(df)
        pd.testing.assert_frame_equal(output, expected_output)