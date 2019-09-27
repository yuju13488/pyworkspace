import m6_function.mymath as math #前導字元，套件package.模組module as alias
print(math.mypow(2,3)) #仍需前導字元.函式

from m6_function.mymath import myabs as abs #僅載入mymath模組中的myabs函式
print(abs(-5)) #不需前導字元

from m6_function.mymath import * #載入mymath模組中的所有函式
print(mysum(-5,5)) #不需前導字元