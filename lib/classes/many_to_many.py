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

    def articletitle(self):
        return {self.title} 
    
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
    
    def fullname(self):
        return print(f" The author is {self.name} ") 

    def articles(self):
        return [article for article in Article.articles if article.magazine == self]

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = str(name)
        self.category = str(category)
    
    def magazinename(self):
        return print(f" The magazine title is {self.name} ")
    
    def magazinecategory(self):
        return print(f" The magazine category is {self.category} "
)

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass