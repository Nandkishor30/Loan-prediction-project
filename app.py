from flask import Flask, request, jsonify,render_template
import test_model
import Loan_db
import joblib
import config
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('loan_prediction.html')

@app.route('/acc_register',methods=['POST'])
def acc_register():
   if request.method == 'POST':
      data = request.form 
      response = Loan_db.register_account(data)

   return jsonify({'msg': response})

@app.route('/login',methods=['POST'])
def login_acc():
   if request.method == 'POST':
      data = request.form
      response = Loan_db.customer_login(data)
   return jsonify({'msg':response})

@app.route('/get_cat_feature_names',methods=['GET'])
def get_list_names():
   res_adr = jsonify({'address':test_model.get_addr()})
   res_adr.headers.add('Access-control-Allow-Origin','*')
   res_purpose = jsonify({'purpose':test_model.get_purpose()})
   res_purpose.headers.add('Access-control-Allow-Origin','*')

   return res_purpose,res_adr

@app.route('/loan_prediction',methods = ['POST'])
def get_loan_pred():
   if request.method == 'POST':
      data = request.form 
      result = test_model.get_loan_pred(data)
      Loan_db.save_prediction_details(loan_amnt, term, rate, emp_lnt, home_os, annual_inc, purpose, addrs, DTI, delinq_2yrs, revol_util, total_acc, longest_lenths, verif_status,result)

      if float(result) == 0.0:
         prediction = "Good Loan"
      else:
         prediction = 'Bad Loan'
      return render_template("result.html", prediction = prediction)
   


if __name__ == "__main__":
    app.run()