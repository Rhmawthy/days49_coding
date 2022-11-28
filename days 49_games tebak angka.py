#program tebak- tebakan angka
import random
angka_acak = random.randint (1,100)
print("masukkan angka <=100")

batas=4
for percobaan in range(batas):
	angka=int(input("masukkan angka :"))
	
	if angka ==angka_acak:
		print("tebakan anda benar")
		break
	else:
	        print	("ulangi lagi")
	