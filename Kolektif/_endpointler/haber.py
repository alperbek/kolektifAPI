from Kolektif import app
from flask import render_template, jsonify
from Kolektif._endpointler._hata import besYuz
from Kolektif.Spatula.haberler import haberVerisi

from _edevat import logVer

@app.route('/haberGorsel')
def haberGorsel():
    logVer()
    return render_template(
        'haberSayfasi.html',
        veriler = haberVerisi,
        anahtarlar = ['Haber'],
        baslik = "Son Dakika Verileri"
    )

@app.route('/haber')
def haberJson():
    try:
        logVer()
        return jsonify(haberVerisi)
    except:
        logVer()
        return besYuz('hata')