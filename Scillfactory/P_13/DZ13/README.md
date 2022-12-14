# My data science projects

* [Проект_1 Домашнее задание: "Визуализация данных"](https://github.com/lyu-bel/IDE/blob/master/Scillfactory/P_13/DZ13/DZ13_visualization.ipynb)

# Проект_1 Домашнее задание: "Визуализация данных
## Оглавление
1. [Описание проекта](#описание-проекта)
2. [Какой кейс решаем](#какой-кейс-решаем)
3. [Задания](#задания)
4. [Условия](#условия)
5. [Этапы работы над проектом](#этапы-работы-над-проектом)
6. [Выводы](#выводы)
    


### Описание проекта
Представлены данные об об оттоке клиентов некоторого банка
файл с данными https://github.com/lyu-bel/IDE/blob/master/Scillfactory/P_13/DZ13/data/churn.csv. Заказчик хочет  разработать кампанию лояльности по удержанию клиентов, для этого ему необходимо выяснить основные причины оттока клиентов. 

### Какой кейс решаем
Нужно установить, чем ушедшие клиенты отличаются от лояльных и как между собой связаны различные признаки, определяющие клиентов. Отчет о проделанной работе представить в виде ноутбука с ответами на заданные  вопросы в виде графиков и подробных выводов, которые можно сделать, исходя из них.
### Задания

9.1. Каково соотношение ушедших и лояльных клиентов? Покажите это на графике и дайте комментарий по соотношению.

9.2. Постройте график, показывающий распределение баланса пользователей, у которых на счету больше 2 500 долларов. Опишите распределение и сделайте выводы.

9.3. Посмотрите на распределение баланса клиента в разрезе признака оттока. Как различаются суммы на накопительном счёте ушедших и лояльных клиентов? Подумайте и напишите, с чем это может быть связано, что может не устраивать ушедших клиентов в банке.

9.4. Посмотрите на распределение возраста в разрезе признака оттока. В какой группе больше потенциальных выбросов? На какую возрастную категорию клиентов стоит обратить внимание банку?

9.5. Постройте график, который показывает взаимосвязь кредитного рейтинга клиента и его предполагаемой зарплаты. Добавьте расцветку по признаку оттока клиентов. Какова взаимосвязь между признаками? Если не видите явной взаимосвязи, укажите это.

9.6. Кто чаще уходит, мужчины или женщины? Постройте график, который иллюстрирует это.

Подсказка
9.7. Как отток клиентов зависит от числа приобретённых у банка услуг? Для ответа на этот вопрос постройте многоуровневую столбчатую диаграмму.

9.8. Как влияет наличие статуса активного клиента на отток клиентов? Постройте диаграмму, иллюстрирующую это. Что бы вы предложили банку, чтобы уменьшить отток клиентов среди неактивных?

9.9. В какой стране доля ушедших клиентов больше? Постройте тепловую картограмму, которая покажет это соотношение на карте мира. Предположите, с чем это может быть связано.

9.10. Переведите числовой признак CreditScore в категориальный. Для этого воспользуйтесь функцией get_credit_score_cat(), которая приведена ниже. Примените её к столбцу CreditScore и создайте новый признак CreditScoreCat — категории кредитного рейтинга.

### Условия
В файле должно содержаться 10 графиков — 10 ответов к заданиям.

Каждый график и преобразования к нему выполняются в отдельной ячейке.

Под графиком вы должны предоставить свой ответ на вопрос по нему и, если это требуется, выводы, которые можно сделать, исходя из графика.

### Этапы работы над проектом
Для визуализации использованы библиотеки seaborn, matplotlib, plotly.express
Перед выбором графика произведен анализ представленных признаков, с целью выявления какие признаки в данных являются числовыми, а какие — категориальными. 
При выборе графика была использована предложенная на схему выбора графика под конкретные задачи.

Написан кода с использование указанных библиотек для построения графиков для решения поставленных задач: 
https://github.com/lyu-bel/IDE/blob/master/Scillfactory/P_13/DZ13/DZ13_visualization.ipynb

### Выводы
Представлен ноутбук с 10 графиками с ответами к заданиям, сделаны выводы

:arrow_up:[к оглавлению](#оглавление)