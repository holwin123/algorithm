print("20234019 박찬건")
import urllib.request
page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
text = page.read().decode("utf8")
where = text.find(">$")
start_of_price = where + 2
end_of_price = start_of_price + 4
price = text[start_of_price:end_of_price]
print(price)
#컴퓨터공학과 20234019 박찬건