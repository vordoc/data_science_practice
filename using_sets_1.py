from pprint import pprint as pp
"""Представим, что нам нужно распределить огромное количество фотографий
по группам исходя из того, что на них изображено. Чтобы автоматизировать
эту задачу, можно начать с инструмента визуального распознавания (visual
recognition), например Clarifai API, который будет генерировать множество
описательных тегов для каждой фотографии.

Затем множества тегов можно сравнить друг с другом с помощью метода intersection().
Этот метод сравнивает два множества и создает новое множество, содержащее элементы, которые есть
в обоих множествах. В данном конкретном случае чем больше тегов в каждом
множестве, тем более схожа тематика этих двух изображений.

Для простоты в следующем примере возьмем только две фотографии. Используя
соответствующие множества описательных тегов, можно определить степень
совпадения тематики этих двух фото:"""


photo1_tags = {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
photo2_tags = {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}

'''Используя метод intersection найдем пересечение двух множеств'''
set_intersection_1 = photo1_tags.intersection(photo2_tags)
print(set_intersection_1)

'''Если в пересечение попало 2 или более одинаковых тега, выведем сообщение'''
if len(set_intersection_1) >= 2:
	print("Photos contain 2 or more similar objects.")


print("\n-------------------------------------------------------------------\n")


"""Предположим, что на входе мы имеем список словарей, где каждый словарь представляет собой одну фотографию.
Задача — распределить фотографии по группам с помощью пересечений тегов и сохранить результат в словарь:
photo_groups = {}"""

photos_list = [
	{
		"name": "photo1.jpg",
		"tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
	},
	{
		"name": "photo2.jpg",
		"tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
	},
	{
		"name": "photo3.jpg",
		"tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
	},
	{
		"name": "photo4.jpg",
		"tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
	}
]


'''Найдем все пары фотографий'''

# for i in range(1, len(photos_list)):
# 	for j in range(i + 1, len(photos_list) + 1):
# 		print(f"Пересечение фото {i} и {j}")


'''функция пересечения тегов в сравниваемых фотографиях, создает имя вида "tag_tag" '''
def intersection(lst1, lst2):
	return "_".join([value for value in lst1 if value in lst2])

# tags_intersection_list = []
photo_groups = {}
for i in range(1, len(photos_list)):
	for j in range(i + 1, len(photos_list) + 1):
		# print(f"Пересечение фото {i} и {j}")
		# используем функцию пересечения тегов
		intersecting_tags = intersection(photos_list[i - 1]["tags"], photos_list[j - 1]["tags"])
		# print(intersecting_tags)
		# tags_intersection_list.append(intersecting_tags)
		if intersecting_tags:
			photo_groups.setdefault(intersecting_tags, list((photos_list[i - 1]["name"], photos_list[j - 1]["name"])))

# print(tags_intersection_list)
pp(photo_groups, sort_dicts=False)



