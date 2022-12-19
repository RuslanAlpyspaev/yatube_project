# yatube_project
Social network
### Описание
Благодаря этому проекту можно будет рекомендовать друзьям прочитанные книги и отправлять открытки из разных городов.
### Технологии
Python 3.9
Django 2.2.19
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
'''
pip install -r requirements.txt
'''
- В папке с файлом manage.py выполните команду:
'''
python3 manage.py runserver
'''
За настройки шаблонов в Django отвечает
переменная TEMPLATES в файле settings.py:
'''
### Авторы
С уважением, Руслан Алпыспаев. 
{% extends 'base.html' %}
{% block title %}
 Главная Страница
{%  endblock %}

{% block content %}
    {%  for post in posts %}
  <!-- класс py-5 создает отступы сверху и снизу блока -->
      <ul>
        <li>
          Автор: {{ post.author.get_full_name }}
        </li>
        <li>
          Дата публикации: {{ post.pub_date|date:"d E Y" }}
        </li>
      </ul>
      <p> {{ post.text }}</p>
    {% if post.group %}
      <a href="{% url 'posts:group_list' post.group.slug %}">все записи группы</a>
    {% endif %}
    {%  if not foorloop.last %}<hr>{% endif %}
    {% endfor %}
{% endblock %}