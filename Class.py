import csv

class topup:
    def __init__(this, title, price, passenger_class, description):
        this.title = title
        this.price = price
        this.passenger_class = passenger_class
        this.description = description
        this.category_title = ""
        
    def getPriceinPoundsAndPence(this):
        priceinPounds = this.price / 100
        return priceinPounds

    def getInfo(this):
        return f"{this.title} - {this.description}"

class ticketCategory:
    def __init__(this, cat_id, title, description):
        this.id = cat_id
        this.title = title
        this.description = description
        this.tickets = []

    def getTitle(this):
        return this.title
    
    def getCode(this):
        return str(this.id)
    
    def addTopup(this, ticket_list):
        this.tickets = ticket_list

class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    pass
