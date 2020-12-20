<p>
<li> official style guide: python.org/dev/peps/pep-0008</li>
<li> using flake8</li>
<li> for url params, use _, not -</li>
<li> database engine: mysql</li>
<li> fixture actually not for dumpdata/loaddata</li>
<li> python manage.py collectstatic</li>
</p>
<p>
<li> installing mysql db: conda install -c bioconda mysqlclient</li>
<li> pip install pymysql</li>
</p>
<p>
<li> https://hsunnystory.tistory.com/76?category=794803</li>
<li> https://12teamtoday.tistory.com/53</li>
</p>
<p>
<li> GCP to use speech-to-text api</li>
<li> https://github.com/googleapis/python-speech/tree/master/samples/microphone </li>
<li> Tutorial: https://webnautes.tistory.com/1247</li>
<li> PyAudio: https://medium.com/@wagnernoise/installing-pyaudio-on-macos-9a5557176c4d</li>
<li>https://cloud.google.com/docs/authentication/getting-started</li>
</p>
<p>
NRCLex: https://github.com/metalcorebear/NRCLex
ref) https://pypi.org/project/NRCLex/
</p>
<li> about Postgres database: https://postgresapp.com/</li>
<li> ref: two-scoops-of-django</li>

<p>배포</p>
<li>https://nerogarret.tistory.com/47?category=800142</li>
<li>Install all the requirements in venv</li>
<li>DB: https://minwoo2815.tistory.com/64</li>
<li>
https://blog.boxcorea.com/wp/archives/2702
sudo apt-get install python3-dev
python3 import nltk 
nltk.download('stopwords')
nltk.download('wordnet')</li>
<li>
https://stackoverflow.com/questions/46619039/django-db-utils-operationalerror-1045-access-denied-for-user-rootlocalho/46619093
flush privileges;
</li>
<li>
	migrate
</li>
<li>python3 -m textblob.download_corpora</li>
<li>home/ubuntu/nltk-data
https://stackoverflow.com/questions/35861482/nltk-lookup-error</li>
mv nltk_data to django-nlp
