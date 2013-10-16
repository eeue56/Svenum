try:
	xrange(5)
except:
	xrange = range


def generate_columns(filename):
	""" Generate the columns from the filename and return """
	columns = None

	with open(filename) as f:

		for line in f:
			print('lining')
			if columns is None:
				columns = [[] for _ in line.split(',')]

			for i, text in enumerate(line.strip().split(',')):
				columns[i].append(text) 
	print(columns)

	return columns

def shitty_hash(value, store=[]):
	""" Very shitty "hash" """
	if value in store:
		return store.index(value)
	store.append(value)
	return store.index(value)

def fix_columns(column_numbers, columns):
	columns_data = {}
	for number in column_numbers:
		new_data = []
		store = []
		
		for data in columns[number]:
			new_data.append(shitty_hash(data, store))
		
		columns[number] = new_data
		columns_data[number] = store
	return columns, columns_data

def save_columns(filename, columns):
	with open(filename, 'w') as f:
		column_length = len(columns[0])
		f.write('\n'.join(','.join(str(column[i]) for column in columns) for i in xrange(column_length)))
		f.write('\n')

def write_enumstore(enum_store, filename='enums.dat'):
	with open(filename, 'w') as f:
		for column_number, store in enum_store.items():
			f.write('{}\n'.format(column_number))
			f.write(','.join(map(str, store)))
			f.write('\n')

def columns_that_need_fixing(columns):
	column_numbers = []

	for i, column in enumerate(columns):
		for line in column:
			try:
				float(line)
			except:
				column_numbers.append(i)
				continue

	return column_numbers



def main():
	filename = "dogs.csv"

	columns = generate_columns(filename)

	need_fixing = columns_that_need_fixing(columns)
	columns, data = fix_columns(need_fixing, columns)

	filename = "dogs2.csv"
	save_columns(filename, columns)

	write_enumstore(data)

def test():
	pass

if __name__ == '__main__':
	main()
