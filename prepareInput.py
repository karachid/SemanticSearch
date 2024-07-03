import json

def read_json_file(file_path):
	try:
		with open(file_path, 'r') as json_file:
			data = json.load(json_file)
		return data
	except FileNotFoundError:
		print("File not found.")
		return None
	except json.JSONDecodeError as e:
		print("JSON decoding error. Make sure the file contains valid JSON.", e)
		return None

def write_json_file(output_file_path, data):
	try:
		with open(output_file_path, 'w') as json_file:
			json_file.write(data)
		print(f"Data written to {output_file_path} successfully.")
	except Exception as e:
		print(f"Error writing to file: {e}")

def add_action_to_json_objects(json_data):
	new_json_data = ""
	for obj in json_data:
		'''print(json.dumps(obj))'''
		#new_json_data += json.dumps({"index":{"_index":"uksrvc-rw-kw","_id":obj["serviceID"]}}) + "\n"
		new_json_data += json.dumps({"index":{"_index":"ctz-service-catalog-index","_id":obj["SERVICE_CATALOG_ID"]}}) + "\n"
		new_json_data += json.dumps(obj, ensure_ascii = False) + "\n"
	return new_json_data

#input_file_path = 'UK-services-translatedSWAHILI.json'
input_file_path = 'CTZ_SERVICE_CATALOG.json'
output_file_path = 'CTZ_SERVICE_CATALOG_OUTPUT_SEMANTIC.json'

input_json_data = read_json_file(input_file_path)
print(type(input_json_data))
print(len(input_json_data))
'''
for i in input_json_data:
	print(i)
	print(json.dumps(i, ensure_ascii = False))
'''
if input_json_data:
	'''print("-------------------") '''
	modified_json_data = add_action_to_json_objects(input_json_data)
	'''print("-------------------")'''
	'''print(modified_json_data)'''
	write_json_file(output_file_path, modified_json_data)

