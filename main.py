# import library speech recognition
import speech_recognition as sr 

# buat variabel bicara dan panggil fungsi Recognizer
bicara = sr.Recognizer()

# dan panggil juga fungsi Microphone untuk mengenali audio melalui Microphone
with sr.Microphone() as sumber:
	print("Bicara Apapun : ")
	audio = bicara.listen(sumber)
	try:
# buat variabel teks untuk menyimpan suara agar dikenal oleh google recognize
		teks = bicara.recognize_google(audio)
# print hasil audio menjadi teks
		print("Kamu Mengatakan : {}".format(teks))
	except:
		print("Maaf,yang Kamu Bicarakan Tidak dimengerti")
