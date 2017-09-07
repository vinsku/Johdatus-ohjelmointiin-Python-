#opintotukiraha.py
#Enter the amount of the study benefits: 335.32
#If the index raise is 1.17 percent, the study benefit,
#after a raise, would be 339.243244 euros
#and if there was another index raise, the study
#benefits would be as much as 343.2123899548 euros

rivi = input("Enter the amount of the study benefits: ")
opintotuki = float(rivi)
muuttuja1 = 1.17
#muuttuja1 = opintotuen korotusprosentti
lopullinenraha = ( opintotuki / 0,0117 ) * 100
print(opintotuki, "If the index raise is 1.17 percent, the study benefit after a raise, would be " ,lopullinenraha "euros")