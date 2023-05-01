

xh = input("Enter hours: ")
xr = input("Enter Rate: ")
try:
	fr = float(xr)
	fh= float(xh)
except:
	print("Error, please enter numeric input")
	quit()

print(fh, fr)
if fh > 40:
	reg = fr * fh
	otp = (fh-40.0)*(fr*0.5)
	xp = reg + otp
else:
	xp = fh * fr
print("Pay:", xp)  

