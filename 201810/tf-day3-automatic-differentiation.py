# encoding: utf-8
# Created tf-day3-automatic-differentiation by wym at 2018/10/11
import sys; print('Python %s on %s' % (sys.version, sys.platform))
import tensorflow as tf
tf.enable_eager_execution()
tfe = tf.contrib.eager
from math import pi
def f(x):
  return tf.square(tf.sin(x))
def grad(f):
  return lambda x: tfe.gradients_function(f)(x)[0]
x = tf.lin_space(-2*pi, 2*pi, 100)  # 100 points between -2π and +2π
import matplotlib.pyplot as plt
plt.plot(x, f(x), label="f")
plt.plot(x, grad(f)(x), label="first derivative")
plt.plot(x, grad(grad(f))(x), label="second derivative")
plt.plot(x, grad(grad(grad(f)))(x), label="third derivative")
plt.legend()
plt.show()
