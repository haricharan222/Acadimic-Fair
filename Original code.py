def spsdGoals(goal_id):

   goal_info = {

       1: 'Sustainable Development Goal 1 More than 700 million people, or 10 per cent of the world population, still live in extreme poverty today, struggling to fulfil the most basic needs like health, education, and access to water and sanitation, to name a few. The majority of people living on less than $1.90 a day live in sub-Saharan Africa. Worldwide, the poverty rate in rural areas is 17.2 per cent—more than three times higher than in urban areas.',

       2: 'Sustainable Development Goal 2 End hunger, achieve food security and improved nutrition and promote sustainable agriculture.',

       3: 'Sustainable Development Goal 3 aims to prevent needless suffering from preventable diseases and premature death by focusing on key targets that boost the health of a countrys overall population.',

       4:'Sustainable Development Goal 4 aims to ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.',

       5:'Sustainable Devolopment Goal 5 Achieve gender equality and empower all women and girls.',

       6:'Sustainable Devolopment Goal 6 Ensure access to water and sanitation for all. Access to safe water, sanitation and hygiene is the most basic human need for health and well-being. Billions of people will lack access to these basic services in 2030 unless progress quadruples.',

       

    

   }

   return goal_info.get(goal_id, 'Invalid User ID')



goal_id = int(input('\nEnter the goal ID:'))

print(spsdGoals(goal_id))


print("\nAnswer the following question : - ")

if goal_id == 1:

   print("By which year do we need to eradicate extreme poverty ? : ")

   answer = input()

   if answer == "2030":

    print("Congratulations", "name", "you have passed the test")

   else:

       print("better luck next time")

elif goal_id == 2:

   print("Before which crisis projections showed 200 m children would be out of school ? : ")

   answer = input()

   if answer == "coronavirus":

       print("Congratulations", "name", "you have passed the test")

   else:

       print("better luck next time")

elif goal_id == 3:

   print("6 out of 10 people around the world use which technology ? : ")

   answer = input()

   if answer == "internet":

       print("Congratulations", "name", "you have passed the test")

   else:

       print("better luck next time")