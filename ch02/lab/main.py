import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 15
cost_per_class = cost_per_week / classes_per_week
print("The cost per each class is:", cost_per_class)
print("Number of weeks:" ,weeks,type(weeks))
print("Number of classes: ",classes,type(classes))
print("Classes per week: ",classes_per_week,type(classes_per_week))
print("Cost per class: ", cost_per_class,type(cost_per_class))
print("Tuition cost: ",tuition,type(tuition))
print("Cost per week: ",cost_per_week,type(cost_per_week))

#Part B
my_list = [4,"pizza",5.5,9,"hello"]
my_list_choice = random.choice(my_list)
print("Random list selection is: ", my_list_choice)