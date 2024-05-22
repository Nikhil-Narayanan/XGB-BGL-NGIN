import pandas as pd 
from typing import Callable
import numpy as np
from category_encoders import OneHotEncoder
import librosa

"""
TODO:
Add Morlet Mexican Hat Columns IFF FFT does well
Consider Insulin etc.
"""

class FeatureEngine:
    def __init__(self,):
        self.training_data = pd.read_csv("cleaned_data/train_data.csv").iloc[:,1:]
        self.validation_data = pd.read_csv("cleaned_data/validation_data.csv").iloc[:,1:]
        self.test_data = pd.read_csv("cleaned_data/test_data.csv").iloc[:,1:]
        self.training_set, self.validation_set, self.test_set = pd.DataFrame(),  pd.DataFrame(),  pd.DataFrame()
        self.training_set = self.training_data.loc[:, ("id", "corresponding_day")]
        self.validation_set = self.validation_data.loc[:, ("id", "corresponding_day")]
        self.test_set = self.test_data.loc[:, ("id", "corresponding_day")]
        self.training_labels = self.training_data.loc[:, 'hypo']
        self.validation_labels = self.validation_data.loc[:, 'hypo']
        self.test_labels = self.test_data.loc[:, 'hypo']
        self.demographic_set = pd.read_csv("Data Tables/HScreening.txt", delimiter = '|')
        # FINAL HOUR DATA
        self.mean_median_diff()  #GOOD
        #self.mel_cepstral() #TODO
        #self.aggregate_window(self.spectral_decrease, "spectral_decrease", True) #TODO
        # NUMERICAL DATA
        #self.aggregate_window(self.gri, "gri")
        #self.aggregate_window(self.tbr, "tbr")
        #self.aggregate_window(self.tir, "tir")
        #self.aggregate_window(self.tar, "tar")
        #self.aggreggate_window(self.centroid, "centroid") #TODO
        #self.aggreggate_window(self.spectral_distance, "spectral_distance") #TODO
        #self.aggregate_window(self.ecdf_percentile, "ecdf_percentile") #TODO
        #self.aggregate_window(self.rolling_mean, "mean")
        #self.aggregate_window(self.rolling_deviation, "std")
        self.aggregate_window(self.fft_means, "fft_mean_coeffs") #GOOD
        # CATEGORICAL DATA
        self.add_demographics() #GOOD
        #self.add_dates()
        del self.training_set['id']
        del self.validation_set['id']
        del self.test_set['id']
        del self.training_set['corresponding_day']
        del self.validation_set['corresponding_day']
        del self.test_set['corresponding_day']
    
    def mean_median_diff(self,) -> None:
        time_columns = [col for col in self.training_data.columns if col >= '23:00:00'][2:-1]
        train_differences = self.training_data[time_columns].diff(axis=1).iloc[:, 1:]
        validation_differences = self.validation_data[time_columns].diff(axis=1).iloc[:, 1:]
        test_differences = self.test_data[time_columns].diff(axis=1).iloc[:, 1:]
        self.training_set['mean_diff'] = train_differences.mean(axis=1)
        self.validation_set['mean_diff'] = validation_differences.mean(axis=1)
        self.test_set['mean_diff'] = test_differences.mean(axis=1)
        self.training_set['median_diff'] = train_differences.median(axis=1)
        self.validation_set['median_diff'] = validation_differences.median(axis=1)
        self.test_set['median_diff'] = test_differences.median(axis=1)

    def mel_cepstral(self,) -> None:
        # Mel Ceptstral coefficients for last hour prior to sleep
        time_columns = [col for col in self.training_data.columns if col >= '23:00:00'][2:-1]
        final_hour_training = np.array(self.training_data[time_columns])
        final_hour_validation = np.array(self.validation_data[time_columns])
        final_hour_test = np.array(self.test_data[time_columns])
        self.mffcs_training = librosa.feature.mfcc(y=final_hour_training, sr=0.2, n_mfcc=1, n_fft=12, n_mels=8)
        self.mffcs_validation = librosa.feature.mfcc(y=final_hour_validation, sr=0.2, n_mfcc=1, n_fft=12, n_mels=8)
        self.mffcs_test = librosa.feature.mfcc(y=final_hour_test, sr=0.2, n_mfcc=1, n_fft=12, n_mels=8)
        #self.training_set['mffcs'] = mffcs_training
        #self.validation_set['mffcs'] = mffcs_validation
        #self.test_set['mffcs'] = mffcs_test

    def add_dates(self,) -> None:
        # Function to convert and encode dates for a given dataset
        def encode_dates(dataset):
            dataset['corresponding_day'] = pd.to_datetime(dataset['corresponding_day'])
            day_encoded = pd.get_dummies(dataset['corresponding_day'].dt.day, prefix='Day', dtype=int)
            month_encoded = pd.get_dummies(dataset['corresponding_day'].dt.month, prefix='Month', dtype=int)
            year_encoded = pd.get_dummies(dataset['corresponding_day'].dt.year, prefix='Year', dtype=int)
            
            # Drop the 'corresponding_day' column if you don't need it anymore
            dataset.drop(['corresponding_day'], axis=1, inplace=True)
            
            # Concatenate the one-hot encoded columns with the dataset
            return pd.concat([dataset, day_encoded, month_encoded, year_encoded], axis=1)
        
        # Apply the encoding function to each dataset
        self.training_set = encode_dates(self.training_set)
        self.validation_set= encode_dates(self.validation_set)
        self.test_set = encode_dates(self.test_set)
    
    def fft_means(self, arr:np.ndarray) -> np.ndarray:
        return fft(arr)
    
    def rolling_deviation(self, arr:np.ndarray) -> np.ndarray:
        return np.std(arr)
    
    def gri(self, arr:np.ndarray) -> np.ndarray:
        # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10563532/pdf/10.1177_19322968221085273.pdfa

        # Define the thresholds for the different categories
        vlow_threshold = 54
        low_threshold = 70
        high_threshold = 180
        vhigh_threshold = 250
        
        # Calculate the percentages for each category
        vlow_percentage = np.mean(arr < vlow_threshold)
        low_percentage = np.mean((arr >= vlow_threshold) & (arr < low_threshold))
        high_percentage = np.mean((arr >= high_threshold) & (arr < vhigh_threshold))
        vhigh_percentage = np.mean(arr >= vhigh_threshold)
        
        # Calculate the GRI according to the formula
        gri_value = (3.0 * vlow_percentage) + (2.4 * low_percentage) \
                    + (1.6 * vhigh_percentage) + (0.8 * high_percentage)
        
        return gri_value
        
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
        Encode them using one-hot encoding and quantile encoding for continuous variables.
        """
        # Columns to merge
        columns_to_merge = [
            'PtID', 'Gender', 'Ethnicity', 'Race', 'SHMostRec', 'SHNumLast12Mon', 'DKAMostRec', 'DKANumLast12Mon',
            'OthGlucLowerMed', 'PEAbnormal', 'Weight', 'Height'
        ]

        # Filter the demographic set to include only the necessary columns
        demographics = self.demographic_set[columns_to_merge].copy()

        # Prepare the one-hot encoder
        encoder = OneHotEncoder(cols=['Gender', 'Ethnicity', 'Race', 'SHMostRec', 'SHNumLast12Mon', 'DKAMostRec', 'DKANumLast12Mon', 'OthGlucLowerMed', 'PEAbnormal'], use_cat_names=True)

        # Fit and transform the encoder on the demographic data (excluding 'Weight' and 'Height')
        demographics_encoded = encoder.fit_transform(demographics.drop(columns=['Weight', 'Height']))

        demographics.loc[:, 'Weight_bin'] = pd.cut(demographics['Weight'], bins=6, labels=False)
        demographics.loc[:, 'Height_bin'] = pd.cut(demographics['Height'], bins=6, labels=False)
         # Prepare one-hot encoder for the binned 'Weight' and 'Height'
        binned_encoder = OneHotEncoder(cols=['Weight_bin', 'Height_bin'], use_cat_names=True)
        demographics_binned_encoded = binned_encoder.fit_transform(demographics[['Weight_bin', 'Height_bin']])

        # Merge the quantile transformed 'Weight' and 'Height' with the one-hot encoded data
        demographics_encoded = pd.concat([demographics_encoded, demographics_binned_encoded], axis=1)

        # Merge the encoded demographic data with each dataset
        self.training_set = self.training_set.merge(demographics_encoded, how='left', left_on='id', right_on='PtID')
        self.validation_set = self.validation_set.merge(demographics_encoded, how='left', left_on='id', right_on='PtID')
        self.test_set = self.test_set.merge(demographics_encoded, how='left', left_on='id', right_on='PtID')

        del self.training_set['PtID']
        del self.validation_set['PtID']
        del self.test_set['PtID']

    def aggregate_window(self, func: Callable, func_name: str, final_hour: bool = False) -> None:
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
        if final_hour:
            time_windows = {'last_1_hour': 60,}

        # Convert the column names to a format we can perform calculations on (number of minutes since 06:00:00)

        stamps = self.training_data.columns[2:218]
        
        times = pd.to_timedelta(stamps).total_seconds()/60  # Convert to minutes

        def compute_mean_frequency(signal, fs):
            fft_values = np.fft.fft(signal)
            fft_freqs = np.fft.fftfreq(len(signal), 1.0/fs)
            positive_freqs = fft_freqs[:len(signal)//2]
            positive_fft_values = fft_values[:len(signal)//2]
            power_spectrum = np.abs(positive_fft_values) ** 2
            mean_frequency = np.sum(positive_freqs * power_spectrum) / np.sum(power_spectrum)
            return mean_frequency

        # Apply the aggregation function over specified time windows
        for window_name, minutes in time_windows.items():
            # Find the time range for each window
            max_time = times.max()
            min_time = max_time - minutes

            # Get columns that fall within the current time window
            columns_to_aggregate = [time for time in stamps if min_time < pd.to_timedelta(time).total_seconds()/60 <= max_time]

            if func == self.fft_means:
                # Process FFT and store mean frequencies in new DataFrames
                mean_freq_data_train = {}
                mean_freq_data_valid = {}
                mean_freq_data_test = {}

                fs = 0.2  # 1 reading every 5 minutes
                compute_mean_freq_func = lambda x: compute_mean_frequency(x, fs)
                
                mean_freq_results_train = np.apply_along_axis(compute_mean_freq_func, 1, self.training_data[columns_to_aggregate].values)
                mean_freq_results_valid = np.apply_along_axis(compute_mean_freq_func, 1, self.validation_data[columns_to_aggregate].values)
                mean_freq_results_test = np.apply_along_axis(compute_mean_freq_func, 1, self.test_data[columns_to_aggregate].values)

                mean_freq_data_train[f'{func_name}_{window_name}_mean_freq'] = mean_freq_results_train
                mean_freq_data_valid[f'{func_name}_{window_name}_mean_freq'] = mean_freq_results_valid
                mean_freq_data_test[f'{func_name}_{window_name}_mean_freq'] = mean_freq_results_test
                
                # Convert dictionary to DataFrame and concatenate
                new_train_df = pd.DataFrame(mean_freq_data_train)
                new_valid_df = pd.DataFrame(mean_freq_data_valid)
                new_test_df = pd.DataFrame(mean_freq_data_test)

                self.training_set = pd.concat([self.training_set, new_train_df], axis=1)
                self.validation_set = pd.concat([self.validation_set, new_valid_df], axis=1)
                self.test_set = pd.concat([self.test_set, new_test_df], axis=1)
                
            else:
                # Apply the function to the selected columns and store in a new column
                self.training_set[f'{func_name}_{window_name}'] = self.training_data[columns_to_aggregate].apply(func, axis=1)
                self.validation_set[f'{func_name}_{window_name}'] = self.validation_data[columns_to_aggregate].apply(func, axis=1)
                self.test_set[f'{func_name}_{window_name}'] = self.test_data[columns_to_aggregate].apply(func, axis=1)