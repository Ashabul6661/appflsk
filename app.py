from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            likes = int(request.form["likes"])
            comments = int(request.form["comments"])
            followers = int(request.form["followers"])

            # Hitung engagement rate
            if followers > 0:
                result = round(((likes + comments) / followers) * 100, 1)
        except:
            result = "Error"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

