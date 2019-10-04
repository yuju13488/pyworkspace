# 6.選擇性敘述的練習-equation
# 一元二次方程式ax2+bx+c=0。輸入a, b, c三值，並計算方程式的根。
# b2-4ac > 0，有兩個不相等的實根。
# b2-4ac = 0，有兩個相等的實根。
# b2-4ac < 0，則印出”沒有實根”。
#=x=(-b+-(b**2-4*a*c)**0.5)/(2*a)

a,b,c=eval(input('a*x^2+b*x+c為一元二次方程式，請輸入a，b，c:'))
D=b*2-4*a*c
if D < 0:
    print('沒有實根')
elif D == 0:
    print('有兩個相等實根為',-b/(2*a))
elif D > 0:
    print('有兩個不相等實根，分別為',(-b+(b**2-4*a*c)**0.5)/(2*a),'和',(-b+(b**2+4*a*c)**0.5)/(2*a))