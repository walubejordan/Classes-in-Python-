Class Book:
     def _int_(self, title,author, pages,genre, volume):
        Self.title = title
        self.author = auther
        self.pages = pages 
        self.genre = genre
        self.volume = volume
    
    def _str_(self):
        return f"{self.title} by {self.author}"
    
    def _str_(self):
        return f"{self.title} by {self.author}"

    def _len_(self):
        return self.pages

    def _del_(self):
        print(f"{self.title} has benn deleted")
    
    #Method to get the charpter
    def get_chapter(self,chapter):
        return f"{self.title} -chapter {chapter}"

    #Method to get author
    def get_author(self):
        return f"{self.title} is written by {self.author}":

    #Method to show all Books information
    def show_info(self):
        return f"{self.title} is written by {self.author}":

    #Create Book object of title
    book1 = Book("The Moon also Sets", "John Dou", 300, "Fiction" 1)

    book2 = Book("The Art of rancing in the Rain" "Garth St", 200, "Fiction", 2)

    book3 = Book("No more mr. nice guy", "Robert L", 200, "Fiction", 1)

    book4 = Book("First Blood", "David M", 400, "Friction", 3)

#Print Author of Books
print(book1.get_author())
print(book2.get_author())
print(book3.show_info())
print(book4.get_chapter(5))




