from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))

@app.route("/",methods=["GET","POST"])
def main():
  name=request.from.get("name")
  return(render_template("main.html",r=name))
  
  




if __name__ == "__main__":
  app.run()
