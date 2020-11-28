# Praca z formatem JSON oraz CSV

#### Zadania zostały wykonane na podstawie tutoriali ze stron:
* https://realpython.com/python-json/
* https://realpython.com/python-csv/

#### Aby zobaczyć wyniki metod przejdź do poszczególnych plikó .ipynb (Referencja na początku każdego rozdziału)

# Spis treści:
* [JSON](#JSON)
* [CSV](#CSV)

# JSON
#### Aby zobaczyć kod źródłowy kliknij [tutaj](./Lab8_json.ipynb)


### Importy:
```
import json
import requests
```
### Utworzenie pliku o formacie JSON w pamięci 
```
data={
    "postId": 1,
    "id": 3,
    "name": "odio adipisci rerum aut animi",
    "email": "Nikita@garfield.biz",
    "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"
  }
```
### Zapisanie pliku w formacie JSON przy wykorzystaniu metody dump()
[plik JSON Tutaj](json_files/data_file.json)
```
with open("json_files/data_file.json", "w") as write_file:
    json.dump(data, write_file)
```
### Przekonwertowanie obiektu JSON na obiekt typu Python native str
```
json.dumps(data)
```
### Specyfikacja stylu wcinania
```
json.dumps(data, indent=4)
```
## Deserializacja obiektu JSON
### Zakodowanie oraz odkodowanie obiektu typu JSON 

Konwersja typów nie jest idealna, przez co obustronna konwersja może prowadzić do niezgodności danych
```
new_shoes = ("Price",299)
encoded_shoes = json.dumps(new_shoes)
decoded_shoes = json.loads(encoded_shoes)

```
### Deserializacja
[plik JSON Tutaj](json_files/data_file.json)
```
with open("json_files/data_file.json", "r") as read_file:
    data = json.load(read_file)
```
### Deserializacja obiektu typu String
W pierwszym kroku tworzymy obiekt typu String z wartością docelowego JSONa
Po czym wykonujemy deserializację metodą json.loads()
```
json_string = """
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
"""
data = json.loads(json_string)
```
### Utworzenie zapytania JSON oraz deserializacja wyniku zapytania
```
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = json.loads(response.text)
```
### Znalezienie użytkownika który utworzył najdłuższy post

Utworzenie listy 
```
posts_by_user={}
```
Znalezienie najdłuższego posta każdego użytkownika
```
for post in posts:
    try:
        if len(post["body"])> posts_by_user[post["userId"]]:
            posts_by_user[post["userId"]]=len(post["body"])
    except KeyError:
            posts_by_user[post["userId"]]=len(post["body"])
```
Posortowanie wyniku
```
longest_post = sorted(posts_by_user.items(),
                      key=lambda x:x[1], reverse=True)
```
Znalezienie najdłuższego posta oraz użytkownika
Metoda również uwzględnia przypadek w którym istnieje więcej niż 1 postów o największej długości 
```
users_longest_posts=[]
for longest in longest_post:
    if longest_post[0][1]>longest[1]:
        break
    users_longest_posts.append(str(longest[0]))
```
Utworzenie Stringa z uzyskanych danych
```
user_string = " and ".join(users_longest_posts)
s = "s" if len(users_longest_posts)>1 else ""
```
### Odfiltrowanie najdłuższego postu pięciu użytkowników z najdłuższymi postami 

Utworzenie listy z pięcioma najdłuższymi postami
```
users = longest_post[:5]
```
Metoda filtrująca na podstawie listy z najdłuższami postami
```
def keep(post):
    counter = False
    for user in users:
        if user[1] == len(post["body"]) and post["userId"] == user[0]:
            counter = True
    return counter
```
Wykonanie przefiltrowania danych oraz zapisanie wyniku do [pliku](./json_files/filtered_data_file.json)
```
with open("json_files/filtered_data_file.json","w") as data_file:
    filtered_posts = list(filter(keep,posts))
    json.dump(filtered_posts,data_file,indent=2)

```
### Zakodowanie oraz odkodowanie obiektów niestandardowych

##### Poniższy kod powinien wyrzucić błąd "TypeError" ponieważ python nie jest w stanie domyślnie zakodować niestandardowych obiektów 

Utworzenie niestandardowego obiektu Elf
```
class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]
```
Próba zakodowania nowego obiektu oraz obsługa wyjątku
```
try:
    elf = Elf(level=4)
    json.dumps(elf)
except TypeError as type_error:
    print("A TypeError has occurred!")
    print("Message: ",type_error.args[0])

```
### Poprawne zakodowanie złożonych niestandardowych obiektów za pomocą metody
```
def encode_complex(z):
    if isinstance(z,complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

```
### Zakodowanie przy pomocy nadpisania metody default() obiektu JSONEncoder
```
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

```
Możliwe wywołania kodowania
```
json.dumps(2 + 5j, cls=ComplexEncoder)
encode = ComplexEncoder()
encode.encode(3 + 6j)
```
### Odkodowanie niestandardowego obiektu
```
complex_json = json.dumps(4+17J,cls=ComplexEncoder)
json.loads(complex_json)
```
### Weryfikacja klucza 
Definicja metody 
```
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct
```
Wywołanie oraz odkodowanie [pliku](./json_files/complex_data.json)
```
with open("json_files/complex_data.json") as complex_data:
    data=complex_data.read()
    z=json.loads(data, object_hook=decode_complex)

```
#CSV

####
```

```
###
```

```
###
```

```
###
```

```
