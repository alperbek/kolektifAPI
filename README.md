# kolektifAPI
Flask Tabanlı Scraper GET API | \w @keyiflerolsun

#

> [/udemyGorsel?kategori=python](https://kolektifapi.herokuapp.com/udemyGorsel?kategori=python)

> [/udemy?kategori=linux](https://kolektifapi.herokuapp.com/udemy?kategori=linux)

> [/udemy/bash](https://kolektifapi.herokuapp.com/udemy/bash)

#

> [/havaGorsel?sehir=canakkale](https://kolektifapi.herokuapp.com/havaGorsel?sehir=canakkale)

> [/hava?sehir=Beylikdüzü](https://kolektifapi.herokuapp.com/hava?sehir=Beylikdüzü)

> [/hava/pursaklar](https://kolektifapi.herokuapp.com/hava/pursaklar)

#

> [/eczaneGorsel?il=canakkale&ilce=merkez](https://kolektifapi.herokuapp.com/eczaneGorsel?il=canakkale&ilce=merkez)

> [/eczane?il=hatay&ilce=samandag](https://kolektifapi.herokuapp.com/eczane?il=hatay&ilce=samandag)

> [/eczane/mardin/nusaybin](https://kolektifapi.herokuapp.com/eczane/mardin/nusaybin)

#

> [/depremGorsel](https://kolektifapi.herokuapp.com/depremGorsel)

> [/deprem](https://kolektifapi.herokuapp.com/deprem)

#

> [/akaryakitGorsel](https://kolektifapi.herokuapp.com/akaryakitGorsel)

> [/akaryakit](https://kolektifapi.herokuapp.com/akaryakit)

#

> [/haberGorsel](https://kolektifapi.herokuapp.com/haberGorsel)

> [/haber](https://kolektifapi.herokuapp.com/haber)

#

> [/bimGorsel](https://kolektifapi.herokuapp.com/bimGorsel)

> [/bim](https://kolektifapi.herokuapp.com/bim)

#

## Proje Gelişimi

### v0.2
- *Spatula*(_Scrape_) dosyaları oluşturulup, `Flask` tek dosya olarak oluşturuldu.
- `gunicorn` ile *Heroku* _Deploy_ edildi.

### v0.7
- Kod okunurluğunu arttırmak ve projenin geliştirilebilmesi için `Flask` ın el verdiği dosya/dizin sistemi oluşturuldu.
- `jinja2` iyileştirmeleri yapıldı ve dosya/dizin sistemi oluşturuldu.
- `gunicorn` ile *Heroku* _Deploy_ edildi.

### v0.9
- `flask_sitemap` kütüphanesi kullanılarak otomatik bir sitemap oluşturuldu.
- `jsonify` ile dönen sayfalara _favicon_ eklendi.
- _gunicorn_'un `app.config` konfigürasyonlarını yoksayması sorunları yüzünden `waitress` _serve_ kullanıldı.

### v1
- `rich` kütüphanesiyle Konsol Log sistemi eklenmiştir..
