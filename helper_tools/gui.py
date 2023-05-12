from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import numpy as np
import webview
from helper_tools.data import DataClass
import io
from datetime import datetime

photo_dict = {}


class gui:

    def __init__(self):
        self . d = DataClass()
        self . land_page()
    
    # Landing Page
    def land_page(self):
        self . tk = Tk()
        self . tk . iconbitmap("X:/ishaan//SBI OOPS/img/sbi_logo.ico")
        self . tk . attributes('-fullscreen', True)
        self . tk . title("Welcome to SBI Net Banking")
        self . tk . configure(background = "lightblue")

        self . images_decode()

        # Main Frame - Container
        mCanvas = Canvas(self . tk)
        mCanvas . pack(fill = BOTH, expand = YES)

        mFrame1 = Frame(mCanvas)
        mFrame1 . pack(fill = BOTH, expand = YES)

        canvas1_scroll = Canvas(mFrame1)
        canvas1_scroll . place(relx=0, rely=0, relheight=1, relwidth=1)

        vsb1 = Scrollbar(mFrame1, orient = 'vertical', command = canvas1_scroll . yview)
        vsb1 . place (relx=1, rely=0, relheight=1, anchor='ne')
        
        canvas1_scroll . configure(yscrollcommand= vsb1 . set)
        canvas1_scroll . bind_all("<MouseWheel>", lambda e: self . _on_mousewheel(e, canvas1_scroll))

        m1Frame = Frame(canvas1_scroll, width = 1600, height = 1600, bg = 'lightblue')
        m1Frame . bind("<Configure>", lambda e: canvas1_scroll . configure(scrollregion=canvas1_scroll.bbox("all")))
        cont_wind = canvas1_scroll . create_window((0,0), window = m1Frame, anchor = 'nw')
        
        c1 = Canvas(m1Frame, width = 1600, height = 1600, bg = 'lightblue', highlightthickness=0)
        c1 . pack()
        
        bfscr = Button(c1, image = self . fscreen, borderwidth = 0, command = lambda: self . tggl_fscreen(self . tk))
        bfscr_wind = c1 . create_window(1555, 0, anchor = "nw", window = bfscr)

        #Personal banking Frame
        c2 = Canvas(c1, width = 600, height = 350, bg = '#F8F8F8')
        c2 . place (x = 100, y = 30)

        # Personal Banking image
        pers_bnk_lbl = Label(c1, image = self . pers_bnk, borderwidth = 0)
        pers_bnk_lbl . place(x = 260, y = 80)

        # Login Button
        lgn_pb = Button(c1, image = self . lgn, borderwidth = 0, command = self . login_page , cursor="hand2")
        lgn_pb . place(x = 310, y = 180)

        # # Registration, Contact Us and Help Buttons
        rgstr_pb = Button(c1, image = self . rgstr, borderwidth = 0, cursor="hand2", command = self . registration_page)
        c2 . create_line(228,220, 228,275, fill = "grey")
        hlp_pb =  Button(c1, image = self . hlp, borderwidth = 0, cursor="hand2")
        c2 . create_line(388,220, 388,275, fill = "grey")
        ccare_pb = Button(c1, image = self . c_care, borderwidth = 0, cursor="hand2")

        rgstr_pb . place(x = 150, y = 250)
        hlp_pb . place(x = 340, y = 250)
        ccare_pb . place(x = 500, y = 250)

        # #Corporate banking Frame
        c3 = Canvas(c1, width = 600, height = 350, bg = '#F8F8F8')
        c3 . place (x = 810, y = 30)

        # # Corporate Banking image
        corp_bnk_lbl = Label(c1, image = self . corp_bnk, borderwidth = 0)
        corp_bnk_lbl . place(x = 920, y = 80)

        # # Registration, Contact Us and Help Buttons
        rgstr_cb = Button(c1, image = self . rgstr, borderwidth = 0, cursor="hand2")
        c3 . create_line(228,220, 228,275, fill = "grey")
        hlp_cb =  Button(c1, image = self . hlp, borderwidth = 0, cursor="hand2")
        c3 . create_line(388,220, 388,275, fill = "grey")
        ccare_cb = Button(c1, image = self . c_care, borderwidth = 0, cursor="hand2")

        rgstr_cb . place(x = 860, y = 250)
        hlp_cb . place(x = 1050, y = 250)
        ccare_cb . place(x = 1210, y = 250)

        # Moving Text Starts
        self . moving_text = "All citizens are requested to take e-pledge by visiting CVC’s website. Path for online “Integrity Pledge” is https://pledge.cvc.nic.in. Amalgamation of banks has been effected from 01-04-2021. Kindly delete beneficiaries of merged banks and register beneficiary with new details on account of change in IFSC / account details. Scheduled payments to such beneficiaries with old details may get failed.   |   Register yourself for Doorstep banking services on 18001037188 / 18001213721 or log on to psbdsb.in and avail the services. Stay Home, Stay Safe.   |   SBI never asks for your Card/PIN/OTP/CVV details on phone, message or email. Please do not click on links received on your email or mobile asking your Bank/Card details.   |   Have you tried our new simplified and intuitive business banking platform? Log in to yonobusiness.sbi to avail business banking services."

        self .c_text = Canvas(c1, bg = "gray68", width = 1600, height = 30, border = 0)
        self .c_text . place(x = 0, y = 400)

        text = self .c_text.create_text(0,-2000, text=self.moving_text, fill = 'black', tags=("marquee",), anchor='w')
        self .x1,self .y1,self .x2,self .y2 = self .c_text.bbox("marquee")
        width = self .x2-self .x1
        height = self .y2-self .y1

        self . fps = 40
        self . shift()
        #Moving Text Ends

        #Links Placement Start
        self . links_place(c1)
        #Links Placement End

        # Banners 
        banners_frm = Frame(c1, width = 1200, height = 300)
        banners_frm . place(x = 100, y = 1000)
        self . banners_section()

        self . tk . mainloop()

    # Login Page
    def login_page(self):
        capcha_sol = "my3xg"
        def reset_entries():
            un_entry . delete(0, END)
            pw_entry . delete(0, END)
            capcha_entry . delete(0, END)

        def bck_2_hm():
            self . tk . attributes("-alpha", 1.0)
            self . tl . destroy()

        def capcha_refresh():
            rand_int = np . random . randint(3, size = 1)
            global capcha_sol
            if rand_int == 0:
                cl2 . itemconfig(capcha_img, image = self . capcha1)
                capcha_sol = "my3xg"
            elif rand_int == 1:
                cl2 . itemconfig(capcha_img, image = self . capcha2)
                capcha_sol = "exnxm"
            elif rand_int == 2:
                cl2 . itemconfig(capcha_img, image = self . capcha3)
                capcha_sol = "7mgb8"

        def profil():

            login_creds = self . d . get_credentials()

            for (x,y) in login_creds:
                if un_entry . get() == str(x) and pw_entry . get() == str(y):
                    if capcha_entry . get() == capcha_sol:
                        self . profile_page(str(x))
                        self . tl . destroy()
                    else:
                        messagebox.showinfo("Error", "Wrong captcha")
                    break

            
            else:
                messagebox.showinfo("Error", "Username or password either wrong or does not exist")
            
        def fgt_pss():
            def fnd_uname(inp):
                def chng(new_pass1, new_pass2, u_name):
                    if new_pass1 == new_pass2:
                        self . d. password_update(repr(new_pass1), u_name)
                    
                    else:
                        messagebox . showerror("Password Mismatch", "The entered passwords do not match")

                # Getting credentials 
                cred_list = self . d. password_data()
                credent_list = [] # For u_name, email_address, contact
                sec_ques_list= [] # For Security Questions
                sec_ans_list = [] # For Security Answers
                
                # For u_name, email_address, contact
                for i in cred_list:
                    a = []
                    for j in [0,8.9]:
                        a . append(i[j])
                    credent_list . append(a)

                # For Security Questions
                for i in cred_list:
                    a = []
                    for j in [2,4,6]:
                        a . append(i[j])
                    sec_ques_list . append(a)

                # For Security Answers
                for i in cred_list:
                    a = []
                    for j in [3,5,7]:
                        a . append(i[j])
                    sec_ans_list . append(a)
                        
                def chng_ps():
                        for i in range(3):
                            if [ch_q . get(), ch_a . get()] == [sec_ques_list[i], sec_ans_list[i]] :
                                Label(tf, text = "Enter new password:", background =  "lightblue") . place(x = 10, y = 200)
                                Label(tf, text = "Confirm new password:", background =  "lightblue") . place(x = 10, y = 230)

                                ps1 = Entry(tf, show = "*")
                                ps2 = Entry(tf, show = "*")
                                ps1 . place(x = 190, y = 200)
                                ps2 . place(x = 190, y = 230)

                                chg_btn = Button(tf, text = "Change Password", command = lambda: chng(ps1 . get(), ps2 . get(), acc_dt[0]))
                                chg_btn . place(x = 140, y = 260)

                                break
                            
                            else:
                                messagebox . showerror("Wrong Input", "Kindly fill the correct details")
                
                for each_cred in credent_list:
                    if inp == each_cred[0] or inp == each_cred[1] or inp == each_cred[2]:
                        text_disp = "Username: " + str(each_cred[0]) 
                        Label(tf, text = text_disp, background =  "lightblue") . place(x = 10, y = 70)
                        Label(tf, text = "Choose your security question:", background =  "lightblue") . place(x = 10, y = 100)
                        Label(tf, text = "Enter your security answer:", background =  "lightblue") . place(x = 10, y = 130)

                        acc_dt = each_cred
                        
                        q_lst = ["What is your childhood friend's name?", 
                                "What is your favorite color?", 
                                "What was your first pet's name?", 
                                "Where were you born?", 
                                "What is your favorite food?", 
                                "What is the color of your eye?", 
                                "What is your favorite destination?"]

                        ch_q = StringVar()
                        q_chose = ttk.Combobox(tf, width = 30, textvariable = ch_q)
                        q_chose['values'] = (self . q_lst)
                        q_chose . place(x = 190, y = 100)

                        ch_a = Entry(tf)
                        ch_a . place(x = 190, y = 130)

                        chng_ps_btn = Button(tf, text = "Submit", command = chng_ps)
                        chng_ps_btn . place(x = 160, y = 160)

                        break
                    
                    else:
                        messagebox . showerror("No such user in the database", "Kindly check the entered username/email address")

            tf = Toplevel()
            tf . iconbitmap("X:/ishaan/SBI OOPS/img/sbi_logo.ico")
            tf . title("Forgot Username/Password")
            tf . configure(background = "lightblue")
            tf . geometry("400x400")

            Label(tf, text = "Enter your username, contact or email address:", background = "lightblue") . place(x = 10, y = 10)
            un_em = Entry(tf)
            un_em . place(x = 260, y = 10)

            sbmit = Button(tf, text = "Submit", command = lambda: fnd_uname(un_em . get()))
            sbmit . place(x = 160, y = 40)

            Label(tf, text = "** In case you don't remember your chosen security questions, contact your respective branch", background = "lightblue", font = "Verdana 6") . place(x = 5, y = 380)

        self . tl = Toplevel()
        self . tl . iconbitmap("X:/ishaan/SBI OOPS/img/sbi_logo.ico")
        self . tl . attributes('-fullscreen', True)
        self . tl . title("Login to SBI Net Banking")
        self . tl . configure(background = "lightblue")

        cl1 = Canvas(self . tl, bg = 'lightblue', highlightthickness=0)
        cl1 . pack(fill = BOTH, expand = TRUE)

        bfscr_lgn = Button(cl1, image = self . fscreen, borderwidth = 0, command = lambda: self . tggl_fscreen(self . tl))
        bfscr_lgn_wind = cl1 . create_window(1575, 0, anchor = "nw", window = bfscr_lgn)

        # Login Credentials Frame Start
        cl2 = Canvas(cl1, width = 1400, height = 700, bg = '#F8F8F8')
        cl2 . place (x = 100, y = 100)

        #Back Button
        bck_btn = Button(cl2, image = self . bck, command = bck_2_hm)
        bck_btn . place(x = 20, y = 20)

        # Side images
        wlc_img = cl2 . create_image(0, 80, anchor = "nw", image = self . lgn_wlc)
        rnd_img1 = cl2 . create_image(700, 120, anchor = "nw", image = self . rnd_pic1)
        rnd_img2 = cl2 . create_image(0, 500, anchor = "nw", image = self . rnd_pic2)
        rnd_img3 = cl2 . create_image(0, 450, anchor = "nw", image = self . rnd_pic3)
        
        # Login Entries -
        # Username
        u_name = cl2 . create_text(120, 150, anchor = "nw", text = "Username: *", font = ('Helvetica 10 bold'))
        un_entry = Entry(self .tl, bg = "#D6DBDF")
        un_window = cl2 . create_window(120, 175, anchor = "nw", window = un_entry)
        #Conditions
        u_name_cond = cl2 . create_text(300, 168, anchor = "nw", text = "Minimum 5 Characters \nOnly allowed special characters -> '_ , ! , #", font = ('Helvetica 8'))
        # Password
        pw = cl2 . create_text(120, 200, anchor = "nw", text = "Password: *", font = ('Helvetica 10 bold'))
        pw_entry = Entry(self .tl, bg = "#D6DBDF", show = "*")
        pw_window = cl2 . create_window(120, 225, anchor = "nw", window = pw_entry)
        #Conditions
        pw_cond = cl2 . create_text(300, 220, anchor = "nw", text = "Must Contain at least 8 Characters with minimum: \nOne Capital Letter \tOne Lowercase Letter \nOne Digit - \tOne Symbol", font = ('Helvetica 8'))
        # Captcha
        capcha = cl2 . create_text(120, 250, anchor = "nw", text = "Enter the Captcha: *", font = ('Helvetica 10 bold'))
        capcha_entry = Entry(self .tl, bg = "#D6DBDF")
        capcha_window = cl2 . create_window(120, 275, anchor = "nw", window = capcha_entry)
        capcha_img = cl2 . create_image(120, 300, anchor = "nw", image = self . capcha1)
        # Buttons
        rld_btn = Button(cl2, image = self . rld, borderwidth = 0, command = capcha_refresh)
        rld_btn . place(x = 250,y = 275)
        lgn_btn = Button(cl2, text = "Login", bg = "#2E86C1", fg = "white", command = profil)
        lgn_btn . place(x = 120, y = 365)
        rst_btn = Button(cl2, text = "Reset", bg = "#2E86C1", fg = "white", command = reset_entries)
        rst_btn . place(x = 180, y = 365)

        # Bind enter key with login button(Just link with the login function not the button itself)
        self . tl . bind("<Return>", lambda e: profil())

        #Forgot Password button
        fgt_pw = Label(cl2, text = "Forgot Login Username/Password?", background = "#F8F8F8", fg = "#30606e", font = ("Helvetica 10"), cursor="hand2")
        fgt_pw . bind("<Button-1>", lambda e: fgt_pss())
        fgt_pw . place(x = 300, y = 375)
        
        # Login Credentials Frame End
        self . tk . attributes("-alpha", 0)

    # Registeration Page
    def registration_page(self):
        pass

    # Profile Page -- It will contain multiple frames to switch between balance, deposits and loans
    def profile_page(self, u_name):
        def payments_func():
            self . payments_frm . tkraise()

        def deposits_func():
            self . deposits_frm . tkraise()
        
        def loans_func():
            self . loans_frm . tkraise()

        details_lst = self . d . get_profile(u_name)

        profile_pic = Image . open(io.BytesIO(details_lst[2])) . resize((150, 150), Image.ANTIALIAS)
        self . profile_pic = ImageTk . PhotoImage(profile_pic)

        self . tp = Toplevel()
        self . tp . iconbitmap("X:/ishaan/_Data Science/SBI/img/sbi_logo.ico")
        self . tp . attributes('-fullscreen', True)
        self . tp . title("Profile")
        self . tp . configure(background = "lightblue")

        canvas_prof = Canvas(self . tp, width = 1600, height = 900, background = "lightblue")
        canvas_prof . place(x = 0, y = 0)
        
        self . prof_frame = Frame(canvas_prof, width = 1250, height = 650, bg = '#F8F8F8')
        self . prof_frame . place(x = 300, y = 200)

        bfscr_prf = Button(canvas_prof, image = self . fscreen, borderwidth = 0, command = lambda: self . tggl_fscreen(self . tp))
        bfscr_prf_wind = canvas_prof . create_window(1575, 0, anchor = "nw", window = bfscr_prf)

        # Canvas for details
        self . profile_details_frame(canvas_prof, details_lst)

        # Canvas for buttons
        opt_canvas = Canvas(canvas_prof, width = 298, height = 646, bg = '#1872AF')
        opt_canvas . place(x = 0, y = 200)

        # Payments button
        payments_btn = Button(opt_canvas, text = "Payments/Transfers", image = self . pmts, command = payments_func, font = "Arial 11", compound = TOP, bg = "#1872AF", borderwidth = 0, activebackground = "#14B2E2")
        payments_btn_wnd = opt_canvas . create_window(0,0, anchor = "nw", window = payments_btn)
        # Deposits Button
        deposit_btn = Button(opt_canvas, text = "Deposits", image = self . dpst, command = deposits_func, font = "Arial 11", compound = TOP, bg = "#1872AF", borderwidth = 0, activebackground = "#14B2E2")
        deposit_btn_wnd = opt_canvas . create_window(0,216, anchor = "nw", window = deposit_btn)
        # Loans Button
        loans_btn = Button(opt_canvas, text = "Apply for Loans", image = self . lns, command = loans_func, font = "Arial 11", compound = TOP, bg = "#1872AF", borderwidth = 0, activebackground = "#14B2E2")
        loans_btn_wnd = opt_canvas . create_window(0,432, anchor = "nw", window = loans_btn)

        # Styling for the Treeviews
        style = ttk.Style(self)
        aktualTheme = style.theme_use()
        style.theme_create("dummy", parent=aktualTheme)
        style.theme_use("dummy")

        # Getting balance 
        self . blnc = details_lst[8]

        # Payments Frame
        self . payments_frame(u_name)

        # Deposits Frame
        self . deposits_frame(u_name)

        # Loans Frame
        self . loans_frame(u_name)

        self . payments_frm . tkraise()

        # Update Security Questions link
        def on_enter_u(e):
            updt_sec_quess . config(font = "Verdana 10 underline", fg = "blue")
        
        def on_leave_u(e):
            updt_sec_quess . config(font = "Verdana 10", fg = "black")


        updt_sec_quess = Label(canvas_prof, text = "Update Security Questions", background = "lightblue", fg = "#30606e", font = ("Verdana 10"), cursor="hand2")
        updt_sec_quess . bind("<Button-1>", lambda e: self . updt_sec_ques(u_name))
        updt_sec_quess . bind("<Enter>", on_enter_u)
        updt_sec_quess . bind("<Leave>", on_leave_u)

        updt_sec_quess . place(x = 1375, y = 850)

    # Profile Page - Details Frame 
    def profile_details_frame(self, canvas_prof, details_lst):
        det_canvas = Canvas(canvas_prof, bg = "#1872AF", width = 1246, height = 160, borderwidth = 0)
        det_canvas . place(x = 300, y = 40)

        logo_pc = canvas_prof . create_image(10,10, anchor = "nw", image = self . sbi_logo)
        prf_pc = det_canvas . create_image(1090,7, anchor = "nw", image = self . profile_pic)
        prf_ttl = canvas_prof . create_text(750, 10, anchor = "nw", text = "PROFILE", font = "Arial 20 bold")

        name_frm = LabelFrame(det_canvas, text = "Name:", bg = "#1872AF", width = 40)
        if details_lst[4] == None:
            full_name = str(details_lst[3]) + " " + str(details_lst[5])
        else:
            full_name = str(details_lst[3]) + " " + str(details_lst[4]) + " " + str(details_lst[5])
        name_lbl = Label(name_frm, text = full_name, bg = "#1872AF", width = 40, justify = "left")
        name_frm . place(x = 20, y = 10)
        name_lbl . pack()

        custid_frm = LabelFrame(det_canvas, text = "Account Number:", bg = "#1872AF", width = 40)
        acc_num = '0'*(7-len(str(details_lst[0]))) + str(details_lst[0])
        custid_lbl = Label(custid_frm, text = acc_num, bg = "#1872AF", width = 40)
        custid_frm . place(x = 20, y = 90)
        custid_lbl . pack()

        mailid_frm = LabelFrame(det_canvas, text = "Email ID:", bg = "#1872AF", width = 40)
        mailid_lbl = Label(mailid_frm, text = details_lst[6], bg = "#1872AF", width = 40)
        mailid_frm . place(x = 370, y = 10)
        mailid_lbl . pack()

        contct_frm = LabelFrame(det_canvas, text = "Contact Number:", bg = "#1872AF", width = 40)
        contct_lbl = Label(contct_frm, text = details_lst[7], bg = "#1872AF", width = 40)
        contct_frm . place(x = 720, y = 10)
        contct_lbl . pack()

    # Profile Page - Payments Frame 
    def payments_frame(self, u_name):
        def dep_func(amnt):

            self . blnc += float(amnt . get())
            self . d . dep_balance(u_name, datetime . now() . strftime("%Y-%m-%d %H:%M:%S"), float(amnt . get()), 0, self . blnc)
            
            deposit_list_ = self . d . get_balance(u_name)

            dep_l = deposit_list_[len(deposit_list_) - 1]
            
            if len(deposit_list_) % 2 == 0:
                self . tree_trans . insert('', 0, text = dep_l, values = dep_l, tags = ('evenrow',))
            else:
                self . tree_trans . insert('', 0, text = dep_l, values = dep_l, tags = ('oddrow',))

            p_can . itemconfigure(cur_blnc,text = self . blnc)
            
        def wdraw_func(amnt):
            
            self . blnc -= float(amnt . get())
            self . d . wth_balance(u_name, datetime . now() . strftime("%Y-%m-%d %H:%M:%S"), 0, float(amnt . get()), self . blnc)
            
            withdraw_list_ = self . d . get_balance(u_name)

            wdraw_l = withdraw_list_[len(withdraw_list_) - 1]

            if len(withdraw_list_) % 2 == 0:
                self . tree_trans . insert('', 0, text = wdraw_l, values = wdraw_l, tags = ('evenrow',))
            else:
                self . tree_trans . insert('', 0, text = wdraw_l, values = wdraw_l, tags = ('oddrow',))

            p_can . itemconfigure(cur_blnc,text = self . blnc)
        
        self . payments_frm = Frame(self . prof_frame, width = 1250, height = 650, bg = '#F8F8F8')
        self . payments_frm . place(x = 0, y = 0)

        p_can = Canvas(self . payments_frm, width = 1250, height = 650, bg = '#F8F8F8')
        p_can . place(x = 0, y = 0)

        
        
        blnc_lst = self . d . get_balance(u_name)

        p_can . create_text(10, 50, text = "Current Balance: ", anchor = "nw")
        cur_blnc = p_can . create_text(100, 50, text = self . blnc, anchor = "nw")

        p_can . create_text(500, 80, text = "Make a Transaction:", font = "Helvetica 16 bold", anchor = "nw")
        p_can . create_text(325, 120, text = "Enter the amount to be deposited/withdrawn: ", font = "Helvetica 10 bold", anchor = "nw")

        amnt = StringVar()
        tran_entry = Entry(p_can, textvariable = amnt, width = 30)
        p_can . create_window(640, 120, window = tran_entry, anchor = "nw")

        dep_btn = Button(p_can, text = "Deposit", command = lambda: dep_func(amnt))
        wdr_btn = Button(p_can, text = "Withdraw", command = lambda: wdraw_func(amnt))
        p_can . create_window(500, 160, anchor = "nw", window = dep_btn)
        p_can . create_window(600, 160, anchor = "nw", window = wdr_btn)

        p_can . create_text(575, 430, text = "Transactions:", font = "Helvetica 16 bold")
        
        # Add a Treeview widget for Transactions
        self . tree_trans = ttk.Treeview(p_can, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)
        trans_columns = {"# 1": "Transaction Number","# 2": "Transaction Time", "# 3": "Deposit", "# 4": "Withdraw", "# 5": "Balance"}
        self . tree_creator(trans_columns, self . tree_trans, blnc_lst, 170)
        self . tree_trans . place(x = 160, y = 450)

    # Profile Page - Deposits Frame 
    def deposits_frame(self, u_name):
        def depos():
            if d . get() in dep_types:
                def calc_dep():

                    if amt_dep . get() != "" and int_rt[d . get()] != "" and per_dep . get() != "":
                        def add_depos(a, i, d, f, t):
                            self . d . new_dep(u_name, datetime . now() . strftime("%Y-%m-%d %H:%M:%S"), t, a, i,d,f)
                            dept_lst = self . d . deposits_get(u_name)

                            dp_l = dept_lst[len(dept_lst) - 1]

                            if len(dept_lst) % 2 == 0:
                                self . tree_dep . insert('', 0, text = dp_l, values = dp_l, tags = ('evenrow',))
                            else:
                                self . tree_dep . insert('', 0, text = dp_l, values = dp_l, tags = ('oddrow',))
                    else:
                        messagebox . showinfo("Error", "Fill all the fields")

                    fin_amt = float(amt_dep.get()) * (1 +  ( float( int_rt[ d.get() ] ) * float( per_dep.get() ) / 100))
                    fin_amt_txt = "Total Amount after {} years: " . format(per_dep.get()) + str(fin_amt)
                    fin_amt_txt_w = d_can . create_text(30, 250, text = fin_amt_txt, anchor = "nw")

                    add_dep_btn = Button(d_can,text = "Make a Deposit", command = lambda: add_depos(amt_dep . get(), int_rt[d . get()], per_dep . get(), fin_amt, d . get()))
                    d_can . create_window(160, 280, anchor = "nw", window = add_dep_btn)
                
                def chng_depos():
                    i_r = "Interest Rate: " + str(int_rt[d.get()])
                    d_can . itemconfig(d_typ, text = d.get())
                    d_can . itemconfig(d_typ_int, text = i_r)

                
                d_can . delete(dep_chs_wind)
                dep_chg = Button(d_can, text = "Change Deposit", command = chng_depos)
                dep_chg_wind = d_can . create_window(30,80, anchor = "nw", window = dep_chg)
                i_r = "Interest Rate: " + str(int_rt[d.get()])
                d_typ = d_can . create_text(30, 120, text = d . get(), anchor = "nw")
                d_typ_int = d_can . create_text(30, 140, text = i_r, anchor = "nw")
                d_can . create_text(30, 170, text = "Amount to be deposited:", anchor = "nw")
                d_can . create_text(30, 190, text = "Period of deposit:", anchor = "nw")
                
                amt_dep = Entry(d_can)
                per_dep = Entry(d_can)
                amt_dep_wind = d_can . create_window(230, 170, anchor = "nw", window = amt_dep)
                per_dep_wind = d_can . create_window(230, 190, anchor = "nw", window = per_dep)

                but_dep = Button(d_can, text = "Calculate Total EMI", command = calc_dep)
                but_dep_wnd = d_can . create_window(140, 220, anchor = "nw", window = but_dep)
            
            else:
                messagebox . showinfo("Error", "Choose a deposit")
        
        self . deposits_frm = Frame(self . prof_frame, width = 1250, height = 650, bg = '#F8F8F8')
        self . deposits_frm . place(x = 0, y = 0)

        d_can = Canvas(self . deposits_frm, width = 1250, height = 650, bg = '#F8F8F8')
        d_can . place(x = 0, y = 0)

        dep_types = ["Fixed Deposit", "Recurring Deposit", "Systematic Investment Plan", "Public Provident Fund", "Joint Account", "Current Account"]
        int_rt = {"Fixed Deposit": 6.7, "Recurring Deposit": 7.3, "Systematic Investment Plan": 8.6, "Public Provident Fund": 9.2, "Joint Account": 2.7, "Current Account": 3.1}

        d_can . create_text(30, 30, text = "Choose your deposit type:", anchor = "nw")
        
        # Combobox
        d = StringVar()
        dep_chose = ttk.Combobox(d_can, width = 45, textvariable = d, state = "readonly")
        dep_chose['values'] = (dep_types)
        dep_chose . place(x = 30, y = 50)

        dep_chs = Button(d_can, text = "Choose Deposit", command = depos)
        dep_chs_wind = d_can . create_window(30,80, anchor = "nw", window = dep_chs)

        # Deposits history list
        dep_lst = self . d . deposits_get(u_name)

        d_can . create_text(575, 430, text = "Deposits:", font = "Helvetica 16 bold")
        # Add a Treeview widget fo Deposits
        self . tree_dep = ttk.Treeview(d_can, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings', height=5)
        dep_columns = {"# 1": "Deposit ID","# 2": "Deposit Time", "# 3": "Deposit Type", "# 4": "Deposit Amount", "# 5": "Deposit Interest", "# 6": "Deposit Duration", "#7": "Final Amount"}
        self . tree_creator(dep_columns, self . tree_dep, dep_lst, 170)
        self . tree_dep . place(x = 40, y = 450)

    # Profile Page - Loans Frame 
    def loans_frame(self, u_name):
        def loans_get(loan_typ):
            def emi_calculation():
                if amnt_depo . get() != '' and tim_per . get() != '':
                    calc_emi = float(amnt_depo . get()) * (float(tim_per . get()) * in_rate / 100)
                    fin_amnt = float(amnt_depo . get()) + calc_emi

                    l_can . itemconfigure(emi_lbl, text = calc_emi)
                    l_can . itemconfigure(fam_lbl, text = fin_amnt)

                    l_can . create_text(500,180, text = "TAKE Your FIRST STEP towards REALIZING your DREAMS", font = "Verdana 13 bold", anchor = "nw")
                    
                    def apply_now():
                        confirmed = messagebox . askyesno("Confirmation", "Are you sure you want to apply for the loan?")
                        if confirmed:
                            self . d . new_loan(u_name, datetime . now() . strftime("%Y-%m-%d %H:%M:%S"), loan_typ, amnt_depo . get(), tim_per . get(), in_rate, calc_emi, fin_amnt)
                            
                            loan_list_ = self . d . get_loans(u_name)

                            loan_l = loan_list_[len(loan_list_) - 1]

                            if len(loan_list_) % 2 == 0:
                                self . tree_loans . insert('', 0, text = loan_l, values = loan_l, tags = ('evenrow',))
                            else:
                                self . tree_loans . insert('', 0, text = loan_l, values = loan_l, tags = ('oddrow',))

                    # Apply for the loan link
                    def on_enter_a(e):
                        apply_loan_txt . config(fg = "red")
                    
                    def on_leave_a(e):
                        apply_loan_txt . config(fg = "blue")

                    apply_loan_txt = Label(l_can, text = "Apply for this Loan Now", background = "#F8F8F8", fg = "blue", font = ("Verdana 13 underline bold"), cursor="hand2")
                    apply_loan_txt . bind("<Button-1>", lambda e: apply_now())
                    apply_loan_txt . bind("<Enter>", on_enter_a)
                    apply_loan_txt . bind("<Leave>", on_leave_a)
                    apply_loan_txt . place(x = 650, y = 210)
                
                else:
                    messagebox . showerror("Blank Field(s)", "All fields are required to be filled")

            if loan_typ in list(int_rt_ln . keys()):
                l_can . create_text(30,250, anchor = "nw", text = "Enter amount to be deposited:")
                l_can . create_text(30,280, anchor = "nw", text = "Interest Rate:")
                l_can . create_text(30,310, anchor = "nw", text = "Enter the time period of deposit:")

                in_rate = int_rt_ln[loan_typ]
                
                amnt_depo = Entry(l_can)
                l_can . create_window(250,250, anchor = "nw", window = amnt_depo)
                l_can . create_text(250,280, anchor = "nw", text = in_rate)
                tim_per = Entry(l_can)
                l_can . create_window(250,310, anchor = "nw", window = tim_per)

                emi_calc_btn = Button(l_can, text = "Calculate EMI", command = emi_calculation)
                emi_calc_btn_wind = l_can . create_window(100,350, anchor = "nw", window = emi_calc_btn)

                l_can . create_text(30,380, text = "EMI", anchor = "nw")
                l_can . create_text(30,410, text = "Final Amount", anchor = "nw")
                emi_lbl = l_can . create_text(250,380, text = "---", anchor = "nw")
                fam_lbl = l_can . create_text(250,410, text = "---", anchor = "nw")

            else:
                messagebox.showinfo("No Input", "Please select an option to proceed")

        self . loans_frm = Frame(self . prof_frame, width = 1250, height = 650, bg = '#F8F8F8')
        self . loans_frm . place(x = 0, y = 0)

        l_can = Canvas(self . loans_frm, width = 1250, height = 650, bg = '#F8F8F8')
        l_can . place(x = 0, y = 0)

        l_can . create_text(30, 30, text = "Choose your required loan type:", anchor = "nw")
        l_can . create_text(250, 30, text = "EMI:", anchor = "nw")

        int_rt_ln = {"Home Loan": 6.65, "Student Loan": 3.5, "Personal Loan": 12.8, "Mortgage Loan": 7.6, "Small Business Loan": 5.9}
        #print(list(int_rt_ln . keys()))

        loan_type = StringVar()

        hom_l = Radiobutton(l_can, text = "Home Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Home Loan", variable = loan_type)
        stu_l = Radiobutton(l_can, text = "Student Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Student Loan", variable = loan_type)
        per_l = Radiobutton(l_can, text = "Personal Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Personal Loan", variable = loan_type)
        mrt_l = Radiobutton(l_can, text = "Mortgage Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Mortgage Loan", variable = loan_type)
        smb_l = Radiobutton(l_can, text = "Small Business Loan", activebackground = "#F8F8F8", background = "#F8F8F8", value = "Small Business Loan", variable = loan_type)

        hom_l_wind = l_can . create_window(30,50, anchor = "nw", window = hom_l)
        stu_l_wind = l_can . create_window(30,80, anchor = "nw", window = stu_l)
        per_l_wind = l_can . create_window(30,110, anchor = "nw", window = per_l)
        mrt_l_wind = l_can . create_window(30,140, anchor = "nw", window = mrt_l)
        smb_l_wind = l_can . create_window(30,170, anchor = "nw", window = smb_l)

        l_can . create_text(250, 55, text = "6.65%", anchor = "nw")
        l_can . create_text(250, 85, text = "3.5%", anchor = "nw")
        l_can . create_text(250, 115, text = "12.8%", anchor = "nw")
        l_can . create_text(250, 145, text = "7.6%", anchor = "nw")
        l_can . create_text(250, 175, text = "5.9%", anchor = "nw")
        
        clc_emi_btn = Button(l_can, text = "Select", command = lambda: loans_get(loan_type . get()))
        clc_emi_btn_wind = l_can . create_window(100,200, anchor = "nw", window = clc_emi_btn)

        # Loans history list
        loans_list = self . d . get_loans(u_name)

        l_can . create_text(575, 430, text = "Loans:", font = "Helvetica 16 bold")

        # Add a Treeview widget for Loans
        self . tree_loans = ttk . Treeview(l_can, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings', height=5)

        loans_columns = {"# 1": "Loan ID","# 2": "Loan Time", "# 3": "Loan Type", "# 4": "Loan Amount", "# 5": "Loan Interest", "# 6": "Loan Duration", "#7": "EMI", "# 8": "Final Amount"}

        self . tree_creator(loans_columns, self . tree_loans, loans_list, 140)        

        self . tree_loans . place(x = 10, y = 450)

    def updt_sec_ques(self, u_name):
            tu = Toplevel()

            tu.iconbitmap("X:/ishaan/_Data Science/SBI/img/sbi_logo.ico")
            tu.geometry("400x210")
            tu.title("Update Security Questions")
            tu.configure(background = "lightblue")

            q_lst = ["What is your childhood friend's name?", 
                                "What is your favorite color?", 
                                "What was your first pet's name?", 
                                "Where were you born?", 
                                "What is your favorite food?", 
                                "What is the color of your eye?", 
                                "What is your favorite destination?"]


            def updt():
                if n1.get()!="" and a1.get()!="" and n2.get()!="" and a2.get()!="" and n3.get()!="" and a3.get()!="":
                    self . d . sec_ques_updat(repr(n1 . get()), repr(a1 . get()), repr(n2 . get()),  repr(a2 . get()), repr(n3 . get()), repr(a3 . get()), u_name)
                    messagebox.showinfo("Information updated", "Your information is updated successfully")
                else:
                    messagebox.showerror("Empty fields", "Please enter all fields")

            q1_u = Label(tu, text = "Choose your first question:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 00)
            a1_u = Label(tu, text = "Answer:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 30)
            q2_u = Label(tu, text = "Choose your second question:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 60)
            a2_u = Label(tu, text = "Answer:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 90)
            q3_u = Label(tu, text = "Choose your third question:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 120)
            a3_u = Label(tu, text = "Answer:", activebackground = "lightblue", background = "lightblue") . place(x = 10, y = 150)

            n1 = StringVar()
            q1_chose = ttk.Combobox(tu, width = 32, textvariable = n1)
            q1_chose['values'] = (q_lst)
            q1_chose . place(x = 180, y = 00)
            
            n2 = StringVar()
            q2_chose = ttk.Combobox(tu, width = 32, textvariable = n2)
            q2_chose['values'] = (q_lst)
            q2_chose . place(x = 180, y = 60)
            
            n3 = StringVar()
            q3_chose = ttk.Combobox(tu, width = 32, textvariable = n3)
            q3_chose['values'] = (q_lst)
            q3_chose . place(x = 180, y = 120)

            a1 = StringVar()
            a2 = StringVar()
            a3 = StringVar()

            ans1_u = Entry(tu, textvariable = a1) . place(x = 180, y = 30)
            ans2_u = Entry(tu, textvariable = a2) . place(x = 180, y = 90)
            ans3_u = Entry(tu, textvariable = a3) . place(x = 180, y = 150)

            b_u = Button(tu, text = "Update", command = updt) . place(x = 100, y = 180)

    # Links on the landing page
    def links_place(self, c1):
        links_ = [
                ["SBI Salary Account", "https://bank.sbi/web/salary-account"], 
                ["Linking of PAN with Aadhaar", "https://eportal.incometax.gov.in/iec/foservices/#/pre-login/bl-link-aadhaar"],
                ["Registration for Doorstep Banking", "https://psbdsb.in/"],
                ["Fair Lending Practice Code", "https://www.onlinesbi.com/documents/Yono_Business_Fair_Practice_Lending_Code.pdf"],
                ["Purchase Insurance Policy", "https://www.sbiyono.sbi/wps/portal/login"],
                ["SBI General Insurance Document Download", "https://www.sbigeneral.in/portal/downloads"],
                ["SBI FasTag", "https://fastag.onlinesbi.com/"],
                ["SBI Mutual Fund", "https://www.sbimf.com/en-us/quick-invest?arn_code=ARN12195"],
                ["NRI Services", "https://bank.sbi/web/nri/home"],
                ["Customer Complaint Form", "https://crcf.sbi.co.in/"],
                ["SBICAP Securities", "http://www.sbismart.com/"],
                ["SBICAP Trustee Company Ltd", "http://www.sbicaptrustee.com/"],
                ["SBI Express Remit", "https://remit.onlinesbi.com/"],
                ["Customer Request and Complaint Form (NEW)", "https://crcf.sbi.co.in/"],
                ["SBI Life Insurance", "http://www.sbilife.co.in/"],
                ["SBI Card", "http://www.sbicard.com/"],
                ["OnlineSBI Global", "https://www.onlinesbiglobal.com/"],
                ["Foreign Travel/EZ-Pay/Gift Cards", "https://prepaid.onlinesbi.com/"],
                ["SBI General Insurance", "http://www.sbigeneral.in/"],
                ["Service charges for non-maintenance of Average Balance in SB accounts", ""],
                ["CASH@SBI", "https://www.sbi.co.in/portal/web/home/cash-at-sbi"],
                ["State Bank Loyalty Rewardz", "https://www.rewardz.sbi/"],
                ["EPF", "https://www.onlinesbi.com/prelogin/epfohome.htm"],
                ["Online Locker Enquiry", "https://retail.onlinesbi.com/preretail/prelogineLockerInitial.htm"],
                ["Loan Against Shares", "https://retail.onlinesbi.com/las/loanagainstsharesinit.htm"],
                ["GSTN Updation", "https://www.onlinesbi.com/documents/GSTN_Transactions_Updation_Process.pdf"],
                ["eSBTR Challan Generation", "https://esbtr.onlinesbi.com/ESBTR1/OnlineReg.do?method=fetchDistrictList"],
                ["Donate - Kerala Floods", "https://kerala.gov.in/home"],
                ["Noida Metro Card", "https://retail.onlinesbi.com/sbijava/retail/html/faq_noida_metro.html"],
                ["SBICAP Trustee Company Ltd My WILL Services Online", "https://sbicaptrustee.in/mywill/index.jsp"],
                ["Nagpur Metro Card", "https://retail.onlinesbi.com/sbijava/retail/html/faq_nagpur_metro.html"],
                ["COVID-19 EMI Deferment", "https://bank.sbi/stopemi"],
                ["PM Mudra Yojana", "https://sbi.co.in/web/business/sme/sme-loans/pm-mudra-yojana"]
                ]

        y_pos = 0

        c4 = Canvas(c1, width = 1200, height = 300, bg = '#F8F8F8')
        c4 . place(x = 150, y = 450)

        links_lbl = ["link_label_{}" . format(i) for i in range(len(links_))] # 

        # for i in range(len(links_)):
        #     exec(f'def on_enter{i}(self, e):   link_label_{i} . config(font = "Verdana 10 underline", fg = "blue")')
        #     exec(f'def on_leave{i}(self, e):   link_label_{i} . config(font = "Verdana 10", fg = "black")')


        for i in range(len(links_)):
            links_lbl[i] = Label(c4, text = links_[i][0], background = "#F8F8F8", fg = "#30606e", font = ("Verdana 10"), cursor="hand2")
            links_lbl[i] . bind("<Button-1>", lambda e: self . callback(links_[i][1]))
            links_lbl[i] . bind("<Enter>", lambda e, i = i: links_lbl[i] . config(font = "Verdana 10 underline", fg = "blue"))
            links_lbl[i] . bind("<Leave>", lambda e, i = i: links_lbl[i] . config(font = "Verdana 10", fg = "black"))
            # exec(f'link_label_{i} . bind("<Enter>", lambda e: self . on_enter{i}(e))')
            # exec(f'link_label_{i} . bind("<Leave>", lambda e: self . on_leave{i}(e))')

            if i < 16:
                if i % 4 == 0:
                    y_pos += 50
                    links_lbl[i] . place(x = 50, y = y_pos)
                elif i % 4 == 1:
                    links_lbl[i] . place(x = 300, y = y_pos)
                elif i % 4 == 2:
                    links_lbl[i] . place(x = 680, y = y_pos)
                elif i % 4 == 3:
                    links_lbl[i] . place(x = 950, y = y_pos)
                    
        

        def more_lnks():
            
            def less_links():
                for i in range(16, len(links_)):
                    links_lbl[i] . place_forget()

                les_lnks . place_forget()
                mor_lnks . place(x = 500, y = 250)
                c4 . configure(height = 300)

            global y_chng
            y_chng = 0
            for i in range(16, len(links_)):
                if i % 4 == 0:
                    y_chng += 50
                    links_lbl[i] . place(x = 50, y = y_pos + y_chng)
                elif i % 4 == 1:
                    links_lbl[i] . place(x = 300, y = y_pos + y_chng)
                elif i % 4 == 2:
                    links_lbl[i] . place(x = 680, y = y_pos + y_chng)
                elif i % 4 == 3:
                    links_lbl[i] . place(x = 950, y = y_pos + y_chng)
            
            c4 . configure(height = y_pos + y_chng + 100)
            mor_lnks . place_forget()
            les_lnks = Button(c4, image = self . m_lk, command = less_links, borderwidth = 0)
            les_lnks . place(x = 500, y = y_pos + y_chng + 50)
            y_chng = 0
            

        mor_lnks = Button(c4, image = self . m_lk, command = more_lnks, borderwidth = 0)
        mor_lnks . place(x = 500, y = 250)

    # Treeviews on the Proflle Page
    def tree_creator(self, cols, tree_name, list, w):
        
        for i in cols:
            tree_name.column(i, anchor=CENTER, width = w)
            tree_name.heading(i, text=cols[i])        


        r = 0

        if list == []:
            list = [["-"] * len(cols)]
            list . append(["-"] * len(cols))
            for tran in list:
                trans = []
                for elem in tran:
                    trans . append(elem)
                if r % 2 == 0:
                    tree_name.insert('', 0, text = trans, values = trans, tags = ('oddrow',))
                else:
                    tree_name.insert('', 0, text = trans, values = trans, tags = ('evenrow',))
                r += 1
        else:
            for tran in list:
                trans = []
                for elem in tran:
                    trans . append(elem)
                if r % 2 == 0:
                    tree_name.insert('', 0, text = trans, values = trans, tags = ('oddrow',))
                else:
                    tree_name.insert('', 0, text = trans, values = trans, tags = ('evenrow',))
                r += 1
        
        tree_name.tag_configure('evenrow', background = 'white')
        tree_name.tag_configure('oddrow', background = 'lightblue')

    def banners_section(self):
        pass

    # Support Functions

    # images in the GUI Interface
    def images_decode(self):
        self . fscreen = Image.open("X:/ishaan/SBI OOPS/img/fscreen.png") . resize((25, 25), Image.ANTIALIAS)
        self . sbi_logo = Image.open("X:/ishaan/SBI OOPS/img/sbi_logo.png") . resize((280, 180), Image.ANTIALIAS)
        self . pers_bnk = Image.open("X:/ishaan/SBI OOPS/img/pers_bankng.JPG") . resize((270, 88), Image.ANTIALIAS)
        self . corp_bnk = Image.open("X:/ishaan/SBI OOPS/img/corp_bankng.JPG") . resize((388, 103), Image.ANTIALIAS)
        self . lgn = Image.open("X:/ishaan/SBI OOPS/img/login.JPG") . resize((138, 38), Image.ANTIALIAS)
        self . rgstr = Image.open("X:/ishaan/SBI OOPS/img/register.JPG") . resize((163, 51), Image.ANTIALIAS)
        self . c_care = Image.open("X:/ishaan/SBI OOPS/img/cust_care.JPG") . resize((165, 55), Image.ANTIALIAS)
        self . hlp = Image.open("X:/ishaan/SBI OOPS/img/help.JPG") . resize((133, 53), Image.ANTIALIAS)
        self . m_lk = Image.open("X:/ishaan/SBI OOPS/img/more_links.JPG") . resize((168, 42), Image.ANTIALIAS)
        self . bck = Image.open("X:/ishaan/SBI OOPS/img/back.png") . resize((60, 40), Image.ANTIALIAS)
        self . capcha1 = Image.open("X:/ishaan/SBI OOPS/img/captcha/1.jpg") . resize((150, 53), Image.ANTIALIAS)
        self . capcha2 = Image.open("X:/ishaan/SBI OOPS/img/captcha/2.jpg") . resize((150, 53), Image.ANTIALIAS)
        self . capcha3 = Image.open("X:/ishaan/SBI OOPS/img/captcha/3.jpg") . resize((150, 53), Image.ANTIALIAS)
        self . rld = Image.open("X:/ishaan/SBI OOPS/img/reload.jpg") . resize((20, 20), Image.ANTIALIAS)
        self . lgn_wlc = Image.open("X:/ishaan/SBI OOPS/img/welc.jpg") . resize((1400, 40), Image.ANTIALIAS)
        self . rnd_pic1 = Image.open("X:/ishaan/SBI OOPS/img/banner11.jpg") . resize((700, 380), Image.ANTIALIAS)
        self . rnd_pic2 = Image.open("X:/ishaan/SBI OOPS/img/prec.jpg") . resize((1400, 200), Image.ANTIALIAS)
        self . rnd_pic3 = Image.open("X:/ishaan/SBI OOPS/img/inst_login.jpg") . resize((700, 50), Image.ANTIALIAS)
        self . prof_bg = Image.open("X:/ishaan/SBI OOPS/img/prof_bg.jpg") . resize((1600, 900), Image.ANTIALIAS)
        self . pmts = Image.open("X:/ishaan/SBI OOPS/img/pay1.png") . resize((296, 191), Image.ANTIALIAS)
        self . dpst = Image.open("X:/ishaan/SBI OOPS/img/deposit1.png") . resize((296, 191), Image.ANTIALIAS)
        self . lns = Image.open("X:/ishaan/SBI OOPS/img/loans1.png") . resize((296, 191), Image.ANTIALIAS)
        self . bnnr1 = Image.open("X:/ishaan/SBI OOPS/banners/banner1.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr2 = Image.open("X:/ishaan/SBI OOPS/banners/banner2.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr3 = Image.open("X:/ishaan/SBI OOPS/banners/banner3.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr4 = Image.open("X:/ishaan/SBI OOPS/banners/banner4.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr5 = Image.open("X:/ishaan/SBI OOPS/banners/banner5.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr6 = Image.open("X:/ishaan/SBI OOPS/banners/banner6.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr7 = Image.open("X:/ishaan/SBI OOPS/banners/banner7.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr8 = Image.open("X:/ishaan/SBI OOPS/banners/banner8.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr9 = Image.open("X:/ishaan/SBI OOPS/banners/banner9.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr10 = Image.open("X:/ishaan/SBI OOPS/banners/banner10.jpg") . resize((1200, 300), Image.ANTIALIAS)
        self . bnnr11 = Image.open("X:/ishaan/SBI OOPS/banners/banner11.jpg") . resize((1200, 300), Image.ANTIALIAS)

        self . fscreen = ImageTk.PhotoImage(self . fscreen)
        self . sbi_logo = ImageTk.PhotoImage(self . sbi_logo)
        self . pers_bnk = ImageTk.PhotoImage(self . pers_bnk)
        self . corp_bnk = ImageTk.PhotoImage(self . corp_bnk)
        self . lgn = ImageTk.PhotoImage(self . lgn)
        self . rgstr = ImageTk.PhotoImage(self . rgstr)
        self . c_care = ImageTk.PhotoImage(self . c_care)
        self . hlp = ImageTk.PhotoImage(self . hlp)
        self . m_lk = ImageTk.PhotoImage(self . m_lk)
        self . bck = ImageTk.PhotoImage(self . bck)
        self . capcha1 = ImageTk.PhotoImage(self . capcha1)
        self . capcha2 = ImageTk.PhotoImage(self . capcha2)
        self . capcha3 = ImageTk.PhotoImage(self . capcha3)
        self . rld = ImageTk . PhotoImage(self . rld)
        self . lgn_wlc = ImageTk . PhotoImage(self . lgn_wlc)
        self . rnd_pic1 = ImageTk . PhotoImage(self . rnd_pic1)
        self . rnd_pic2 = ImageTk . PhotoImage(self . rnd_pic2)
        self . rnd_pic3 = ImageTk . PhotoImage(self . rnd_pic3)
        self . prof_bg = ImageTk . PhotoImage(self . prof_bg)
        self . pmts = ImageTk . PhotoImage(self . pmts)
        self . dpst = ImageTk . PhotoImage(self . dpst)
        self . lns = ImageTk . PhotoImage(self . lns)
        self . bnnr1 = ImageTk . PhotoImage(self . bnnr1)
        self . bnnr2 = ImageTk . PhotoImage(self . bnnr2)
        self . bnnr3 = ImageTk . PhotoImage(self . bnnr3)
        self . bnnr4 = ImageTk . PhotoImage(self . bnnr4)
        self . bnnr5 = ImageTk . PhotoImage(self . bnnr5)
        self . bnnr6 = ImageTk . PhotoImage(self . bnnr6)
        self . bnnr7 = ImageTk . PhotoImage(self . bnnr7)
        self . bnnr8 = ImageTk . PhotoImage(self . bnnr8)
        self . bnnr9 = ImageTk . PhotoImage(self . bnnr9)
        self . bnnr10 = ImageTk . PhotoImage(self . bnnr10)
        self . bnnr11 = ImageTk . PhotoImage(self . bnnr11)

        photo_dict['fscreen'] = self . fscreen

    # Toggling between full screen
    def tggl_fscreen(self, wind):
        if wind . attributes('-fullscreen') == False:
            wind . attributes('-fullscreen', True)
        else:
            wind . attributes('-fullscreen', False)
            wind . state("zoomed")

    # Open Web Links
    def callback(self, url):
        webview . create_window("Link Opened", url)
        webview . start()

    # Bind mousewheel scrolling
    def _on_mousewheel(self, event,c):
        c . yview_scroll(int(-1*(event.delta/120)), "units")

    # Moving text on the landing page
    def shift(self):
        self . x1,self .y1,self .x2,self .y2 = self .c_text.bbox("marquee")
        if(self .x2<0 or self .y1<0): #reset the coordinates
            self .x1 = self .c_text.winfo_width()
            self .y1 = self .c_text.winfo_height()//2
            self .c_text.coords("marquee",self .x1,self .y1)
        else:
            self .c_text.move("marquee", -2, 0)
        self .c_text.after(1000//self . fps,self . shift)




