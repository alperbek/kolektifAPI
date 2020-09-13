from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif._endpointler._hata import besYuz
from Kolektif.Spatula.disc import udemySpatula

from _edevat import logVer

kaynak = 'discudemy.com'

@app.route('/udemyGorsel')
def udemyGorsel():
    kategori = request.args.get('kategori')
    if not kategori:
        logVer()
        return besYuz('hata')

    try:
        udemySpatula(kategori)
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return render_template(
        'veriSayfasi.html',
        veriler = udemySpatula(kategori),
        baslik = "udemy Verileri"
    )

@app.route('/udemy')
def udemyJsonArgs():
    kategori = request.args.get('kategori')
    if not kategori:
        logVer()
        return besYuz('hata')

    try:
        udemySpatula(kategori)
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = udemySpatula(kategori))

@app.route('/udemy/<kategori>')
def udemyJsonDizin(kategori):
    if not kategori:
        return besYuz('hata')

    try:
        udemySpatula(kategori)
    except:
        logVer()
        return besYuz('hata')

    logVer()
    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = udemySpatula(kategori))