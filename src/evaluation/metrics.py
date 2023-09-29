"""
About metrics
"""
import tensorboard.plugins.hparams.api as hp
import tensorflow as tf


class Metrics:
    """
    The Metrics class
    """

    def __init__(self):
        self.name = 'Metrics'

    @staticmethod
    def definitions_keras():
        """
        The metrics definitions via keras

        :return:
        """

        metrics = [tf.keras.metrics.TruePositives(name='tp'),
                   tf.keras.metrics.FalsePositives(name='fp'),
                   tf.keras.metrics.TrueNegatives(name='tn'),
                   tf.keras.metrics.FalseNegatives(name='fn'),
                   tf.keras.metrics.Precision(name='precision'),
                   tf.keras.metrics.Recall(name='recall'),
                   tf.keras.metrics.AUC(name='auc'),
                   tf.keras.metrics.F1Score(name='f_score')]

        return metrics

    @staticmethod
    def definitions_tensorflow():
        """
        The metrics definitions via tensorflow

        :return:
        """

        metrics = [hp.Metric('tp'),
                   hp.Metric('fp'),
                   hp.Metric('tn'),
                   hp.Metric('fn'),
                   hp.Metric('precision'),
                   hp.Metric('recall'),
                   hp.Metric('auc')]

        return metrics
 