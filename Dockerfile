
# kullanacağım image'ı tanımladım.
FROM python  
#hangi path'de çalışacağını belirttim
WORKDIR /python-notes
#gerekli olan python paketlerini kurulumu için requierments.txt'yi ekledim
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
#gerekli olan python paketlerini kurdum
RUN pip install -r requirements.txt
#bulunduğum
COPY app.py app.py

CMD [ "python3", "app.py"]
