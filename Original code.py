name=str(input("enter your name:"))

from tkinter import *
root=Tk()


root.title('OPTION APP')
root.iconbitmap('C:/Users/har22/.vscode/Google Chat.ico')
root.geometry("800x600")


def open():
    
    my_label = Label(root,text =clicked.get())
    my_label.grid(row=2,column=2,padx=10,pady=10,ipadx=30)

options = [
    
    'SDG goal 1',
    'SDG goal 2',
    'SDG goal 3',
    'SDG goal 4',
    'SDG goal 5',
    'SDG goal 6',
    'SDG goal 7',
    'SDG goal 8',
    'SDG goal 9',
    'SDG goal 10',
    'SDG goal 11',
    'SDG goal 12',
    'SDG goal 13',
    'SDG goal 14',
    'SDG goal 15',
    'SDG goal 16',
    'SDG goal 17',
    
]

clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root,clicked,*options)
drop.grid(row=0,column=1,padx=10,pady=10)

root.mainloop()



def spsdGoals(goal_id):

   goal_info = {

       1: 'Sustainable Development Goal 1,no poverty, More than 700 million people, or 10 per cent of the world population, still live in extreme poverty today, struggling to fulfil the most basic needs like health, education, and access to water and sanitation, to name a few. The majority of people living on less than $1.90 a day live in sub-Saharan Africa. Worldwide, the poverty rate in rural areas is 17.2 per cent—more than three times higher than in urban areas.',

       2: 'Sustainable Development Goal 2, Zero hunger, End hunger, achieve food security and improved nutrition and promote sustainable agriculture.',

       3: 'Sustainable Development Goal 3, Good health and well-being, aims to prevent needless suffering from preventable diseases and premature death by focusing on key targets that boost the health of a countrys overall population.',

       4:'Sustainable Development Goal 4, Quality education, aims to ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.',

       5:'Sustainable Devolopment Goal 5, Gender equality, Achieve gender equality and empower all women and girls.',

       6:'Sustainable Devolopment Goal 6, Clean water and sanitation, Ensure access to water and sanitation for all. Access to safe water, sanitation and hygiene is the most basic human need for health and well-being. Billions of people will lack access to these basic services in 2030 unless progress quadruples.',

       7:'Sustainable Devolopement Goal 7,Affordable and clean energy,ensuring access to clean and affordable energy, which is key to the development of agriculture, business, communications, education, healthcare and transportation.',

       8:'Sustainable Devolopement Goal 8, Decent work and economic growth,FULL EMPLOYMENT AND DECENT WORK WITH EQUAL PAY. ',

       9:'Sustainable Devolopment Goal 9, Industry, innovation and infrastructure, seeks to build resilient infrastructure, promote sustainable industrialization and foster innovation.',

       10:'Sustainable Devolopment Goal 10,Reduced inequalities,reducing inequalities in income as well as those based on age, sex, disability, race, ethnicity, origin, religion or economic or other status within a country.',

       11:'Sustainable Devolopment Goal 11,Sustainable cities and communities, strengthening capacities for planning for urban development, improving access to public transportation and enhancing waste management.',

       12:'Sustainable Devolopment Goal 12,Responsible consumption and production, Ensure sustainable consumption and production patterns. Goal 12 is about ensuring sustainable consumption and production patterns, which is key to sustain the livelihoods of current and future generations. ',

       13:'Sustainable Devolopment Goal 13, Climate on Action,seeks to achieve a climate-neutral world by mid-century and to limit global warming to well below 2°C — with an aim of 1.5°C — compared with pre-industrial times.',

       14:'Sustainable Devolopment Goal 14,Life below water,aims to protect and ensure the sustainable use of oceans. This includes reducing marine pollution and ocean acidification, end overfishing and conserve marine and coastal ecosystems.',

       15:'Sustainable Devolopment Goal 15,Peace, Life on land", focuses specifically on managing forests sustainably, halting and reversing land and natural habitat degradation, successfully combating desertification and stopping biodiversity loss.',

       16:'Sustainable Devolopment Goal 16,Peace, justice, and strong institutions, calls for peaceful and inclusive societies based on respect for human rights, protection of the most vulnerable, the rule of law and good governance at all levels.',

       17:'Sustainanble Devolopment Goal 17,Partnerships for the goals,Revitalize the global partnership for sustainable development. Goal 17 is about revitalizing the global partnership for sustainable development. The 2030 Agenda is universal and calls for action by all countries developed and developing to ensure no one is left behind.',


    

   }

   return goal_info.get(goal_id, 'Invalid Goal ID')



goal_id = int(input('\nEnter the goal ID:'))

print(spsdGoals(goal_id))


print("\nAnswer the following question : - ")

if goal_id == 1:

   print("By which year do we need to eradicate extreme poverty ? : ")

   answer = input()

   if answer == "2030":

    print("Congratulations", name, "you have passed the test")
    
    

   else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 2:

   print("Before which crisis projections showed 200 m children would be out of school ? : ")

   answer = input()

   if answer == "coronavirus":

       print("Congratulations", name, "you have passed the test")

   else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 3:

   print("6 out of 10 people around the world use which technology ? : ")

   answer = input()

   if answer == "internet":

       print("Congratulations", name, "you have passed the test")
   else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")


elif goal_id == 4:

   print("Which SDG focuses on achieving gender equality? : ")

   answer = input()

   if answer == "Education":
      
      print("Congratulations", name, "you have passed the test")
   else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")
   
elif goal_id == 5:
   
   print("Which SDG focuses on achieving gender equality:")

   answer = input()

   if answer == "Gender":
      
      print("Congratulations", name, "you have passed the test")
   else:

       print("You entered the wrong answer...", name, ", Better Luck Next Time!")   

elif goal_id == 6:
       
       print("Which SDG is dedicated to clean water and sanitation?")

       answer = input()

       if answer == "Water":
          
          print("Congratulations", name, "you have passed the test")
       else:

        print("You entered the wrong answer...", name, "Better Luck Next Time!")
          
elif goal_id == 7:
       
       print("Which SDG aims to ensure access to affordable and clean energy?")

       answer = input()

       if answer == "Energy":
             
         print("Congratulations", name, "you have passed the test")
       else:

        print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 8:

    print("Which SDG promotes decent work and economic growth?")

    answer = input()

    if answer == "Work":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 9:

    print("Which SDG focuses on industry, innovation, and infrastructure?")

    answer = input()

    if answer == "Industry":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 10:

    print("Which SDG aims to reduce inequality within and among countries?")       

    answer = input()

    if answer == "Inequality":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 11:

    print("Which SDG is about making cities and human settlements inclusive, safe, resilient, and sustainable?")

    answer = input()

    if answer == "Cities":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")


elif goal_id == 12:

    print("Which SDG focuses on responsible consumption and production?")

    answer = input()

    if answer == "Consumption":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")  

elif goal_id == 13:

    print("Which SDG focuses on climate action?")

    answer = input()

    if answer == "Climate":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 14:

    print("Which is SDG goal is dedicated to life below water")

    answer = input()

    if answer == "Oceans":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 15:

    print(" Which SDG focuses on life on land?")

    answer = input()

    if answer == "Forests":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 16:

    print("Which SDG promotes peace, justice, and strong institutions?")

    answer = input()

    if answer == "Peace":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")

elif goal_id == 17:

    print("Which SDG focus on partnerships for the goals?")

    answer = input()

    if answer == "Partnerships":

        print("Congratulations", name, "you have passed the test")
    else:

       print("You entered the wrong answer...", name, "Better Luck Next Time!")  
       
                 
