from tkinter import *

#function part for billing system
# Product prices constants
PRICES = {
    # Cosmetics prices
    'bath_soap': 40,
    'face_cream': 140,
    'face_wash': 240,
    'hair_spray': 340,
    'hair_gel': 140,
    'body_lotion': 260,
    
    # Grocery prices
    'rice': 80,
    'food_oil': 180,
    'wheat': 60,
    'sugar': 45,
    'salt': 20,
    'daal': 160,
    
    # Cold Drinks prices
    'coca_cola': 60,
    'pepsi': 60,
    'fanta': 60,
    'sprite': 60,
    'limca': 60,
    'mountain_dew': 60
}



def Total():
    #function to calculate total bill
    try:
        #getting the values from the entry fields
        
        Bath_Soap=int(Bath_SoapEntry.get())
        Face_Cream=int(Face_CreamEntry.get())
        Face_wash=int(Face_washEntry.get())
        Hair_Spray=int(Hair_SprayEntry.get())
        Hair_Gel=int(Hair_GelEntry.get())
        Body_Lotion=int(Body_LotionEntry.get())
     
        Rice=float(RiceEntry.get())
        Food_Oil=float(Food_OilEntry.get())
        Wheat=float(WheatEntry.get())
        Sugar=float(SugarEntry.get())
        Salt=float(SaltEntry.get())
        Daal=float(DaalEntry.get())

        Coca_Cola=float(Coca_ColaEntry.get())
        Pepsi=float(PepsiEntry.get())
        Fanta=float(FantaEntry.get())
        Sprite=float(SpriteEntry.get())
        Limca=float(LimcaEntry.get())
        Mountain_Dew=float(Mountain_DewEntry.get())
       

        #calculating the total for cosmetics
        Total_Cosmetics=((Bath_Soap )*PRICES['bath_soap']+(Face_Cream )*PRICES['face_cream']+(Face_wash )*PRICES['face_wash']+
                         (Hair_Spray )*PRICES['hair_spray']+(Hair_Gel)*PRICES['hair_gel']+(Body_Lotion )*PRICES['body_lotion'])
        Total_CosmeticsEntry.delete(0,END)
        Total_CosmeticsEntry.insert(0,f'Rs { Total_Cosmetics} ' )
        #calculating the total for grocery
        Total_Grocery=((Rice )*PRICES['rice']+(Food_Oil )*PRICES['food_oil']+(Wheat )*PRICES['wheat']+
                        (Sugar )*PRICES['sugar']+(Salt )*PRICES['salt']+(Daal )*PRICES['daal'])
        Total_GroceryEntry.delete(0,END)
        Total_GroceryEntry.insert(0,f' RS {Total_Grocery}')
        #calculating the total for cold drinks
        Total_Cold_Drinks=((Coca_Cola or 0)*PRICES['coca_cola']+(Pepsi or 0)*PRICES['pepsi']+(Fanta or 0)*PRICES['fanta']+
                           (Sprite or 0)*PRICES['sprite']+(Limca or 0)*PRICES['limca']+(Mountain_Dew or 0)*PRICES['mountain_dew'])
        Total_Cold_DrinksEntry.delete(0,END)
        Total_Cold_DrinksEntry.insert(0,f'RS  {Total_Cold_Drinks} ')

      
    except ValueError:
        pass


#GUI part for billing system
#creating a window for the project
root=Tk()
root.title("Billing System")
root.geometry("1300x850+310+130")
root.iconbitmap("icon.ico")
#header for the project
header=Label(root,text="Retail Billing System",font=("times mew roman",30,"bold"),bg="gray20",fg="gold",bd=12,relief=GROOVE)

header.pack(fill=X,pady=5)
#------------------------------------------------------------------------------------------------------




#custumer details frame
frame1=LabelFrame(root,text="custumer details",font=("times new roman",15,"bold"),bg="gray20",fg="gold",bd=12,relief=SUNKEN)
                  
frame1.pack(fill=X)

#entry for name 
nameLabel=Label(frame1,text="Name",bg="gray20",fg="white",font=("times new roman",15,"bold") )
nameLabel.grid(row=0,column=0,padx=20)


nameEntry=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=18)
nameEntry.grid(row=0,column=1,pady=10,padx=10)


#entry for phone number
phoneLabel=Label(frame1,text="Phone Number",bg="gray20",fg="white",font=("times new roman",15,"bold") )
phoneLabel.grid(row=0,column=2,padx=20)

phoneEntry=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=18)
phoneEntry.grid(row=0,column=3,pady=10,padx=10)

#entry for email
billNumLabel=Label(frame1,text="Bill Number",bg="gray20",fg="white",font=("times new roman",15,"bold") )        
billNumLabel.grid(row=0,column=4,padx=20)

BillNumEntry=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=18)
BillNumEntry.grid(row=0,column=5,pady=10,padx=10)


#search button
SearchButton=Button(frame1,text="SEARCH",font=("times new roman",15,"bold"),bg="gold",fg="black",bd=4,relief=GROOVE,width=10)

SearchButton.grid(row=0,column=6,pady=10,padx=35)

#------------------------------------------------------------------------------------------------------



#frame for product details
frame2=Frame(root,bg="gray20",bd=10,relief=SUNKEN)
frame2.pack(fill=X ,pady=5)

#Lableframe for cosmetics


frame3=LabelFrame(frame2,text="Cosmetics",font=("times new roman",15,"bold"),bg="gray20",fg="gold",bd=12,relief=SUNKEN)
frame3.grid(row=0,column=0,padx=8,pady=3)
#Lable for soap
Bath_SoapLabel=Label(frame3,text="Bath Soap",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Bath_SoapLabel.grid(row=0,column=0,pady=10,sticky=W)
Bath_SoapEntry=Entry(frame3,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Bath_SoapEntry.grid(row=0,column=1,pady=10,padx=10)
Bath_SoapEntry.insert(0,0)

#Lable for Face Cream
Face_CreamLabel=Label(frame3,text="Face Cream",bg="gray20",fg="white",font=("times new roman",15,"bold") )  
Face_CreamLabel.grid(row=1,column=0,pady=10,sticky=W)
Face_CreamEntry=Entry(frame3,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10) 
Face_CreamEntry.grid(row=1,column=1,pady=10,padx=10)
Face_CreamEntry.insert(0,0)
#Lable for Face Wash    
Face_washLabel=Label(frame3,text="Face Wash",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Face_washLabel.grid(row=2,column=0,pady=10,sticky=W)
Face_washEntry=Entry(frame3,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Face_washEntry.grid(row=2,column=1,pady=10,padx=10)
Face_washEntry.insert(0,0)

#Lable for Hair Spray
Hair_SprayLabel=Label(frame3,text="Hair Spray",bg="gray20",fg="white",font=("times new roman",15,"bold") )      
Hair_SprayLabel.grid(row=3,column=0,pady=10,sticky=W)
Hair_SprayEntry=Entry(frame3,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Hair_SprayEntry.grid(row=3,column=1,pady=10,padx=10)
Hair_SprayEntry.insert(0,0)
#Lable for Hair Gel
Hair_GelLabel=Label(frame3,text="Hair Gel",bg="gray20",fg="white",font=("times new roman",15,"bold") )  
Hair_GelLabel.grid(row=4,column=0,pady=10,sticky=W)
Hair_GelEntry=Entry(frame3,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Hair_GelEntry.grid(row=4,column=1,pady=10,padx=10)
Hair_GelEntry.insert(0,0)
#Lable for Body Lotion
Body_LotionLabel=Label(frame3,text="Body Lotion",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Body_LotionLabel.grid(row=5,column=0,pady=10,sticky=W)
Body_LotionEntry=Entry(frame3,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Body_LotionEntry.grid(row=5,column=1,pady=10,padx=10)
Body_LotionEntry.insert(0,0)
#Lableframe for grocery
frame4=LabelFrame(frame2,text="Grocery",font=("times new roman",15,"bold"),bg="gray20",fg="gold",bd=12,relief=SUNKEN)
frame4.grid(row=0,column=1,padx=8,pady=3)
#Lable for Rice
RiceLabel=Label(frame4,text="Rice",bg="gray20",fg="white",font=("times new roman",15,"bold") )
RiceLabel.grid(row=0,column=0,pady=10,sticky=W)
RiceEntry=Entry(frame4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
RiceEntry.grid(row=0,column=1,pady=10,padx=10)
RiceEntry.insert(0,0)
#Lable for Food Oil
Food_OilLabel=Label(frame4,text="Food Oil",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Food_OilLabel.grid(row=1,column=0,pady=10,sticky=W)
Food_OilEntry=Entry(frame4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Food_OilEntry.grid(row=1,column=1,pady=10,padx=10)
Food_OilEntry.insert(0,0)
#Lable for Wheat
WheatLabel=Label(frame4,text="Wheat",bg="gray20",fg="white",font=("times new roman",15,"bold") )
WheatLabel.grid(row=2,column=0,pady=10,sticky=W)
WheatEntry=Entry(frame4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
WheatEntry.grid(row=2,column=1,pady=10,padx=10)
WheatEntry.insert(0,0)
#Lable for Sugar
SugarLabel=Label(frame4,text="Sugar",bg="gray20",fg="white",font=("times new roman",15,"bold") )
SugarLabel.grid(row=3,column=0,pady=10,sticky=W)
SugarEntry=Entry(frame4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
SugarEntry.grid(row=3,column=1,pady=10,padx=10)
SugarEntry.insert(0,0)
#Lable for Salt
SaltLabel=Label(frame4,text="Salt",bg="gray20",fg="white",font=("times new roman",15,"bold") )
SaltLabel.grid(row=4,column=0,pady=10,sticky=W)
SaltEntry=Entry(frame4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
SaltEntry.grid(row=4,column=1,pady=10,padx=10)
SaltEntry.insert(0,0)
#Lable for Daal
DaalLabel=Label(frame4,text="Daal",bg="gray20",fg="white",font=("times new roman",15,"bold") )
DaalLabel.grid(row=5,column=0,pady=10,sticky=W)
DaalEntry=Entry(frame4,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
DaalEntry.grid(row=5,column=1,pady=10,padx=10)
DaalEntry.insert(0,0)


#frameLabel for cold drinks
frame5=LabelFrame(frame2,text="Cold Drinks",font=("times new roman",15,"bold"),bg="gray20",fg="gold",bd=12,relief=SUNKEN)
frame5.grid(row=0,column=2,padx=8,pady=3)
#Lable for Coca Cola
Coca_ColaLabel=Label(frame5,text="Coca Cola",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Coca_ColaLabel.grid(row=0,column=0,pady=10,sticky=W)
Coca_ColaEntry=Entry(frame5,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Coca_ColaEntry.grid(row=0,column=1,pady=10,padx=10)
Coca_ColaEntry.insert(0,0)
#Lable for Pepsi
PepsiLabel=Label(frame5,text="Pepsi",bg="gray20",fg="white",font=("times new roman",15,"bold") )
PepsiLabel.grid(row=1,column=0,pady=10,sticky=W)
PepsiEntry=Entry(frame5,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
PepsiEntry.grid(row=1,column=1,pady=10,padx=10)
PepsiEntry.insert(0,0)
#Lable for Fanta
FantaLabel=Label(frame5,text="Fanta",bg="gray20",fg="white",font=("times new roman",15,"bold") )
FantaLabel.grid(row=2,column=0,pady=10,sticky=W)
FantaEntry=Entry(frame5,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
FantaEntry.grid(row=2,column=1,pady=10,padx=10)
FantaEntry.insert( 0,0)
#Lable for Sprite       
SpriteLabel=Label(frame5,text="Sprite",bg="gray20",fg="white",font=("times new roman",15,"bold") )
SpriteLabel.grid(row=3,column=0,pady=10,sticky=W)
SpriteEntry=Entry(frame5,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
SpriteEntry.grid(row=3,column=1,pady=10,padx=10)
SpriteEntry.insert(0,0)
#Lable for Limca
LimcaLabel=Label(frame5,text="Limca",bg="gray20",fg="white",font=("times new roman",15,"bold") )
LimcaLabel.grid(row=4,column=0,pady=10 ,sticky=W)
LimcaEntry=Entry(frame5,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
LimcaEntry.grid(row=4,column=1,pady=10,padx=10)
LimcaEntry.insert(0,0)
#Lable for Mountain Dew
Mountain_DewLabel=Label(frame5,text="Mountain Dew",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Mountain_DewLabel.grid(row=5,column=0,pady=10)
Mountain_DewEntry=Entry(frame5,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Mountain_DewEntry.grid(row=5,column=1,pady=10,padx=10)

Mountain_DewEntry.insert(0,0)

#frame for bill area
frame6=Frame(frame2,bd=10,relief=SUNKEN)
frame6.grid(row=0,column=3,padx=8,pady=5  )

#Lable for bill Area
billLabel=Label(frame6,text="Bill Area",font=("times new roman",15,"bold"),bd=7,relief=SUNKEN )
billLabel.pack(fill=X) 
#scroll bar for bill area
scrollBar=Scrollbar(frame6,orient=VERTICAL,bd=8,relief=SUNKEN,activebackground="gold")
scrollBar.pack(side=RIGHT,fill=Y)

#text area for bill     
billArea=Text(frame6,width=55,height=20,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN,yscrollcommand=scrollBar.set)
billArea.pack()
scrollBar.config(command=billArea.yview)
#------------------------------------------------------------------------------------------------------



#Lable frame for bill menu

frame7=LabelFrame(root,text="Bill Menu",font=("times new roman",15,"bold"),bg="gray20",fg="gold",bd=12,relief=SUNKEN)
frame7.pack(fill=X,pady=5)
#Lable for total cosmetics
Total_CosmeticsLabel=Label(frame7,text="Total Cosmetics",bg="gray20",fg="white",font=("times new roman",15,"bold") )    
Total_CosmeticsLabel.grid(row=0,column=0,pady=10,sticky=W)
Total_CosmeticsEntry=Entry(frame7,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)   
Total_CosmeticsEntry.grid(row=0,column=1,pady=10,padx=10)
#Lable for total grocery
Total_GroceryLabel=Label(frame7,text="Total Grocery",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Total_GroceryLabel.grid(row=1,column=0,pady=10,sticky=W)
Total_GroceryEntry=Entry(frame7,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Total_GroceryEntry.grid(row=1,column=1,pady=10,padx=10)
#Lable for total cold drinks
Total_Cold_DrinksLabel=Label(frame7,text="Total Cold Drinks",bg="gray20",fg="white",font=("times new roman",15,"bold") )

Total_Cold_DrinksLabel.grid(row=2,column=0,pady=10,sticky=W)
Total_Cold_DrinksEntry=Entry(frame7,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Total_Cold_DrinksEntry.grid(row=2,column=1,pady=10,padx=10)


#Lable for cosmetics Discount
Cosmetic_DiscountLabel=Label(frame7,text="Discount",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Cosmetic_DiscountLabel.grid(row=0,column=2,pady=10,sticky=W)
Cosmetic_DiscountEntry=Entry(frame7,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Cosmetic_DiscountEntry.grid(row=0,column=3,pady=10,padx=10)

#Lable for grocery Discount
Grocery_DiscountLabel=Label(frame7,text="Discount",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Grocery_DiscountLabel.grid(row=1,column=2,pady=10,sticky=W)
Grocery_DiscountEntry=Entry(frame7,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)  
Grocery_DiscountEntry.grid(row=1,column=3,pady=10,padx=10)

#Lable for cold drinks Discount 
Cold_Drinks_DiscountLabel=Label(frame7,text="Discount",bg="gray20",fg="white",font=("times new roman",15,"bold") )
Cold_Drinks_DiscountLabel.grid(row=2,column=2,pady=10,sticky=W)
Cold_Drinks_DiscountEntry=Entry(frame7,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,width=10)
Cold_Drinks_DiscountEntry.grid(row=2,column=3,pady=10,padx=10)


#frame for buttons
frame8=Frame(frame7,bd=10,relief=SUNKEN)
frame8.grid(row=1,column=4,pady=10,padx=5)
#Button for total
TotalButton=Button(frame8,text="Total",font=("times new roman",15,"bold"),bg="gold",fg="black",bd=4,relief=GROOVE,width=10,command=Total)
TotalButton.grid(row=0,column=0,pady=10,padx=5 ,)
#Button for Generate Bill
GenerateBillButton=Button(frame8,text="Generate Bill",font=("times new roman",15,"bold"),bg="gold",fg="black",bd=4,relief=GROOVE,width=10)
GenerateBillButton.grid(row=0,column=1,pady=10,padx=5)
#button for Email Bill
EmailBillButton=Button(frame8,text="Email Bill",font=("times new roman",15,"bold"),bg="gold",fg="black",bd=4,relief=GROOVE,width=10)
EmailBillButton.grid(row=0,column=2,pady=10,padx=5)
#BUTTON FOR Print Bill
PrintBillButton=Button(frame8,text="Print Bill",font=("times new roman",15,"bold"),bg="gold",fg="black",bd=4,relief=GROOVE,width=10)
PrintBillButton.grid(row=0,column=3,pady=10,padx=5)
#Button for clear
ClearButton=Button(frame8,text="Clear",font=("times new roman",15,"bold"),bg="gold",fg="black",bd=4,relief=GROOVE,width=10)
ClearButton.grid(row=0,column=4,pady=10,padx=5)


root.mainloop()

