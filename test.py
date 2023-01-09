#abcdefg

for i in "abcdefg":
    print(i)

def something():
    print("Hello world")
#decorator i think. probably doesnt work
def canitwork(msg):
    def idunknow():
        return "HI" + msg
    return idunknow()

message = canitwork("Blek")
print(message)