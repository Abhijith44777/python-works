from json import load

f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\books.json")

data=load(f)

# for books in data:
#     print(books)


# to printall title

all_titles=[books.get("title")for books in data]

# print(all_titles)

# books page with pages<250

page_filter=[books.get("title") for books in data if books.get("pages")<250]

# print(page_filter)

# to print all genres

all_genres=[books.get("genre") for books in data]

# print(set(all_genres))


# to print genre count

genre_count={genre:all_genres.count(genre) for genre in all_genres}

# print(genre_count)

# to print costly books

costly_books=max(data,key=lambda d:d.get("price"))

# print(costly_books)

# author with more than one books

author=[books.get("author")for books in data]
# print(author)

autho_count={auth:author.count(auth)for auth in author}

print([k for k,v in autho_count.items() if v>1])

