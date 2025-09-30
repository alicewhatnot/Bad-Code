class OrderStatus:
    '''Returns shipping information
    called to check status or change
    shipping status'''
    def __init__(self):
        self.has_shipped = False

    def shipItem(self):
        self.has_shipped = True

    def __str__(self):
        return "Shipped" if self.has_shipped else "Processing"

class Product:
    '''Product defined in terms of ID and price'''
    def __init__(self, name, price):
        self.__product_ID = str(name)
        self.__product_price = float(price)

    #Getters to return the ID or price
    def getID(self):
        return self.__product_ID

    def getPrice(self):
        return self.__product_price

class Order:
    '''Collects product objects with additional info'''
    def __init__(self, order_num, date):      
        self.__order_number = str(order_num)
        self.__order_date = str(date)
        self.__products_ordered = []
        self.__items_ordered = 0
        self.__status = OrderStatus()
        
    def addItem(self, product):
        #Adding a product object that is called
        self.__products_ordered.append(product)
        self.__items_ordered += 1
          
    def getOrderStatus(self):
        return str(self.__status)
    
    def getOrderItemID(self, item):
        product = self.__products_ordered[item-1]
        return product.getID()
        
    def getOrderItemPrice(self, item):
        product = self.__products_ordered[item-1]
        return product.getPrice()

#Main Code testing
product1 = Product("beans", 0.45)
product2 = Product("eggs", 1.25)

myOrder = Order(1, "1/1/17")
myOrder.addItem(product1)
myOrder.addItem(product2)

print(myOrder.getOrderStatus())       
print(myOrder.getOrderItemID(1))      
print(myOrder.getOrderItemPrice(1))   
