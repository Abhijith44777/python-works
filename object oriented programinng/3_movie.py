class Movie:

    title:str

    rating:int

    run_time:int
    
    director:int

    genre:str

    def set_movie(self,title,rating,run_time,director,genre):

        self.title=title

        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre

    def display(self):

        print(self.title,self.rating,self.run_time,self.director,self.director,self.genre)

movie_instance1=Movie()
movie_instance2=Movie()
        
movie_instance1.set_movie("ARM",4.5,2.5,"jithn lal","action")
movie_instance2.set_movie("KGF",4.9,2.45,"Prasant neel","action")
movie_instance1.display()
movie_instance2.display()