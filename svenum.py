try:
	xrange(5)
except:
	xrange = range

def csv_split(line, splitter):
	in_quote = False
	out = []
	current_stash = []

	for letter in line:
		if letter in '\'"':
			if in_quote:
				in_quote = False
			else:
				in_quote = True
		elif letter in splitter:
			if in_quote:
				current_stash.append(letter)
			else:
				out.append(''.join(current_stash))
				current_stash = []
		else:
			current_stash.append(letter)
	else:
		out.append(''.join(current_stash))

	return out


def generate_columns(filename):
	columns = None

	with open(filename) as f:

		for line in f:
			if columns is None:
				print(csv_split(line, ','))
				columns = [[] for _ in csv_split(line.strip(), ',')]

			for i, text in enumerate(csv_split(line.strip(), ',')):
				columns[i].append(text) 

	return columns

def shitty_hash(value, store=[]):
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
			if line == '':
				continue
			try:
				float(''.join(l for l in line if l not in '"\''))
			except:
				column_numbers.append(i)
				break

	return column_numbers



def main():
	filename = "results.csv"

	columns = generate_columns(filename)

	need_fixing = columns_that_need_fixing(columns)
	columns, data = fix_columns(need_fixing, columns)

	filename = "results2.csv"
	save_columns(filename, columns)

	write_enumstore(data)

def test():
	pass

if __name__ == '__main__':
	main()