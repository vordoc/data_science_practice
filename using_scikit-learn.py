import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

"""Библиотека scikit-learn имеет множество подмодулей с собственной функциональностью.
Поэтому обычно импортируется не весь модуль, а только подмодуль,
необходимый для конкретной задачи (скажем, sklearn.model_selection).

Чтобы получить точную прогностическую модель, ее необходимо обучить на
большом количестве маркированных образцов, поэтому первый шаг на пути
к созданию модели, способной классифицировать отзывы о товарах, — получение набора отзывов,
которые уже маркированы как положительные или отрицательные.
Это избавит вас от необходимости самостоятельно собирать отзывы и вручную маркировать их.

Существует несколько онлайн-ресурсов с размеченными наборами данных.
Один из лучших — Machine Learning Repository Калифорнийского университета UC Irvine.
Скачаем оттуда и распакуем файл sentiment labelled sentences.zip.

Набор данных Sentiment Labelled Sentences был создан для статьи Димитриоса
Котзиаса и др. (Dimitrios Kotzias et al.) «От групповых меток к индивидуальным с помощью глубоких признаков»
(«From Group to Individual Labels Using Deep Features»).

Архив .zip содержит отзывы с IMDb, Amazon и Yelp в трех разных файлах с расширением .txt.
Отзывы маркированы по тональности: положительные или отрицательные (1 или 0 соответственно);
для каждого источника представлено 500 положительных и 500 отрицательных отзывов,
всего в датасете 3000 маркированных отзывов. Для простоты будем использовать только экземпляры
с Amazon. Они находятся в файле amazon_cells_labelled.txt"""

data_path = 'E:/Data science/DS_training/sentiment labelled sentences/amazon_cells_labelled.txt'

"""Чтобы упростить дальнейшие вычисления, необходимо преобразовать загруженный 
текстовый файл с отзывами в более управляемую структуру данных. 
Можно прочитать данные из amazon_cells_labelled.txt и преобразовать в 
pandas DataFrame.
Используем метод pandas read_csv() для преобразования исходных данных 
в датафрейм. Указываем два столбца: первый для хранения отзывов и второй 
для соответствующих оценок тональности. Поскольку в исходном файле для 
отделения отзывов и соответствующих оценок используется табуляция, 
мы указываем \t в качестве разделителя"""

df = pd.read_csv(data_path, names=['review', 'sentiment'], sep='\t')

"""Теперь, когда мы импортировали датасет, нужно разделить его на две части: 
одну — для обучения прогностической модели, а другую — для проверки ее 
точности. В scikit-learn это можно сделать всего несколькими строками кода:

Разбиваем датасет с помощью функции train_test_split() из модуля sklearn.model_selection. 
Отзывы и соответствующие им оценки тональности передаются в функцию в виде массивов NumPy, 
полученных через свойство values соответствующих серий, извлеченных из датафрейма. 

Параметр test_size мы передаем, чтобы управлять тем, как именно будет разделен датасет. 
Значение 0.2 означает, что 20% отзывов будут случайным образом отнесены к тестовому набору. 
Соответственно, мы следуем схеме 80/20 — оставшиеся 80% отзывов составят обучающий набор. 
Параметр random_state инициализирует внутренний генератор случайных чисел. 
Он необходим для разбиения данных случайным образом"""

reviews = df['review'].values
sentiments = df['sentiment'].values
reviews_train, reviews_test, sentiment_train, sentiment_test = train_test_split(reviews, sentiments,
																				test_size=0.2, random_state=500)

"""Для обучения и тестирования модели требуется численно выразить текстовые 
данные. И здесь в дело вступает модель под названием мешок слов (bag of words, BoW). 
Эта модель представляет текст в виде набора (мешка) входящих в него 
слов в числовом формате. 

Наиболее типичной числовой характеристикой, генерируемой моделью BoW, 
является частота слов — сколько раз каждое слово 
встречается в тексте. Следующий простой пример показывает, как модель BoW 
преобразует текст в числовой вектор признаков на основе частоты встречаемости слов:

Text: I know it. You know it too.
BoW: { "I":1, "know":2, "it":2, "You":1, "too":1}
Vector: [1,2,2,1,1]

Для создания BoW-матрицы текстовых данных можно использовать функцию
scikit-learn CountVectorizer(). 
Она преобразует текстовые данные в числовые векторы признаков (n-мерные векторы числовых признаков, представляющих 
некоторый объект) и выполняет токенизацию (разделение текста на отдельные слова и знаки препинания), 
используя либо стандартный, либо пользовательский токенизатор. 
Пользовательский токенизатор может быть реализован с помощью инструмента обработки естественного языка (NLP), 
такого как spaCy.

Вот как можно преобразовать отзывы в векторы признаков:
Прежде всего, создаем объект vectorizer. Затем применяем метод векторизатора fit() 
для построения словаря из лексем (tokens), найденных в датасете 
reviews, содержащем все отзывы из обучающего и тестового наборов. 
После этого используем метод transform() объекта vectorizer для преобразования 
текстовых данных в обучающем и тестовом наборах в числовые векторы признаков."""

vectorizer = CountVectorizer()
vectorizer.fit(reviews)
X_train = vectorizer.transform(reviews_train)
X_test = vectorizer.transform(reviews_test)

"""Теперь, когда у нас есть обучающий и тестовый наборы в виде числовых векторов, 
можно приступать к обучению и тестированию модели. 
Сначала обучим классификатор scikit-learn LogisticRegression() для прогнозирования тональности отзыва. 
Логистическая регрессия — это простой, но популярный алгоритм для решения задач классификации.
Во фрагменте кода ниже мы создаем классификатор LogisticRegression(), затем используем его метод fit() 
для обучения модели на обучающих данных"""

classifier = LogisticRegression()
classifier.fit(X_train, sentiment_train)

"""Теперь нужно оценить, насколько точно модель делает прогнозы, на новых 
данных. Именно поэтому обычно набор маркированных данных разделяют на 
обучающий и тестовый, как мы сделали это выше. Так можно оценить модель 
с помощью тестового набора:"""

accuracy = classifier.score(X_test, sentiment_test)
print("Accuracy:", accuracy)

"""Мы получили вывод: Accuracy: 0.81 
Это означает, что точность модели — 81%. Если поэкспериментировать с параметром random_state 
в функции train_test_split(), можно получить немного другое значение, 
поскольку обучающая и тестовая выборки формируются из 
исходного набора случайным образом."""

"""Теперь, когда мы обучили и протестировали модель, она готова к анализу 
новых, немаркированных данных. Это даст нам более полное представление 
о том, насколько хорошо работает модель. 
Добавим в нее несколько новых отзывов. 
На первом шаге создадим список новых отзывов, затем преобразуем текст каждого из них в числовые векторы признаков. 
И наконец, спрогнозируем классы тональности для новых образцов."""

new_reviews = ['Old version of python is useless', 'Very good effort, five stars', 'Clear and concise']
X_new = vectorizer.transform(new_reviews)
print(classifier.predict(X_new))
print(type(X_new))

"""На выходе получим [0 1 1]
Вспомним: 0 - означает отрицательный отзыв, а 1 — положительный. 

Как видим, модель сработала для этих отзывов. Она показала, что первый — отрицательный, 
а два других — положительные."""


"""
ВЫВОДЫ

Мы поверхностно познакомились с некоторыми из наиболее популярных 
сторонних библиотек Python для анализа данных и машинного обучения. 

Мы начали с изучения библиотеки NumPy и ее объектов многомерных массивов, а затем рассмотрели библиотеку pandas 
и ее структуры данных Series и DataFrame. Научились создавать массивы NumPy, объекты pandas Series 
и объекты pandas DataFrame из встроенных структур Python (например, списков) и из источников данных, 
хранящихся в стандартных форматах, таких как JSON. 
Мы также исследовали, как получать доступ к данным в этих объектах и управлять ими. 
Наконец, мы использовали scikit-learn, популярную библиотеку машинного обучения на Python, 
для построения прогностической модели классификации."""