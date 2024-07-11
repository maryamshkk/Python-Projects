class ContestentData():
    def __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department

    def get_name(self):
        print(" Name:           |", self.name)
    
    def get_age(self):
        print(" Age:            |",self.age)

    def get_department(self):
        print(" Department:     |",self.department)

    
class QuizData:
    data=[]

    def __init__(self):
        self.welcome_message()
        self.input_contestent_data()
        self.display_data()
        self.quiz()
    
    def welcome_message(self):
        print("Welcome to Quiz Game")
        play=input("Do you want to play ? ")
        if play.lower() != "yes":
            print("Your loss! ")
            quit()
        print("OKAY! Let's Start :) \n")

    def input_contestent_data(self):
        while True:
            age=input("Enter your Age: ")
            try:
                age=int(age)
                if age>=18:
                    break
            except ValueError:
                print("AGE should be greater than 18! ")

        name=input("Enter your Name: ").capitalize()
        depart=input("Enter your Department: ").capitalize()
        self.data.append(ContestentData(name=name,age=age,department=depart))
        print("Your information has been eneterd Successfully! \n")

    def display_data(self):
        for d in self.data:
            d.get_name()
            d.get_age()
            d.get_department()
            return

    def quiz(self):
        score=0
        print()
        q1=input("What is the Capital of Pakistan ? ")
        if q1 == "islamabad":
            print("Correct! ")
            score+=1
        else:
            print("Incorrect! ")
    
        q2=input("What does WHO Stands for ? ")
        if q2 == "world health organization":
            print("Correct! ")
            score+=1
        else:
            print("Incorrect! ")

        q3=input("How many opening does Stack has ? ")
        if q3 == "1" or "one":
            print("Correct! ")
            score+=1
        else:
            print("Incorrect! ")

        q4=input("In what galaxy is our solar system located ? ")
        if q4 == "milky way":
            print("Correct! ")
            score+=1
        else:
            print("Incorrect! ")

        q5=input("What type of gas is absorbed by plants ? ")
        if q5 == "carbon dioxide":
            print("Correct! ")
            score+=1
        else: 
            print("Incorrect! ")
        print()

        if score>=3:
            print("Congratulations! You have Qualified the test.")
            print("Your Total Score is: ")
            print(score)  
        else:
            print("You didn't qualified the Test Criteria! Try better next time. ")
            print("Your Total Score is: ")
            print(score)

object=QuizData()