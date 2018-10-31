import pickle

a = {'name': 'David', 'age': '64'}
b = ['aa', 'bb', 'cc']
p_str = pickle.dumps(a)
print(p_str)

# Write the data into .txt file
with open('/Users/ouyang/Desktop/input.txt', 'wb') as file:
    pickle.dump(a, file)

# It store the data in a dictionary format,
# and it will also return a dictionary type after load()
with open('/Users/ouyang/Desktop/input.txt', 'rb') as file:
    data = pickle.load(file)
print(data)
print(type(data))
