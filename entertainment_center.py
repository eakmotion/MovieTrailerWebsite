import fresh_tomatoes
import media

moana = media.Movie("MOANA",
        "In Ancient Polynesia, when a terrible curse incurred by Maui reaches an impetuous Chieftain's daughter's island, she answers the Ocean's call to seek out the demigod to set things right.",
        "https://resizing.flixster.com/e9wR4EBx89WvSjW4m6Vz5kY5pIg=/206x305/v1.bTsxMjIyMTc2NDtwOzE3MTk2OzEyMDA7NDU3OzY3NQ",
        "https://www.youtube.com/watch?v=LKFuXETZUsI")

fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them",
                   "The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.",
                   "https://resizing.flixster.com/dn961AgpVqjM4AmO67XSTg2CzpM=/206x305/v1.bTsxMjIzMjgwMDtqOzE3MTk2OzEyMDA7NjI0OzkyNQ",
                   "https://www.youtube.com/watch?v=YdgQj7xcDJo")

doctor_strange = media.Movie("Doctor Strange",
                "A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.",
                "https://resizing.flixster.com/CBPV4WpDIVsoQkrVYE-zJ8RZmoE=/206x305/v1.bTsxMjE3OTkzMTtqOzE3MTk1OzEyMDA7Mzg3OzU3Ng",
                "https://www.youtube.com/watch?v=YdgQj7xcDJo")

movies = [moana, fantastic_beasts, doctor_strange]
fresh_tomatoes.open_movies_page(movies)
