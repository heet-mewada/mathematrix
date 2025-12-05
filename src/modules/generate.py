import random
import numpy
import matplotlib as mlp 


class algebra:
    def findthex_simple()-> list:
        no_terms = random.randint(1,5)
        print(f'{no_terms}, this is the number of terms')
        print("-------------------")
        position_variable = random.randint(1,no_terms)
        print(f'{position_variable}, this is the position of the variable')
        print("-------------------")
        operands = ["+", "-", "*", "/", "^2", "^3"]
        operands_list = []
        if no_terms != 1:
            for x in range(0, no_terms-1): # Generating Operands 
                operation_decision = random.choice(operands)
                operands_list.append(operation_decision)
                if operation_decision == "^2" or operation_decision == "^3": # Power takes an operand spot that needs to be handled
                    operation_decision= random.choice(operands[0:3])
                    operands_list.append(operation_decision)
        index = 0
        for x in operands_list:
            print(f"{x}, index: {index}")
            print("--------------")
            index+=1
        list_of_terms=[ ]
        for x in range(0, no_terms): # Generating the terms 
            constant = random.randint(1,100)
            constant = str(constant)
            list_of_terms.append(constant)
            print(f"{list_of_terms}, this is before variable is assigned")
        answer_equals = 0
        list_of_terms[position_variable-1] = list_of_terms[position_variable-1] + "x"
        print(f"{list_of_terms}, this is list of terms after variable is assigned")
        print("-------------------")
        equation_list=[]
        for x in range(0, no_terms): # Generating the equation
            if x != no_terms:
                print(x) 
                equation_list.append(list_of_terms[x])
                if no_terms != 1 and x != no_terms-1:
                    equation_list.append(operands_list[x])
                    if operands_list[x] == "^2" or operands_list[x] == "^3":
                        equation_list.append(operands_list[x+1])
                        operands_list.remove(operands_list[x+1])
            else:
                print("reached end of list")
        print(f"{equation_list}, this is the equations list")
        print("-------------------")
        return equation_list
    def findthex_quadric() -> list:
        pass


def convert_into_string(equation: list) -> str:
    resultant_equation = ' '.join(equation)
    print(f"{resultant_equation}, this is the equation in string form")
    return resultant_equation


            

        
if __name__ == "__main__":
    x = 1
    while x == 1: #infinite loop for testing
        testing_input= input('what do you wish to test?')
        y = 1
        match testing_input:
            case 'algebra':
                test_object = algebra
                internal_testing= input('what do you wish to test inside algebra class?')
                match internal_testing:
                    case 'simple':
                        equation_listform = test_object.findthex_simple()
                        equation_string = convert_into_string(equation_listform)
                    case 'other':
                        y = 0
                    case _:
                        print("Invalid, exitting")
                        y = 0
            case 'quit':
                print("exitting")
                x = 0
            case _:
                print('invalid, exitting')
                x = 0
