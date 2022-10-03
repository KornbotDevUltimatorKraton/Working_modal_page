from flask import Flask,render_template,redirect,url_for
app = Flask(__name__) 

@app.route("/")
def index():
  
     return render_template("typeable_modal_popup.html")
@app.route("/profile")
def profile():
       return render_template("profile_set.html")
@app.route("/document")
def document():
       return render_template("document_byid.html")
@app.route("/tab")
def tab_ex():
      return render_template("Tab_test.html")
if __name__ == "__main__":
       
       app.run(debug=True,host="0.0.0.0",port=3090)



