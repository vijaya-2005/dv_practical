from flask import Flask ,render_template,request
app = Flask("__name__")
@app.route("/",methods=["post","get"])
def register():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("username")
        print(user)
    return render_template("register.html")
if __name__=="__main__":
    app.run(debug=True)