year = int(input("Enter year of birth: "))

if year >= 1900:
    zodiac = year % 12
    if zodiac == 4:
        print("Your Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")
    elif zodiac == 5:
        print("Your Chinese Zodiac Sign is : Ox (牛 / Niú)")
    elif zodiac == 6:
        print("Your Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")
    elif zodiac == 7:
        print("Your Chinese Zodiac Sign is : Rabbit (兔 / Tù)")
    elif zodiac == 8:
        print("Your Chinese Zodiac Sign is : Dragon (龙 / Lóng)")
    elif zodiac == 9:
        print("Your Chinese Zodiac Sign is : Snake (蛇 / Shé)")
    elif zodiac == 10:
        print("Your Chinese Zodiac Sign is : Horse (马 / Mǎ)")
    elif zodiac == 11:
        print("Your Chinese Zodiac Sign is : Goat (羊 / Yáng))")
    elif zodiac == 0:
        print("Your Chinese Zodiac Sign is : Monkey (猴 / Hóu)")
    elif zodiac == 1:
        print("Your Chinese Zodiac Sign is : Rooster (鸡 / Jī)")
    elif zodiac == 2:
        print("Your Chinese Zodiac Sign is : Dog (狗 / Gǒu)")
    elif zodiac == 3:
        print("Your Chinese Zodiac Sign is : Pig (猪 / Zhū)")

else:
    print("Invalid Year, It should not be earlier than 1900")
    exit()


