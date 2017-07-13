#Asks of your name and age so you insert and prints it out
def get_age():
    return int(raw_input("Whats your age"))
    return age

def get_name():
    return raw_input("Whats your name?")
    
age = get_age()
name = get_name()
print "hey, " + name + ", you are " + str(age) + "years old, dude!"

