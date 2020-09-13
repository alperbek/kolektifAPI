from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif._endpointler._hata import besYuz
from Kolektif.Spatula.hal import yerliMeyve_jsonVeri, yerliSebze_jsonVeri, ithal_jsonVeri, yerliMeyve_anahtarlar

from _edevat import logVer

kaynak = 'ibb.istanbul'

@app.route('/halGorsel')
def halGorsel():
    tur = request.args.get('tur')

    if tur == 'meyve':
        logVer()
        return render_template(
            'veriSayfasi.html',
            veriler = yerliMeyve_jsonVeri,
            anahtarlar = yerliMeyve_anahtarlar,
            baslik = "Güncel Yerli Meyve Verileri"
        )

    elif tur == 'sebze':
        logVer()
        return render_template(
            'veriSayfasi.html',
            veriler = yerliSebze_jsonVeri,
            anahtarlar = yerliMeyve_anahtarlar,
            baslik = "Güncel Yerli Sebze Verileri"
        )

    elif tur == 'ithal':
        logVer()
        return render_template(
            'veriSayfasi.html',
            veriler = ithal_jsonVeri,
            anahtarlar = yerliMeyve_anahtarlar,
            baslik = "Güncel İthal Ürün Verileri"
        )

    else:
        logVer()
        return besYuz('hata')

@app.route('/hal')
def halJson():
    tur = request.args.get('tur')
    if not tur: return besYuz('hata')

    if tur == 'meyve':
        logVer()
        return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = yerliMeyve_jsonVeri)
    
    elif tur == 'sebze':
        logVer()
        return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = yerliSebze_jsonVeri)
    
    elif tur == 'ithal':
        logVer()
        return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = ithal_jsonVeri)
    
    else:
        logVer()
        return besYuz('hata')


@app.route('/hal/<tur>')
def halJsonTur(tur):
    if not tur: return besYuz('hata')

    if tur == 'meyve':
        logVer()
        return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = yerliMeyve_jsonVeri)
    
    elif tur == 'sebze':
        logVer()
        return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = yerliSebze_jsonVeri)
    
    elif tur == 'ithal':
        logVer()
        return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = ithal_jsonVeri)
    
    else:
        logVer()
        return besYuz('hata')