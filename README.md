# Baza danych (projekt zaliczeniowy)

## Plany

- Czego dokładnie baza? Coś w rodzaju pejsbuka
- Co robimy z danymi? Wstawianie, usuwanie, wyszukiwanie, listowanie
- Czy chcemy interfejs graficzny? Tak
- Jakieś inne wodotryski - tak (zapytania - proste, wydruk - raczej pdf)


## Technikalia (do rozstrzygnięcia po powyszym)

- Jaki format bazy? JSON 
- Jaka biblioteka do interfejsu - Kivy
- Jaka biblioteka do wodotrysków? - znaleźć
- Jakie klasy/obiekty/wzorce projektowe wykorzystać - potem
- Czy robimy testy jednostkowe - tak
- Czy robimy testy wyzszego poziomu (i jeśli tak to czym) - zobaczymy

## Nice to have

- Zastanowić się nad wydajnością działania bazy - zobaczymy
- Statystyki bazy - moze, jeśli czasu wystarczy


## Linki do znalezisk

Kivy - https://kivy.org/#home

## Projekt

### Format danych

- users
    - id
    - name
    - surname
    - birth date
    - friends
    - photos
    - like (comments, posts)
    - posts
    - comments
    - average daily activity
    - joined on

- commets
    - id
    #is_first_comment baza 
    - first comment and reply comment
    - likes 
    #baza text
    - text
    - parent id (previous post/comment id)
    #napisać komentarz w bazie danych -> parent_id

- likes
    - id
    #comments_likes
    - comment likes
    #posts likes
    - post likes
    - parent id 

- posts
    - id
    - text
    #zrobic attacjmenty w bazie
    - attachments
    - likes

### Co mamy?
- Profile.py
- Modele bez metod 

### Czego brakuje?
- Metod do modeli
- Metod do User activity (kontrolery)
- Zmiany danych w bazie
- widoków
- 