import joblib
import json
import numpy as np






def get_column_name():
        global __column_list
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Name_of_column.json","r") as f:
                __column_list = json.load(f)["columns_name"]
        return __column_list

def load_saved_artifacts():
        print("Loading saved dara....start")
        


        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of addr_state.json", "r") as f:
                __addrs_state = json.load(f)['addr_state']
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of home_ownership.json", "r") as Q:
                __home_ownership = json.load(Q)['home_ownership']
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of purpose.json", "r") as W:
                __purpose_1 = json.load(W)['purpose']
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of term.json", "r") as R:
                __term_1 = json.load(R)['term']
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of verification_status.json", "r") as Z:
                __verification_status = json.load(Z)['verification_status']
        file_path = 'D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/dt_loan_project.pkl'
        __model = joblib.load(open(file_path,'rb'))
                
                
def get_loan_pred(loan_amnt,term,rate,emp_lnt,home_os,annual_inc,purpose,addrs,DTI,delinq_2yrs,revol_util,total_acc,longest_lenths,verif_status):
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of addr_state.json", "r") as f:
                __addrs_state = json.load(f)['addr_state']
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of home_ownership.json", "r") as Q:
                __home_ownership = json.load(Q)['home_ownership']
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of purpose.json", "r") as W:
                __purpose_1 = json.load(W)['purpose']
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of term.json", "r") as R:
                __term_1 = json.load(R)['term']
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Label_list of verification_status.json", "r") as Z:
                __verification_status = json.load(Z)['verification_status']
        file_path = 'D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/dt_loan_project.pkl'
        __model = joblib.load(open(file_path,'rb'))
        with open("D:/Python/Class Practice/Machine learning/Loan_prediction/artifacts/Name_of_column.json","r") as f:
                __column_list = json.load(f)["columns_name"]

                                
                
        a = np.zeros(len(__column_list))
        a[0] = int(loan_amnt)
        a[1] = __term_1.index(term)
        a[2] = float(rate)
        a[3] = float(emp_lnt)
        a[4] = __home_ownership.index(home_os)
        a[5] = float(annual_inc)
        a[6] = __purpose_1.index(purpose)
        a[7] = __addrs_state.index(addrs)
        a[8] = float(DTI)
        a[9] = float(delinq_2yrs)
        a[10]= float(revol_util)
        a[11]= float(total_acc)
        a[12]= float(longest_lenths)
        a[13]= __verification_status.index(verif_status)

        return round(__model.predict([a])[0],2) 

if __name__ == "__main__":
    print(get_loan_pred(5000,'36 months',10.65,10.0,'RENT',24000.0,'credit_card','AZ',27.65,0.0,83.7,9.0,26.0,'verified'))
#     print("The Predicted price is :",price)