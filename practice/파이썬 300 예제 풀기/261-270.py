# 261-270
class Stock:
    def __init__(self, name, code, per, pbr, benefit):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.benefit = benefit

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, benefit):
        self.benefit = benefit

    def get_per(self):
        return self.per


samsung = Stock("samsung", "005930", 15.79, 1.33, 2.83)
hyundae = Stock("hyundae", "005380", 8.70, 0.35, 4.27)
LG = Stock("LG", "066570", 317.34, 0.69, 1.37)

list = [samsung, hyundae, LG]

for i in list:
    print(i.get_code(), i.get_per())
