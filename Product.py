class Product:
    # SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.
    def __init__(self,name,category,price,id=0):
        self.name = name
        self.category = category
        self.price = price
        self.id = id
    
    def price (self,percent_change,is_incrersed):
        if(is_incrersed):
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change

    def print_info(self):
        print(f"product name:{self.name}, category: {self.category}, price: {self.price},id: {self.id}")
        return self

