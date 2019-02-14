from keras.layers import Input, Flatten, Reshape


x = Input(batch_shape=(16, 10))
print(x)

#x = Input(batch_shape=(16, 10))
#x = Flatten()(x)
#print(x)

x = Input(batch_shape=(16, 10, 10))
x = Reshape((-1,))(x)
print(x)