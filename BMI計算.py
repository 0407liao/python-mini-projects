身高=float(input("請輸入您的身高(M)"))
體重=int(input("請輸入您的體重(Kg)"))
BMI = 體重/(身高*身高)
print('您的BMI大約為',float(BMI))

if BMI<18.5 :print("體重過輕")
elif 18.5<=BMI<24:print("體重健康")
else :print("體重過重")
input("按Enter鍵結束")