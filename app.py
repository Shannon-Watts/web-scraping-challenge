from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Connection 
conn = "mongodb://27017"
client = pymongo.MongoClient(conn)

db = client.mars
collection = db.mars



# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    mars_data = db.mars.find_one()
    return render_template("index.html", mars=mars_data)


# scrape route
@app.route("/scrape")
def scrape():    
    data = scrape_mars.scrape_all()
    col.insert(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)