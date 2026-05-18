from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPS Lokasi Pengguna</title>

    <style>
        body{
            font-family: Arial, sans-serif;
            background:#f4f4f4;
            padding:40px;
            text-align:center;
        }

        .card{
            background:white;
            max-width:600px;
            margin:auto;
            padding:30px;
            border-radius:12px;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);
        }

        button{
            background:#007bff;
            color:white;
            border:none;
            padding:12px 20px;
            border-radius:8px;
            cursor:pointer;
        }

        .result{
            margin-top:20px;
            text-align:left;
            background:#fafafa;
            padding:15px;
            border-radius:8px;
        }
    </style>
</head>
<body>

<div class="card">
    <h1>Lokasi GPS Pengguna</h1>

    <button onclick="getLocation()">
        Ambil Lokasi
    </button>

    <div class="result" id="result">
        Belum ada data lokasi
    </div>
</div>

<script>
function getLocation() {

    const result = document.getElementById("result");

    if (navigator.geolocation) {

        result.innerHTML = "Mengambil lokasi...";

        navigator.geolocation.getCurrentPosition(

            function(position) {

                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                const accuracy = position.coords.accuracy;

                result.innerHTML = `
                    <h3>Data Lokasi</h3>

                    <p><b>Latitude:</b> ${latitude}</p>

                    <p><b>Longitude:</b> ${longitude}</p>

                    <p><b>Akurasi:</b> ${accuracy} meter</p>

                    <a href="https://www.google.com/maps?q=${latitude},${longitude}" target="_blank">
                        Buka Google Maps
                    </a>
                `;
            },

            function(error) {

                result.innerHTML = "Gagal mengambil lokasi.";
            }
        );

    } else {

        result.innerHTML = "Browser tidak mendukung geolocation.";
    }
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

# Penting untuk Vercel
app = app
