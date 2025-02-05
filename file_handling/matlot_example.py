import matplotlib.pyplot as plot


month=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

rainFalls =[100,30,40,50,60,100,30,80,90,120,70,98]


plot.bar(month,rainFalls, color='red')

plot.title("monthly rain falls bar ")

plot.xlabel('month')
plot.ylabel('rainfalls')
plot.show()
