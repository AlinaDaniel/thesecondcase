# Case #2.
# Developers:   Zemtseva A. (%),
#               Zaitseva A. (%),
#               Daniel A.   (%).


# TODO (Zaitseva A): Circle function for calculating a annual income.

pass


# TODO (Daniel A): The user chooses which category of the population he belongs to.

pass


# TODO (Daniel A): Function for one subject.

pass


# TODO (Zemtseva A): Function for a married couple.

pass


# TODO (Zaitseva A): Function for a single parent.
# function for a single parent.

annual_income = int(input('Enter your annual income: '))

S_1 = 0.1
S_2 = 0.15
S_3 = 0.25
S_4 = 0.28
S_5 = 0.33
S_6 = 0.35
S_7 = 0.396

D_1 = 0
D_2 = 12_951
D_3 = 49_401
D_4 = 127_551
D_5 = 206_601
D_6 = 405_101
D_7 = 432_201

import sys
if annual_income in range(12_951):
    n = S_1*(annual_income - D_1)
elif annual_income in range(12_951, 49_401):
    n = S_2*(annual_income - D_2) + S_1*(D_2 - D_1)
elif annual_income in range(49_401, 127_551):
    n = S_3*(annual_income - D_3) + S_2*(D_3 - D_2) + S_1*(D_2 - D_1)
elif annual_income in range(127_551, 206_601):
    n = S_4*(annual_income - D_4) + S_3*(D_4 - D_3) + S_2*(D_3 - D_2) + S_1*(D_2 - D_1)
elif annual_income in range(206_601, 405_101):
    n = S_5*(annual_income - D_5) + S_4*(D_5 - D_4) + S_3*(D_4 - D_3) + S_2*(D_3 - D_2) + S_1*(D_2 - D_1)
elif annual_income in range(405_101, 432_201):
    n = S_6*(annual_income - D_6) + S_5*(D_6 - D_5) + S_4*(D_5 - D_4) + S_3*(D_4 - D_3) + S_2*(D_3 - D_2) \
        + S_1*(D_2 - D_1)
elif annual_income in range(432_201, sys.maxsize**10):
    n = S_7*(annual_income - D_7) + S_6*(D_7 - D_6) + S_5*(D_6 - D_5) + S_4*(D_5 - D_4) + S_3*(D_4 - D_3) \
        + S_2*(D_3 - D_2) + S_1*(D_2 - D_1)
print('the amount of tax is ', n)

pass


# TODO (Zemtseva A): Circle function for calculating an amount of the annual tax.

pass


# TODO (Daniel A): Localization for the case.

pass


# TODO (Daniel A): Code rewiew.

pass
