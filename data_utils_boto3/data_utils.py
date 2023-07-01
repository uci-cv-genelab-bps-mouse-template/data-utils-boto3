"""
Data utility functions for downloading directly from the AWS Bucket for the BPS Microscopy Benchmark Training Dataset
https://registry.opendata.aws/bps_microscopy/

Authors: Nadia Ahmed & Jacob Campbell
"""
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import io
from io import BytesIO
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import pyprojroot
import sys
sys.path.append(str(pyprojroot.here()))

def get_bytesio_from_s3(
    s3_client: boto3.client, bucket_name: str, file_path: str
) -> BytesIO:
    """
    This function retrieves individual files from a specific aws s3 bucket blob/file path as
    a BytesIO object to enable the user to not have to save the file to their local machine.

    args:
        s3_client (boto3.client): s3 client should be configured for open UNSIGNED signature.
        bucket_name (str): name of bucket from AWS open source registry.
        file_path (str): blob/file path name from aws including file name and extension.

    returns:
        BytesIO: BytesIO object from the file contents
    """
    raise NotImplementedError

def get_file_from_s3(
    s3_client: boto3.client, bucket_name: str, s3_file_path: str, local_file_path: str
) -> str:
    """
    This function retrieves individual files from a specific aws s3 bucket blob/file path and
    saves the files of interest to a local filepath on the user's machine.

    args:
      s3_client (boto3.client): s3 client should be configured for open UNSIGNED signature.
      bucket_name (str): name of bucket from AWS open source registry.
      s3_file_path (str): full blob/file path name from aws including file name and extension.
      local_file_path (str): user's local directory.

    returns:
      str: local file path with naming convention of the file that was downloaded from s3 bucket
    """
    raise NotImplementedError

def save_tiffs_local_from_s3(
    s3_client: boto3.client,
    bucket_name: str,
    s3_path: str,
    local_fnames_meta_path: str,
    save_file_path: str,
) -> None:
    """
    This function retrieves tiff files from a locally stored csv file containing specific aws s3 bucket
    filenames, constructs the appropriate paths to retrieve the files of interest locally to the user's 
    machine following the same naming convention as the files from s3.

    args:
      s3_client (boto3.client): s3 client should be configured for open UNSIGNED signature.
      bucket_name (str): name of bucket from AWS open source registry.
      s3_path (str): blob/file directory where files of interest reside in s3 from AWS
      local_fnames_meta_path (str): file path for user's local directory containing the csv file containing the filenames
      save_file_path (str): file path for user's local directory where files of interest will be saved
    returns:
      None
    """
    raise NotImplementedError

def export_subset_meta_dose_hr(
    dose_Gy_specifier: list,
    hr_post_exposure_val: list,
    in_csv_path_local: str,
    out_dir_csv: str
) -> tuple:
    """
    This function opens a csv file that contains the filenames of the bps microscopy data from the 
    s3 bucket saved either locally or as a file_buffer object as a pandas dataframe. The dataframe
    is then sliced over the attributes of interest and written to another csv file for data 
    versioning.

    args:
      dose_Gy (list): dose_Gy is a list of string(s) corresponding to the dose(s) of interest ['hi', 'med', 'low']
      hr_post_exposure_val (list): hr_post_exposure_val is a list of integer(s) corresponding to the hour(s) post 
      exposure of interest [4, 24, 48]
      in_csv_path_local (str): a string of input original csv file
      out_dir_csv (str): a string of the output directory you would like to write the subset_meta file to

    returns:
      Tuple[str, int]: a tuple of the output csv file path and the number of rows in the output csv 
      file
    """
    raise NotImplementedError

def train_test_split_subset_meta_dose_hr(
        subset_meta_dose_hr_csv_path: str,
        test_size: float,
        out_dir_csv: str,
        random_state: int = None,
        stratify_col: str = None
        ) -> tuple:
    """
    This function reads in a csv file containing the filenames of the bps microscopy data for
    a subset selected by the dose_Gy and hr_post_exposure attributes. The function then opens
    the file as a pandas dataframe and splits the dataframe into train and test sets using
    sklearn.model_selection.train_test_split. The train and test dataframes are then exported
    to csv files in the same directory as the input csv file.

    args:
        subset_meta_dose_hr_csv_path (str): a string of the input csv file path (full path includes filename)
        test_size (float or int): a float between 0 and 1 corresponding to the proportion of the data
        that should be in the test set. If int, represents the absolute number of test samples.
        out_dir_csv (str): a string of the output directory you would like to write the train and test
        random_state (int, RandomState instance or None, optional): controls the shuffling
        applied to the data before applying the split. Pass an int for reproducible output
        across multiple function calls.
        stratify (array-like or None, optional): array containing the labels for stratification. 
        Default: None.
    returns:
        Tuple[str, str]: a tuple of the output csv file paths for the train and test sets
    """
    return NotImplementedError
