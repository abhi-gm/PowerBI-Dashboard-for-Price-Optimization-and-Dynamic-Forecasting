from flask import Flask, render_template, redirect, request,Response
import pandas as pd 
import boto3
import numpy as np
app = Flask(__name__)


@app.route("/")
def florish():
   return render_template("index.html")


@app.route("/florish",methods=['POST'])
def flo():
   return render_template("index.html")


@app.route("/power",methods=['POST'])
def power():
   return render_template("main.html")

@app.route("/jupyter",methods=['POST'])
def jupyter():
   return render_template("jupyter.html")




@app.route('/', methods=("POST", "GET"))
def html_table():
    return render_template('meantable.html',  tables=[meandf.to_html(classes='data')], titles=meandf.columns.values)



@app.route("/hello")
def hello():
   return "Testing Conection Working !!"


@app.route("/cs")
def start():
    return render_template("index.html")

@app.route("/cs",methods=['POST'])
def marks():
    
    if request.method == 'POST': 
        try :
            cusNo = int(request.form["cus"])
            d= X.loc[cusNo]
            df = pd.DataFrame(data=d)
            df = df.T
            seg = rfmmodel.predict(df)[0]
        except Exception as e:
	        return render_template("error.html")

    return render_template("index.html",seg_ment = seg)
        

rfmmodel = joblib.load("rfmModel.pkl")
npd = joblib.load("NextPurchase.pkl")
meandf=joblib.load('meanagg')

#Bucket S3
bucket_name= "customermsinfo"




#s3 client to return s3 session 
def s3_client():
    session = boto3.Session()
    s3 = session.client('s3')
    return s3

#s3 resource session to check if file is there for download  
def s3_resources():
    session = boto3.Session()
    s3 = session.resource('s3')
    return s3

X=joblib.load('X')




@app.route('/gold', methods=["POST"])
def gold():
    my_bucket = s3_resources().Bucket(bucket_name)
    key = 'RFM/gold.csv'
    file_obj = my_bucket.Object(key).get()
    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )

@app.route('/silver', methods=["POST"])
def silver():
    my_bucket = s3_resources().Bucket(bucket_name)
    key = 'RFM/silver.csv'
    file_obj = my_bucket.Object(key).get()
    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )
    
@app.route('/bronze', methods=["POST"])
def bronze():
    my_bucket = s3_resources().Bucket(bucket_name)
    key = 'RFM/bronze.csv'
    file_obj = my_bucket.Object(key).get()
    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )


if __name__ == '__main__':
    app.run(debug= True)
 