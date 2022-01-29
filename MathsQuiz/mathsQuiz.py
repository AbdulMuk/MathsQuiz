from os import system, name
import random
import math

clear = lambda: system('cls' if name =='nt' else 'clear')

def remove0(num, a, b):

    while num == 0:
        num = random.randint(a, b)
    return num

def checkAns(ans, userAns, incorrectMsg, correct):

    ans = ans.replace(" ", "")
    ans = ans.replace(",", "")
    userAns = userAns.replace(" ", "")
    userAns = userAns.replace(",", "")

    if ans == userAns.lower():
        print("Correct, well done!")
        correct += 1
    else:
        print(incorrectMsg)
    
    print(f"Total correct: {correct}")
    return correct # to keep count. return will be assigned to correct in parent

def arithmetic(a, b, operator):

    clear()
    cont = ""
    qNum = 1
    correct = 0
    op = operator # don't want to reassign operator so mix will work

    while cont.lower() != "b":

        # for mix, choose a random operator
        if operator == "mix":
            ops = ["+", "-", "x", "÷"]
            op = random.choice(ops)

        num1 = random.randint(a, b)
        num2 = random.randint(a, b)

        # sperating divide
        if op == "÷":
            
            # don't want division by zero
            # this is to remove zero from the negative to positive range and from the mix questions
            num1 = remove0(num1, a, b)
            num2 = remove0(num2, a, b)
            
            # num3 and num4 are introduced to avoid decimal division results
            num3 = num1 * num2
            num4 = num2
            ans = num1

        # the rest
        else:
            num3 = num1
            num4 = num2
            if op == "+":
                ans = num3 + num4
            elif op == "-":
                ans = num3 - num4
            elif op == "x":
                ans = num3 * num4
        
        ans = str(ans)
        print(f"Question {qNum}")
        userAns = input(f"{num3} {op} {num4} = ")
        incorrectMsg = f"Incorrect, {num3} {op} {num4} = {ans}"

        # check ans
        correct = checkAns(ans, userAns, incorrectMsg, correct)
        cont = input("\nPress any key to continue or b for back: ")
        print()
        qNum += 1

def arithmeticMenu():
    
    userChoice = ""
    while userChoice.lower() != "b":
        clear()
        
        difficulty = ["Easy 0 to 10", "Medium 0 to 100", "Hard -100 to 100"]
        qType = ["Addition", "Subtraction", "Multiplication", "Division", "Mix"]
        print("Arithmetic Menu\n")
        print(f"{difficulty[0]:24}{difficulty[1]:24}{difficulty[2]:24}\n")
        print(f"1.  {qType[0]:20}6.  {qType[0]:20}11.  {qType[0]:20}")
        print(f"2.  {qType[1]:20}7.  {qType[1]:20}12.  {qType[1]:20}")
        print(f"3.  {qType[2]:20}8.  {qType[2]:20}13.  {qType[2]:20}")
        print(f"4.  {qType[3]:20}9.  {qType[3]:20}14.  {qType[3]:20}")
        print(f"5.  {qType[4]:20}10. {qType[4]:20}15.  {qType[4]:20}")
        print("\nPress 1 - 15 or b for back\n")
        userChoice = input("Choose your question type: ")
        
        if userChoice == "1": arithmetic(0, 10, "+")

        elif userChoice == "2": arithmetic(0, 10, "-")

        elif userChoice == "3": arithmetic(0, 10, "x")

        elif userChoice == "4": arithmetic(1, 10, "÷")

        elif userChoice == "5": arithmetic(0, 10, "mix")

        elif userChoice == "6": arithmetic(0, 100, "+")

        elif userChoice == "7": arithmetic(0, 100, "-")

        elif userChoice == "8": arithmetic(0, 100, "x")

        elif userChoice == "9": arithmetic(1, 100, "÷")

        elif userChoice == "10": arithmetic(0, 100, "mix")

        elif userChoice == "11": arithmetic(-100, 100, "+")

        elif userChoice == "12": arithmetic(-100, 100, "-")

        elif userChoice == "13": arithmetic(-100, 100, "x")

        elif userChoice == "14": arithmetic(-100, 100, "÷")

        elif userChoice == "15": arithmetic(-100, 100, "mix")

def generalQuiz():

    # question and answer pairs as a list
    generalQs = [
        ["How many degrees are there in a straight line", "180"],
        ["How many degrees are there in a right angle", "90"],
        ["How many degrees are there in a complete circle", "360"],
        ["What is the sum of the angles inside a triangle", "180"],
        ["What is the sum of the angles inside a square", "360"],
        ["What is the sum of the angles inside a pentagon", "540"],
        ["What is the sum of the exterior angles of any polygon", "360"],
        ["How many centimeters are there in a meter", "100"],
        ["How many millimeters are there in a meter", "1,000"],
        ["How many millimeters are there in a centimeter", "10"],
        ["How many meters are there in a kilometer", "1,000"],
        ["How many milligrams are there in a gram", "1,000"],
        ["How many milligrams are there in a kilogram", "1,000,000"],
        ["How many micrograms are there in a gram", "1,000,000"],
        ["How many centilitres are there in a litre", "100"],
        ["How many millilitres are there in a centilitre", "10"],
        ["How many inches are there in a foot", "12"],
        ["How many feet are there in a yard", "3"],
        ["What is the longest side in a right angle triangle called", "hypotenuse"],
        ["What is the side next to the angle in a right angle triangle called", "adjacent"],
        ["What is the side opposite the angle in a right angle triangle called", "opposite"],
        ["What is a regular triangle called (all sides the same, all angles the same)", "equilateral triangle"],
        ["What is a triangle with 2 sides and 2 angles the same called", "isosceles triangle"],
        ["What is a quadrilateral with 2 pairs of parallel sides called", "parallelogram"],
        ["What is a regular quadrilateral called (all sides the same, all angles the same)", "square"],
        ["How many sides does a triangle have", "3"],
        ["How many sides does a quadrilateral have", "4"],
        ["How many sides does a pentagon have", "5"],
        ["How many sides does a hexagon have", "6"],
        ["What do you call a shape with 10 sides", "decagon"],
        ["What do you call a shape with 8 sides", "octagon"],
        ["What do you call the distance around a shape", "perimeter"],
        ["What do you call the distance around a cirlce", "circumference"],
        ["What is the line from the center of a cirlce to the edge called", "radius"],
        ["What is the line from one side of a cirlce to the other side passing through the centre called", "diameter"],
        ["Speed = distance divided by what", "time"],
        ["Circumference = 2 times pi times what", "radius"]
    ]

    clear()
    print("Instructions: Type the answers without any units. Commas and spaces will be ignored.")
    input("\nPress any key to continue. ")

    qNum = 1
    correct = 0
    cont = ""

    while cont.lower() != "b":

        # choose a random list from generalQs, index 0 is the question, index 1 is the answer
        question = random.choice(generalQs)
        print(f"\nQuestion {qNum}")
        userAns = input(f"{question[0]}? ")
        incorrectMsg = f"Incorrect, the correct answer is: {question[1]}"

        # check answer
        correct = checkAns(question[1], userAns, incorrectMsg, correct)
        cont = input("\nPress any key to continue or b for back: ")
        qNum += 1

# argument is a list, removes all zero terms
# removes number if number is 1 or -1, leaving just the sign and the variable
# if number term (no var) then 1 and -1 are not removed
def checkTerm(term):

    if term[0] == 0:
        return ""

    elif term[0] == 1:
        if term[1] == "":
            return f"+ 1 "
        else:
            return f"+ {term[1]} "

    elif term[0] == -1:
        if term[1] == "":
            return f"- 1 "
        else:
            return f"- {term[1]} "

    else:
        if term[0] > 0:
            return f"+ {term[0]}{term[1]} "
        else:
            return f"- {term[0] * -1}{term[1]} " # space between - sign and number

# takes a 3 tier list and outputs a list
def makeListCT(qList):

    newList = []

    for inner1 in qList: # list of terms
        newStr = ""

        for inner2 in inner1: # list of coeffficient and term
            # use checkTerm to make a string from inner-most list
            # concat all terms to make 1 string
            newStr += checkTerm(inner2)
        
        # strip the leading + sign and any whitespace
        # make a new q and a list
        newStr = newStr.lstrip("+")
        newStr = newStr.strip()
        newList.append(newStr)

    return newList

replaceCarr = lambda userAns: userAns.replace("^2", "²")

def collectTerms(type, letters):

    a = random.choice(letters)
    b = random.choice(letters)
    c = random.choice(letters)
    d = random.choice(letters)

    # if any letters are the same, pick again
    while a == b or a == c or a == d or b == c or b == d or c == d:
        a = random.choice(letters)
        b = random.choice(letters)
        c = random.choice(letters)
        d = random.choice(letters)

    num1 = random.randint(-9, 9)
    num2 = random.randint(-9, 9)
    num3 = random.randint(-9, 9)
    num4 = random.randint(-9, 9)
    num5 = random.randint(-9, 9)
    num6 = random.randint(-9, 9)
    num7 = random.randint(-9, 9)
    num8 = random.randint(-9, 9)
    # remove 0
    num1 = remove0(num1, -9, 9)
    num2 = remove0(num2, -9, 9)
    num3 = remove0(num3, -9, 9)
    num4 = remove0(num4, -9, 9)
    num5 = remove0(num5, -9, 9)
    num6 = remove0(num6, -9, 9)
    num7 = remove0(num7, -9, 9)
    num8 = remove0(num8, -9, 9)

    # question and answer list stored as a 4 tier list
    # q and a's are stored as lists
    # each q and a is a list of terms
    # each term is a list of coefficient and term
    # will make every permutation of the answer list so users can answer 3a + 5b or 5b + 3a
    # makeListCT function will be used to turn this into meaningful question and answer expressions
    if type == "s":

        q1 = [[num1, a], [num2, b], [num3, a], [num4, b]]
        a1 = [[num1 + num3, a], [num2 + num4, b]]
        l1 = [[i, j] for i in a1 for j in a1 if (i != j)]
        l1.insert(0, q1)

        q2 = [[num1, a], [num2, ""], [num3, b], [num4, b], [num5, a], [num6, ""]]
        a2 = [[num1 + num5, a], [num3 + num4, b], [num2 + num6, ""]]
        l2 = [[i, j, k] for i in a2 for j in a2 for k in a2 if (i != j and i != k and j != k)]
        l2.insert(0, q2)

        q3 = [[num1, a], [num2, b], [num3, a], [num4, b], [num5, a], [num6, b]]
        a3 = [[num1 + num3 + num5, a], [num2 + num4 + num6, b]]
        l3 = [[i, j] for i in a3 for j in a3 if (i != j)]
        l3.insert(0, q3)

        q4 = [[num1, a], [num2, b], [num3, ""], [num4, c], [num5, a], [num6, b], [num7, ""], [num8, c]]
        a4 = [[num1 + num5, a], [num2 + num6, b], [num4 + num8, c], [num3 + num7, ""]]
        l4 = [[i, j, k, l] for i in a4 for j in a4 for k in a4 for l in a4 if (i != j and i != k and i != l and j != k and j != l and k != l)]
        l4.insert(0, q4)

        q5 = [[num1, a], [num2, a], [num3, b], [num4, c], [num5, b], [num6, c]]
        a5 = [[num1 + num2, a], [num3 + num5, b], [num4 + num6, c]]
        l5 = [[i, j, k] for i in a5 for j in a5 for k in a5 if (i != j and i != k and j != k)]
        l5.insert(0, q5)

        q6 = [[num1, a], [num2, b], [num3, d], [num4, c], [num5, d], [num6, b], [num7, a], [num8, c]]
        a6 = [[num1 + num7, a], [num2 + num6, b], [num4 + num8, c], [num3 + num5, d]]
        l6 = [[i, j, k, l] for i in a6 for j in a6 for k in a6 for l in a6 if (i != j and i != k and i != l and j != k and j != l and k != l)]
        l6.insert(0, q6)

        q7 = [[num1, a], [num2, b], [num3, a], [num4, c], [num5, b], [num6, a], [num7, c], [num8, b]]
        a7 = [[num1 + num3 + num6, a], [num2 + num5 + num8, b], [num4 + num7, c]]
        l7 = [[i, j, k] for i in a7 for j in a7 for k in a7 if (i != j and i != k and j != k)]
        l7.insert(0, q7)

        questions4dList = [l1, l2, l3, l4, l5, l6, l7]

    else:

        q1 = [[num1, f"{a}²"], [num2, a], [num3, f"{a}²"], [num4, a]]
        a1 = [[num1 + num3, f"{a}²"], [num2 + num4, a]]
        l1 = [[i, j] for i in a1 for j in a1 if (i != j)]
        l1.insert(0, q1)

        q2 = [[num1, f"{a}²"], [num2, ""], [num3, a], [num4, a], [num5, f"{a}²"], [num6, ""]]
        a2 = [[num1 + num5, f"{a}²"], [num3 + num4, a], [num2 + num6, ""]]
        l2 = [[i, j, k] for i in a2 for j in a2 for k in a2 if (i != j and i != k and j != k)]
        l2.insert(0, q2)

        q3 = [[num1, f"{a}²"], [num2, a], [num3, f"{a}²"], [num4, a], [num5, f"{a}²"], [num6, a]]
        a3 = [[num1 + num3 + num5, "a²"], [num2 + num4 + num6, "a"]]
        l3 = [[i, j] for i in a3 for j in a3 if (i != j)]
        l3.insert(0, q3)

        q4 = [[num1, a], [num2, f"{b}²"], [num3, ""], [num4, b], [num5, a], [num6, f"{b}²"], [num7, ""], [num8, b]]
        a4 = [[num2 + num6, f"{b}²"], [num1 + num5, a], [num4 + num8, b], [num3 + num7, ""]]
        l4 = [[i, j, k, l] for i in a4 for j in a4 for k in a4 for l in a4 if (i != j and i != k and i != l and j != k and j != l and k != l)]
        l4.insert(0, q4)

        q5 = [[num1, f"{a}²"], [num2, f"{a}²"], [num3, a], [num4, ""], [num5, a], [num6, ""]]
        a5 = [[num1 + num2, f"{a}²"], [num3 + num5, "x"], [num4 + num6, ""]]
        l5 = [[i, j, k] for i in a5 for j in a5 for k in a5 if (i != j and i != k and j != k)]
        l5.insert(0, q5)

        q6 = [[num1, f"{a}²"], [num2, f"{b}²"], [num3, b], [num4, a], [num5, b], [num6, f"{b}²"], [num7, f"{a}²"], [num8, a]]
        a6 = [[num1 + num7, f"{a}²"], [num2 + num6, f"{b}²"], [num4 + num8, a], [num3 + num5, b]]
        l6 = [[i, j, k, l] for i in a6 for j in a6 for k in a6 for l in a6 if (i != j and i != k and i != l and j != k and j != l and k != l)]
        l6.insert(0, q6)

        q7 = [[num1, f"{a}²"], [num2, a], [num3, f"{a}²"], [num4, ""], [num5, a], [num6, f"{a}²"], [num7, ""], [num8, a]]
        a7 = [[num1 + num3 + num6, f"{a}²"], [num2 + num5 + num8, a], [num4 + num7, ""]]
        l7 = [[i, j, k] for i in a7 for j in a7 for k in a7 if (i != j and i != k and j != k)]
        l7.insert(0, q7)

        questions4dList = [l1, l2, l3, l4, l5, l6, l7]

    # choose a random list from questions, index 0 is the question, the rest are answers
    question3dList = random.choice(questions4dList)
    question = makeListCT(question3dList)
    return question

# not for 1st term, + - before num
checkNum = lambda num: f"+ {num}" if num > 0 else f"- {num * -1}"

# for coefficients, removes num if 1 leaving + -
def check1(num):

    if num == 1:
        return f""
    elif num == -1:
        return f"-"
    else:
        return num

# not for 1st term, does both the above
def checkBoth(num):

    if num > 0:
        if num == 1:
            return f"+ "
        else:
            return f"+ {num}"
    else:
        if num == -1:
            return f"- "
        else:
            return f"- {num * -1}"

def expBracket(type, letters):

    x = random.choice(letters)
    num1 = random.randint(-9, 9)
    num2 = random.randint(-9, 9)
    num3 = random.randint(-9, 9)
    num4 = random.randint(-9, 9)

    # remove 0
    num1 = remove0(num1, -9, 9)
    num2 = remove0(num2, -9, 9)
    num3 = remove0(num3, -9, 9)
    num4 = remove0(num4, -9, 9)

    # question and answers as a list
    if type == "s":
        questions = [
            [f"{num1}({x} {checkNum(num2)})",
            f"{check1(num1)}{x} {checkNum(num1 * num2)}",
            f"{num1 * num2} {checkBoth(num1)}{x}"],

            [f"{num1}({check1(num2)}{x} {checkNum(num3)})",
            f"{check1(num1 * num2)}{x} {checkNum(num1 * num3)}",
            f"{num1 * num3} {checkBoth(num1 * num2)}{x}"],

            [f"{num1}({num2} + {x})",
            f"{check1(num1)}{x} {checkNum(num1 * num2)}",
            f"{num1 * num2} {checkBoth(num1)}{x}"],

            [f"{num1}({num2} - {x})",
            f"{check1(num1 * -1)}{x} {checkNum(num1 * num2)}",
            f"{num1 * num2} {checkBoth(num1 * -1)}{x}"],

            [f"{num1}({num2} {checkBoth(num3)}{x})",
            f"{check1(num1 * num3)}{x} {checkNum(num1 * num2)}",
            f"{num1 * num2} {checkBoth(num1 * num3)}{x}"],

            [f"{x}({check1(num1)}{x} {checkNum(num2)})",
            f"{check1(num1)}{x}² {checkBoth(num2)}{x}",
            f"{check1(num2)}{x} {checkBoth(num1)}{x}²"],

            [f"{check1(num1)}{x}({check1(num2)}{x} {checkNum(num3)})",
            f"{check1(num1 * num2)}{x}² {checkBoth(num1 * num3)}{x}",
            f"{check1(num1 * num3)}{x} {checkBoth(num1 * num2)}{x}²"]
        ]
    else:
        questions = [
            [f"({x} {checkNum(num1)})({x} {checkNum(num2)})",
            f"{x}² {checkTerm([num1 + num2, f'{x}'])}{checkNum(num1 * num2)}",
            f"{x}² {checkNum(num1 * num2)} {checkTerm([num1 + num2, f'{x}'])}",
            f"{checkTerm([num1 + num2, f'{x}'])}+ {x}² {checkNum(num1 * num2)}",
            f"{checkTerm([num1 + num2, f'{x}'])}{checkNum(num1 * num2)} + {x}²",
            f"{num1 * num2} + {x}² {checkTerm([num1 + num2, f'{x}'])}",
            f"{num1 * num2} {checkTerm([num1 + num2, f'{x}'])}+ {x}²"],

            [f"({num1} + {x})({num2} + {x})",
            f"{x}² {checkTerm([num1 + num2, f'{x}'])}{checkNum(num1 * num2)}",
            f"{x}² {checkNum(num1 * num2)} {checkTerm([num1 + num2, f'{x}'])}",
            f"{checkTerm([num1 + num2, f'{x}'])}+ {x}² {checkNum(num1 * num2)}",
            f"{checkTerm([num1 + num2, f'{x}'])}{checkNum(num1 * num2)} + {x}²",
            f"{num1 * num2} + {x}² {checkTerm([num1 + num2, f'{x}'])}",
            f"{num1 * num2} {checkTerm([num1 + num2, f'{x}'])}+ {x}²"],

            [f"({x} {checkNum(num1)})²",
            f"{x}² {checkBoth(2 * num1)}{x} {checkNum(num1 ** 2)}",
            f"{x}² {checkNum(num1 ** 2)} {checkBoth(2 * num1)}{x}",
            f"{check1(2 * num1)}{x} + {x}² {checkNum(num1 ** 2)}",
            f"{check1(2 * num1)}{x} {checkNum(num1 ** 2)} + {x}²",
            f"{num1 ** 2} + {x}² {checkBoth(2 * num1)}{x}",
            f"{num1 ** 2} {checkBoth(2 * num1)}{x} + {x}²"],

            [f"({check1(num1)}{x} {checkNum(num2)})²",
            f"{check1(num1 ** 2)}{x}² {checkBoth(2 * num1 * num2)}{x} {checkNum(num2 ** 2)}",
            f"{check1(num1 ** 2)}{x}² {checkNum(num2 ** 2)} {checkBoth(2 * num1 * num2)}{x}",
            f"{check1(2 * num1 * num2)}{x} {checkBoth(num1 ** 2)}{x}² {checkNum(num2 ** 2)}",
            f"{check1(2 * num1 * num2)}{x} {checkNum(num2 ** 2)} {checkBoth(num1 ** 2)}{x}²",
            f"{num2 ** 2} {checkBoth(num1 ** 2)}{x}² {checkBoth(2 * num1 * num2)}{x}",
            f"{num2 ** 2} {checkBoth(2 * num1 * num2)}{x} {checkBoth(num1 ** 2)}{x}²"],

            [f"({check1(num1)}{x} {checkNum(num2)})({check1(num3)}{x} {checkNum(num4)})",
            f"{check1(num1 * num3)}{x}² {checkTerm([num1 * num4 + num2 * num3, f'{x}'])}{checkNum(num2 * num4)}",
            f"{check1(num1 * num3)}{x}² {checkNum(num2 * num4)} {checkTerm([num1 * num4 + num2 * num3, f'{x}'])}",
            f"{checkTerm([num1 * num4 + num2 * num3, f'{x}'])}{checkBoth(num1 * num3)}{x}² {checkNum(num2 * num4)}",
            f"{checkTerm([num1 * num4 + num2 * num3, f'{x}'])}{checkNum(num2 * num4)} {checkBoth(num1 * num3)}{x}²",
            f"{num2 * num4} {checkBoth(num1 * num3)}{x}² {checkTerm([num1 * num4 + num2 * num3, f'{x}'])}",
            f"{num2 * num4} {checkTerm([num1 * num4 + num2 * num3, f'{x}'])}{checkBoth(num1 * num3)}{x}²"]
        ]

    # choose a random list from questions, index 0 is the question, the rest are answers
    question = random.choice(questions)
    return question

def fctBracket(type, letters):

    x = random.choice(letters)
    num1 = random.randint(-9, 9)
    num2 = random.randint(-9, 9)

    # remove 0
    num2 = remove0(num2, -9, 9)

    # remove 0, 1 and -1
    while num1 == 0 or num1 == 1 or num1 == -1:
        num1 = random.randint(-9, 9)

    # question and answers as a list
    if type == "s":
        questions = [
            [f"{num1}{x} {checkNum(num1 * num2)}",
            f"{num1}({x} {checkNum(num2)})",
            f"{num1}({num2} + {x})",
            f"{num1 * -1}(-{x} {checkNum(num2 * -1)})",
            f"{num1 * -1}({num2 * -1} - {x})"],

            [f"{num1 * 2}{x} {checkNum(num1 * 3)}",
            f"{num1}(2{x} + 3)",
            f"{num1}(3 + 2{x})",
            f"{num1 * -1}(-2{x} - 3)",
            f"{num1 * -1}(-3 - 2{x})"],

            [f"{num1 * 3}{x} {checkNum(num1 * 2)}",
            f"{num1}(3{x} + 2)",
            f"{num1}(2 + 3{x})",
            f"{num1 * -1}(-3{x} - 2)",
            f"{num1 * -1}(-2 - 3{x})"],

            [f"{num1 * 3}{x} {checkNum(num1 * 4)}",
            f"{num1}(3{x} + 4)",
            f"{num1}(4 + 3{x})",
            f"{num1 * -1}(-3{x} - 4)",
            f"{num1 * -1}(-4 - 3{x})"],

            [f"{num1 * 3}{x} {checkNum(num1 * 5)}",
            f"{num1}(3{x} + 5)",
            f"{num1}(5 + 3{x})",
            f"{num1 * -1}(-3{x} - 5)",
            f"{num1 * -1}(-5 - 3{x})"],

            [f"{num1 * num2}{x} {checkNum(num1)}",
            f"{num1}({check1(num2)}{x} + 1)",
            f"{num1}(1 {checkBoth(num2)}{x})",
            f"{num1 * -1}({check1(num2 * -1)}{x} - 1)",
            f"{num1 * -1}(-1 {checkBoth(num2 * -1)}{x})"],

            [f"{num1 * num2}{x} {checkNum(num1 * 2)}",
            f"{num1}({check1(num2)}{x} + 2)",
            f"{num1}(2 {checkBoth(num2)}{x})",
            f"{num1 * -1}({check1(num2 * -1)}{x} - 2)",
            f"{num1 * -1}(-2 {checkBoth(num2 * -1)}{x})"],

            [f"{num1 * num2}{x} {checkNum(num1 * 5)}",
            f"{num1}({check1(num2)}{x} + 5)",
            f"{num1}(5 {checkBoth(num2)}{x})",
            f"{num1 * -1}({check1(num2 * -1)}{x} - 5)",
            f"{num1 * -1}(-5 {checkBoth(num2 * -1)}{x})"],

            [f"{num1}{x}² + {x}",
            f"{x}({num1}{x} + 1)",
            f"{x}(1 {checkNum(num1)}{x})",
            f"-{x}({num1 * -1}{x} - 1)",
            f"-{x}(-1 {checkNum(num1 * -1)}{x})"],

            [f"{num1}{x}² - {x}",
            f"{x}({num1}{x} - 1)",
            f"{x}(-1 {checkNum(num1)}{x})",
            f"-{x}({num1 * -1}{x} + 1)",
            f"-{x}(1 {checkNum(num1 * -1)}{x})"],

            [f"{x}² {checkNum(num1)}{x}",
            f"{x}({x} {checkNum(num1)})",
            f"{x}({num1} + {x})",
            f"-{x}(-{x} {checkNum(num1 * -1)})",
            f"-{x}({num1 * -1} - {x})"],

            [f"{num1}{x}² {checkNum(num1 * num2)}{x}",
            f"{num1}{x}({x} {checkNum(num2)})",
            f"{num1}{x}({num2} + {x})",
            f"{num1 * -1}{x}(-{x} {checkNum(num2 * -1)})",
            f"{num1 * -1}{x}({num2 * -1} - {x})"],
        ]
    else:
        questions = [
            [f"{x}² {checkTerm([num1 + num2, f'{x}'])}{checkNum(num1 * num2)}",
            f"({x} {checkNum(num1)})({x} {checkNum(num2)})",
            f"({num1} + {x})({x} {checkNum(num2)})",
            f"({x} {checkNum(num1)})({num2} + {x})",
            f"({num1} + {x})({num2} + {x})",
            f"({x} {checkNum(num2)})({x} {checkNum(num1)})",
            f"({num2} + {x})({x} {checkNum(num1)})",
            f"({x} {checkNum(num2)})({num1} + {x})",
            f"({num2} + {x})({num1} + {x})"],

            [f"{x}² {checkNum(2 * num1)}{x} {checkNum(num1 ** 2)}",
            f"({x} {checkNum(num1)})²",
            f"({num1} + {x})²",
            f"({x} {checkNum(num1)})({x} {checkNum(num1)})",
            f"({num1} + {x})({x} {checkNum(num1)})",
            f"({x} {checkNum(num1)})({num1} + {x})",
            f"({num1} + {x})({num1} + {x})"]
        ]

    # choose a random list from questions, index 0 is the question, the rest are answers
    question = random.choice(questions)
    return question

def algebra(cat, type):

    clear()
    cont = ""
    qNum = 1
    correct = 0
    letters = ["a", "b", "c", "d", "e", "n", "m", "p", "q", "r", "t", "x", "y", "z"]

    print("Instructions:\n")
    print("If a coefficient = 1 then only write the variable\n")
    print("e.g. a + 2b - c\n")
    print("To write squared, use ^2\n")
    print("e.g. 3x^2 - 4x + 6\n")
    if cat == "q":
        print("For Quadratic factorisation, only use 2 brackets\n")
        print("These will not be accepted:  2(x + 1)(x + 2) ,  -(n + 2)(n + 3)\n")
    print("Not following the above will result in incorrect answer even if it's correct\n")
    input("Press any key to continue ")

    while cont.lower() != "b":
        
        if cat == "c":
            question = collectTerms(type, letters)
        elif cat == "e":
            question = expBracket(type, letters)
        else:
            question = fctBracket(type, letters)

        print(f"\nQuestion {qNum}")
        userAns = input(f"{question[0]} = ")
        incorrectMsg = f"Incorrect, the correct answer is: {question[1]}"

        # format userAns
        userAns = userAns.replace(" ", "")
        userAns = replaceCarr(userAns)
        userAns = userAns.lower()
        userAns = userAns.lstrip("+")

        # check if userAns matches any of the answers
        checkCorrect = False
        question.pop(0) # remove question leaving only answers
        for ans in question:
            ans = ans.replace(" ", "")
            ans = ans.lstrip("+")
            checkCorrect = checkCorrect or userAns == ans
            if checkCorrect: break

        if checkCorrect:
            print("Correct, well done!")
            correct += 1
        else:
            print(incorrectMsg)
        
        print(f"Total correct: {correct}")
        cont = input("\nPress any key to continue or b for back: ")
        qNum += 1

def algebraMenu():

    userChoice = ""
    while userChoice.lower() != "b":
        clear()

        heading = ["Linear (single brackets)", "Quadratic (double brackets)"]
        qType = ["Collecting terms", "Expanding brackets", "Factorising"]
        print("Algebra Menu\n")
        print(f"{heading[0]:35}{heading[1]:35}\n")
        print(f"1. {qType[0]:32}4. {qType[0]:32}")
        print(f"2. {qType[1]:32}5. {qType[1]:32}")
        print(f"3. {qType[2]:32}6. {qType[2]:32}")
        print("\nPress 1 - 6, or b for back.\n")
        userChoice = input("Choose your category: ")

        if userChoice == "1": algebra("c", "s")

        elif userChoice == "2": algebra("e", "s")

        elif userChoice == "3": algebra("f", "s")
        
        elif userChoice == "4": algebra("c", "q")
        
        elif userChoice == "5": algebra("e", "q")

        elif userChoice == "6": algebra("f", "q")

def multiples(num, b):

    multiplesList = []
    for i in range(1, b):
        multiplesList.append(num * i)

    return multiplesList

def factors(num):

    factorsList = []
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            factorsList.append(i)
            if num / i != i:
                factorsList.append(int(num / i))

    factorsList.sort()
    return factorsList

def mfQuestions(cat):

    clear()
    cont = ""
    qNum = 1
    correct = 0

    print("Instructions:\n")
    print(f"Enter all the {cat} seperated by spaces\n")
    input("Press any key to continue ")

    while cont.lower() != "b":
        print(f"\nQuestion {qNum}")
        num = random.randint(1, 100)

        if cat == "multiples":
            ans = [str(x) for x in multiples(num, 11)]
            userAns = input(f"List the first ten multiple of {num}: ").split()

        elif cat == "factors":
            ans = [str(x) for x in factors(num)]
            userAns = input(f"List all the factors of {num}: ").split()

        # check answer
        if set(ans) == set(userAns):
            print("Correct, well done!")
            correct += 1
        else:
            print("Incorrect, the correct answer is:", *ans, sep = " ")
        
        print(f"Total correct: {correct}")
        
        cont = input("\nPress any key to continue or b for back: ")
        qNum += 1

def numbersMenu():

    userChoice = ""
    while userChoice.lower() != "b":
        clear()
        
        print("Numbers Menu\n")
        print("1. Multiples")
        print("2. Factors")
        print("\nPress 1 - 2, or b for back.\n")
        userChoice = input("Choose your category: ")

        if userChoice == "1": mfQuestions("multiples")

        elif userChoice == "2": mfQuestions("factors")

def mulTable():

    clear()

    for n in range(1, 13):
        mulList = []
        for m in range(1, 13):
            mulList.append(f'{n*m:3}')
        print(*mulList)
    input("\nPress any key to continue ")

def mfInfo(cat):

    clear()

    while True:
        num = input(f"\nEnter a number to show it's {cat} or press b for back: ")
        if num.lower() == "b": break

        try:
            num = int(num)
        except:
            print("\nPlease enter a whole number")
            continue

        # program hangs if number gets too large
        if num > 1000000000:
            print("\nPlease enter a lower number")
            num = str(num)
            continue
        elif num < 1 and cat == "factors":
            print("\nPlease enter a whole number greater than zero")
            num = str(num)
            continue

        if cat == "multiples":
            numList = multiples(num, 21)
        else:
            numList = factors(num)
        
        print(*numList, sep = ", ")
        num = str(num)

def mainMenu():
    
    userChoice = ""
    while userChoice.lower() != "e":
        clear()

        heading = ["Questions", "Information"]
        questionCat = ["General quiz", "Arithmetic Operations", "Numbers", "Algebra"]
        infoCat = ["Multiplication table", "Multiples of numbers", "Factors of numbers"]
        print("Main Menu\n")
        print(f"{heading[0]:33}{heading[1]:33}\n")
        print(f"1. {questionCat[0]:30}5. {infoCat[0]:30}")
        print(f"2. {questionCat[1]:30}6. {infoCat[1]:30}")
        print(f"3. {questionCat[2]:30}7. {infoCat[2]:30}")
        print(f"4. {questionCat[3]:30}")
        print("\nPress 1 - 7, or e to exit.\n")
        userChoice = input("Choose your category: ")

        if userChoice == "1": generalQuiz()

        elif userChoice == "2": arithmeticMenu()

        elif userChoice == "3": numbersMenu()

        elif userChoice == "4": algebraMenu()

        elif userChoice == "5": mulTable()

        elif userChoice == "6": mfInfo("multiples")

        elif userChoice == "7": mfInfo("factors")

# main
print("Welcome to Maths Quiz\n\n")
print("Created by: Abdul Mukit. © 2022\n")
input("Press any key to continue. ")
mainMenu()
