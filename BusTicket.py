import csv
from Class import topup, ticketCategory, User, Admin
from userInput import getIntegerInput, getStringInput

categoryObjectList = []
topup_list = []
basket = []

def loadFiles():

    filename = "mobile_products.csv"
    categoryNames = [] 

    with open(filename, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for line in csv_reader:
            new_topup = topup(line["topup_title"],
                              int(line["topup_price_in_pence"]),
                              line["topup_passenger_class_name"],
                              line["topup_description"])
            
            new_topup.category_title = line["category_title"]
            topup_list.append(new_topup)

            if line["category_title"] not in categoryNames:
                categoryNames.append(line["category_title"])
                
                newCategory = ticketCategory(len(categoryObjectList) + 1,
                                             line["category_title"],
                                             line["category_description"])
                
                categoryObjectList.append(newCategory)

def main():
    
    loadFiles() 
    
    while True:
        print("\n=== LOGIN ===")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        
        role = getIntegerInput("Choice: ", 1, 3)
        
        if role == 1:
            name = getStringInput("Enter Name: ")
            currentUser = User(name)
            print(f"Hello {name}")
            customerMenu()
        elif role == 2:
            pw = getStringInput("Password: ")
            if pw == "admin123":
                currentUser = Admin("Admin")
                print("Welcome Admin")
                adminMenu()
            else:
                print("Wrong password.")
        elif role == 3:
            print("Bye.")
            break

def saveOrder():
    with open('orders.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        for item in basket:
            writer.writerow([item.title, item.price])
    print("Order saved")

def customerMenu():
    while True:
        print("\n=== CUSTOMER MENU ===")
        print("1. Buy Ticket")
        print("2. Checkout")
        print("3. Log Out")
        
        choice = getIntegerInput("Choice: ", 1, 3)
        
        if choice == 1:
            print("\nSelect Category:")
            for i in range(len(categoryObjectList)):
                cat = categoryObjectList[i]
                print(f"{i+1}. {cat.getTitle()}")
            
            catNum = getIntegerInput("Choice: ", 1, len(categoryObjectList))
            selectedCat = categoryObjectList[catNum-1]
            
            availableTickets = []
            for t in topup_list:
                if t.category_title == selectedCat.getTitle():
                    availableTickets.append(t)
            
            print(f"\nTickets for {selectedCat.getTitle()}:")
            for i in range(len(availableTickets)):
                t = availableTickets[i]
                print(f"{i+1}. {t.title} - £{t.getPriceinPoundsAndPence()}")
            
            tNum = getIntegerInput("Select ticket (0 to cancel): ", 0, len(availableTickets))
            if tNum > 0:
                picked = availableTickets[tNum-1]
                basket.append(picked)
                print("Added to basket.")

        elif choice == 2:
            if len(basket) == 0:
                print("Basket is empty.")
            else:
                total = 0
                print("\nYour Basket:")
                for item in basket:
                    print(f"- {item.title} £{item.getPriceinPoundsAndPence()}")
                    total += item.price
                
                print(f"Total: £{total/100}")
                
                confirm = getStringInput("Buy now? (y/n): ")
                if confirm == "y":
                    saveOrder()
                    basket.clear()
        
        elif choice == 3:
            break

def adminMenu():
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. View Sales Report")
        print("2. Change Ticket Price")
        print("3. Log Out")
        
        choice = getIntegerInput("Choice: ", 1, 3)
        
        if choice == 1:
            print("\n=== Sales Report ===")
            salesCounts = {}
            
            try:
                with open('orders.csv', mode='r') as f:
                    reader = csv.reader(f)
                    for line in reader:
                        if len(line) > 0:
                            ticketName = line[0]
                            if ticketName in salesCounts:
                                salesCounts[ticketName] += 1
                            else:
                                salesCounts[ticketName] = 1
                
                for name in salesCounts:
                    count = salesCounts[name] 
                    print(f"{name}: ({count})")
            except FileNotFoundError:
                print("No sales recorded yet.")

        elif choice == 2:
            print("\n=== Change Price ===")
            search = getStringInput("Search ticket name: ")
            
            foundTickets = []
            for t in topup_list:
                if search.lower() in t.title.lower(): 
                    foundTickets.append(t)
            
            if len(foundTickets) == 0:
                print("No tickets found.")
            else:
                for i in range(len(foundTickets)):
                    t = foundTickets[i]
                    print(f"{i+1}. {t.title} - £{t.getPriceinPoundsAndPence()}")
                
                sel = getIntegerInput("Select ticket (0 to cancel): ", 0, len(foundTickets))
                if sel > 0:
                    target = foundTickets[sel-1]
                    newPrice = getIntegerInput("Enter new price (in pence): ", 0, 100000)
                    target.price = newPrice
                    print("Price updated.")

        elif choice == 3:
            break

if __name__ == "__main__":
    main()
