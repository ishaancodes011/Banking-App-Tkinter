import mysql.connector

class DataClass:

    def __init__(self):
        self . conn = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='sbi_database')
        # Login Credentials - u_name, password, sec q&a -3 -> 1. get credentials
        # Profile Details -> 1. get profile details
        # Balance - transactions, deposits and loans -> 1. transactions 2. loans 3. deposits
   
    # Profile Details
    def get_credentials(self):
        login_creds = []

        lgn_cur = self . conn . cursor()
        lgn_cur . execute("select  u_name, password from login_credentials;")
        login_creds = lgn_cur . fetchall()

        self . conn . commit()

        return login_creds

    def password_data(self):
        credentials = []

        crd_cur = self . conn . cursor()
        crd_cur . execute("select a.u_name, a.password, a.sec_ques1, a.sec_ans1, a.sec_ques2, a.sec_ans2, a.sec_ques3, a.sec_ans3, b.email_address, b.contact from login_credentials a inner join profile_details on login_credentials.u_name = profile_details.u_name;")
        credentials = crd_cur . fetchall()

        self . conn . commit()

        return credentials

    def password_update(self, new_pass, u_name):
        pdupdt_cur = self . conn . cursor()
        pdupdt_cur . execute("update login_credentials set password = {} where u_name = {};" . format(new_pass, u_name))

        self . conn . commit()

    def sec_ques_updat(self, q1, a1, q2, a2, q3, a3, u_name):
        updt_cur = self . conn . cursor()
        updt_cur . execute("update login_credentials set sec_ques1 = {}, sec_ans1 = {}, sec_ques2 = {}, sec_ans2 = {}, sec_ques3 = {}, sec_ans3 = {} where u_name = {};" . format(q1, a1, q2, a2, q3, a3, repr(u_name)))

        self . conn . commit()

    def get_profile(self, u_name):
        det = []

        prof_cur = self . conn . cursor()
        prof_cur . execute("select * from profile_details where u_name = {};" . format(repr(u_name)))
        det = prof_cur . fetchone()

        self . conn . commit()
        return det

    def get_balance(self, u_name):
        blc = []

        blc_cur =  self . conn . cursor()
        blc_cur . execute("select transaction_id, time_trans, deposit, withdraw, balance from account_balance where u_name = {}" . format(repr(u_name)))
        blc = blc_cur . fetchall()
        
        self . conn . commit()
       
        return blc

    def dep_balance(self, u_name, time, amnt, withdraw, blnc):

        deposit_cur = self . conn . cursor()
        deposit_cur . execute("insert into account_balance (u_name, time_trans, deposit, withdraw, balance) values ({}, {}, {}, {}, {})" . format(repr(u_name), repr(time), amnt, withdraw, blnc))

        self . conn . commit()

        updt_blnc_cur = self . conn . cursor()
        updt_blnc_cur . execute("update profile_details set balance = {} where u_name = {}" . format(blnc, repr(u_name)))

        self . conn . commit()
            
    def wth_balance(self, u_name, time, deposit, amnt, blnc):

        wth_cur = self . conn . cursor()
        wth_cur . execute("insert into account_balance (u_name, time_trans, deposit, withdraw, balance) values ({},{}, {}, {}, {})" . format(repr(u_name), repr(time), deposit, amnt, blnc))

        self . conn . commit()

        updt_blnc_cur = self . conn . cursor()
        updt_blnc_cur . execute("update profile_details set balance = {} where u_name = {}" . format(blnc, repr(u_name)))

        self . conn . commit()

    def deposits_get(self, u_name):
        dep_list = []
        
        dep_cur = self . conn . cursor()
        dep_cur . execute("select deposit_id, time_dep, deposit_type, deposit_amount, deposit_interest, deposit_duration, final_amount from account_deposits where u_name = {}" . format(repr(u_name)))
        dep_list = dep_cur . fetchall()

        self . conn . commit()

        return dep_list

    def new_dep(self, u_name, time, dep_typ, a, i,d,f):
        depo_cur = self . conn  . cursor()
        depo_cur . execute("insert into account_deposits (u_name, time_dep, deposit_type, deposit_amount, deposit_interest, deposit_duration, final_amount) values ({},{},{},{},{},{}, {})" . format(repr(u_name), repr(time), repr(dep_typ), float(a), repr(i), repr(d), repr(f)))

        self . conn . commit()

    def get_loans(self, u_name):
        loans_list = []
        
        loans_cur = self . conn . cursor()
        loans_cur . execute("select loan_number, time_loan, loan_type, loan_amount, loan_interest, loan_period, emi, final_amount from loans_hist where u_name = {}" . format(repr(u_name)))
        loans_list = loans_cur . fetchall()

        self . conn . commit()

        return loans_list


    def new_loan(self, u_name, time, loan_typ, amnt_depo, tim_per, in_rate, calc_emi, fin_amnt):
        loan_cur = self . conn . cursor()
        loan_cur . execute("insert into loans_hist (u_name, time_loan, loan_type, loan_amount, loan_period, loan_interest, emi, final_amount) values({}, {}, {}, {}, {}, {}, {}, {})" . format(repr(u_name), repr(time), repr(loan_typ), float(amnt_depo), float(tim_per), in_rate, calc_emi, fin_amnt))


    def register_new(self):
        pass

        # rgstr_cur = self . conn . cursor()
        # self . conn . execute("insert into login_credentials")
        

        # self . conn . commit()

    def close_conn(self):
        self . conn . close()