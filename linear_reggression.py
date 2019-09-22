with open('train.csv', 'r') as f:
    #read from csv line by line, rstrip helps to remove '\n' at the end of line
    lines = [line.rstrip() for line in f]

dat = []
for line in lines:
    words = line.split(',')
    tup = (words[0],words[1])
    dat.append(tup)
a = []
b = []
for i in range(1, len(dat)):
    a.append(dat[i][0])
    b.append(dat[i][1])
x = []
y = []
for i in range(len(a)):
    x.insert(i, float(a[i]))
    y.insert(i, float(b[i]))





#used as the input value of the algoirthm
#x = [17, 13, 12, 15, 16, 14, 16, 16, 18, 19]
#y = [94, 73, 59, 80, 93, 85, 66, 79, 77, 91]




x_len = len(x)
y_len = len(y)

#find the mean of x
x_sum = 0
for i in x:
    x_sum += i
x_mean = float(x_sum) / x_len


#find the mean of y
y_sum = 0
for i in y:
    y_sum += i
y_mean = float(y_sum) / y_len



#       _
#find x-x for eaach row
a = []
for i in x:
    a.append(round(i - x_mean,2))


#       _
#find y-y for eaach row
b = []
for i in y:
    b.append(round(i - y_mean,2))



#find (x - mean(x)) * (y - mean(y))
c = []
for i in range(0, x_len, 1):
    c.append(round(a[i] * b[i],2))


#find sum of c
c_sum = 0
for i in c:
    c_sum =round(c_sum + i, 2)



#find (x - mean(x))^2
d = []
for i in a:
    d.append(round(i * i, 2))

#find sum of d
d_sum = 0
for i in d:
    d_sum = round(d_sum + i, 2)



#find (y - mean(y))^2
e = []
for i in b:
   e.append(round(i * i, 2))

#find sum of e
e_sum = 0
for i in e:
    e_sum = round(e_sum + i,2)



#find r = sum( ((x - mean(x))^2)((y - mean(y))^2) )
r = round(c_sum/((d_sum * e_sum)**.5), 3)



#find standard deviation of x
x_sd = round((d_sum / (x_len - 1))**.5, 3)

#find standard deviation of y
y_sd = round((e_sum / (y_len - 1))**.5, 3)



#find B = r* (standard_deviation(y) / standard_deviation(x) )
B = round( r * (y_sd / x_sd), 3)


#find A = mean(y) - (B * mean(x))
A = round(y_mean - (B * x_mean), 3)







######################################

#make actual (linear) prediction here

######################################


#testing our model


#make user to enter the input of the algorithm
X = int(input("enter the input you want to give in the algorithm (only one number)"))


#predicts the Y value correspondes to the use input, X

Y = round(A + (B * X), 3)



#output the predicted value of Y
print("\n\nThe value of Y axis is =   " + str(Y))
