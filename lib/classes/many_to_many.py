class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be of type str.")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after instantiation.")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Create a new Article instance and associate it with the author and magazine
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        # Return a unique list of magazine categories the author has contributed to
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be of type str.")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be of type str.")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        # Return a list of titles of all articles in the magazine
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        # Count how many articles each author has written for the magazine
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        # Return authors who have written more than 2 articles
        return [author for author, count in author_counts.items() if count > 2]


class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        author.articles().append(self)
        magazine.articles().append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be of type str.")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive.")
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after instantiation.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        self._magazine = value