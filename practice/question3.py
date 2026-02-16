def flightid(fID):
    if len(fID) == 10:
        if fID[:2] == "SA":
            message = "ScotAir"
        elif fID[:2] == "RF":
            message = "Roland Flights"
        elif fID[:2] == "JJ":
            message = "Jet-Jet"
        else:
            return "wrong input try again..."

        if fID[2:5] == "DUB":
            message += " flight arriving from DUB"
        elif fID[2:5] == "INV":
            message += " flight arriving from INV"
        else:
            return "wrong input try again..."

        if int(fID[5:7]):
            for i in range(1, 25):
                if int(fID[5:7]) == i:
                    message += f" at {i}:"
        else:
            return "wrong input try again..."

        if int(fID[7:9]):
            for i in range(0, 60):
                if int(fID[7:9]) == i:
                    message += f"{i}"
        else:
            return "wrong input try again..."

        if not fID[9] == "A" or fID[9] == "D":
            return "wrong input try again..."

        return message
    else:
        return "FlightID should be 10 letters"


a = input("Enter the FlightID: ")
print(flightid(a))
