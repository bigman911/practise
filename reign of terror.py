import time
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
            c2a = input("Your struggling with the lesson, do you 1-ask your colleges or 2-ask the teacher")#branch 1
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
                        if c5a == "yes" or "Yes":
                            print("You ace the test and get called out on cheating")
                    else:
                        print("Slade got you\n GAME OVER", count, "points")
                        hisc.write(str(user + "-" + str(count) + "\n"))
                        quit()
                if c3a == "2":
                    count = count + 20
                    print("Slade got you\n GAME OVER", count, "points")
                    hisc.write(str(user + "-" + str(count) + "\n"))
                    quit()

            if c2a =="1":
                print("You ask the pupil on your desk but he ignores\n The teacher hears you and starts walking over")
                time.sleep(1)
                print("Get the question right to think an excuse")
            time.sleep(1)
            q = input("When was St. Georges founded?\n 1-1967 2-1987 3  -1978")
            if q == "3":
                print("You say you were asking the time and get away with it, \n  +50 points ")
                count = count +50
                time.sleep(1)

                c3a = input("It's break time,\n where do you go?"
                           "1-Libary 2-Playground")
            else:
                print("Slade got you\n GAME OVER", count, "points")
                hisc.write(str(user + "-" + str(count) + "\n"))
                quit()




        if c1 == "2":
            print("You come to the door of the English room, its very loud,from what you can "
              "hear it's ranting about female rights.\n As you open the door the student who was making the noise is"
              "being caned in front of the entire class")
            time.sleep(1)
c2b = input("What do  you do? 1-Nothing or 2-Punch the teacher in the throat")   #branch 2
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
                        print("Slade got you\n GAME OVER", count, "points")
                        hisc.write(str(user + "-" + str(count) + "\n"))
                        quit()
                    if secondtime - firsttime <= 5:
                        print("sort me out")
                
            if c2b == "1":
                print("You stand awkwardly in front of the beating and get push over the desk and receive and black eye"
                  "from the slipper.\n You die from the impact. \nSlade got you\n GAME OVER",count,"points")
            hisc.write(str(user + "-" + str(count) + "\n"))
            quit()


