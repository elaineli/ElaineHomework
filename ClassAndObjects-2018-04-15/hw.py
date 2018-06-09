class Movie:

    ratings = {'G': 'kids', 'PG13': 'teenage', 'R': 'adult'}
    producer = ''

    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating

    def goodForKids(self):
        if self.rating == 'G':
            outcome = 'The movie ' + self.title + ' is good for kids'
        if self.rating == 'PG13':
            outcome = 'The movie ' + self.title + ' is not good for kids'
        return outcome

    def __str__(self):
        return 'The movie' + self.title + ' is a ' + self.ratings[self.rating] + ' movie'


movie1 = Movie('Avengers', '2018', 'Action', 'PG13')
movie2 = Movie('StarWars', '2017', 'Action', 'G')


print(Movie.ratings)
print(movie1.ratings)
print(Movie.rating)

