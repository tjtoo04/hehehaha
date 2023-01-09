#abcdefg

for i in "abcdefg":
    print(i)

def something():
    print("Hello world")

def canitwork(msg):
    def idunknow():
        return "HI" + msg

message = canitwork("Blek")
print(message)