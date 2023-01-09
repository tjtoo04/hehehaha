#abcdefg

for i in "abcdefg":
    print(i)

def something():
    print("Hello world")

def canitwork(msg):
    def idunknow():
        return "HI" + msg
    return idunknow()

message = canitwork("Blek")
print(message)