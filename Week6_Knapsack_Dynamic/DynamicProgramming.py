"""
Dynamic Programming: 
-->Recursive bir yapı olması gereklidir. 
-->Tekrar tekrar aynı işlemi yapmaktan kaçınarak bir çözüm üretmeye çalışıyor.
-->Böl ve işgal et, bölüyor ve recursive çağırım yapıyor. Recursive çağırdığında tekrarlı yaptığı işlemleri engelleyerek daha hızlı bir çözüm üretmeye çalışıyor.
Optimal Substructure:
    Bir global çözümün, subproblems kombinasyonundan oluşuyor ise buna diyoruz.
Örnek:
Örnek olarak MergeSort algoritmasını verirsek, parçalara bölüyor ve kıyaslayarak birleştiriyor.
-->Global optimal çözüm, local optimal çözümlerin bir kombin edilmesiyle ortaya çıkıyor diyebiliriz. Bunu gördüğümüz gibi bu problemi Dynamic yapıya uyarlayabiliriz.
Overlapping subproblems:
    Dynamic problemin en önemli kısmıdır. Dİyelimki bir problemi parçalayıp çözebiliyoruz, fakat parçalandığında aynı problem tekrar tekrar ortaya çıkıyorsa 
o zaman ben bu yapıyı dynamic yapıya aktarabiliyorum demektir.
Mesela fib örneğindeki gibi düşünürsek eğer aynı olan fib değerleri birden fazla kes kullanılmış olabiliyor. Bunu önlemek adına memoization yapmamız gereklidir.
Onu engelleme yoluda bir değişken tutmak ve elde ettiği değerleri oraya yazdırmak mantığı ile oluşturulmuş yapı.

-->Normmalde memorysiz yaparsak eğer fib karmaşıklığı "0((2^n+1)-1)"dir. Fakat bellek ile yapılırsa eğer karmaşıklığı 0(n)'dir.

"""

def fib(n): #normal fib recursive
    
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fastFib(n, memo={}):
    
    if n==0 or n==1:
        return 1
    try:
        return memo[n] #eğer bellekte kayıtlı ise bu değeri yollar.
    except KeyError:
        result=fastFib(n-1,memo)+fastFib(n-2,memo)
        memo[n]=result
    return result

print(fib(5))
print(fastFib(5))







