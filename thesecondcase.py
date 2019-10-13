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

annual_income = int(input('Enter your annual income: '))

TAX_RATE_1 = 0.1
TAX_RATE_2 = 0.15
TAX_RATE_3 = 0.25
TAX_RATE_4 = 0.28
TAX_RATE_5 = 0.33
TAX_RATE_6 = 0.35
TAX_RATE_7 = 0.396

BOUNDARY_INCOME_1 = 0
BOUNDARY_INCOME_2 = 18_151
BOUNDARY_INCOME_3 = 73_801
BOUNDARY_INCOME_4 = 148_851
BOUNDARY_INCOME_5 = 226_851
BOUNDARY_INCOME_6 = 405_101
BOUNDARY_INCOME_7 = 457_601

import sys
if annual_income in range(18_151):
    n = TAX_RATE_1*(annual_income - BOUNDARY_INCOME_1)
elif annual_income in range(12_951, 73_801):
    n = TAX_RATE_2*(annual_income - BOUNDARY_INCOME_2) + TAX_RATE_1*(BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
elif annual_income in range(73_801, 148_851):
    n = TAX_RATE_3*(annual_income - BOUNDARY_INCOME_3) + TAX_RATE_2*(BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2)\
        + TAX_RATE_1*(BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
elif annual_income in range(148_851, 226_851):
    n = TAX_RATE_4*(annual_income - BOUNDARY_INCOME_4) + TAX_RATE_3*(BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3)\
        + TAX_RATE_2*(BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + TAX_RATE_1*(BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
elif annual_income in range(226_851, 405_101):
    n = TAX_RATE_5*(annual_income - BOUNDARY_INCOME_5) + TAX_RATE_4*(BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4)\
        + TAX_RATE_3*(BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + TAX_RATE_2*(BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) \
        + TAX_RATE_1*(BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
elif annual_income in range(405_101, 457_601):
    n = TAX_RATE_6*(annual_income - BOUNDARY_INCOME_6) + TAX_RATE_5*(BOUNDARY_INCOME_6 - BOUNDARY_INCOME_5)\
        + TAX_RATE_4*(BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + TAX_RATE_3*(BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) \
        + TAX_RATE_2*(BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + TAX_RATE_1*(BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
elif annual_income in range(457_601, sys.maxsize**10):
    n = TAX_RATE_7*(annual_income - BOUNDARY_INCOME_7) + TAX_RATE_6*(BOUNDARY_INCOME_7 - BOUNDARY_INCOME_6)\
        + TAX_RATE_5*(BOUNDARY_INCOME_6 - BOUNDARY_INCOME_5) + TAX_RATE_4*(BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4)\
        + TAX_RATE_3*(BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + TAX_RATE_2*(BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2)\
        + TAX_RATE_1*(BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
print('the amount of tax is ', n)

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
