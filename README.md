# Baza danych (projekt zaliczeniowy)

## Ogólnie

- Czego dokładnie baza? Jest to baza danych dla administratora portalu takiego jak facebook lub nasza klasa
- Co robimy z danymi? Wstawianie, usuwanie, wyszukiwanie (względem id, imienia i nazwiska), listowanie
- Podstawowa reprezentacja graficzna


## Technikalia 

- Jaki format bazy? JSON 
- Jaka biblioteka do interfejsu? Kivy


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
- Metod do modeli
- Metod do User activity (kontrolery)
- Zmiany danych w bazie
- Widoki

### Temat pfojektu (ze strony)
Baza danych książek, płyt, itp. Baza powinna być zapisywana do pliku (txt, CSV, JSON). Operacje na bazie: wstawianie, usuwanie, wyszukiwanie, listowanie.