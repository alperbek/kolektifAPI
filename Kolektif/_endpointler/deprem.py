from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif._endpointler._hata import besYuz
from Kolektif.Spatula.depremVeri import anahtarlar, jsonVeri

from _edevat import logVer

kaynak = 'afet.gen.tr'

@app.route('/depremGorsel')
def depremGorsel():
    try:
        jsonVeri
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return render_template(
        'veriSayfasi.html',
        veriler = jsonVeri,
        anahtarlar = anahtarlar,
        baslik = "Son Depremler Verisi"
    )

@app.route('/deprem')
def depremJsonArgs():
    try:
        jsonVeri
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = jsonVeri)