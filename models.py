import tensorflow as tf



class MeterModel:


	def inference(x,drop_prob):

		with tf.variable_scope('hidden1'):
			conv = tf.layers.conv2d(x,filters=32,kernel_size=[5,5],padding='SAME')
			activation = tf.nn.relu(conv)
			pool = tf.layers.max_pooling2d(activation,pool_size=[2,2],stride=2,padding='same')
			dropout = tf.layers.dropout(pool, rate=drop_prob)
			hidden1 = dropout

		with tf.variable_scope('hidden2'):
			conv = tf.layers.conv2d(hidden1, filters=64,kernel_size=[5,5],padding='same')
			activation = tf.nn.relu(conv)
			pool = tf.layers.max_pooling2d(activation,pool_size=[2,2],stride=2,padding='same')
			dropout = tf.layers.dropout(pool, rate=drop_prob)
			hidden2 = dropout

		with tf.variable_scope('hidden3'):
			conv = tf.layers.conv2d(hidden2, filters=128, kernel_size=[5,5],padding='same')
			activation = tf.nn.relu(conv)
			pool = tf.layers.max_pooling2d(activation,pool_size=[2,2],stride=2,padding='same')
			dropout = tf.layers.dropout(pool,rate=drop_prob)
			hidden3 = dropout

		flatten = tf.reshape(hidden3,[-1,12 * 12 * 128])

		with tf.variable_scope('hidden4'):
			dense = tf.layers.dense(flatten,units=1024,activation=tf.nn.relu)
			hidden4 = dense

		with tf.variable_scope('output'):
			dense = tf.layers.dense(hidden4,units=2)
			output = dense

		return output

	def loss(output_logits,labels):
		loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=labels,logits=output_logits))
		return loss

