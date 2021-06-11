from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)  
app.secret_key = 'khjgasDFYUHJKFAESDFYUHJKLAWEFYHJKUGyuhjklasd12'


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    session["strawberry"] = request.form["strawberry"]
    session["rasberry"] = request.form["rasberry"]
    session["apple"] = request.form["apple"]
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["student_id"] = request.form["student_id"]
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    