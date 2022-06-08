from Product import Product

class Store:
    def __init__(self,name) -> None:
        self.name = name
        self.products = []
        self.id = 1

    def add_product(self,new_products=[]):
        for i in new_products:
            i.id = self.id 
            self.products.append(i)
            self.id +=1
        return self
    
    def sell_product(self,id):
        for i in self.products:
            if(i.id == id):
                self.products[id].print_info()
                del self.products[id]
                break
        return self

    def inflation (self,percent_increase=0):
        for i in self.products:
            i.update_price(percent_increase,True)
        return self
    
    def set_clearance(self,category,percent_discount=0):
        for i in self.products:
            if i.category == category:
                i.update_price(percent_discount,False)
        return self

