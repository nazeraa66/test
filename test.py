from flask import Flask

app = Flask(__name__)

@app.route("/")
def biodata():
    nama = "Ribhina Oktimanta"
    umur = 17
    alamat = "Kud Lingkungan Sidodadi"
    email = "rbhnaoktmnta25@gmail.com"
    telp = "081298554372"
    pendidikan = "SMA Swasta Airlangga"
    hobi = "Healing & Memasak"

    return f"""
    <html>
    <head>
        <title>Biodata</title>
    </head>
    <body>
        <h1>Biodata Diri</h1>
        <p>Nama : {nama}</p>
        <p>Umur : {umur}</p>
        <p>Alamat : {alamat}</p>
        <p>Email : {email}</p>
        <p>Telp : {telp}</p>
        <p>Pendidikan : {pendidikan}</p>
        <p>Hobi : {hobi}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
