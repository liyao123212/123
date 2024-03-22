
class Stack:
    def __init__(self):
        self.items = []
    def pop(self):
        return self.items.pop()
    def get_length(self):
        return len(self.items)

    def push(self, elem):
        return self.items.append(elem)
def Match_blankets(string):
    stack = Stack()
    stack2=Stack()
    string_array = [""] * len(string)
    match_dict = {")": "(", "]": "[", "}": "{"}
    num=0
    for i in string:
        if i not in {"(","[","{",")", "]", "}"}:
            string_array[num]=" "
        if i in {"(","{","["}:
            stack2.push(num)
            stack.push(i)
        if i in {")", "]", "}"}:
            if stack.get_length()!=0:
                get_ = stack.pop()
                if get_ == match_dict[i]:
                    string_array[num]=" "
                    string_array[stack2.pop()] = " "
                else:
                    string_array[num]="?"
            else:
                string_array[num] = "?"
        num+=1

    for x in range(stack2.get_length()):
        get_=stack2.pop()
        string_array[get_]="x"

    output_string = "".join(string_array)
    print(output_string)
if __name__ == "__main__":
    string = input("请输入字符串\n")
    Match_blankets(string)