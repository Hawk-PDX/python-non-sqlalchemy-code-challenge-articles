class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not 5 <= len(title) <= 50:
            raise Exception("Title must be between 5 and 50 characters")
        self.title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise Exception("Title is immutable")
        else:
            if not isinstance(value, str):
                raise Exception("Title must be a string")
            if not 5 <= len(value) <= 50:
                raise Exception("Title must be between 5 and 50 characters")
            self._title = value
    
    def __repr__(self):
        return f"Author: {self.author}, Magazine: {self.magazine}, Title: {self.title}"
        
class Author:
    all = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception("Name is immutable")
        else:
            if not isinstance(value, str):
                raise Exception("Name must be a string")
            if len(value) == 0:
                raise Exception("Name cannot be empty")
            self._name = value
            
    def __repr__(self):
        return f"Author: {self.name}"

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles())) or None

class Magazine:
    all = []
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise Exception("Name must be between 2 and 16 characters, inclusive")
        self.name = name
        self.category = category
    
    def _validate_string(self, value, field_name, min_length=None, max_length=None):
        if not isinstance(value, str):
            raise Exception(f"{field_name} must be a string")
        if min_length is not None and len(value) < min_length:
            raise Exception(f"{field_name} must be at least {min_length} characters")
        if max_length is not None and len(value) > max_length:
            raise Exception(f"{field_name} must be no more than {max_length} characters")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        self._validate_string(value, "Category", min_length=1)
        self._category = value
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._validate_string(value, "Name", min_length=2, max_length=16)
        self._name = value
            
    def __repr__(self):
        return f"Magazine: {self.name}, Category: ({self.category})"

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]
        
    def contributing_authors(self):
        contributors = self.contributors()
        contributing_authors = [author for author in contributors if len([article for article in self.articles() if article.author == author]) > 2]
        if not contributing_authors:
            return None
        return contributing_authors