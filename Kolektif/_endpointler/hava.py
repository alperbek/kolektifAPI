from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif._endpointler._hata import besYuz
from Kolektif.Spatula.hava import anahtarlar, havaDurumu

from _edevat import logVer

kaynak = 'google.com.tr'

@app.route('/havaGorsel')
def havaGorsel():
    sehir = request.args.get('sehir')
    if not sehir:
        logVer()
        return besYuz('hata')

    try:
        havaDurumu(sehir)
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return render_template(
        'veriSayfasi.html',
        veriler = havaDurumu(sehir),
        anahtarlar = anahtarlar(sehir),
        baslik = "Hava Durumu Verisi"
    )

@app.route('/hava')
def havaJsonArgs():
    sehir = request.args.get('sehir')
    if not sehir:
        logVer()
        return besYuz('hata')

    try:
        havaDurumu(sehir)
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = havaDurumu(sehir))

@app.route('/hava/<sehir>')
def havaJsonDizin(sehir):
    if not sehir:
        logVer()
        return besYuz('hata')

    try:
        havaDurumu(sehir)
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = havaDurumu(sehir))