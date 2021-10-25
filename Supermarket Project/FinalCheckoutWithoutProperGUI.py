from tkinter import*
import tkinter as tk
from tkinter import Button
from decimal import *
from tkinter.font import Font
import datetime
getcontext().prec=3
UserE = ""
mycolor = '#4acd63'

xdt = datetime.datetime.now()

root = tk.Tk()
root.configure(bg=mycolor)
root.attributes()
root.title('Rich Supermarket')
root.geometry("900x700")

ReceiptObjectsList = []
##############################################################################
###############Login Screen###################################################
##############################################################################
loginscreen = Tk()
loginscreen.configure(bg=mycolor)
loginscreen.attributes()
loginscreen.title('Login Systems')
loginscreen.geometry("400x200")
##############################################################################
Card = 500
GiftCard = 50
Cash = 100
#################################################################################################
########################Lists of Employee####### #################################################
EmployeeFName=["Kristle","Deanna","Corey","Ora","Tawna","Dianne","Raquel","Eldon","Charissa","Hipolito","Kathie","Chance","Hayden","Fidelia","Emory","Margareta","Berneice","Simone","Joellen","Illa","Mahalia","Joy","Mozell","Emerita","Lauralee","Nada","Shakira","Krystyna","Blythe","Dinah","Elton","Kimberlie","Ellyn","Jacinto","Vivienne","Alyssa","Edna","Brianne","Hyman","Eugenio","Camilla","Stacey","Arletha","Virgina","Karisa","Belkis","Dolores","Rene","Kendra","Kai","Dulce","Fannie","Shirly","Lilla","Ria","Bonny","Zana","Carry","Rico","Thora","Lahoma","Rocco","Celeste","Nikki","Jody","Cherri","Shawnna","Nubia","Wonda","Domitila","Jed","Marge","Kandi","Martina","Cierra","Sherill","Nelda","Renata","Kristie","Shanice","James","Anjanette","Connie","Barabara","Colleen","Yajaira","Vada","Lucia","Tomeka","Jaclyn","Chung","Evie","Fernanda","Audry","Genoveva","Arlean","Joseph","Lucretia","Andy","Drew","Chanel","Hershel","Caryl","Kari","Sheldon","Shanika","Yuonne","Emma","Tobias","Zofia","Danette","Esther","Laine","Lachelle","Sasha","Tashina","Debbie","Vikki","Arline"]
EmployeeLName=["Felton","Clifton","Cornell","Roman","Daniel","Thanh","Cole","Billy","Arnulfo","Eldridge","Asa","Sammie","Walter","Joan","Rogelio","Sebastian","Peters","Teddy","Kennith","Lynn","Rod","Graciela","Crista","Bob","Beverley","Roselia","Kyle","Carina","Simone","Helena","Albert","Sharmaine","Stephany","Latoya","Johana","Mercedes","Dot","Rachele","Mary","Alverta","Jacki","Modesto","Mollie","Jimmie","Shantelle","Aracelis","Eulah","Julia","Pam","Dorthy","Krystal","Mirta","Geneva","Dustin","Bill","Hermina","Shaunna","Rachal","Valeria","Elisabeth","Valene","Mei","Wendi","Gilberto","Brett","Tiffani","Majorie","Lizette","Carmine","Julene","Jenae","Sanda","Sondra","Yen","Elaine","Stevie","Leisha","Domitila","Lashanda","Amiee","Charlsie","Dorcas","Zack","Prince","Leon","Noella","Dyan","Mariano","Scott","Sherise","Noel","Retta","Cammy","Dionna","Patience","Armand","Claretha","Vivian","Shana","Despina","Mozelle","Elvera","Lorine","Doug","Karan","Eulah","Jackson","Audie","Malena","Ron","Shaquana","Dannielle","Risa","Lyndsey","Lacie","Beatris","Hollie","Clementine","Saint"]
EmployeeID=["Felton2187","Clifton2188","Cornell2189","Roman2187","Daniel2188","Thanh2189","Cole2187","Billy2188","Arnulfo2189","Eldridge2187","Asa2188","Sammie2189","Walter2187","Joan2188","Rogelio2189","Sebastian2187","Peters2188","Teddy2189","Kennith2187","Lynn2188","Rod2189","Graciela2187","Crista2188","Bob2189","Beverley2187","Roselia2188","Kyle2189","Carina2187","Simone2188","Helena1387","Albert1387","Sharmaine1388","Stephany1389","Latoya1387","Johana1388","Mercedes1387","Dot1388","Rachele1387","Mary1388","Alverta1389","Jacki1387","Modesto1388","Mollie1389","Jimmie1387","Shantelle1388","Aracelis1389","Eulah1387","Julia1388","Pam1389","Dorthy1387","Krystal1388","Mirta1389","Geneva1387","Dustin1388","Bill1389","Hermina1387","Shaunna1388","Rachal1389","Valeria1389","Elisabeth2387","Valene2388","Mei2390","Wendi2391","Gilberto2392","Brett2387","Tiffani2388","Majorie2390","Lizette2391","Carmine2392","Julene2387","Jenae2388","Sanda2390","Sondra2391","Yen2392","Elaine2387","Stevie2388","Leisha2390","Domitila2391","Lashanda2392","Amiee2387","Charlsie2388","Dorcas2390","Zack2391","Prince2392","Leon2387","Noella2388","Dyan2390","Mariano2391","Scott2392","Sherise1287","Noel1288","Retta1289","Cammy1290","Dionna1291","Patience1292","Armand1293","Claretha1294","Vivian1287","Shana1288","Despina1289","Mozelle1290","Elvera1291","Lorine1292","Doug1293","Karan1294","Eulah1287","Jackson1288","Audie1289","Malena1290","Ron1291","Shaquana1292","Dannielle1293","Risa1294","Lyndsey1287","Lacie1288","Beatris1289","Hollie1290","Clementine1291","Saint1292"]
EmployeeStore=[1101,1102,1103,1101,1102,1103,1101,1102,1103,1101,1102,1103,1101,1102,1103,1101,1102,1103,1101,1102,1103,1101,1102,1103,1101,1102,1103,1101,1102,301,301,302,303,301,302,301,302,301,302,303,301,302,303,301,302,303,301,302,303,301,302,303,301,302,303,301,302,303,303,1301,1302,1304,1305,1306,1301,1302,1304,1305,1306,1301,1302,1304,1305,1306,1301,1302,1304,1305,1306,1301,1302,1304,1305,1306,1301,1302,1304,1305,1306,201,202,203,204,205,206,207,208,201,202,203,204,205,206,207,208,201,202,203,204,205,206,207,208,201,202,203,204,205,206]
#################################################################################################

#########################################################################
def Login(loginscreen):
    if UserE.get() in EmployeeFName:
        UserIndex = EmployeeFName.index(UserE.get())
        print("User Entered the index is" + str(UserIndex))
    else:print("No such user exists")
        
def PassWord(loginscreen):
    global LoginValidator
    PassEntered = PassWordE.get()
    if PassEntered in EmployeeID:
       PassIndex = EmployeeID.index(PassEntered)
       LoginValidator = True
    else: PassIndex == UserIndex
    print("password entered, the index is " + str(PassIndex))
    
def OpenRegister():
    if LoginValidator == True:
        print("Good login")
        root.deiconify()
        loginscreen.withdraw()
        #webbrowser.get(chrome).open_new("Google.com")
    else: print("Bad login")
    
def LoginComplete():
    Login(loginscreen)
    PassWord(loginscreen)
    OpenRegister()


ChckPhoto = PhotoImage(master = root, file= "/Supermarket Project/images/checkout.png")
RmvPhoto = PhotoImage(master = root,file= '/Users/Rchrd/OneDrive/Desktop/Supermarket Project/images/RemoveItem.png')
AddPhoto = PhotoImage(master = root,file= '/Users/Rchrd/OneDrive/Desktop/Supermarket Project/images/AddItem.png')
LogPhoto = PhotoImage(master = loginscreen, file= '/Users/Rchrd/OneDrive/Desktop/Supermarket Project/images/Login.png')
############################################################################################################################################################
#########################################Log In Screen##############################################################################
############################################################################################################################################################
#(CheckoutPage, width = 300, height = 500, bg='White',highlightthickness= 1)
login_frame = Frame(loginscreen, bg = mycolor, highlightthickness = 1)
login_frame.pack(padx=10, pady=20)

Font_Login = Font(login_frame,family ="COCOGOOSE",size= 13,weight="bold")
Label(login_frame,font = Font_Login, text= "Welcome Employee! Please Login", bg= mycolor, width="300", height ="2", fg="White").pack()
UserE= Entry(login_frame,width=25,textvariable = "")
UserE.pack()

PassWordE= Entry(login_frame,width=25,textvariable="Password", show= "*")
PassWordE.pack()

LoginBtn=Button(login_frame,text="Login", image= LogPhoto, command=LoginComplete, highlightthickness =0, bd = 0)
LoginBtn.pack()

UserE.insert(0,"Username")
PassWordE.insert(0,"PassWord")

def entry_clear(e):
    if UserE.get() == 'Username' or PassWordE.get() == 'Password':
        UserE.delete(0,END)
        PassWordE.delete(0,END)
    pass

UserE.bind("<Button-1>",entry_clear)
PassWordE.bind("<Button-1>",entry_clear)

############################################################################################################################################################
#############################################################################################IMAGES###################################

UserNameList=[]
PassWordList=[]
UIndex = 0
ShoppingCart=[]
ShoppingCartPrice=[]
######################################FRAMES##################################################
optionsframe = Frame(root,width = 500,height=60,bg=mycolor,highlightthickness= 1)
optionsframe.pack(side = TOP, fill=BOTH)

frame= Frame(root,width=5000,height=600,bg=mycolor,highlightthickness= 1)
frame.pack(side = LEFT, fill=BOTH)

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
AllAisles=produceaisle+babyaisle+bwsaisle+beveragesaisle+breakfastaisle+cgsaisle+spicesaisle+spicesaisle+cccaisle+pastasaisle+dairyaisle
################################################################################
#List of Prices
produceprices=[0.52,0.23,0.3,0.19,0.28,0.32,0.48,0.9,0.11,0.5,0.99,0.99,0.54,0.01,0.65,0.57,0.06,0.46,0.06,0,0.65,0.17,0.35,0.35,0.39,0.08,0.34,0.18,0.21,0.69,0.6,0.82,0.29,0.54,0.23,0.07,0.36,0.8,0.03,0.08,0.31,0.76,0.86,0.5,0.42,0.94,0.56,0.73]
babyprices=[12,14,7,2.83,9,11,1.93,1]
bwsprices=[12,12,13,13,13,12,15,15,12,14,14,14,14,12,11,9,9,32,23,18,22,24,27]
beverageprices=[1.50,1,1,1,1,2.25,2,0.75,1.15]
breakfastprices=[2.50,2.50,2.50,2.50]
cgsprices=[3,3,2.75]
spicesprices=[1.89,1.89,2,2,2,2]
cccprices=[2.49,3.49,3.49]
pastaprices=[0.79,0.79,0.79,0.79]
dairyprices=[1.25,2,1.50,1.50,1.50,3]
AllPrices= produceprices+babyprices+bwsprices+beverageprices+breakfastprices+cgsprices+spicesprices+cccprices+pastaprices+dairyprices

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
AllBarcodes= producebarcodes+babybarcodes+bwsbarcodes+beveragesbarcodes+breakfastbarcodes+cgsbarcodes+pastabarcodes+dairybarcodes
###############################################################################?>/#
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
AllProducts= Produce+Baby+BWS+Beverages+Breakfast+CGS+Spices+CCC+Pastas+Dairy
################################################################################
###########################COMMANDS#############################################
def SelfCheckOut():
    
    pass
def LoggingOut():
    root.withdraw()
    loginscreen.deiconify()
    pass

def Cashout():
    PrintReceipt()
    pass
def PrintReceipt():
    zip_object = zip(ShoppingCart,ShoppingCartPrice)
    for element1, element2 in zip_object:
        ReceiptObjects = (element1,element2)
        ReceiptObjectsList.append(ReceiptObjects)
        pass
    myFile = open("Rich SuperMarket Receipts.txt","w")
    myFile.write("Thank you for shopping at Rich SuperMarket" + "\n" + str(xdt)+"\n")
    myFile.write("------------------------------------------------------\n")
    for element in ReceiptObjectsList:
        myFile.write(str(element) + "\n")
    myFile.write("------------------------------------------------------\n")
    myFile.write("Your Total was: " + format(NewShoppingCartPrice,".2f") + "\n ")
    myFile.write("------------------------------------------------------\n")
    myFile.close()
    print(ReceiptObjectsList)

def finish():
    root.destroy()
    CheckoutPage.destroy()
    loginscreen.destroy()
    
def Comeback():
    root.deiconify()
    CheckoutPage.withdraw()
    

def discount():
    messagebox.showerror()
    pass

def delete():
    global NewShoppingCartPrice
    x1 = AppendedItems.get(ACTIVE)
    AppendedItems.delete(ANCHOR)
    x2 = AllProducts.index(x1)
    x3 = AllPrices[x2]
    x4 = ShoppingCartPrice.remove(x3)
    pricelabel.config(text="Price: " + format(x3,".2f"))
    ShoppingCart.remove(x1)
    NewShoppingCartPrice = sum(ShoppingCartPrice)
    totallabel.config(text="Total Price: " + format(NewShoppingCartPrice,".2f"))
    
def select():
    global totallabel
    global NewShoppingCartPrice
    x1 = productlistbox.get(ANCHOR)
    AppendedItems.insert(0,x1)
    x2= AllProducts.index(x1)
    barcodeindex = AllProducts.index(x1)
    barlabel = AllBarcodes[barcodeindex]
    barcodelabel.config(text= barlabel,font = Font_barcode)
    x3 = AllPrices[x2]
    x4 = ShoppingCartPrice.append(x3)
    pricelabel.config(text="Price: " + format(x3,".2f"))
    ShoppingCart.append(x1)
    NewShoppingCartPrice = sum(ShoppingCartPrice)
    totallabel.config(text="Total Price: " + format(NewShoppingCartPrice,".2f"))

################################BUTTONS,WIDGETS,LABELS,ETC###################################
#############################################################################################
#UserE= Entry(frame,width=45).pack()

productlistbox = Listbox(frame)
productlistbox.pack(padx= 20 , pady=100, ipadx = 100)

AppendedItems = Listbox(root)
AppendedItems.pack(pady= 125, ipadx = 200)
###THIS ADDS ALL THE PRODUCTS INTO THE PRODUCT LIST BOX#####
for item in AllProducts:
    productlistbox.insert(END,item)
    pass

###########################################################################################################################
    
def CheckOut():
    global CheckoutPage
    CheckoutPage = Tk()
    CheckoutPage.configure(bg=mycolor)
    CheckoutPage.title('Check Out Screen')
    CheckoutPage.geometry("900x700")
    
    root.withdraw()  
    
    Font_options = Font(CheckoutPage,family ="MONDAY-PERSONAL USE",size= 20)
    Font_items = Font(CheckoutPage,family ="IMPACT",size= 10)
    Font_cash= Font(CheckoutPage, family="BUTTON_", size = 15)
    Font_bottomopt = Font(CheckoutPage,family="BUTTONHILIGHTFLF",size = 20)
    Cashlabel = Label(CheckoutPage,font=Font_options, text ="Please provide currency",bg=mycolor, fg="White")
    Cashlabel.pack(side=TOP)
    zip_object = zip(ShoppingCart,ShoppingCartPrice)
   
    CheckoutAppended = Listbox(CheckoutPage, width =50, font= Font_items, bg= mycolor,fg="White",selectbackground=mycolor)
    CheckoutAppended.pack()
    
    for element1, element2 in zip_object:
        ReceiptObjects = (element1,element2)
        ReceiptObjectsList.append(ReceiptObjects)
        
    for item in ReceiptObjectsList:
    	CheckoutAppended.insert(END,item)

    
    chckframe = Frame(CheckoutPage, width = 500, height = 500, bg=mycolor,highlightthickness= 1)
    chckframe.pack()  

    
        
    #Checkoutlabel = Label(CheckoutPage,text ="Please provide a payment")
    #Checkoutlabel.pack()
    
    ChckTotalPricelbl = Label(CheckoutPage,font= Font_options, text = "Your total is : " + format(NewShoppingCartPrice,".2f"),bg=mycolor, fg="White")
    ChckTotalPricelbl.pack(side= TOP)
    
    
    #receiptframe = Frame(CheckoutPage, width = 300, height = 500, bg=mycolor, highlightthickness= 2)
    #receiptframe.pack(side=TOP)
    #CashPhoto = PhotoImage(master = CheckoutPage,file= '/Users/Rchrd/OneDrive/Desktop/Supermarket Project/images/Cash.png')
    Cashbtn=Button(chckframe,text='Cash', font='Font_bottomopt',command= Cashout,highlightthickness = 0, bd = 0,bg=mycolor, fg="White")
    Cashbtn.pack(side= TOP)
    #Paybtn=Button(CheckoutPage,text='Submit Payment', command= delete,highlightthickness = 0, bd = 0)
    #Paybtn.pack()
    
    #GoBackPhoto = PhotoImage(master= CheckoutPage, file ='/Users/Rchrd/OneDrive/Desktop/Supermarket Project/images/Close.png')
    GBbtn= Button(chckframe,text='Back to Checkout', font= Font_bottomopt, command= Comeback,highlightthickness =0, bd = 0,bg=mycolor, fg="White")
    GBbtn.pack(side= BOTTOM)
    
    #ClosePhoto = PhotoImage(master= CheckoutPage, file= '/Users/Rchrd/OneDrive/Desktop/Supermarket Project/images/End.png')
    Closebtn=Button(chckframe, text='Close', font= Font_bottomopt, command= finish, highlightthickness = 0, bd = 0,bg=mycolor, fg="White")
    Closebtn.pack(side=BOTTOM)
    
    pass


#############################################################################################

###########################BUTTONS#########################################################################################
###########################################################################################################################

addbtn= Button(root ,text='Add',image =AddPhoto, command= select, highlightthickness =0, bd = 0)
addbtn.pack()

rmvbtn=Button(root,text='remove',image=RmvPhoto, command= delete,highlightthickness = 0, bd = 0)
rmvbtn.pack()

chckbtn=Button(root,text='Check Out',image= ChckPhoto, highlightthickness = 0, bd = 0,command = CheckOut)
chckbtn.pack()

LogOutBtn = Button(optionsframe, text = "←",bg= mycolor, fg= "White",height = 5, width = 5, command = LoggingOut)
LogOutBtn.pack(side = LEFT)

SelfCheckBtn = Button(optionsframe, text = "✢", bg= mycolor, fg="White", height = 5, width = 5, command = SelfCheckOut)
SelfCheckBtn.pack(side = LEFT)
#####################################################################################################
####################################LABELS#####################################################################################################
#####################################################################################################

Font_barcode = Font(root,family ="BARCODE TFB",size= 20,weight="bold")
barcodelabel = Label(root, text ='', font = Font_barcode, bg = mycolor, fg="White")
barcodelabel.pack()


pricelabel = Label(root, text= '', bg= mycolor,fg="White")
pricelabel.pack()

totallabel=Label(root,text='',bg=mycolor,fg="White")
totallabel.pack()


root.withdraw()

loginscreen.mainloop()