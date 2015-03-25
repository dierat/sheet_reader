import xlrd


def open_file(path):
	# Target spreadsheet has 1 page, 101 relevant
	# rows, and 6 relevant columns
	book = xlrd.open_workbook(path)
	rows = []
	first_sheet = book.sheet_by_index(0)
	for n in range(1, 102):
		rows.append(first_sheet.row_values(n))
	print rows


open_file(101_radical.xlsx)