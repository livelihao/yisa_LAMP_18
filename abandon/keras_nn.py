import os
import time
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
import tensorflow as tf
from imblearn.over_sampling import SMOTE

bottlenecks = pd.read_csv('./bottlenecks.csv')
targets = pd.read_csv('./target.csv')
daibao = targets['daibao']
kouzhao = targets['kouzhao']
laxiang = targets['laxiang']
maozi = targets['maozi']
yanjing = targets['yanjing']

RANDOM_STATE = 500
OP_RATE = 0.01
batch_size = 32

def get_batch(x,y,batch):
    n_samples = len(x)
    for i in range(batch, n_samples, batch):
        yield x[i-batch:i], y[i-batch:i]
smo = SMOTE(random_state=RANDOM_STATE)
X_smo, y_smo = smo.fit_sample(bottlenecks, laxiang)

X_train, X_test, y_db_train, y_db_test = train_test_split(X_smo, y_smo, test_size=0.15, random_state=RANDOM_STATE)
# ss = StandardScaler()
# X_train = ss.fit_transform(X_train)
# X_test = ss.transform(X_test)

n_features = 2048; n_classes = 2
x_input = tf.placeholder(tf.float32, shape=[None, 2048], name='input')
y_input = tf.placeholder(tf.int32, shape=[None])
W = tf.Variable(tf.truncated_normal([n_features, n_classes]))
b = tf.Variable(tf.zeros([n_classes]))

logits = tf.sigmoid(tf.matmul(x_input, W)+b)
predict = tf.arg_max(logits, 1, name='predict')
loss = tf.losses.sparse_softmax_cross_entropy(logits=logits, labels=y_input)
loss = tf.reduce_mean(loss)
tf.summary.scalar('loss', loss)
optimizer = tf.train.AdamOptimizer(OP_RATE).minimize(loss)
acc, acc_op = tf.metrics.accuracy(labels=y_input, predictions=predict)
tf.summary.scalar('acc', acc_op)
merge_summary = tf.summary.merge_all()

with tf.Session() as sess:
    train_writer = tf.summary.FileWriter('log', sess.graph)
    saver = tf.train.Saver(max_to_keep=4)
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    step = 0
    for epoch in range(100):
        for tx,ty in get_batch(X_train, y_db_train, batch_size):
            step += 1
            loss_value, _, acc_value, train_summary = sess.run([loss, optimizer, acc_op, merge_summary],
                                                               feed_dict={x_input: tx, y_input: ty})
            train_writer.add_summary(train_summary, step)
            if step % 100 == 0:
                saver.save(sess, 'Model/model', global_step=step)
            print('loss = {}, acc = {}'.format(loss_value, acc_value))
        acc_value = sess.run([acc_op], feed_dict={x_input: X_test, y_input: y_db_test})
        print('val acc = {}'.format(acc_value))



