class TaskAllocationProtocol:
    def taskgenerator(self, fitem, fname, pitem, pname, citem, cname,):

        secret_number = 9 # here is a value we want the user to gues
        guess_count = 0 # here we start the count
        guess_limit = 3 # here we limit the number of guesses the user can enter
        while guess_count < guess_limit: # here we specify that the user has to guess a value within 3 tries
           guess = int(input('guess: ')) # here we convert the user input into an integer
           guess_count += 1 # then we increase the count to avoid an infinit loop
           if guess == secret_number: # now we do an if statement to notify the user they won
               print('you won!')
               break # here we stop the while loop from running even if the user has only entered one guess
        else: # here we want make an additional decision if our while condition is not met
           print('Sorry you loose!') # here this line will run if the user enters 3 guesses but doesnt actually guess the right number

        print("to generate a family task")
        fname = input("enter a name for your task here: ")

        print("to generate a parent task")
        pname = input("enter a name for your task here: ")

        print("to generate a child task")
        cname = input("enter a name for your task here: ")


    def families(self, fitem, fname):
        famlist = {
            fitem: fname
        }


    def parents(self, pitem, pname):
        parentslist = {
            pitem: pname
        }


    def children(self, citem, cname):
        childrenlist = {
            citem: cname
        }

