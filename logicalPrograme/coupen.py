"""
@Author : Avinash Jadhav
@Date : 2021-11-12
@Last Modify by : Avinash Jadhav
@Title : generate coupens
"""

import random


class Coupon:
    """
      @Description : generate coupon from random function and store into a file
      @Parameter   : parameter is amount of coupon you want to generate
      @return      : -
    """
    try:
        def generate(amount):
            coupon = open("coupons.txt", "a")

            for x in range(0, amount):
                a = random.randint(1000, 9999)
                a = str(a)

                total = ""
                total = str(total)
                total = a

                coupon.write(total)
                coupon.write("\n")

        if __name__ == "__main__":
            amount = int(input("How many coupons do you want to generate: "))
            generate(amount)
        print("\nCode's have been generated!")

    except ValueError as e:
        print("\n please enter digit amount only",e)

