# SEOScraper

Uno semplice scraper per finalità SEO
Attualmente sono presenti due spider: `url` per fare il crawling di tutte le pagine di un sito e `pdf` per raccogliere tutti i link a pdf presenti.

## Prerequisiti

Su MacOSX Python è già presente quindi è necessario installare il package manager `pip` (se non lo avete già):

```
curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
```

Per installare il framework Scrapy, su MacOSX basta semplicemente eseguire il comando:

```
sudo pip install Scrapy
```

Ed è fatto.

## Configurazione

Le impostazioni principali si trovano in nel file `settings.py`. Alcuni parametri da prendere in considerazione:

`USER_AGENT` : è una stringa con cui il bot si presenta al webserver. E' buona norma mettere il nome dello spider con relativo URL, a volte a fini diagnostici e di analisi, può essere utile mettere un user-agent comune (che ho lasciato commentato).

`CONCURRENT_REQUESTS` : sono il numero di richieste contemporanee effettuate. Il default è 16, può tornare utile inserire un valore più basso per evitare che il crawling risulti troppo "aggressivo"

`DOWNLOAD_DELAY` : la distanza di tempo tra una richiesta e l'altra

`DEPTH_LIMIT` : il livello di profondità massima di crawling

Poi basta inserire in `spiders/url.py` o `spiders/pdf.py` il dominio e le URL a partire dalle quali faremo iniziare le nostre operazioni di crawling:

Esempio:

`allowed_domains = ["example.com"]`
```
start_urls = (
    'http://www.example.com/index.aspx',
    'http://www.example.com/en/index.php'
)
```

## Utilizzo

Per lanciare lo spider e salvere i risultati come un CSV è sufficiente spostarsi nella directory principale del progetto e dare:

### URL Spider
```
 scrapy crawl url -o urls.csv -t csv
```
Qualora volessimo l'output in formato JSON:
```
 scrapy crawl url -o urls.json -t json
```
O in XML:
```
scrapy crawl url -o urls.xml -t xml

```
### PDF Spider
```
 scrapy crawl pdf -o urls.csv -t csv
```
Per quanto riguarda i formati, vale lo stesso discorso dell'URL spider .

## TODO
* Aggiungere le funzionalità di Screaming Frog (http://www.screamingfrog.co.uk/seo-spider/)
