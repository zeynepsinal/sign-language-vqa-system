# 🤟 İşaret Dili VQA Sistemi

Bu proje, TensorFlow, MobileNetV2 ve Streamlit kullanılarak geliştirilmiş derin öğrenme tabanlı bir işaret dili harf tanıma ve görsel soru cevaplama (Visual Question Answering - VQA) uygulamasıdır.

Sistem, kullanıcı tarafından yüklenen işaret dili görsellerini analiz ederek Amerikan İşaret Dili (ASL) alfabesindeki harfleri tahmin eder ve aşağıdaki gibi basit sorulara cevap verebilir:

- Bu görselde hangi harf var?
- Model ne kadar emin?
- Bu işaretin anlamı nedir?

> Model dosyası büyük boyutlu olduğu için GitHub deposuna eklenmemiştir. Eğitilen model Colab ortamında oluşturulmuştur: https://colab.research.google.com/drive/1Eu-0dkE8di209dtcrEutZaxe5Vm6o9A6?usp=sharing
---

## Proje Amacı

Bu projenin temel amacı, işitme engelli bireylerin iletişim süreçlerini desteklemek ve işaret dili bilmeyen bireylerle daha kolay iletişim kurmalarına katkı sağlamaktır.

Proje kapsamında geliştirilen sistem:

- El işareti görüntüsünü analiz eder,
- İlgili harfi tahmin eder,
- Tahminin güven skorunu hesaplar,
- Kullanıcının sınırlı sayıdaki sorusuna anlamlı cevaplar verir.

---

##  Kullanılan Model

Sınıflandırma modeli olarak ImageNet üzerinde önceden eğitilmiş **MobileNetV2** mimarisi kullanılmıştır.

Modelin son katmanları:

- Global Average Pooling
- Dropout (%30)
- Softmax aktivasyonlu Dense katmanı

Transfer learning yaklaşımı sayesinde model kısa sürede yüksek doğrulukla eğitilmiştir.

---

##  Kullanılan Veri Seti

### ASL Alphabet Dataset

- 29 sınıf
- A-Z harfleri
- `del`, `nothing`, `space`
- Yaklaşık 87.000 eğitim görüntüsü

Veri seti bağlantısı:

https://www.kaggle.com/datasets/grassknoted/asl-alphabet

---

## 🛠 Kullanılan Teknolojiler

- Python
- TensorFlow / Keras
- MobileNetV2
- Streamlit
- NumPy
- Pillow
- Google Colab

---

##  Proje Yapısı

```text
clean_sign/
├── app.py
├── asl_alphabet_model_fast.keras
├── README.md
└── venv
|__.gitignore

##Kurulum ve Çalıştırma

Aşağıdaki komutları sırasıyla çalıştırarak projeyi kurabilir ve uygulamayı başlatabilirsiniz.

```bash
git clone https://github.com/zeynepsinal/sign-language-vqa.git
cd sign-language-vqa

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

Uygulama çalıştırıldıktan sonra tarayıcıda otomatik olarak aşağıdaki adres açılacaktır:
http://localhost:8501
