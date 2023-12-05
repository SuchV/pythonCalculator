# Simple calculator in python for learning purposes
#
# Ideas List:
# Add graphic interface
# Add try clauses to check for wrong types of inputs
# The counting resets on every new game_loop opening, add global result and inputs and add it as parameters to the game loop function

# def numeric(equation):
#     if '+' in equation:
#         y = equation.split('+')
#         x = int(y[0])+int(y[1])
#     elif '-' in equation:
#         y = equation.split('-')
#         x = int(y[0])-int(y[1])
#     return x


def main():
    #One time function that executes on the first program start
    def opening_Screen():
        print("Welcome to the calculator!")
        print("If you want to check what commands you can use, type 'help'")
        print("#########################")
    
    #Function that checks for every input if it contains any important keywords like "help"
    #Returns 1 if it finds any keyword in user input    
    def check_input_event(input):
        if input.lower() == "help":    
                print("Here's a list of all the operations you can use:")
                print("'+' : add")
                print("'-' : substract")
                print("'/' : divide")
                print("'*' : multiply")
                print("''  : get result")
                return 1
                
        
    def program_Loop():
        #Setting important program variables before the main program loop
        program_State = True
        opening_Screen()
        opening_Screen_event_seen = True
        all_Inputs = []
        result = 0
        if opening_Screen_event_seen == False: opening_Screen()
        
        #Main program loop
        while program_State == True: 
            print("Your number: ")
            user_Number = input()
            if check_input_event(user_Number) == 1:
                program_Loop()
            all_Inputs.append(user_Number)
            
            print("Your calculations: ")
            for element in all_Inputs:
                print(element,end="")
            print("")
            
            print("What you want to do:")
            picked_Operation = input()
            if check_input_event(picked_Operation) == 1:
                program_Loop()
                
            match picked_Operation:
                case "+":
                    all_Inputs.append(picked_Operation)
                case "-":
                    all_Inputs.append(picked_Operation)
                case "*":
                    all_Inputs.append(picked_Operation)
                case "/":
                    all_Inputs.append(picked_Operation)
                case "stop":
                    print("Here's your result: ")
                    print(result)
                case "exit":
                    print("you exited the program")
                    program_State = False
                case _:
                    print("wrong argument!")
                    
            print("Your calculations: ")
            for element in all_Inputs:
                print(element,end="")
            print("")
                                        
    program_Loop()
    print("Thank you for using the calculator, see you soon!")
    
if __name__ == "__main__":
    main()