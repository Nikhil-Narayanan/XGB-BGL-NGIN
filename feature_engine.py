import pandas as pd 
from typing import Callable
import numpy as np
from scipy.fft import fft
from category_encoders import OneHotEncoder

class FeatureEngine:
    def __init__(self,):
        self.training_set = pd.read_csv("cleaned_data/train_data.csv")
        self.validation_set = pd.read_csv("cleaned_data/validation_data.csv")
        self.test_set = pd.read_csv("cleaned_data/test_data.csv")
        self.demographic_set = pd.read_csv("Data Tables/HScreening.txt", delimiter = '|')
        self.time_series = pd.read_csv("Experimental_Notebooks/resampled_day.csv")
        self.aggregate_window(self.tar, "tar")
        self.aggregate_window(self.tbr, "tbr")
        self.aggregate_window(self.rolling_mean, "mean")
        self.aggregate_window(self.rolling_deviation, "std")
        self.aggregate_window(self.tir, "tir")
        self.aggregate_window(self.fft, "fft")
        self.add_demographics()


    
    def fft(self, arr:np.ndarray) -> np.ndarray:
        return fft(arr)
    
    def rolling_deviation(self, arr:np.ndarray) -> np.ndarray:
        return np.std(arr)
    
    def tar(self, arr: np.ndarray) -> np.ndarray:
        mask = arr > 180
        return np.mean(mask)
    
    def tir(self, arr: np.ndarray) -> np.ndarray:
        mask = (arr >= 70) & (arr <= 180)
        return np.mean(mask)
    
    def tbr(self, arr: np.ndarray) -> np.ndarray:
        mask = arr < 70
        return np.mean(mask)
    
    def rolling_mean(self, arr: np.ndarray) -> np.ndarray:
        return np.mean(arr)

    def add_demographics(self) -> None:
        """
        Merge selected demographic features into the training, validation, and test sets.
        Encode them using one-hot encoding.
        """
        # Columns to merge
        columns_to_merge = [
            'PtID', 'Gender', 'Ethnicity', 'Race', 'SHMostRec', 'SHNumLast12Mon', 'DKAMostRec', 'DKANumLast12Mon',
            'OthGlucLowerMed', 'Weight', 'Height', 'PEAbnormal'
        ]

        # Filter the demographic set to include only the necessary columns
        demographics = self.demographic_set[columns_to_merge]

        # Prepare the encoder
        encoder = OneHotEncoder(cols=['Gender', 'Ethnicity', 'Race', 'SHMostRec', 'SHNumLast12Mon', 'DKAMostRec', 'DKANumLast12Mon', 'OthGlucLowerMed', 'PEAbnormal'], use_cat_names=True)

        # Fit and transform the encoder on the demographic data
        demographics_encoded = encoder.fit_transform(demographics)

        # Merge the encoded demographic data with each dataset
        self.training_set = self.training_set.merge(demographics_encoded, how='left', left_on='id', right_on='PtID')
        self.validation_set = self.validation_set.merge(demographics_encoded, how='left', left_on='id', right_on='PtID')
        self.test_set = self.test_set.merge(demographics_encoded, how='left', left_on='id', right_on='PtID')

    def aggregate_window(self, func: Callable, func_name: str) -> None:
        """
        Apply func over various window sizes and add columns to training and validation sets for the output of these aggregate functions
        
        Args:
        func (Callable): A function to apply to each aggregate window.
        func_name (str): The name of the function, used to create new column names.
        """
        # Define the time intervals in minutes for aggregation
        time_windows = {
            'last_10_minutes': 10,
            'last_30_minutes': 30,
            'last_1_hour': 60,
            'last_3_hours': 180,
            'last_6_hours': 360,
            'last_12_hours': 720
        }

        # Convert the column names to a format we can perform calculations on (number of minutes since 06:00:00)

        stamps = self.training_set.columns[6:222]
        
        times = pd.to_timedelta(stamps).total_seconds()/60  # Convert to minutes

        # Apply the aggregation function over specified time windows
        for window_name, minutes in time_windows.items():
            # Find the time range for each window
            max_time = times.max()
            min_time = max_time - minutes

            # Get columns that fall within the current time window
            columns_to_aggregate = [time for time in stamps if min_time < pd.to_timedelta(time).total_seconds()/60 <= max_time]

            if func == self.fft:
                # Process FFT and store results in new DataFrames
                fft_data_train = {}
                fft_data_valid = {}
                fft_data_test = {}

                fft_results_train = np.apply_along_axis(func, 1, self.training_set[columns_to_aggregate].values)
                fft_results_valid = np.apply_along_axis(func, 1, self.validation_set[columns_to_aggregate].values)
                fft_results_test = np.apply_along_axis(func, 1, self.test_set[columns_to_aggregate].values)

                for i in range(fft_results_train.shape[1]):
                    fft_data_train[f'{func_name}_{window_name}_real_{i}'] = fft_results_train[:, i].real
                    fft_data_train[f'{func_name}_{window_name}_imag_{i}'] = fft_results_train[:, i].imag
                    fft_data_valid[f'{func_name}_{window_name}_real_{i}'] = fft_results_valid[:, i].real
                    fft_data_valid[f'{func_name}_{window_name}_imag_{i}'] = fft_results_valid[:, i].imag
                    fft_data_test[f'{func_name}_{window_name}_real_{i}'] = fft_results_test[:, i].real
                    fft_data_test[f'{func_name}_{window_name}_imag_{i}'] = fft_results_test[:, i].imag
                
                # Convert dictionary to DataFrame and concatenate
                new_train_df = pd.DataFrame(fft_data_train)
                new_valid_df = pd.DataFrame(fft_data_valid)
                new_test_df = pd.DataFrame(fft_data_test)

                self.training_set = pd.concat([self.training_set, new_train_df], axis=1)
                self.validation_set = pd.concat([self.validation_set, new_valid_df], axis=1)
                self.test_set = pd.concat([self.test_set, new_test_df], axis=1)
                
            else:
                # Apply the function to the selected columns and store in a new column
                self.training_set[f'{func_name}_{window_name}'] = self.training_set[columns_to_aggregate].apply(func, axis=1)
                self.validation_set[f'{func_name}_{window_name}'] = self.validation_set[columns_to_aggregate].apply(func, axis=1)
                self.test_set[f'{func_name}_{window_name}'] = self.test_set[columns_to_aggregate].apply(func, axis=1)