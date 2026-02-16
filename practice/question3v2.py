def flightid(fid):
    message = "Invalid input..."
    reply = ""

    if len(fid) != 10:
        return message

    if fid[0:2] == "SA":
        reply += "ScotAir"
    elif fid[0:2] == "RF":
        reply += "Roland Flights"
    elif fid[0:2] == "JJ":
        reply += "Jet-Jet"
    else:
        return message

    if fid[-1] == 'A':
        reply += " flight arriving from "
    elif fid[-1] == 'D':
        reply += "flight departing for "
    else:
        return message

    if not fid[5:9].isdigit():
        return message

    for i in range(2,5):
        reply += fid[i]

    hour = int(fid[5:7])
    minute = int(fid[7:9])

    if (0 < hour < 24) and (0 < minute < 59) and (fid[5:9] == int):
        reply += f" at {fid[5:9]}"
    else:
        return message

    return  reply

fID = input("Enter the flightID: ")
print(flightid(fID))





