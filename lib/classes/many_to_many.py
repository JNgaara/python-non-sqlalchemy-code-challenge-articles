class Article:
    def __init__(self, author, magazine, title):
        if hasattr(self, 'author'):
            raise AttributeError("Cannot modify the author after initialisation")
        
        self.author = author(author)
        self.magazine = magazine(magazine)
        self.title = str(title)

    def articletitle(self):
        return print(f" The article title is {self.title} ") 
        
class Author:
    def __init__(self, name):
        self.name = str(name)
    
    def fullname(self):
        return print(f" The author is {self.name} ") 

    def articles(self):
        pass

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