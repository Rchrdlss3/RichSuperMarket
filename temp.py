echo "# RichSuperMarket" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Rchrdlss3/RichSuperMarket.git
git push -u origin main

from tkinter import *
from tkinter import Tk
mycolor = '#4acd63'
root = Tk()

#This is the Main Screen Where Employee or Customer start#
def customercheck():
    root.configure(bg=mycolor)
    root.title('Rich Supermarket')
    root.geometry("1100x700")
    Label(text ="Hello Customer", bg= mycolor, width="300", height ="2", font=("Calibri",13)).pack()
    customerscreen()
    customerscreen.tkraise()

def employeecheck():
    root.config
    root.configure(bg=mycolor)
    root.title('Rich Supermarket')
    root.geometry("1100x700")
    Label(text ="Hello Employee", bg= mycolor, width="300", height ="2", font=("Calibri",13)).pack()

#The employee screen
def employeescreen(): 
    root.configure(bg="red")
    root.title('Rich Supermarket')
    root.geometry("1100x700")
    
#The Customer Screen
def customerscreen():
    root = Tk()
    root.configure(bg="blue")
    root.title('Rich Supermarket')
    root.geometry("1100x700")
    
#This is the mainscreen of where the user decides wether the customer or cashier is using

def mainscreen():
    root.configure(bg=mycolor)
    root.title('Rich Supermarket')
    root.geometry("1100x700")
    Label(text ="Please Proceed to Checkout Here", bg= mycolor, width="300", height ="2", font=("Calibri",13)).pack()
    Button(text="Employee", command = employeecheck).pack()
    Button(text="Customer", command = customercheck).pack()
    root.mainloop()
mainscreen()


root.mainloop()
    
#List of Aisle numbers
produceaisle=["1","3","1","1","2","2","1","3","1","3","1","1","2","2","1","3","1","3","1","1","2","2","1","3","1","3","1","1","2","2","1","3","1","2","2","2","3","1","1","1","2","2","1","3","1","3","1","1"]
babyaisle=["4","4","4","4","4","4","4","4"]
bwsaisle=["6","6","6","6","6","6","6","6","6","6","6","6","6","6","6","6","6","6","6","6","6","6","6"]
beveragesaisle=["5","5","5","5","5","5","5","5","5"]
breakfastaisle=["7","7","7","7"]
cgsaisle=["7","7","7"]
spicesaisle=["8","8","8","8","8","8"]
cccaisle=["9","9","9"]
pastasaisle=["9","9","9","9"]
dairyaisle=["5","5","5","5","5","5"]

################################################################################
#List of Prices
produceprices=[0.52,0.23,0.3,0.19,0.28,0.32,0.48,0.9,0.11,0.5,0.99,0.99,0.54,0.01,0.65,0.57,0.06,0.46,0.06,0,0.65,0.17,0.35,0.35,0.39,0.08,0.34,0.18,0.21,0.69,0.6,0.82,0.29,0.54,0.23,0.07,0.36,0.8,0.03,0.08,0.31,0.76,0.86,0.5,0.42,0.94,0.56,0.73]
babyprices=[12,14,7,2.83,9,11,1.93,1]
bwsprices=[12,12,13,13,13,12,15,15,12,14,14,14,14,12,11,9,9,32,23,18,22,24,27]
beverageprices=[1.50,1,1,1,1,2.25,2,0.75,1.15]
breakfastprices=[2.50,2.50,2.50,2.50]
cgsprcies=[3,3,2.75]
spciesprices=[1.89,1.89,2,2,2,2]
cccprices=[2.49,3.49,3.49]
pastaprices=[0.79,0.79,0.79,0.79]
dairyprcies=[1.25,2,1.50,1.50,1.50,3]
################################################################################
#List of Barcodes
producebarcodes=["3501","300","6984","6331","2674","3704","1651","3493","8597","5445","6068","5401","1042","3401","5337","5338","5632","3831","9776","8800","1911","1519","7944","7182","7911","9800","8550","5613","6363","7574","4708","4090","6639","6556","996","4779","6480","1537","2444","7366","1858","7731","7493","6670","5501","7829","2301","2022"]
babybarcodes=["4310","2385","2969","6891","4444","6669","8283","5376"]
bwsbarcodes=["2080","2783","66","2874","7518","5948","2179","4252","6111","9157","8552","4781","1224","694","8771","1986","6560","9406","9914","8197","8469","4312","8548"]
beveragesbarcodes=["3277","3354","4707","2318","2209","2504","2759","2254","4205"]
breakfastbarcodes=["2260","4437","3468","3081"]
cgsbarcodes=["2989","2113","4955"]
spicesbarcodes=["4570","4231","3976","2787","3680","2615"]
cccbarcodes=["3034","2934","4974"]
pastabarcodes=["3373","2007","4373","2285"]
dairybarcodes=["2805","4945","3846","2338","2594","4778"]
################################################################################
# This is the list of all the products within Rich Supermarket
Produce = ["Arugula","Asian Greens","Basil","Beets","Bokchoy","Broccoli","Broccoli Rabe","Brussel Sprouts","Cabbage","Cantaloupe","Cauliflower","Chard","Collard Greens","Cucumbers","Cucuzza","Edamame","Eggplants","Escarole","Fall / Winter Squash","Fennel","Garlic","Garlic Scapes","Hakurei Turnips","Honeydew","Kale","Kohlrabi","Leeks","Lettuce","Melons","Napa Cabbage","Onions","Parsley","Poblano Peppers","Potatoes","Radishes","Romanesco","Salad Turnips","Scallions","Shishito Peppers","Spinach","Spring Mix/Salad Mix Greens","String Beans","Sweet Peppers","Sweet Potatoes","Tomatoes - Beefsteak","Cherry Tomatoes","Roma Tomatoes","Zucchini / Summer Squash"]
Baby = ["Rich's Baby Formula","Rich's Baby Formula (Vitamin C)","Rich's Baby Bottles","Rich's Baby Milk","Rich's Baby Oil","Rich's Baby Lotion","Rich's Baby Distilled Water","Rich's Baby Water"]
BWS = ["Budweiser","Bud Light","Miller Lite","High Life","Coors Light","Bud Light Lim","Bud Select 55","Busch","Busch Light","Coors","Labatts","Corona","Corona Premiere","Modelo","Heineken","Mike's Hard Flavors","White Claw Flavors","Barefoot Carbernet","Barefoot Merlot","Red Moscato","Barefoot Moscato","Barefoot Chardonnay","Barefoot Pinot Grigio"]
Beverages = ["Pepsi","Rich Value","Coca Cola","Gatorade","Maxwell House Coffee","RedBull","Ocean Spray","Rich Water","Poland Springs"]
Breakfast =["Rich Wheats","Rich Pebbles","Rich Coco Pebbles","Rich O's"]
CGS =["Campbell's Chicken Noodle","Ramen Noodles","Rich Chowder"]
Spices =["Sugar","Salt","Pepper","Garlic Powder","Onion Powder","Rich Adobo"]
CCC =["Rich Sandwich Cookies","Oreos","Chips Ahoy"]
Pastas =["Macaroni Elbows","Linguine","Spaghetti","Penne"]
Dairy =["Rich Milk","Almond Milk","Fat Free Milk","2% Milk","1% Milk","Coconut Milk"]
################################################################################


