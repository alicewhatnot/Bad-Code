def valid_user(username):
    return username.isalpha()

def valid_id(userID):
    return userID[0] == "I" and userID[1] == "D"

def valid_room_num(roomNum):
    return roomNum[0].isalpha() and roomNum[0].isupper() and roomNum[1].isdigit() and roomNum[2].isdigit() and len(roomNum) == 3

print(valid_user("Fred"))
print(valid_id("ID34"))
print(valid_room_num("A56"))