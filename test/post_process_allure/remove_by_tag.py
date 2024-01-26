import os

TAG = 'setup'

def get_file_list():
	parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	path = os.path.join(parent_dir, 'allure-results')
	return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f[-5:] == ".json"]

def select_by_tag():
	selected = []
	for f in get_file_list():
		with open(f, 'r') as jsonfile:
			if f'"name":"tag","value":"{TAG}"' in jsonfile.read():
				selected.append(f)
	return selected

def delete_from(file_list):
	for f in file_list:
		os.remove(f)

delete_from(select_by_tag())