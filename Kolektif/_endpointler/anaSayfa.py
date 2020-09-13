from Kolektif import app
from flask import render_template
import json

from _edevat import logVer

istekler = json.load(open("Kolektif/istekler.json", "r+", encoding='utf8'))

@app.route('/')
def anaSayfa():
 #   for i in istekler.keys():
 #       print(i)

    logVer()
    return render_template(
        'anaSayfa.html',
        veriler = istekler,
        baslik = "Python / Flask ile yazılmış REST API"
    )
