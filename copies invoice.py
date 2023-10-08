numberofcopies = int(input("how many copies do you want?"))
invoice = float
if numberofcopies == 10 :
    invoice = numberofcopies * 0.30
elif numberofcopies == 30 : 
    invoice = (10*0.30) + ((numberofcopies - 10) * 0.25)
else :
    invoice = (10*0.30) + (20*0.25) + ((numberofcopies - 30) * 0.20)
print("The corresponding invoice is", invoice, "dh")
