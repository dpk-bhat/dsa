def main():
    output_file = open("outputPS5.txt", "w")
    task_int = 0
    count = 0

    class Node:
        def __init__(self, data, next=None) -> None:
            nonlocal count
            self.data = data
            self.next = None

        def __str__(self) -> str:
            return str(self.data)

    class LinkedList:
        nonlocal count
        def __init__(self) -> None:
            self.head = None

        def is_empty(self):
            return True if self.head else False

        def __sizeof__(self) -> int:
            return count

    class Task:
        def __init__(self, task_string) -> None:
            nonlocal task_int
            task_int += 1
            self.task_string = task_string
            self.task_number = "TA" + str(task_int).zfill(3)
            self.is_complete = False
        def __str__(self) -> str:
            return f'[{self.task_number}, {self.task_string}, {self.is_complete}]'

    def addTask(linked_list, task_string=""):
        nonlocal count
        # check if task_string is not null/empty
        if task_string:
            # if there are no nodes, create a linked list
            task = Task(task_string)
            node = Node(task, None)
            if linked_list == None:
                linked_list = LinkedList()
                linked_list.head = node
            # else append a node to exsisting linked list
            else:
                temp = linked_list.head
                while temp.next != None:
                    temp = temp.next
                temp.next = node
            output_file.write("ADDED:" + task.task_number + "-" + task_string)
            count += 1
            return linked_list
        else:
            invalidInput()
            return None

    def removeTask(linked_list, task_string="", task_number=""):
        nonlocal count
        if (task_string or task_number) and linked_list:
            temp = linked_list.head
            if (
                temp.data.task_number == task_number
                or temp.data.task_string == task_string
            ):
                output_file.write(
                    "REMOVED:"
                    + temp.data.task_number
                    + "-"
                    + temp.data.task_string
                )
                linked_list.head = temp.next
                count -= 1
            else:
                while temp.next != None:
                    prev = temp
                    temp = temp.next
                    if (
                        temp.data.task_number == task_number
                        or temp.data.task_string == task_string
                    ) and linked_list:
                        output_file.write(
                            "REMOVED:"
                            + temp.data.task_number
                            + "-"
                            + temp.data.task_string
                        )
                        prev.next = temp.next
                        count -= 1
                        break
            return linked_list
        else:
            invalidInput()
            return None

    def searchTask(linked_list, search_string=""):
        temp = linked_list.head
        output_file.write("SEARCHED:" + search_string)
        output_file.write( "-" * 60 + "\n" )
        while temp != None:
            found = False
            if search_string.strip().strip(".").lower() in temp.data.task_string.strip().lower():
                output_file.write(
                    temp.data.task_number + " " + temp.data.task_string
                )
                found = True
            temp = temp.next
        if not found:
            output_file.write("\nTASK NOT FOUND\n")
        output_file.write("-" * 60 + "\n" )

    def completeTask(linked_list, task_string="", task_number=""):
        if task_string or task_number:
            temp = linked_list.head
            if (
                task_string == temp.data.task_string
                or task_number == temp.data.task_number
            ):
                temp.data.is_complete = True
                output_file.write(
                    "COMPLETED:" + temp.data.task_number + "-" + task_string
                )
            else:
                while temp.next != None:
                    if (
                        task_string == temp.data.task_string
                        or task_number == temp.data.task_number
                    ):
                        temp.data.is_complete = True
                        output_file.write(
                            +"COMPLETED:"
                            + temp.data.task_number
                            + "-"
                            + task_string
                        )
                    temp = temp.next

    def incompleteTask(linked_list, task_string="", task_number=""):
        if task_string or task_number:
            temp = linked_list.head
            if (
                task_string == temp.data.task_string
                or task_number == temp.data.task_number
            ):
                temp.data.is_complete = False
                output_file.write(
                    "UNCOMPLETED:" + temp.data.task_number + "-" + task_string
                )
            else:
                while temp.next != None:
                    if (
                        task_string == temp.data.task_string
                        or task_number == temp.data.task_number
                    ):
                        temp.data.is_complete = False
                        output_file.write(
                            "UNCOMPLETED:"
                            + temp.data.task_number
                            + "-"
                            + task_string
                        )
                    temp = temp.next

    def statusTask(linked_list):
        # append to file
        output_file.write(
            "Task-Number".ljust(15) + "Task-String".ljust(30) + "Task-Status" + "\n"+"-" * 60
        )
        # Print all the task in the linked list
        temp = linked_list.head
        while temp.next != None:
            status = "C" if temp.data.is_complete else "I"
            output_file.write(
                "\n"
                + temp.data.task_number.ljust(15)
                + temp.data.task_string[:-2].ljust(30)
                + status
            )
            temp = temp.next
        output_file.write("\n" + "-" * 60 + "\n")

    def invalidInput():
        # print invalid input
        output_file.write("Invalid Input")

    def print_linked_list(linked_list):
        head = linked_list.head
        while head:
            print(f'{head.data} ->', end='')
            head=head.next

    def initiateToDoList(read_input_file):
        file = open(read_input_file, "r")
        lines = file.readlines()
        linked_list = None
        nonlocal count
        for line in lines:
            instruction, task_string = line.split(":")
            instruction = instruction.strip().lower()

            if instruction == "add a task":
                linked_list = addTask(linked_list, task_string)
                print_linked_list(linked_list)
            elif instruction == "remove task":
                linked_list = removeTask(linked_list, task_string)
                print_linked_list(linked_list)
            elif instruction == "search task":
                searchTask(linked_list, task_string)
                print_linked_list(linked_list)
            elif instruction == "mark complete":
                completeTask(linked_list, task_string)
                print_linked_list(linked_list)
            elif instruction == "mark incomplete":
                incompleteTask(linked_list, task_string)
                print_linked_list(linked_list)
            elif instruction == "task status":
                statusTask(linked_list)
                print_linked_list(linked_list)
            else:
                invalidInput()
            print(count)
        
    initiateToDoList("C:\BITS\Sem 2\DSA\Assignemnt 1\inputPS5.txt")


main()


# Handle empty linked list and invlid input