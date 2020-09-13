from Kolektif import app
from flask import render_template, jsonify
from Kolektif._endpointler._hata import besYuz
from Kolektif.Spatula.akaryakit import akaryakitFiyat, anahtarlar

from _edevat import logVer

@app.route('/akaryakitGorsel')
def akaryakitGorsel():
    logVer()
    return render_template(
        'veriSayfasi.html',
        veriler     = akaryakitFiyat(),
        anahtarlar  = anahtarlar(),
        baslik      = "Güncel Akaryakıt Verileri"
    )

@app.route('/akaryakit')
def akaryakit():
    try:
        akaryakitFiyat()
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return jsonify(akaryakitFiyat())