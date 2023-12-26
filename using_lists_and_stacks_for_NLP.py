"""Списки и стеки имеют широкое применение, в том числе в области обработки
естественного языка (NLP, Natural Language Processing). Например, они используются для извлечения
из текста именных групп (noun chunk).

Такая группа состоит из существительного и зависимых слов
(то есть всех слов слева от существительного, которые синтаксически от него зависят, например прилагательных
или артиклей в английском языке).

Таким образом, чтобы извлечь из текста
все именные группы, нужно найти в нем все существительные с зависимыми
словами, располагающимися слева от существительного. Это можно сделать
с помощью алгоритма на основе стека"""


"""Импортируем библиотеку spacy"""
import spacy

# текст который необходимо разобрать
txt = 'List is a ubiquitous data structure in the Python programming language.'

# загружаем модель для английского языка
nlp = spacy.load('en_core_web_sm')

doc = nlp(txt)

stk = []

for word in doc:
	# Если мы нашли существительное или один из дочерних элементов, расположенных слева от этого существительного,
	# отправляем слово в стек с помощью метода append()
	if word.pos_ == 'NOUN' or word.pos_ == 'PROPN':
		stk.append(word.text)
	elif (word.head.pos_ == 'NOUN' or word.head.pos_ == 'PROPN') and (word in word.head.lefts):
		stk.append(word.text)
	# определяем, что следующее слово в тексте не является частью именной
	# группы (ни существительным, ни дочерним словом слева от него), а значит,
	# полученная группа полная, и мы извлекаем ее из стека
	elif stk:
		chunk = ''
		while stk:
			chunk = stk.pop() + ' ' + chunk
		print(chunk.strip())


print('\n--------------------------------------------------------------\n')


txt_1 = 'List is arguably the most useful type in the Python programming language.'

nlp_1 = spacy.load('en_core_web_sm')
doc_1 = nlp_1(txt_1)

'''перебираем слова предложения в цикле внутри спискового включения, 
заменяя нулями те слова, вершины для которых не находятся справа'''
head_lefts = [t.text if t in t.head.lefts else 0 for t in doc_1]
print(head_lefts)

print('\n--------------------------------------------------------------\n')

'''Получившийся список head_lefts содержит на один элемент больше, чем количество слов 
в предложении. Это происходит потому, что spaCy фактически разбивает текст 
на лексемы (tokens), которые могут быть как словами, так и знаками препинания. 
Последний 0 в списке — это точка в конце предложения.

Теперь нам нужен способ перемещения по этому списку, чтобы найти и извлечь 
именные группы. Создадим набор фрагментов текста, начинающихся с определенного места и продолжающихся до конца текста. 
В следующем фрагменте кода будем двигаться пословно от начала до конца текста, на каждой итерации 
создавая матрицу с позицией вершины.'''

for word in doc:
	head_lefts = [t.text if t in t.head.lefts else 0 for t in doc_1[word.i:]]
	print(head_lefts)

print('\n--------------------------------------------------------------\n')
'''Далее проанализируем каждый фрагмент в поисках первого встретившегося нуля. 
Слова до нуля (включительно) потенциально могут составлять именную группу.'''

for word in doc:
	head_lefts = [t.text if t in t.head.lefts else 0 for t in doc[word.i:]]
	i0 = head_lefts.index(0)
	if i0 > 0:
		noun = [1 if t.pos_ == 'NOUN' or t.pos_ == 'PROPN' else 0 for t in reversed(doc[word.i:word.i+i0 + 1])]
		try:
			i1 = noun.index(1) + 1
		except ValueError:
			pass
		print(head_lefts[:i0 + 1])
		print(doc[word.i + i0 + 1 - i1])


'''Теперь можно включить новый код в решение из предыдущего раздела. Собрав 
все воедино, получим следующий скрипт:'''

print('\n--------------------------------------------------------------\n')

txt = 'List is arguably the most useful type in the Python programming language.'
nlp = spacy.load('en_core_web_sm')
doc = nlp(txt)
stk = []

for w in doc:
	head_lefts = [1 if t in t.head.lefts else 0 for t in doc[w.i:]]
	i0 = 0
	try:
		i0 = head_lefts.index(0)
	except ValueError:
		pass
	i1 = 0
	if i0 > 0:
		noun = [1 if t.pos_ == 'NOUN' or t.pos_ == 'PROPN' else 0 for t in reversed(doc[w.i:w.i+i0 + 1])]
		try:
			i1 = noun.index(1)+1
		except ValueError:
			pass
	if w.pos_ == 'NOUN' or w.pos_ == 'PROPN':
		stk.append(w.text)
	elif (i1 > 0):
		stk.append(w.text)
	elif stk:
		chunk = ''
		while stk:
			chunk = stk.pop() + ' ' + chunk
		print(chunk.strip())





















