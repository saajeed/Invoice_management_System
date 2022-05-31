
from tkinter import*
import math,random,os;
from tkinter import messagebox
from datetime import datetime
class Bill_App:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1350x700+0+0")
       self.root.title("Billing software")
       bg_color="#074463"
       title=Label(self.root,text="Billing software",fg="white",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold"),pady=10).pack(fill=X)
       ###################variables
       ####################Cosmetics
       self.soap=IntVar();
       self.face_cream = IntVar();
       self.face_wash = IntVar();
       self.spray = IntVar();
       self.gell = IntVar();
       self.loshan = IntVar();
       ####################grocery
       self.rice = IntVar();
       self.food_oil = IntVar();
       self.daal = IntVar();
       self.wheat = IntVar();
       self.suger = IntVar();
       self.tea = IntVar();
       ####################Cold Drinks
       self.maza = IntVar();
       self.coke = IntVar();
       self.frooti = IntVar();
       self.seven_up = IntVar();
       self.limca= IntVar();
       self.sprite = IntVar();
       #########################Total Product Price & Tax Variable
       self.cosmetics_price=StringVar();
       self.grocery_price = StringVar();
       self.cold_drink_price = StringVar();
       self.cosmetics_tax = StringVar();
       self.grocery_tax = StringVar();
       self.cold_drink_tax = StringVar();
       ############################Customer
       self.c_name=StringVar();
       self.c_phone=StringVar();
       self.bill_no=StringVar();
       x=random.randint(100,900);
       self.bill_no.set(str(x));
       self.search_bill=StringVar();
       #########Customer details frame
       F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
       F1.place(x=0,y=80,relwidth=1)
       cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5)
       cname_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_name,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
       cphn_lbl = Label(F1, text="Phone Number", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=5)
       cphn_txt = Entry(F1, width=15, font="arial 15",textvariable=self.c_phone, bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)
       c_bill_lbl = Label(F1, text="Bill number ", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=4, padx=20, pady=5)
       c_bill_txt = Entry(F1, width=15, font="arial 15",textvariable=self.search_bill, bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)
       bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=50)

       ###########Cosmetics Frame#########
       F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),
                       fg="gold", bg=bg_color)
       F2.place(x=0, y=180, width=325 , height=380)
       bath_lbl=Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
       bath_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5, textvariable=self.soap,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
       Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=1, column=0, padx=10, pady=10, sticky="w")
       Face_cream_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5,textvariable=self.face_cream, relief=SUNKEN).grid(row=1, column=1,
                                                                                                      padx=10, pady=10)
       Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=2, column=0, padx=10, pady=10, sticky="w")
       Face_w_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, textvariable=self.face_wash,relief=SUNKEN).grid(row=2, column=1,
                                                                                                      padx=10, pady=10)
       Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=3, column=0, padx=10, pady=10, sticky="w")
       Hair_s_txt = Entry(F2,textvariable=self.spray, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                      padx=10, pady=10)
       Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=4, column=0, padx=10, pady=10, sticky="w")
       Hair_g_txt = Entry(F2,textvariable=self.gell, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                      padx=10, pady=10)
       Body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=5, column=0, padx=10, pady=10, sticky="w")
       Body_txt = Entry(F2,textvariable=self.loshan, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                      padx=10, pady=10)
       ###########Grocery Frame#########
       F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                       fg="gold", bg=bg_color)
       F2.place(x=318, y=180, width=325, height=380)
       Rice_lbl = Label(F2, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=0, column=0, padx=10, pady=10, sticky="w")
       Rice_txt = Entry(F2,textvariable=self.rice, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                      padx=10, pady=10)
       Food_oil_lbl = Label(F2, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="lightgreen").grid(
          row=1, column=0, padx=10, pady=10, sticky="w")
       Food_oil_txt = Entry(F2,textvariable=self.food_oil, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=10)
       Daal_lbl = Label(F2, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(
          row=2, column=0, padx=10, pady=10, sticky="w")
       Daal_txt = Entry(F2,textvariable=self.daal, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
       Wheat_lbl = Label(F2, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(
          row=3, column=0, padx=10, pady=10, sticky="w")
       Wheat_txt = Entry(F2,textvariable=self.wheat, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
       Sugar_lbl = Label(F2, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=4, column=0, padx=10, pady=10, sticky="w")
       Sugar_txt = Entry(F2, textvariable=self.suger,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
       Tea_lbl = Label(F2, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,
                        fg="lightgreen").grid(
          row=5, column=0, padx=10, pady=10, sticky="w")
       Tea_txt = Entry(F2,textvariable=self.tea, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                      padx=10, pady=10)
       ###########Cold Drinks Frame#########
       F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),
                       fg="gold", bg=bg_color)
       F2.place(x=625, y=180, width=325, height=380)
       maza_lbl = Label(F2, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=0, column=0, padx=10, pady=10, sticky="w")
       maza_txt = Entry(F2, textvariable=self.maza, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                      padx=10, pady=10)
       coca_cola_cream_lbl = Label(F2, text="Coca Cola", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="lightgreen").grid(
          row=1, column=0, padx=10, pady=10, sticky="w")
       coca_cola_txt = Entry(F2, textvariable=self.coke,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=10)
       Frooti_lbl = Label(F2, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(
          row=2, column=0, padx=10, pady=10, sticky="w")
       Frooti_txt = Entry(F2,textvariable=self.frooti, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
       seven_up_lbl = Label(F2, text="7UP", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(
          row=3, column=0, padx=10, pady=10, sticky="w")
       seven_uo_txt = Entry(F2, textvariable=self.seven_up,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
       limca_lbl = Label(F2, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
          row=4, column=0, padx=10, pady=10, sticky="w")
       limca_txt = Entry(F2,textvariable=self.limca, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
       sprite_lbl = Label(F2, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                        fg="lightgreen").grid(
          row=5, column=0, padx=10, pady=10, sticky="w")
       sprite_txt = Entry(F2,textvariable=self.sprite, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                      padx=10, pady=10)
       ########### Bill Area #######
       F5=Frame(self.root,bd=10,relief=GROOVE)
       F5.place(x=950,y=180,width=370,height=380)
       bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
       scrol_y=Scrollbar(F5,orient=VERTICAL)
       self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
       scrol_y.pack(side=RIGHT,fill=Y)
       scrol_y.config(command=self.txtarea.yview)
       self.txtarea.pack(fill=BOTH,expand=1)
       #====== Buttom Frame ==============
       F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                       fg="gold", bg=bg_color)
       F6.place(x=0, y=560, relwidth=1, height=145)
       m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
       m1_txt=Entry(F6,width=18,textvariable=self.cosmetics_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

       m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
                      font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
       m2_txt = Entry(F6,textvariable=self.grocery_price, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

       m3_lbl = Label(F6, text="Total Cold Drink Price", bg=bg_color, fg="white",
                      font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
       m3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

       c1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white",
                      font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
       c1_txt = Entry(F6, width=18,textvariable=self.cosmetics_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

       c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white",
                      font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
       c2_txt = Entry(F6,textvariable=self.grocery_tax, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

       c3_lbl = Label(F6, text="Cold Drink Tax", bg=bg_color, fg="white",
                      font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
       c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

       btn_F=Frame(F6,bd=7,relief=GROOVE)
       btn_F.place(x=750,width=580,height=105)
       total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white", bd=2,pady=15,width=9,font="arial 15 bold").grid(row=0,column=0,padx=4,pady=11)
       GBill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area, bg="cadetblue",fg="white", bd=2,pady=15,width=9,font="arial 15 bold").grid(row=0,column=1,padx=4)
       Clear_btn=Button(btn_F,text="Clear",command = self.clear_data,bg="cadetblue",fg="white", bd=2,pady=15,width=9,font="arial 15 bold").grid(row=0,column=2,padx=4)
       Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",command=self.Exit_app,fg="white", bd=2,pady=15,width=9,font="arial 15 bold").grid(row=0,column=3,padx=4)

    def total(self):
        #====== Cosmetics======#
        self.c_s_p=self.soap.get()*40;
        self.c_fc_p=self.face_cream.get()*120;
        self.c_fw_p=self.face_wash.get()*180;
        self.c_hs_p=self.spray.get()*140;
        self.c_hg_p=self.gell.get()*140;
        self.c_bl_p=self.loshan.get()*180;
        self.total_cosmetic_price=float(
                                        self.c_s_p+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_hs_p+
                                        self.c_hg_p+
                                        self.c_bl_p

                                  );
        self.cosmetics_price.set(str(self.total_cosmetic_price)+" Taka");
        self.c_tax=round((self.total_cosmetic_price*0.02),2);
        self.cosmetics_tax.set(str(self.c_tax));
         #==================Grocery==========#
        self.g_r_p = self.rice.get() * 40;
        self.g_fo_p =  self.food_oil.get() * 60;
        self.g_d_p =  self.daal.get() * 120;
        self.g_w_p =   self.wheat.get() * 180;
        self.g_s_p =  self.suger.get() * 25;
        self.g_t_p=self.tea.get() * 85;
        self.total_grocery_price = float(
                                         self.g_r_p+
                                         self.g_fo_p+
                                         self.g_d_p+
                                         self.g_w_p+
                                         self.g_s_p+
                                         self.g_t_p

        )
        self.grocery_price.set(str(self.total_grocery_price)+" Taka");
        self.g_tax=round((self.total_grocery_price * 0.02), 2);
        self.grocery_tax.set(str(self.g_tax));
        #=======Drinks====#
        self.d_m_p =  (self.maza.get() * 40);
        self.d_c_p =    (self.coke.get() * 60);
        self.d_f_p =   (self.frooti.get() * 120);
        self.d_l_p = (self.seven_up.get() * 180);
        self.d_s_p =   (self.limca.get() * 25) ;
        self.d_sp_p =   (self.sprite.get() * 85);


        self.total_cold_drink_price = float(
                                        self.d_m_p+
                                        self.d_c_p+
                                        self.d_f_p+
                                        self.d_l_p+
                                        self.d_s_p+
                                        self.d_sp_p

        )
        self.cold_drink_price.set(str(self.total_cold_drink_price)+" Taka");
        self.d_tax=round((self.total_cold_drink_price * 0.02), 2);
        self.cold_drink_tax.set(str(self.d_tax));
        self.Total_bill=round((self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax
                              ),2);

    def welcome_bill(self):
       now=datetime.today()
       dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
       self.date=dt_string
       self.txtarea.delete('1.0',END);
       self.txtarea.insert(END,f"\t Assalamualikum {self.c_name.get()}");
       self.txtarea.insert(END,f"\n\n Date & Time : {self.date}")
       self.txtarea.insert(END, f"\n Bill Number   : {self.bill_no.get()}");
       self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}");
       self.txtarea.insert(END, f"\n Phone Number  : {self.c_phone.get()}");
       self.txtarea.insert(END,"\n=========================================");
       self.txtarea.insert(END, "\n Product \t\t QTY\t     Price(Taka)");
       self.txtarea.insert(END, "\n=========================================");
    def bill_area(self):
         if self.c_name.get()=="" or self.c_phone.get()=="":
              messagebox.showerror("Error","Customer details are missing ")
         elif self.cosmetics_tax.get()=="0.0" and self.cold_drink_tax.get()=="0.0" and self.grocery_tax.get() =="0.0":
             messagebox.showerror("Error", "No Product Purchased");

         else :
           self.welcome_bill()
           #=====Cosmetics======#
           if self.soap.get()!=0:
               self.txtarea.insert(END, f"\n Bath Soap \t\t {self.soap.get()}\t\t  {self.c_s_p}");
           if self.face_cream.get()!=0:
               self.txtarea.insert(END, f"\n Face Cream \t\t {self.face_cream.get()}\t\t  {self.c_fc_p}");
           if self.face_wash.get()!= 0:
               self.txtarea.insert(END, f"\n Face Wash \t\t {self.face_wash.get()}\t\t  {self.c_fw_p}");
           if self.spray.get() != 0:
               self.txtarea.insert(END, f"\n Hair Spary \t\t {self.spray.get()}\t\t  {self.c_hs_p}");
           if self.gell.get() != 0:
               self.txtarea.insert(END, f"\n Hair Gel \t\t {self.gell.get()}\t\t  {self.c_hg_p}");
           if self.loshan.get() != 0:
               self.txtarea.insert(END, f"\n Body Losan \t\t {self.loshan.get()}\t\t  {self.c_bl_p}");



               #====Grocery===#
           if self.rice.get() != 0:
                   self.txtarea.insert(END, f"\n Rice \t\t {self.rice.get()}\t\t  {self.g_r_p}");
           if self.wheat.get() != 0:
                   self.txtarea.insert(END, f"\n Wheat \t\t {self.wheat.get()}\t\t  {self.g_w_p}");
           if self.food_oil.get() != 0:
                   self.txtarea.insert(END, f"\n Food Oil \t\t {self.food_oil.get()}\t\t  {self.g_fo_p}");
           if self.daal.get() != 0:
                   self.txtarea.insert(END, f"\n Daal \t\t {self.daal.get()}\t\t  {self.g_d_p}");
           if self.suger.get() != 0:
                   self.txtarea.insert(END, f"\n Sugar \t\t {self.suger.get()}\t\t  {self.g_s_p}");
           if self.tea.get() != 0:
                   self.txtarea.insert(END, f"\n Tea \t\t {self.tea.get()}\t\t  {self.g_t_p}");

                #===Cold Drinks===#
           if self.maza.get() != 0:
               self.txtarea.insert(END, f"\n Maza \t\t {self.maza.get()}\t\t  {self.d_m_p}");
           if self.coke.get() != 0:
               self.txtarea.insert(END, f"\n Coca Cola \t\t {self.coke.get()}\t\t  {self.d_c_p}");
           if self.frooti.get() != 0:
               self.txtarea.insert(END, f"\n Frooti \t\t {self.frooti.get()}\t\t  {self.d_f_p}");
           if self.seven_up.get() != 0:
               self.txtarea.insert(END, f"\n Seven Up \t\t {self.seven_up.get()}\t\t  {self.d_s_p}");
           if self.limca.get() != 0:
               self.txtarea.insert(END, f"\n Limca \t\t {self.limca.get()}\t\t  {self.d_l_p}");
           if self.sprite.get() != 0:
               self.txtarea.insert(END, f"\n Sprite \t\t {self.sprite.get()}\t\t  {self.d_sp_p}");
           self.txtarea.insert(END, "\n-----------------------------------------");
           if self.cosmetics_tax.get()!="0.0":
            self.txtarea.insert(END,f"\n Cosmetics Tax  \t\t\t\t{ self.cosmetics_tax.get()}")
           if self.grocery_tax.get() != "0.0":
               self.txtarea.insert(END, f"\n Grocery Tax  \t\t\t\t{self.grocery_tax.get()}")
           if self.cold_drink_tax.get() != "0.0":
               self.txtarea.insert(END, f"\n Cold Drinks Tax \t\t\t\t{self.cosmetics_tax.get()}")

           self.txtarea.insert(END, f"\n Total \t\t\t\t{self.Total_bill}")
           self.txtarea.insert(END, "\n-----------------------------------------");
           self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
             return
    def find_bill(self):
        x=0;
        for i in os.listdir("bills/") :
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                x=1;
        if x==0:
            print(x)
            messagebox.showerror("Error","invalid Bill no. ")

    def clear_data(self):
        op = messagebox.askyesno("Eixt", "Do you really want to clear?")
        if op > 0:
            self.soap.set(0);
            self.face_cream.set(0);
            self.face_wash.set(0);
            self.spray.set(0);
            self.gell.set(0);
            self.loshan.set(0);
            ####################grocery
            self.rice.set(0);
            self.food_oil.set(0);
            self.daal.set(0);
            self.wheat.set(0);
            self.suger.set(0);
            self.tea.set(0);
            ####################Cold Drinks
            self.maza.set(0);
            self.coke.set(0);
            self.frooti.set(0);
            self.seven_up.set(0);
            self.limca.set(0);
            self.sprite.set(0);
            #########################Total Product Price & Tax Variable
            self.cosmetics_price.set("");
            self.grocery_price.set("");
            self.cold_drink_price.set("");
            self.cosmetics_tax.set("");
            self.grocery_tax.set("");
            self.cold_drink_tax.set("");
            ############################Customer
            self.c_name.set("");
            self.c_phone.set("");
            self.bill_no.set("");
            x = random.randint(100, 900);
            self.bill_no.set(str(x));
            self.search_bill.set("");
            self.welcome_bill();
    def Exit_app(self):
        op=messagebox.askyesno("Eixt","D o you really want to exit?")
        if op>0:
            self.root.destroy()








root =Tk()
obj = Bill_App(root)
root.mainloop()