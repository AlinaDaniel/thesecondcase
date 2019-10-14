# Case #2 "Progressive taxation".

# The program displays the amount of tax for an individual taking into account
# his monthly income and annual tax deductions.

# Developers:   Zemtseva A. (%),
#               Zaitseva A. (%),
#               Daniel A.   (%).

import sys
import local as lc

name_month = [lc.TXT_JAN, lc.TXT_FAB, lc.TXT_MAR, lc.TXT_APR, lc.TXT_MAY, lc.TXT_JUN, lc.TXT_JUL,
              lc.TXT_AUG, lc.TXT_SEP, lc.TXT_OCT, lc.TXT_NOV, lc.TXT_DEC]

annual_income = 0
for month in range(12):
    # Cycle for calculating the total income for the year.
    print(lc.TXT_INCOME, name_month[month], end =': ')
    income = float(input())
    annual_income += income

# The user chooses which category of the population he belongs to.
category_of_population = str.lower(input(lc.TXT_FAMILY_STATUS))
tax_deduction = int(input(lc.TXT_TAX_DEDUCTION))

if category_of_population == lc.TXT_ONE_SUBJECT:
    # Function, calculating the amount of annual tax for one subject.
    TAX_RATE_1 = 0.1
    TAX_RATE_2 = 0.15
    TAX_RATE_3 = 0.25
    TAX_RATE_4 = 0.28
    TAX_RATE_5 = 0.33
    TAX_RATE_6 = 0.35
    TAX_RATE_7 = 0.396

    BOUNDARY_INCOME_1 = 0
    BOUNDARY_INCOME_2 = 9_076
    BOUNDARY_INCOME_3 = 36_901
    BOUNDARY_INCOME_4 = 89_351
    BOUNDARY_INCOME_5 = 186_351
    BOUNDARY_INCOME_6 = 405_101
    BOUNDARY_INCOME_7 = 406_751

    if annual_income in range(BOUNDARY_INCOME_2):
        # The annual income is in first step.
        amount_of_tax = TAX_RATE_1 * (annual_income - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_2, BOUNDARY_INCOME_3):
        # The annual income is in second step.
        amount_of_tax = TAX_RATE_2 * (annual_income - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_3, BOUNDARY_INCOME_4):
        # The annual income is in third step.
        amount_of_tax = TAX_RATE_3 * (annual_income - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_4, BOUNDARY_INCOME_5):
        # The annual income is in fourth step.
        amount_of_tax = TAX_RATE_4 * (annual_income - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_5, BOUNDARY_INCOME_6):
        # The annual income is in fifth step.
        amount_of_tax = TAX_RATE_5 * (annual_income - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_6, BOUNDARY_INCOME_7):
        # The annual income is in sixth step.
        amount_of_tax = TAX_RATE_6 * (annual_income - BOUNDARY_INCOME_6) + \
                        TAX_RATE_5 * (BOUNDARY_INCOME_6 - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_7, sys.maxsize ** 10):
        # The annual income is in seventh step.
        amount_of_tax = TAX_RATE_7 * (annual_income - BOUNDARY_INCOME_7) + \
                        TAX_RATE_6 * (BOUNDARY_INCOME_7 - BOUNDARY_INCOME_6) + \
                        TAX_RATE_5 * (BOUNDARY_INCOME_6 - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
elif category_of_population == lc.TXT_MARRIED_COUPLE:
    # Function, calculating the amount of annual tax for a married couple.
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

    if annual_income in range(BOUNDARY_INCOME_2):
        # The annual income is in first step.
        amount_of_tax = TAX_RATE_1 * (annual_income - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_2, BOUNDARY_INCOME_3):
        # The annual income is in second step.
        amount_of_tax = TAX_RATE_2 * (annual_income - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_3, BOUNDARY_INCOME_4):
        # The annual income is in third step.
        amount_of_tax = TAX_RATE_3 * (annual_income - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_4, BOUNDARY_INCOME_5):
        # The annual income is in fourth step.
        amount_of_tax = TAX_RATE_4 * (annual_income - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_5, BOUNDARY_INCOME_6):
        # The annual income is in fifth step.
        amount_of_tax = TAX_RATE_5 * (annual_income - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_6, BOUNDARY_INCOME_7):
        # The annual income is in sixth step.
        amount_of_tax = TAX_RATE_6 * (annual_income - BOUNDARY_INCOME_6) + \
                        TAX_RATE_5 * (BOUNDARY_INCOME_6 - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_7, sys.maxsize ** 10):
        # The annual income is in seventh step.
        amount_of_tax = TAX_RATE_7 * (annual_income - BOUNDARY_INCOME_7) + \
                        TAX_RATE_6 * (BOUNDARY_INCOME_7 - BOUNDARY_INCOME_6) + \
                        TAX_RATE_5 * (BOUNDARY_INCOME_6 - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
elif category_of_population == lc.TXT_SINGLE_PARENT:
    # Function, calculating the amount of annual tax for a single parent.
    TAX_RATE_1 = 0.1
    TAX_RATE_2 = 0.15
    TAX_RATE_3 = 0.25
    TAX_RATE_4 = 0.28
    TAX_RATE_5 = 0.33
    TAX_RATE_6 = 0.35
    TAX_RATE_7 = 0.396

    BOUNDARY_INCOME_1 = 0
    BOUNDARY_INCOME_2 = 12_951
    BOUNDARY_INCOME_3 = 49_401
    BOUNDARY_INCOME_4 = 127_551
    BOUNDARY_INCOME_5 = 206_601
    BOUNDARY_INCOME_6 = 405_101
    BOUNDARY_INCOME_7 = 432_201

    if annual_income in range(BOUNDARY_INCOME_2):
        # The annual income is in first step.
        amount_of_tax = TAX_RATE_1 * (annual_income - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_2, BOUNDARY_INCOME_3):
        # The annual income is in second step.
        amount_of_tax = TAX_RATE_2 * (annual_income - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_3, BOUNDARY_INCOME_4):
        # The annual income is in third step.
        amount_of_tax = TAX_RATE_3 * (annual_income - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_4, BOUNDARY_INCOME_5):
        # The annual income is in fourth step.
        amount_of_tax = TAX_RATE_4 * (annual_income - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_5, BOUNDARY_INCOME_6):
        # The annual income is in fifth step.
        amount_of_tax = TAX_RATE_5 * (annual_income - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_6, BOUNDARY_INCOME_7):
        # The annual income is in sixth step.
        amount_of_tax = TAX_RATE_6 * (annual_income - BOUNDARY_INCOME_6) + \
                        TAX_RATE_5 * (BOUNDARY_INCOME_6 - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)
    elif annual_income in range(BOUNDARY_INCOME_7, sys.maxsize ** 10):
        # The annual income is in seventh step.
        amount_of_tax = TAX_RATE_7 * (annual_income - BOUNDARY_INCOME_7) + \
                        TAX_RATE_6 * (BOUNDARY_INCOME_7 - BOUNDARY_INCOME_6) + \
                        TAX_RATE_5 * (BOUNDARY_INCOME_6 - BOUNDARY_INCOME_5) + \
                        TAX_RATE_4 * (BOUNDARY_INCOME_5 - BOUNDARY_INCOME_4) + \
                        TAX_RATE_3 * (BOUNDARY_INCOME_4 - BOUNDARY_INCOME_3) + \
                        TAX_RATE_2 * (BOUNDARY_INCOME_3 - BOUNDARY_INCOME_2) + \
                        TAX_RATE_1 * (BOUNDARY_INCOME_2 - BOUNDARY_INCOME_1)

# Taking into account annual tax deductions.
result = amount_of_tax - tax_deduction


# TODO (Zaitseva A): Circle function for calculating a annual income.

pass


# TODO (Daniel A): Localization for the case.

pass


# TODO (Daniel A, Zemtseva A): Code rewiew.

pass


print(lc.TXT_ANNUAL_TAX, round(result, 2), '$')