
def computepay(hours, rate) :            
	#print("In computepay", hours, rate)
	if hours > 40:
		reg = rate * hours
		otp = (hours-40.0)*(rate*0.5)
		pay = reg + otp
	else:
		pay = hours * rate
	#print("Returning", pay)
	return pay 


xh = input("Enter hours: ")
xr = input("Enter Rate: ")
fr = float(xr)
fh= float(xh)

xp = computepay(fh, fr)
print("Pay:", xp)  

