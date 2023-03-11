from flask import Flask # flask kütüphanemizi projemize import ettik.

app = Flask(__name__) # flask nesnesini app'e atadım.
@app.route("/hakkımda") #endpoint oluşturdum
def talha1():  #fonksiyon oluşturdum
    return "merhaba ben talha devops konularına çalışıyorum." #hakkımda yazısı yazdım. 
@app.route("/") # anasayfa için endpoint oluşturdum
def talha(): # fonksiyon oluşturdum.
    return "Anasayfa" # anasayfa yazısı ekledi
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
