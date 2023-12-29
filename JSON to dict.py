from pprint import pprint as pp

"""С помощью словарей структуры данных Python можно преобразовывать в строки JSON и наоборот.
Вот как загрузить строку, представляющую собой документ JSON, в словарь, используя лишь оператор присваивания"""

dict_1 = { "PONumber" : 2608,
"ShippingInstructions" : {"name": "John Silver",
						"Address": { "street" : "426 Light Street",
									"city" : "South San Francisco",
									"state" : "CA",
									"zipCode" : 99237,
									"country" : "United States of America" },
						"Phone": [{ "type" : "Office", "number" : "809-123-9309" },
								   { "type" : "Mobile", "number" : "417-123-4567" }]
			}
		}

'''Сохраним словарь непосредственно в файл JSON с помощью модуля json, используя метод json.dump():'''

import json

with open("text.json", "w") as text_file:
	json.dump(dict_1, text_file)


'''Используем метод json.load() для преобразования содержимого файла JSON в словарь Python:'''

with open("text.json", "r") as text_file_1:
	dict_2 = json.load(text_file_1)


pp(dict_2, sort_dicts=False)

