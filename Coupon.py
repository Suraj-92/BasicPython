'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number? 
    This program simulates this random process.
'''


import random


class Coupons:
    def logic(self, number):

        total_Coupons = []

        for i in range(number):
            random_number = random.randint(10, 100)
            total_Coupons.append(random_number)

            unique_Coupons = set(total_Coupons)
            coupons = list(unique_Coupons)
        return coupons


if __name__ == '__main__':
    while True:  # exception blocks
        try:
            number_ofCoupons = int(input("Enter number of two digits coupons numbers:"))

            if number_ofCoupons < 10 or number_ofCoupons > 500:
                print("Please enter between 10 and 500 ")
                continue
            coupon_Obj = Coupons()
            distinct_Coupons = coupon_Obj.logic(number_ofCoupons)
            print(distinct_Coupons)
            break
        except Exception:
            print("Enter valid input")
            continue
