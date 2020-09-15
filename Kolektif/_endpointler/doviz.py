from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif._endpointler._hata import besYuz
from Kolektif.Spatula.doviz import anahtarlar, jsonVeri

from _edevat import logVer

kaynak = 'altinkaynak.com'

@app.route('/dovizGorsel')
def dovizGorsel():
    try:
        jsonVeri
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return render_template(
        'veriSayfasi.html',
        veriler     = jsonVeri,
        anahtarlar  = anahtarlar,
        baslik      = f"Güncel Döviz Verileri"
    )

@app.route('/doviz')
def dovizJson():
    try:
        jsonVeri
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = jsonVeri)