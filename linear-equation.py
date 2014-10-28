"""
y = mx + b

m = slope

m = (n*sum(xy) - sum(x)*sum(y))/(n*sum(x^2)-(sum(x)^2))

n is the number of matched pairs

b = ybar - m*xbar
"""
xtot = 0
ytot = 0
xytot = 0
xsquaretot = 0
ybar = 0
xbar = 0
n = 0
m = 0
b = 0
with open('/Users/rhettshipp1/Desktop/Data-Files/xycoordinates.txt') as f:
    #skip title row
    f.next()    
    for line in f:
        n += 1
        xtot += float(line.split()[0])
        ytot += float(line.split()[1])
        xytot += float(line.split()[0])*float(line.split()[1])
        xsquaretot += float(line.split()[0])**2
ybar = ytot / n
xbar = xtot / n
m = ((n*xytot) - (xtot*ytot)) / ((n*xsquaretot) - (xtot**2))
b = ybar - (m*xbar)
print 'the slope is ' + str(m)
print 'the y-intercept is ' + str(b)