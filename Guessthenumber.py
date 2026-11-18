import random
random_number=random.randint(1,50)
attempts=5
answer=0
while answer != random_number:
    answer=int(input("Pick a number 1-50!"))
    if answer==random_number:
       print("Good Job! your correct!")



    else:
      attempts=attempts-1
      diff=answer-random_number
      if attempts==0:
         print("Out of attempts, Answer was:", random_number)

      else:
        if diff<=5:
             print("Boiling hot!, Attempts left:",attempts )

        elif diff<=15:
            print("Warm, Attempts left:", attempts)
        elif diff<=20:
            print("Colder, Attempts left:", attempts)
        elif diff<=25:
          print("Freezing Cold!, Attempts left:", attempts)
    

