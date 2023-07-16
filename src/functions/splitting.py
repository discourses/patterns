"""
splitting.py
"""
import pandas as pd
import sklearn.model_selection as sms


class Splitting:
    """
    Class Splitting
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def exc(independent: pd.DataFrame, dependent: pd.DataFrame,
            train_size: float, random_state: int, stratify=None) -> (pd.DataFrame, pd.DataFrame,
                                                                     pd.DataFrame, pd.DataFrame):
        """
        Stratified splitting of a dataset

        :param independent:
        :param dependent:
        :param train_size:
        :param random_state:
        :param stratify:
        :return:
        """

        return sms.train_test_split(independent, dependent, train_size=train_size,
                                    random_state=random_state, stratify=stratify)
