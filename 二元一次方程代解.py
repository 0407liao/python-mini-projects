X=float(input("請輸入須帶入的X"))
Y=float(input("請輸入須帶入的Y"))
A=float(input("請輸入須帶入的X項係數"))
B=float(input("請輸入須帶入的Y項係數"))
C=float(input("請輸入化簡後等號右邊的數"))
運算=input("請輸入XY之間要使用的符號(+/-)")
if 運算=="+":左邊=X*A+Y*B
else :左邊=X*A-Y*B
print('左邊運算結果',左邊,'右邊數字',C)
if 左邊==C:
 print(f"您的X,{X},和您的Y,{Y},是對的")
else : print(f"您的X{X},和您的Y{Y}是錯的")
input("按Enter鍵結束")