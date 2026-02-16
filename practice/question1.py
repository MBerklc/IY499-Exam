def create_id(studentID):
    message = "Invalid number"
    reply = ""
    total = 0

    # length check
    if len(studentID) != 7:
        return message

    # must be all digits
    if not studentID.isdigit():
        return message

    # sum indices 1,3,5 (because range(1,7,2))
    for i in range(1, 7, 2):
        total += int(studentID[i])

    if total != 14:
        return message

    # first 2 digits
    reply += studentID[0:2]

    # last digit meaning
    if studentID[-1] == "1":
        reply += " indicates home status"
    elif studentID[-1] == "2":
        reply += " indicates an RUK"
    elif studentID[-1] == "3":
        reply += " indicates international student"
    else:
        return message

    return reply

enterID = input("Enter your ID: ")
print(create_id(enterID))