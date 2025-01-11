from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Remove or comment out the following lines:
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001)

# Add this line at the end of the file
app = app
