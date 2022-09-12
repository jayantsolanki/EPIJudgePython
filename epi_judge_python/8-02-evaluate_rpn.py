from typing import List
from test_framework import generic_test
import math
"""
Write a program to evaluate postfix expression (Reverse Polish Notation)
Example: "1729", "3,4,+,2,*,1,+", "1,1,+,-2,*", "-641, 6, /, 28, /"
Logic: process subexpressions, keeping partial values in a stack
Time: O(n)
"""
def evaluate(expression: str) -> int:

    intermediate_results: List[int] = []
    delimiter = ','
    operators = {#nice way to organize multiple function
        '+': lambda y, x: x + y,#notice the order of x and y here, importnt
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        # '/': lambda y, x: x // y
        '/': lambda y, x: math.ceil(x / y) if (x / y) < 0  else math.floor(x / y) # use this
    }

    for token in expression.split(delimiter):# comma
        if token in operators:
            intermediate_results.append(operators[token](
                intermediate_results.pop(), intermediate_results.pop()))# pop two elements from stack and evaluate then push it back
        else:  # token is a number.
            intermediate_results.append(int(token))
    return intermediate_results[-1]

# variant 1
"""
program for evaluating prefix expression
eg: "-,/,*,20,*,50,+,3,6,300,2"
Logic: read it backwards and start putting it into stack and evaluate
"""
def prefix_evaluate(expression: str) -> int:

    intermediate_results: List[int] = []
    delimiter = ','
    operators = {
        '+': lambda x, y: x + y,#reverses here too
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y#only concern with integer
    }
    # token = 
    for token in expression.split(delimiter)[::-1]:# comma, also read backwards
        print(token)
        print(intermediate_results)
        if token in operators:
            intermediate_results.append(operators[token](
                intermediate_results.pop(), intermediate_results.pop()))# pop two elements from stack and evaluate then push it back
        else:  # token is a number.
            intermediate_results.append(int(token))
    return intermediate_results[-1]
prefix_evaluate('-,/,*,20,*,50,+,3,6,300,2')
prefix_evaluate('-,-2,123')

#variant 2 infix to postfix
"""
https://runestone.academy/ns/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
Create an empty stack called opstack for keeping operators. Create an empty list for output.

Convert the input infix string to a list by using the string method split.

Scan the token list from left to right.

If the token is an operand, append it to the end of the output list.

If the token is a left parenthesis, push it on the opstack.

If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.

If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.

When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.
"""
class Stack:#simple
    def __init__(self):
         
        # main stack
        self.mainStack = []

    def empty(self):
        return len(self.mainStack) == 0

    def push(self, x):
        self.mainStack.append(x)

    def peek(self):
        return  self.mainStack[-1]          
 
    def pop(self):
        if self.empty():#check if empty
            return None
        return(self.mainStack.pop())
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:#other operators
            while (not opStack.empty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('8-02-evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
