dimension=0 按列找 
dimension=1 按行找 
tf.argmax()返回最大数值的下标 
通常和tf.equal()一起使用，计算模型准确度

correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
1
2
栗子

>>> import tensorflow as tf
>>> a = tf.constant([1.,2.,3.,0.,9.,])
>>> b = tf.constant([[1,2,3],[3,2,1],[4,5,6],[6,5,4]])
>>> with tf.Session() as sess:
...     sess.run(tf.argmax(a, 0))
Output:
4
>>> with tf.Session() as sess:
...     sess.run(tf.argmax(b, 0))
Output:
array([3, 2, 2])
>>> with tf.Session() as sess:
...     sess.run(tf.argmax(b, 1))
Output:
array([2, 0, 2, 0])