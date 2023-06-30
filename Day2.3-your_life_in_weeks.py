'''
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html
'''
age = input("What is your current age? ")
 
#caliculations are made by assuming 90 is the max age a person can live

years_leftover = 90 - int(age)
leftover_months = years_leftover * 12 
leftover_weeks = years_leftover * 52
leftover_days = years_leftover * 365

print(f"You have {leftover_days} days, {leftover_weeks} weeks, and {leftover_months} months left.")


