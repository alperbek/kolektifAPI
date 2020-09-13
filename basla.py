# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from kekikTaban._renkler import *
from kekikTaban._evrensel import *
from kekikTaban._degiskenler import *

from _edevat import *

#-----------------------------------#
print(f"{yesil}{logo}")             # yeşil renk koduyla logomuzu yazdırdık
print(ust_bilgi)                    # Üst Bilgimizi yazdırdık
#-----------------------------------#

from Kolektif import app
import os

port = int(os.environ.get("PORT", 5000))
host = "0.0.0.0"

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_AS_ASCII'] = False
    app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
    #app.run(debug = True, host = '0.0.0.0', port = port)
    
    onemli(f'\n\tKolektifAPI {host}:{port}\' başlatılmıştır...\n')
    
    from waitress import serve
    serve(app, host = host, port = port)