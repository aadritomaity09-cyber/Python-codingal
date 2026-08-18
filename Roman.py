class roman:
    def romannum(self):
        integer=(1000,900,500,400,100,90,50,40,10,9,5,4,1)
        m=("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")
        g=int(input("Enter the number that you want converted "))
        o=0
        while g:
            i=g//integer[o]
            g%=integer[o]
            while i:
                print(m[o], end="")
                i-=1
            o+=1
ob=roman()
ob.romannum()