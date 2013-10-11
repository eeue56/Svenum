def generate_columns(filename):
	columns = None

	with open(filename) as f:
		for line in f:
			if columns is None:
				columns = [[] for _ in line.split(',')]

			for i, text in enumerate(line.split(',')):
				columns[i].append(text) 

	return columns

def shitty_hash(value, store=[]):
	if value in store:
		return store.index(value)
	store.append(value)
	return store.index(value)

def fix_columns(column_numbers, columns):
	for number in column_numbers:
		new_data = []
		store = []
		
		for data in columns[number]:
			new_data.append(shitty_hash(data, store))

def save_columns(filename, columns):
	with open(filename, 'wb') as f:
		column_length = len(columns[0])
		f.write('\n'.join(','.join(column[i] for column in columns)) for i in xrange(column_length) + '\n')


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
	columns = fix_columns(need_fixing, columns)
	save_columns(filename, columns)

def test():
	pass

if __name__ == '__main__':
	main()