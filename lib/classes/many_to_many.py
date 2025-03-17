class Article:
    articles = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise ValueError("Title must be an non-empty string between 5-50 characters")
        self.author = author(author)
        self.magazine = magazine(magazine)
        self.title = str(title)
        Article.articles.append(self)

    def title(self):
        return {self.title} 
   
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be of type str.")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive.")
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after instantiation.")
        self._title = value

    def author(self):
        return self.author
    
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author")
        self.author = value
    def magazine(self):
        return self.magazine
    
    def magazine(self, value):
         if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
         self.magazine = value
        
class Author:
    def __init__(self, name):
        
        if hasattr(self, 'author'):
            raise AttributeError("Cannot modify the author after initialisation")
        if not isinstance(author, str) or len(author)==0:
            raise ValueError("The author name must be  a non-empty string")
        
        self.name = str(name)
    
    def name(self):
        return self.name 

    def articles(self):
        return [article for article in Article.articles if article.magazine == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))


    def add_article(self, magazine, title):
        
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self.name = str(name)
        self.category = str(category)
    
    def name(self):
        return self.name 
    
    def name(self, value):
        if not isinstance(value, str) or not (2< len(value)<=16):
            raise ValueError("the magazine name should be a string between 2 and 16 charaters")
        self.name = value
        
    def category(self):
        return self.category

    def category(self, value):
        if not isinstance(value, str) or  len(value)==0:
            raise ValueError("tthe category must be a non-empty string")
        self.name = value

    def articles(self):
        return [article for article in Article.articles if article.magazine == self]


    def contributors(self):
        return list(set(article.author for article in self.articles()))

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