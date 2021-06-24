
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask
app = Flask(__name__)

# Use Flask_pymongo to set mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app" 
mongo = PyMongo(app)

# Create Flask Home Route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Create Flask Scraping Route
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_info()
    mars.update({}, mars_data, upsert= True)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()
