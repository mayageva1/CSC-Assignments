class Food():
    def __init__(self,n,v,c):
        self.name = n 
        self.value = v
        self.calories = c

    def getValue(self):
        return self.value
    def getCalories(self):
        return self.calories
    def getName(self):
        return self.name 

#create menu
def BuildMenuItems(names, values, calories):
    menu = []
    for i in range (0, len(names)):
        menu.append(Food(names[i],values[i],calories[i]))
    return menu

def GreedyAlgorithm(menu, maxCalories):
    #sort menu according to value
    sortedMenu = sorted(menu, key=Food.getValue, reverse=True)
    #Allocate memory for the solution
    solution = []
    totalCalories = 0
    totalValue = 0
    #Go through each item in menu starting with the most valueab;e
    #Add the food to the solution if we are under the calorie budget
    for i in range(0, len(sortedMenu)):
        #check if we can add the item without exceeding the calories
        if(totalCalories + sortedMenu[i].getCalories() <= maxCalories):
            solution.append(sortedMenu[i])
            #update calorie count
            totalCalories = totalCalories + sortedMenu[i].getCalories()
            totalValue = totalValue + sortedMenu[i].getValue()
    return solution, totalValue

names = ['wine','beer','pizza','burger','fries','cola','apple','donut']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]  
maxCalories = 750
menu = BuildMenuItems(names,values,calories)
solution,totalValue = GreedyAlgorithm(menu,maxCalories)
for i in range(0,len(solution)):
    print(solution[i].getName())
print("Total value =", totalValue)