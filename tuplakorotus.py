#tuplakorotus.py
#Enter the amount of the study benefits: 335.32
#If the index raise is 1.17 percent, the study benefit,
#after a raise, would be 339.243244 euros
#and if there was another index raise, the study
#benefits would be as much as 343.2123899548 euros


rivi = input("Enter the amount of the study benefits: ")
opintotuki = float(rivi)
opintotuki = (opintotuki / 100) * 1.17 + opintotuki
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be ", opintotuki, "euros")
print("and if there was another index raise, the study")
print("benefits would be as much as", (opintotuki / 100) * 1.17 + opintotuki, "euros")


