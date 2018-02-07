from textwrap import dedent
from sys import exit

class LoveSong():
    def song(self):
        print(dedent("""It's so amazing to be loved
        I'd follow you to the moon in the sky above, above
        And it's so amazing, so amazing
        I could stay forever, forever
        Here in love and would leave you never
        'Cause we go amazing love
        Truly it's amazing, so amazing
        Love brought us together, together
        I would leave you never and never
        'Cause we got amazing"""))

print(dedent("""Today is Valentines Day!
You have the day all planned out for your date.
You just have some last minute decisions to make, 
but first are you male or female."""))

while True:
    gender = input("> ")

    if gender == "male":
        print(dedent("""Your beautiful date is waiting on you to pick
        her up. But where do you take her?"""))

        print(dedent("""You have two options for you date night.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        1. Take your girlfriend on a dinner date.
        2. Take your girlfriend on a picnic.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Which do you choose 1 or 2?"""))

        option = input("> ")

        if option == "1":
            print("So decided to take her on a dinner date.")
            print("What do you drive to go pick her up?")
            print("1. 1990 Crown Vic.")
            print("2. 2017 Mustang.")

            while True:

                car = input("> ")

                if car == "1":
                    print(dedent("""She looks at you and then the car. She then
                    happily jumps in the car ready to go. You all head on 
                    to your dinner date. You both enjoy the night. You take her home 
                    listening to this song..."""))
                    LoveSong().song()
                    exit()
                elif car == "2":
                    print(dedent("""She slaps you for spending all your money on 
                    a stupid car. Your day is ruined. Sorry sucka!"""))
                    exit()
                else:
                    print("Please enter a valid number.")

        elif option == "2":
            print(dedent("""You decide to take her on a picnic.
            Her face lights up in excitement.
            You have decide between two places for the picnic.
            ~~~~~~~~~~~~~~~~~~~~~~~
            1. Resevoir
            2. Park
            ~~~~~~~~~~~~~~~~~~~~~~~"""))

            while True:

                place = input("> ")

                if place == "1":
                    print(dedent("""You all go to the Resevoir for the picnic. 
                    You lay a blanket out for you all to sit down on and 
                    lay out the food. All of a sudden a flock of geese begin
                    to surround the both of you. They start to chase you all.
                    They chase your date all the way into the resevoir.
                    ~~~~~~~~~~~~~~~~~~~
                    She drowns and your day is ruined.
                    Sucks to be you!"""))
                    exit()
                elif place == "2":
                    print(dedent("""You all go to the park and the picnic goes
                    wonderfully. You enjoy your date so well that you decide 
                    that you want to marry her."""))
                    LoveSong().song()
                    exit()
                else:
                    print("Please enter a valid number.")

    elif gender == "female":
        print(dedent("""You're waiting on your handsome date to come over.
        You decided to fix him a dinner.
        ~~~~~~~~~~~~~~~~~~~~~~~~~
        1. Chicken dinner
        2. Meatloaf dinner
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Which do you choose 1 or 2?"""))

        dinner = input("> ")

        if dinner == "1":
            print(dedent("""You decided to make him a chicken dinner. 
            You both sit down to a candle light chicken dinner. 
            You sit eagerly waiting on him to take a bite. He picks
            up his fork and gets a piece of chicken on it and puts 
            it in his mouth. He begins to chew his food that you
            prepared. 
            His eyes then begins to bulge and he turns red. He starts 
            grasping at his throat. You look in horror as he falls over
            and dies. It turned out he was allergic to one of the seasonings
            that you seasoned the chicken with.
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~
            BUMMER you killed your date!"""))
            exit()
            
        elif dinner == "2":
            print(dedent(""" You decided to fix him a meatloaf dinner. 
            Surprisingly, he loved it. He cleaned his plate and wanted
            seconds and thirds. You both live happily ever after.""" ))
            LoveSong().song()
            exit()
        
    else:
        print("Please enter a valid answer.")