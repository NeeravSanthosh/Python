class Japan():
    def capital(self):
        print("Tokyo is the capital of Japan")
    def language(self):
        print("Japanese is the primary language of Japan")
    def type(self):
        print("Japan is a highly developed counttry")

        
class Egypt():
    def capital(self):
        print("Cairo is the capital of Egypt")
    def language(self):
        print("Arabic is the primary language of Egypt")
    def type(self):
        print("Egypt is a unitary semi-presidential republic")
obj1 = Japan()
obj2 = Egypt()
for country in (obj1,obj2):
    country.capital()
    country.language()
    country.type()