class Order():
    def __init__(self,order_num,date, object):
#add product here        
        self.__order_number = str(order_num)
        self.__order_date = str(date)
        self.__products_ordered = []
        self.__items_ordered = 0
        self.__status = orderStatus()
        
    def addItem(self,object):
        
        self.__products_ordered.append(product)
        self.__items_ordered += 1
        self.__status = "products added"
        
    def getOrderStatus(self):
        return self.__status
    
    def getOrderItemID(self,item):
        product = self.products_ordered[item-1]
        return product.__product__ID
        
    def getOrderItemPrice(self,item):
        product = self.products_ordered[item-1]
        return product.__product_price 
        
class orderStatus():
    def shipItem():
        has_shipped = False

class Product():
    def __init__(self,name,price):
        self.__product_ID = str(name)
        self.__product_price = float(price)

product1 = Product("beans", 0.45)
product2 = Product("eggs", 1.25)

myOrder = Order(1, "1/1/17")
myOrder.addItem(product1)
myOrder.addItem(product2)
print (myOrder.getOrderStatus())
print (myOrder.getOrderItemID(1))
print (myOrder.getOrderItemPrice(1))