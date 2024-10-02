from pymongo import MongoClient
import config


db_name = config.HPP_DATABASE
myclient = MongoClient(config.MONGODB_URL)
db = myclient[db_name]
collection_user = db['customer_details']
collection_prediction = db['loan_prediction']


def register_account(customer_data):
    customer_data_dict = {}
    customer_data_dict['name'] = customer_data['name']
    customer_data_dict['password'] = customer_data['password']
    customer_data_dict['mailid'] = customer_data['mailid']
    customer_data_dict['phone'] = customer_data['phone']
    customer_data_dict['ACC_No'] = customer_data['ACC_No']
    customer_data_dict['DOB'] = customer_data['DOB']

    collection_user.insert_one(customer_data)
    return 'success'

def customer_login(login_details):
    customer_data_dict ={}

    customer_data_dict['ACC_no'] = login_details['ACC_No']
    customer_data_dict['mailid'] = login_details['mailid']
    customer_data_dict['passward'] = login_details['passward']

    response = collection_user.find_one(customer_data_dict)
    if not response:
        return "Invalid Account Details"
    return "Login Succesfully"

def save_prediction_details(self,loan_amnt,term,rate,emp_lnt,home_os,annual_inc,purpose,addrs,DTI,delinq_2yrs,revol_util,total_acc,longest_lenths,verif_status):
    bad_loan_prediction_details = {'loan_amnt':loan_amnt,'term':term,'rate':rate,'emp_lnt':emp_lnt,'home_os':home_os,'annual_inc':annual_inc,'purpose':purpose,'addrs':addrs,'DTI':DTI,'delinq_2yrs':delinq_2yrs,'revol_util':revol_util,'total_acc':total_acc,'longest_lenths':longest_lenths,'verif_status':verif_status}


    collection_prediction.insert_one(bad_loan_prediction_details)

    return "Saved Successfully Account Details"


    