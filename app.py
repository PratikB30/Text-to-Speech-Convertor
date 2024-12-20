import os
from pathlib import Path
# from gtts import gTTS
from werkzeug.utils import secure_filename
from flask import Flask, flash, redirect, render_template, request, send_file
# from website import create_app

#app = create_app()
app = Flask(__name__)

ALLOWED_EXTENSIONS = {
    ".txt",
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".png",
    ".doc",
    ".docx",
    ".odt",
}
UPLOAD_FOLDER = os.path.join("env/uploads/")
AUDIO_FOLDER = os.path.join("conversions/")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["AUDIO_FOLDER"] = AUDIO_FOLDER
app.config["SECRET_KEY"] = "NotASecret"

filename = ""

def download(filename):
    from convert import speak
    fname = f"{Path(filename).stem}.mp3"
    print(fname)
    speak(request.form["confirm"], fname, False)
    return send_file(
        os.path.join(app.config["AUDIO_FOLDER"], fname),
        as_attachment=True,
        download_name=fname,
        mimetype="audio/mp3",
    )

def allowed_file(filename):
    return "." in filename and Path(filename).suffix in ALLOWED_EXTENSIONS
    
@app.route("/home", methods=["GET", "POST"])
def home():
    from convert import ocr
    global filename
    if request.method == "POST":
        if request.files:
            file = request.files["file"]

            if file.filename == "":
                flash("No selected file")
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename or "")
                print(filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                print(filename)
                return confirm(ocr(file))

        if request.form["confirm"]:
            return download(filename)

    return render_template("index.html")

@app.route("/txtconvert", methods=["GET", "POST"])
def tconvert():
    from convert import ocr
    global filename
    if request.method == "POST":
        if request.files:
            file = request.files["file"]

            if file.filename == "":
                flash("No selected file")
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename or "")
                print(filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                print(filename)
                return confirm(ocr(file))

        if request.form["confirm"]:
            return download(filename)

    return render_template("txtconvert.html")

# @app.route("/home")
# def home():
#return render_template("index.html")

#@app.route("/confirm", methods=["GET", "POST"])
def confirm(output):
    return render_template("confirm.html",output=output)

def txtconvert(output):
    return render_template("txtconvert.html",output=output)

@app.route("/")
def redirc():
    return redirect("/home")

if __name__== '__main__':
    app.run(debug=True)