"""Small helper module providing TF1-style input placeholders with lazy imports.
This avoids importing TensorFlow at module import time which can cause issues in some environments.
"""

from typing import Tuple


def neural_net_image_input(image_shape: Tuple[int, int, int]):
    """Return a TF placeholder named 'x' with shape [None, *image_shape].
    Lazy-imports TensorFlow when called.
    """
    import tensorflow.compat.v1 as tf
    try:
        tf.disable_v2_behavior()
    except Exception:
        pass
    return tf.placeholder(tf.float32, [None, *image_shape], name='x')


def neural_net_label_input(n_classes: int):
    """Return a TF placeholder named 'y' with shape [None, n_classes].
    Lazy-imports TensorFlow when called.
    """
    import tensorflow.compat.v1 as tf
    try:
        tf.disable_v2_behavior()
    except Exception:
        pass
    return tf.placeholder(tf.float32, [None, n_classes], name='y')


def neural_net_keep_prob_input():
    """Return a TF placeholder named 'keep_prob' (scalar).
    Lazy-imports TensorFlow when called.
    """
    import tensorflow.compat.v1 as tf
    try:
        tf.disable_v2_behavior()
    except Exception:
        pass
    return tf.placeholder(tf.float32, name='keep_prob')
