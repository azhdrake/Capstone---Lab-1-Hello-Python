#I misread the question and added mediocre data validatin for dates. rather then just having a birth month.
name = input("What is your name? ")

print("Hello, " + name + ". Your name has "+ str(len(name)) +" letters in it.")

birthday = input("What is your birthday in xx-xx-xxxx format? ")

birthday = birthday.split("-")

while int(birthday[0]) > 12 or int(birthday[0]) <= 0 or int(birthday[1]) <= 0 or int(birthday[1]) > 31 or int(birthday[2]) > 2020:
    birthday = input("please enter a valid date in xx-xx-xxxx format. ")
    birthday = birthday.split("-")


if(birthday[0] == "01" or birthday[0] == "1"):
    print("Happy birth month!")

