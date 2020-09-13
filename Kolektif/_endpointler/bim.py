from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif._endpointler._hata import besYuz
from Kolektif.Spatula.bimAktuel import basliklar, aktuelBim

from _edevat import logVer

kaynak = 'bim.com.tr'

@app.route('/bimGorsel')
def bimGorsel():
    try:
        aktuelBim()
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return render_template(
        'veriSayfasi.html',
        veriler     = aktuelBim()['urunler'],
        anahtarlar  = basliklar,
        baslik      = f"Bim Aktüel Verileri\n({aktuelBim()['tarih']})"
    )

@app.route('/bim')
def bimJsonArgs():
    try:
        aktuelBim()
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = aktuelBim())