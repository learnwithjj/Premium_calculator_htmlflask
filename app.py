
from flask import Flask, render_template, request
from pymongo import MongoClient
from mongopass import mongopass
import subprocess as sp

 
app=Flask(__name__)
client=MongoClient(mongopass)
db=client.test
collection=db.names_col

@app.route("/")
def my_home():
    date=sp.getoutput("date /t")
    return render_template("home.html",date=date)


@app.route("/count")
def insert_val():
    return render_template("count.html")

@app.route("/getac", methods=['GET','POST'])
def getac():
    global a
    a=int(request.form.get('a'))
    global c
    c=int(request.form.get('c'))
    x=[]
    x.append(a)
    x.append(c)
    return render_template("curd.html",result=x)


@app.route("/get", methods=['GET', 'POST'])
def get():
    
    x=[]
    if request.method=='POST':
        for i in range(a):
            
            aage=int(request.form.get(f"aage_{i}"))
            acity=int(request.form.get(f"acity_{i}"))
            atenure=int(request.form.get(f"atenure_{i}"))
            asumInsured=int(request.form.get(f"asuminsured_{i}"))
            cursor1=collection.find_one({"Age":aage,"TierID":acity,"Tenure":atenure,"SumInsured":asumInsured},{'Rate':1,'_id':0})
            x.append(cursor1['Rate'])

        for j in range(c):
            cage=int(request.form.get(f"cage_{j}"))
            ccity=int(request.form.get(f"ccity_{j}"))
            ctenure=int(request.form.get(f"ctenure_{j}"))
            csumInsured=int(request.form.get(f"csuminsured_{j}"))
            cursor2=collection.find_one({"Age":cage,"TierID":ccity,"Tenure":ctenure,"SumInsured":csumInsured},{'Rate':1,'_id':0})
            x.append(cursor2['Rate'])

        sum=0
        for k in x:
            sum+=k    

        
    return render_template("response.html",result=str(sum))



if __name__=="__main__":
    app.run()