"""
splitting.py
"""
import pandas as pd
import sklearn.model_selection as sms


class Splitting:
    """
    Class Splitting
    """

    def __init__(self, random_state: int):
        """
        Constructor
        """

        self.__random_state = random_state

    def __splitting(self, independent: pd.DataFrame, dependent: pd.DataFrame,
                    train_size: float, stratify=None) -> (pd.DataFrame, pd.DataFrame):
        """

        :param independent:
        :param dependent:
        :param train_size:
        :param stratify:
        :return:
        """

        x_training: pd.DataFrame
        x_testing: pd.DataFrame
        y_training: pd.DataFrame
        y_testing: pd.DataFrame
        x_training, x_testing, y_training, y_testing = sms.train_test_split(
            independent, dependent, train_size=train_size, random_state=self.__random_state, stratify=stratify)

        training = x_training.join(y_training)
        testing = x_testing.join(y_testing)

        return training, testing

    def exc(self, independent: pd.DataFrame, dependent: pd.DataFrame,
            train_size: float, stratify=None) -> (pd.DataFrame, pd.DataFrame):
        """
        Stratified splitting of a dataset

        :param independent:
        :param dependent:
        :param train_size:
        :param stratify:
        :return:
            training: pandas.DataFrame
            testing: pandas.DataFrame
        """

        return self.__splitting(independent=independent, dependent=dependent,
                                train_size=train_size, stratify=stratify)
