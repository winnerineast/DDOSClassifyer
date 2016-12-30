import tensorflow as tf

filename_queue = tf.train.string_input_producer(["2777.csv"])

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
record_defaults = [[""], [""], [""], [""], [""],[""],[""],[""],[""],[""]];
col1, col2, col3, col4, col5, col6, col7, col8,col9,col10  = tf.decode_csv(value, record_defaults=record_defaults);
features = tf.pack([col4, col5, col6, col7,col8,col9]);

with tf.Session() as sess:
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)

  for i in range(1200):
      example, label = sess.run([features, col8]);
      print(label);

  coord.request_stop()
  coord.join(threads)