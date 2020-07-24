# Created by Xavier Conzet

import die

die_one = die.dice(6)
die_two = die.dice(20)




for i in range(3):
    x = die_one.roll(die_one.numSides)
    y = die_two.roll(die_two.numSides)
    total = x + y
    print("Roll of a 6-sided Die: " + str(x) + " Roll of a 20-sided Die: " + str(y) + " Total: " + str(total))


input("\nPress enter to exit")


