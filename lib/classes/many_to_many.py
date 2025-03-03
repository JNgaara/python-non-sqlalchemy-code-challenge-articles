class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = str(title)

    def articletitle(self):
        return f" The article title is {self.title} "
        
class Author:
    def __init__(self, name):
        self.name = str(name)
    
    def fullname(self):
        return f" The author is {self.name} "

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
        return f" The magazine title is {self.name} "
    
    def magazinecategory(self):
        return f" The magazine category is {self.category} "


    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass