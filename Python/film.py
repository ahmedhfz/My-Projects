import random

class Get_type:
    def __init__(self):
        self.movies = {
            "horror": horror_list,
            "comedy": comedy_list,
            "action": action_list,
            "science fiction": science_fiction_list
        }

    def get_type(self):
        while True:
            film_type = input("Which type of films do you like (or enter 'q' to quit): ").lower().strip()
            if film_type == 'q':
                print("Quitting...")
                break
            else:
                self.print_film(film_type)

    def print_film(self, film_type):
        if film_type in self.movies:
            if not self.movies[film_type]:
                print("There are no more movies of this type.")
                self.get_type()
            else:
                film = random.choice(self.movies[film_type])
                print(f"----------------{film.name} : {film.date}----------------")
                self.movies[film_type].remove(film)
                self.ask_again(film_type)
        else:
            print(f"{film_type} is not a valid type")

        

    def ask_again(self, film_type):
        choice = input(f"Do you want another {film_type} film (yes/no): ").lower().strip()
        if choice == "yes":
            self.print_film(film_type)
        elif choice == "no":
            return
        else:
            print("Invalid choice please enter yes or no")
class Films:
    
    def __init__(self,name,date):
        self.name = name
        self.date = date
        
class Horror(Films):
    
    def __init__(self,name,type,date):
        super().__init__(name,date)
        self.type = type

h1 = Horror("The Exorcist","Horror",1973)
h2 = Horror("The Shining","Horror",1980)
h3 = Horror("A Nightmare on Elm Street","Horror",1984)
h4 = Horror("The Silence of the Lambs","Horror",1991)
h5 = Horror("The Conjuring","Horror",2013)
horror_list = [h1,h2,h3,h4,h5]

class Comedy(Films):
    
    def __init__(self,name,type,date):
        super().__init__(name,date)
        self.type = type

c1 = Comedy("Superbad", "Comedy", 2007)
c2 = Comedy("The Hangover", "Comedy", 2009)
c3 = Comedy("Bridesmaids", "Comedy", 2011)
c4 = Comedy("Deadpool", "Comedy", 2016)
c5 = Comedy("The Grand Budapest Hotel", "Comedy", 2014)
comedy_list = [c1, c2, c3, c4, c5]


class Action(Films):
    
    def __init__(self,name,type,date):
        super().__init__(name,date)
        self.type = type

a1 = Action("Die Hard", "Action", 1988)
a2 = Action("The Dark Knight", "Action", 2008)
a3 = Action("Mad Max: Fury Road", "Action", 2015)
a4 = Action("Inception", "Action", 2010)
a5 = Action("John Wick", "Action", 2014)
action_list = [a1, a2, a3, a4, a5]

class ScienceFiction(Films):
    
    def __init__(self,name,type,date):
        super().__init__(name,date)
        self.type = type

sf1 = ScienceFiction("Blade Runner", "Science Fiction", 1982)
sf2 = ScienceFiction("The Matrix", "Science Fiction", 1999)
sf3 = ScienceFiction("Inception", "Science Fiction", 2010)
sf4 = ScienceFiction("Interstellar", "Science Fiction", 2014)
sf5 = ScienceFiction("The Terminator", "Science Fiction", 1984)
science_fiction_list = [sf1, sf2, sf3, sf4, sf5]

get = Get_type()

get.get_type()

