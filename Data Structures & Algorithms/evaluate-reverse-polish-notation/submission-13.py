class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return
        # Reverse Polish Notation (RPN) is a mathematical convention of writing all the operands
        # BEFORE the operator i.e. 3 4 + is an isomorphic translation in the RPN universe of what
        # we perceive 3 + 4 to mean in our 'normal' universe.

        # if i have 2 operands and an operator after it, I need to add both operands to the stack
        # first and then perform the operation by popping values off the stack (First IN Last Out)

        # we dont need to track where the last operator was. as soon as we see an operator,
        # evaluate its operation using all the values on the stack ie pop everything and push the calculated value
        # back onto the stack to be used in the evaluation of the next operation
        
        eval_stack = []
        pos_of_last_operator = None

        for t in tokens:
            if t.lstrip('-').isdigit(): #.isdigit() ONLY works on positive integers!
                int_to_push = int(t)
                eval_stack.append(int_to_push)
            else: # we have hit an operator
                match t:
                    case '+':
                        # for _ in range(2):
                        #     val_on_top_of_stack = eval_stack.pop()
                        #     values_in_operation.append(val_on_top_of_stack) # the value at end of the list forms the base of the operation
                        val_on_top_of_stack = eval_stack.pop()
                        operation_result = val_on_top_of_stack + eval_stack.pop()
                        eval_stack.append(operation_result)
                    case '-':
                        # for _ in range(2):
                        #     val_on_top_of_stack = eval_stack.pop()
                        #     values_in_operation.append(val_on_top_of_stack) # the value at end of the list forms the base of the operation
                        val_on_top_of_stack = eval_stack.pop()
                        operation_result = eval_stack.pop() - val_on_top_of_stack
                        eval_stack.append(operation_result)
                    case '*':                       
                        # for _ in range(2):
                        #     val_on_top_of_stack = eval_stack.pop()
                        #     values_in_operation.append(val_on_top_of_stack) # the value at end of the list forms the base of the operation
                        val_on_top_of_stack = eval_stack.pop()
                        operation_result = eval_stack.pop() * val_on_top_of_stack
                        eval_stack.append(operation_result)
                    case '/':
                        val_on_top_of_stack = eval_stack.pop()
                            # values_in_operation.append(val_on_top_of_stack) # the value at end of the list forms the base of the operation
                            # operation_result = int(values_in_operation[-1] / values_in_operation[0]) # floor division on negative numbers is sticky: -0.04 gets rounded down to -1, NOT 0. use int() for nearest integer instead
                            # the above lines of code was written when I wanted to defend for edge cases where there would be maybe >2 operands in an operation

                        operation_result = int(eval_stack.pop() / val_on_top_of_stack)

                        # for i in values_in_operation[-2::-1]: # caution with negative steps: default start index is -1
                        #     operation_result //= i
                        eval_stack.append(operation_result)

        return eval_stack[-1]                        

