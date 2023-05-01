import csv
#import insurance.csv into our file and inspect the contents.
ages = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

with open('insurance.csv', 'r') as insurance_costs:
    insurance = csv.reader(insurance_costs)
    for row in insurance:
        ages.append(row[0])
        sex.append(row[1])
        bmi.append(row[2])
        children.append(row[3])
        smoker.append(row[4])
        region.append(row[5])
        charges.append(row[6])
        #contains age, sex, bmi, children, smoker, region, charges
#turn age into a workable set
updated_ages = []
for age in ages:
    if age == 'age':
        continue
    updated_ages.append(age)
ages_integer = list(map(int, updated_ages))
ages_integer
#find the average age
def average(lst):
    return sum(lst)/len(lst)
print("The average age of our customer is "+str(round(average(ages_integer),2))+" years old.")

#Where are the majority of individuals from
#work with region
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in region:
    if i == 'northeast':
        count1 += 1
    elif i == 'northwest':
        count2 += 1
    elif i == 'southeast':
        count3 += 1
    elif i == 'southwest':
        count4 += 1
#print out the region with the most customers
print("Most of our customers ("+ str(max(count1,count2,count3,count4))+") come from the southwest.")
#compare average cost smoker vs. non_smoker
no_smoker = 0
yes_smoker = 0
for lung in smoker:
    if lung == 'yes':
        yes_smoker += 1
    elif lung == 'no':
        no_smoker += 1
print("The number of our customers who smoke: " + str(yes_smoker) + ".") 
print("The number of our customers who do not smoke: " + str(no_smoker) + ".")
#average cost of smoker
#turn charges into a workable set
smoker_cost = 0
no_smoker_cost = 0
for cost in range(1,len(charges)-1):
    if smoker[cost] == 'yes':
        smoker_cost +=  float(charges[cost])
    elif smoker[cost] == 'no':
        no_smoker_cost += float(charges[cost])
#divide the total charges by smokers to get the average cost for a smoker
average_smoker_cost = smoker_cost/yes_smoker
average_no_smoker_cost = no_smoker_cost/no_smoker

print("The average cost of insurance for a smoker is $"+ str(round(average_smoker_cost,2)))
print("The average cost of insurance for a non smoker is $" + str(round(average_no_smoker_cost,2)))

#lets get the average of all our customers first
nu_charges=0
for charge in charges:
    if charge == 'charges':
        continue
    else:
        nu_charges += float(charge)
average_charge = nu_charges/len(charges)-1
print("The average cost per customer is : $" + str(round(average_charge, 2)))
