from pprint import pprint as pp
"""Рассмотрим практический пример - подсчет кол-ва вхождений каждого слова в тексте"""

some_txt = ("Python is one of the most promising programming languages today. Due to the simplicity of Python syntax, "
	   "many researchers and scientists prefer Python over many other languages.")


"""сначала уберем из текста знаки препинания"""
some_txt = some_txt.replace('.', '').replace(',', '')

print(some_txt)

"""теперь разобьём текст на слова и поместим их в список"""
words_list = some_txt.split()

"""подсчитаем количество вхождений каждого слова в список. 
Реализуем это с помощью словаря, используя метод setdefault():"""
words_dict = {}

for word in words_list:
	words_dict.setdefault(word, 0)
	words_dict[word] += 1

sorted_words_dict = dict(sorted(words_dict.items(), key=lambda x: x[1], reverse=True))

pp(sorted_words_dict, sort_dicts=False)




