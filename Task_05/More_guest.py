# The program insert more person's for bigger table in dinner

guest_list = ['Ali','Hasan','Imad','Waseem']

for i in range(len(guest_list)):
    print(f"Deer {guest_list[i]}!, The honor of your presence is requested for dinner at eight thirty in Meshbell's Hall.")

print("The person's who didn't make it for a dinner are: 'Ali' and 'Imad'.")

guest_list[0] = 'Abbas'
guest_list[2] = 'Nasir'

for i in range(len(guest_list)):
    print(f"Deer! {guest_list[i]}!, Join us for a night of culinary delights and laughter at our dinner party")

guest_list.insert(0,"wasem")  # Name waseem is added at the begaining of a list
guest_list.insert(2, "Shadab") # Name shadab is added at the middle of a list
guest_list.append('Salman')

for i in range(len(guest_list)):
        print(f"Deer {guest_list[i]}, We would be honored if you could join us for a delightful dinner party.")