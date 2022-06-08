from Store import Store
from Product import Product


dorahStore = Store("Dorah")

kitKat = Product("kitKat","chocolate",1)

dorahStore.add_product([kitKat])

kitKat = Product("kitKat","chocolate",1)
fishfash = Product("fishfash","chips",0.5)
orangeJuice = Product("orangeJuice","Juice",1)

dorahStore.add_product([kitKat,fishfash,orangeJuice])

for i in dorahStore.products:
    i.print_info()

print ("-"*100,"\n")
dorahStore.add_product([kitKat,fishfash,orangeJuice]).sell_product(2).sell_product(5)

for i in dorahStore.products:
    i.print_info()
