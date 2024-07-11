# The program replace the guest list by new one's
# with one's who can't make it

guest_list = ['Ali','Hasan','Imad','Waseem']

for i in range(len(guest_list)):
    print(f"Deer {guest_list[i]}!, The honor of your presence is requested for dinner at eight thirty in Meshbell's Hall.")

print("The person's who didn't make it for a dinner are: 'Ali' and 'Imad'.")

guest_list[0] = 'Abbas'
guest_list[2] = 'Nasir'

for i in range(len(guest_list)):
    print(f"Deer! {guest_list[i]}!, The honor of your presence is requested for dinner at eight thirty in Meshbell's Hall.")

