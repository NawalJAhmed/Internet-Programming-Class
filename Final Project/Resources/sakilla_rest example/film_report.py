from utility import db_access

films = db_access.list_of_all_films()
stores = db_access.list_of_all_stores()

template = "{:>5}   {:30} {:>15}  {:>15} "
row = template.format("ID", "Title", "In Inventory", "Rentals")
print(row)

for film in films:
    film_id = film['film_id']
    inventory = db_access.inventory_for_film(film_id)
    row = template.format(film_id, film['title'], len(inventory), db_access.count_rentals_for_film(film_id),
                         )
    print(row)



#  http://ksuweb.kennesaw.edu/~bsetzer/4720sp16/nanoc/output/notes/0215B-web-arch-rest/

#  ~bsetzer  is mapped to home/bsetzer/public_html

