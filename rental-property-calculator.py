
class Roi():
    def __init__(self):
        self.value = []
        Roi.income(self)
    def income(self):
        ri = input("What is your expected monthly rental income? ($)")
        self.value.append(float(ri))
        la = input("What is your expected monthly laundry income? ($)")
        self.value.append(float(la))
        st = input("What is your expected monthly storage location revenue? ($)")
        self.value.append(float(st))
        ms = input("Please insert any other miscellanious monthly income: ($)")
        self.value.append(float(ms))
        Roi.expenses(self)
    def expenses(self):
        tx = input("What are your expected monthly property tax expenses? ($)")
        self.value.append(float(tx))
        ins = input("What are your expected monthly insurance expenses? ($)")
        self.value.append(float(ins))
        ut = input("What are you expected monthly utilities expenses? ($)")
        self.value.append(float(ut))
        hoa = input("What are your expected monthly HOA fees? ($)")
        self.value.append(float(hoa))
        vac = input("What are you expected monthly vacancy fees? ($)")
        self.value.append(float(vac))
        wea = input("What are your expected monthly fees reguarding snow removal and lawn care? ($)")
        self.value.append(float(wea))
        rep = input("What are your expected monthly repair fees? ($)")
        self.value.append(float(rep))
        pm = input("What are yur exected monthly property management expenses? ($) ")
        self.value.append(float(pm))
        cp = input("What are your expected monthly capital expenditures? ($)")
        self.value.append(float(cp))
        mg = input("What are your expected monthly mortgage payments? ($)")
        self.value.append(float(mg))
        Roi.cocroi(self)
    def cocroi(self):
        dp = input("How much will you pay for your down payment? ($)")
        self.value.append(float(dp))
        cc = input("What are your closing costs? ($)")
        self.value.append(float(cc))
        rb = input("What is your renovations budget? ($)")
        self.value.append(float(rb))
        misc = input("What are your other upfront investment expenses? ($)")
        self.value.append(float(misc))
        u = 0
        v= 0
        for x in range(len(self.value)):
            if x <= 3:
                u += self.value[x]
            elif x<=13:
                u -= self.value[x]
            elif x == 14:
                u = u*12
                v += self.value[x]
            else:
                v += self.value[x]
        print("Your return on investment is:", 100*(u/v), "%")
r = Roi()
r.__init__()






