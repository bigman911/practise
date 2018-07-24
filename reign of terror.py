import time

def ending(score):
    if score <= 0:
        print("You become Derek's personal slave\n", count, "points")
        hisc.write(str(user + "-" + str(count) + "\n"))
        quit()
    elif score <= 75:
        print("You remain at the school and continue to recieve regualr beatings\n", count, "points")
        hisc.write(str(user + "-" + str(count) + "\n"))
        quit()
    elif score > 75:
        print("You escape from the school and successfully get slade arrested\n", count, "points")
        hisc.write(str(user + "-" + str(count) + "\n"))
        quit()


hisc = open("highscore.txt", "a+")

count = 0
user = input("What's your username?")
start = input("Welcome to Reign of Terror \n 1-Start Game 2-Highscores")

if start == "2":
    hisc = open("highscore.txt", "r")
    file_contents = hisc.read()
    print(file_contents)

if start == "1":
    c1 = input("It's your first day at St. Georges, what subjects do you choose?"
               " \n 1-Maths 2-English ")

    if c1 == "1":
        print("You walk into Maths class, the teacher introduces you to the students.")
        time.sleep(2)
        c2a = input("Your struggling with the lesson, do you 1-ask your colleges or 2-ask the teacher")  # branch 1
        if c2a == "2":
            c3a = input("You ask the teacher for help, Mr Slade comes over to your desk, and "
                        "slams a bloody wooden padle on your desk. \n What do you do?\n 1-Kick Slade into the "
                        "balls 2-Accept your punishment")
            if c3a == "1":
                c4a = input("To stun Derek get the question right\n"
                            "How many years did Slade get\n"
                            "1-101 2-12 3-21")
                if c4a == "3":
                    print("Slade falls to the ground, you run")
                    count = count + 100
                    time.sleep(1)
                    c5a = input("You have a test tomorrow,\n Do you revise?")
                    if c5a == "yes" or c5a == "Yes":
                        print("You ace the test and get called out on cheating")
                        count = count - 25
                        print("Slade got you\n GAME OVER")
                        time.sleep(1)
                        ending(count)

                    if c5a == "no" or c5a == "No":
                        k = input("What was Slade's other alias. \n 1-Edward Marsh 2-Gary Glitter")
                        if k == "1":
                            count = count + 100
                            print("Got em, you scraped a pass ")

                    else:
                        print("Slade got you\n GAME OVER")
                        time.sleep(1)
                        ending(count)


                else:
                    print("Slade got you\n GAME OVER")
                    time.sleep(1)
                    ending(count)
            if c3a == "2":
                count = count + 20
                print("Slade got you\n GAME OVER")
                time.sleep(1)
                ending(count)

        if c2a == "1":
            print("You ask the pupil on your desk but he ignores\n The teacher hears you and starts walking over")
            time.sleep(1)
            print("Get the question right to think an excuse")
        time.sleep(1)
        q = input("When was St. Georges founded?\n 1-1967 2-1987 3-1978")
        if q == "3":
            print("You say you were asking the time and get away with it, \n  +50 points ")
            count = count + 50
            time.sleep(1)

            c3a = input("It's break time,\n where do you go?"
                        "1-Library 2-Playground")
            if c3a == "1":
                c4a = input("You walk into the library, and someone is crying in the corner.\n"
                            "Slade walks over to him and hits him with a cane."
                            "\n What do you do? 1-Hit Slade with a book 2-Allow Derek to hit you as well")
                if c4a == "2":
                    print("Slade got you\n GAME OVER", count, "points")
                    hisc.write(str(user + "-" + str(count) + "\n"))
                    quit()
                if c4a == "1":
                    p = input("What colour did Slade go when he died?\n"
                              "1-Red 2-Brown 3-Green")
                    if p == "Green" or p == "green":
                        print("Slade got knocked out and broke his neck on the table.\n+150 points")
                        count = count + 150

            if c3a == "2":


        else:
            print("Slade got you\n GAME OVER")
            time.sleep(1)
            ending(count)

    if c1 == "2":
        print("You come to the door of the English room, its very loud,from what you can "
              "hear it's ranting about female rights.\n As you open the door the student who was making the noise is"
              " being caned in front of the entire class")
        time.sleep(1)
c2b = input("What do  you do? 1-Nothing or 2-Punch the teacher in the throat")  # branch 2
if c2b == "2":
    print("The teacher didn't even flinch, he's chasing after you.\n Get the question right to do damage.")
    time.sleep(1)
    a = input("Who was the headmaster of St. Georges")

    if a == "Derek Slade":
        print("You threw yourself through the window and escaped,\n +100 points")
        count = count + 100
        time.sleep(1)
        print("Slade followed you and is chasing, \n Press enter to run, you have 5 seconds")
        no = 0
        input("")
        print("Start pressing")
        firsttime = time.time()
        while no < 15:
            input("")
            no = no + 1
            secondtime = time.time()
            if secondtime - firsttime >= 5:
                print("Slade got you\n GAME OVER")
                time.sleep(1)
                ending(count)
        if secondtime - firsttime <= 5:
            print("You got away \n +200 points")
            count = count + 200
    else:
        print("Slade got you\n GAME OVER")
        time.sleep(1)
        ending(count)

if c2b == "1":
    print("You stand awkwardly in front of the beating and get push over the desk and receive and black eye"
          "from the slipper.\n You die from the impact.")
    print("Slade got you\n GAME OVER")
    time.sleep(1)
    ending(count)



