# John Marsland, Last updated 9/19/2025
def arithmetic_arranger(show_answers=True):
    question = 1
    while question != 0:
        question = input("Enter the problems you would like to solve (+, -, *, /) in the following format:\n21 + 3, 40 - 10, 80 + 20\nEnter 0 to exit\nProblem: ")
        if question == str(0):
            return "Thank you for using the calculator!"
        problems = question.split(',')
    
        # Splits problems into usable parts
        groups = [group.split() for group in problems]
    
        # Error checker
        if len(problems) > 5:
            return "Error: Too many problems."
    
        # Loop checking for content errors
        for group in groups:
            # Check Operator
            if group[1] != '+' and group[1] != '-' and group[1] != '*' and group[1] != '/':
                return "Error: Choose a valid operation: '+', '-', '*', '/'."
            
            # Check digits only
            elif not group[0].isdigit() or not group[2].isdigit():
                return "Error: Numbers must only contain digits."
            
            # Check length of digits
            elif len(group[0]) > 4 or len(group[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
    
        # Sections the problems into top, operator, and bottom
        # While looping also regularizes the spacing of the     
        # operands
        tops = []
        operators = []
        bottoms = []
        for group in groups:
            # Normalization
            top_len = len(group[0])
            bot_len = len(group[2])
            dif = top_len - bot_len
            if dif > 0:
                group[2] = ' '*dif + group[2]
            elif dif < 0:
                group[0] = ' '*abs(dif) + group[0]
            # Sectioner
            tops.append(group[0])
            operators.append(group[1])
            bottoms.append(group[2])
    
        # Structures the format of the printed content
        top = ''
        bottom = '' 
        dashes = ''
        
        for i, (t, o, b) in enumerate(zip(tops, operators, bottoms)):
            if i+1 < len(tops):
                top += f'  {t}    '
                bottom += f'{o} {b}    '
                dashes += '-'*(2+len(b)) + '    '
            else:
                top += f'  {t}'
                bottom += f'{o} {b}'
                dashes += '-'*(2+len(b))
        problems = f'{top}\n{bottom}\n{dashes}'
    
        # In case answers are shown
        answer_list = []
        answer_string = ''
        i = 1
        if show_answers:
            for t, o, b in zip(tops, operators, bottoms):
                op1 = int(t)
                op2 = int(b)
                if o == '+':
                    answer = str(op1 + op2)
                elif o == '-':
                    answer = str(op1 - op2)
                elif o == '*':
                    answer = str(op1 * op2)
                elif o == '/':
                    answer = str(op1 / op2)
        
                dif = 2+len(b) - len(answer)
                answer = ' '*dif + answer
                if i < len(tops):
                    answer_string += f'{answer}    '
                else: 
                    answer_string += f'{answer}'
                i += 1
            problems += f'\n{answer_string}\n'
        print(problems)
    problems = []
print(f'\n{arithmetic_arranger()}')
