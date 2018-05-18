import media

coco = media.Movie("Coco",
                   "The story follows a 12-year-old boy named Miguel Rivera "
                   "who is accidentally transported to the land of the dead",
                   "https://vignette.wikia.nocookie.net/disney/images/1/14/Coco"
                   "_poster.png/revision/latest?cb=20170912170727",
                   "https://www.youtube.com/watch?v=Rvr68u6k5sI")

up = media.Movie("Up",
                 "Seventy-eight year old Carl Fredricksen travels to Paradise "
                 "Falls in his home equipped with balloons, inadvertently "
                 "taking a young stowaway.",
                 "https://img.hindilinks4u.to/2014/11/Up-2009-In-Hindi.jpg",
                 "https://www.youtube.com/watch?v=BDCSncUZxvs")

wall_e = media.Movie("WALL-E",
                   "In the distant future, a small waste-collecting robot"
                   " inadvertently embarks on a space journey that will "
                   "ultimately decide the fate of mankind.",
                   "https://pixar-planet.fr/wp-content/uploads/2010/04/affiche"
                   "-walle-40.jpg",
                   "https://www.youtube.com/watch?v=qGBZWbg_26A")

coco = media.Movie("Coco",
                   "The special bond that develops between plus-sized "
                   "inflatable robot Baymax, and prodigy Hiro Hamada, who team "
                   "up with a group of friends to form a band of "
                   "high-tech heroes.",
                   "https://lumiere-a.akamaihd.net/v1/images/image_478f52c0."
                   "jpeg?width=1200&region=0%2C0%2C2000%2C2000",
                   "https://www.youtube.com/watch?v=Sh5EO5h_do0")

print(coco.poster_image_url)
