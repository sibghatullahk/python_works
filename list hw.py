guest=['leonardo','brad Pitt','daniel day lewis','scorsese','al pacino','norm macdonald']
#print(f"Hello, {guest[0].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[1].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[2].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[3].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[4].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[5].title()}. I would like you to attend a party at my house. Regards!")
#print(f"{guest[3].title()} can't make it to the party due to unforseen circumstances.")
guest[3]='dave chappele'
print(guest)
#print(f"Hello, {guest[0].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[2].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[3].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[4].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[5].title()}. I would like you to attend a party at my house. Regards!")
#alert="I found a bigger table. Let us invite some more guests."
#print(alert)
guest.insert(0,"bill burr")
guest.insert(4, "imran")
guest.insert(6,"dostayevski")
print(guest)
guest.append("makaveli")
print(guest)
#print(f"Hello, {guest[0].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[2].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[3].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[4].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[5].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[6].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[7].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[8].title()}. I would like you to attend a party at my house. Regards!")
#print(f"Hello, {guest[9].title()}. I would like you to attend a party at my house. Regards!")
alert="Oops! no more space. Pop guests out."
print(alert)
guests_popped=guest.pop(9)
print(f"Sorry, {guests_popped.title()}")
guests_popped=guest.pop(8)
print(f"Sorry, {guests_popped.title()}")
guests_popped=guest.pop(7)
print(f"Sorry, {guests_popped.title()}")
guests_popped=guest.pop(6)
print(f"Sorry, {guests_popped.title()}")
guests_popped=guest.pop(5)
print(f"Sorry, {guests_popped.title()}")
guests_popped=guest.pop(4)
print(f"Sorry, {guests_popped.title()}")
guests_popped=guest.pop(3)
print(f"Sorry, {guests_popped.title()}")
guests_popped=guest.pop(2)
print(f"Sorry, {guests_popped.title()}")
print(guest)
print(f"Hello, {guest[0].title()}. I would like you to attend a party at my house. Regards!")
print(f"Hello, {guest[1].title()}. I would like you to attend a party at my house. Regards!")
guests_popped=guest.pop(1)
print(f"Sorry, {guests_popped.title()}")
guests_popped=guest.pop(0)
print(f"Sorry, {guests_popped.title()}")
print(guest)