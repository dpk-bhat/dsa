def main():
    output_file = open("outputPS5.txt", "w")
    task_int = 0
    count = 0

    class Node:
        def __init__(self, data, next=None) -> None:
            self.data = data
            self.next = None

        def __str__(self) -> str:
            return str(self.data)

    class LinkedList:
        nonlocal count

        def __init__(self) -> None:
            self.head = None
            self.tail = None
            self.count = 0

        def is_empty(self) -> bool:
            return True if self.head == None else False

        def __sizeof__(self) -> int:
            return count

        def append(self, task):
            nonlocal count
            node = Node(task, None)
            try:
                if self.is_empty():
                    self.head = node
                    self.tail = node
                else:
                    self.tail.next = node
                    self.tail = node
                count += 1
                return task
            except:
                print("Something went wrong during Append")

        def remove(self, task):
            nonlocal count
            temp = self.head
            try:
                if temp == None:
                    log_error("LINKED LIST IS EMPTY")
                else:
                    if temp.data == task:
                        self.head = self.head.next
                        return temp.data
                    else:
                        while temp.next != None:
                            prev = temp
                            temp = temp.next
                            if temp.data == task:
                                prev.next = temp.next
                                count -= 1
                                if temp == self.tail:
                                    self.tail = prev
                                return temp.data
                return None
            except:
                print("Something went wrong during Remove")

        def find(self, task):
            temp = self.head
            found_tasks = []
            try:
                if temp == None:
                    log_error("LINKED LIST IS EMPTY")
                else:
                    while temp != None:
                        if task.task_string in temp.data.task_string.lower().strip().strip(".") :
                            found_tasks.append(temp.data)
                        temp = temp.next
                    return found_tasks
                return None
            except:
                print("Something went wrong during Find")
    class Task:
        def __init__(self, task_string, task_number="") -> None:
            nonlocal task_int
            task_int += 1
            self.task_string = task_string
            self.is_complete = False
            if task_number == "":
                self.task_number = "TA" + str(task_int).zfill(3)
            else:
                self.task_number = task_number

        def __str__(self) -> str:
            return (
                f"[{self.task_number}, {self.task_string.strip()}, {self.is_complete}]"
            )

        def __eq__(self, other) -> bool:
            if (
                self.task_string == other.task_string
                or self.task_number == other.task_number
            ):
                return True
            else:
                return False

    def addTask(linked_list, task_string=""):
        nonlocal count
        # check if task_string is not null/empty
        if task_string:
            # Create a task and append it to the linked list
            task_to_add = Task(task_string)
            task = linked_list.append(task_to_add)
            output_file.write("ADDED:" + task.task_number + "-" + task_string)
        else:
            log_error("TASK STRING IS EMPTY")

    def removeTask(linked_list, task_string="", task_number=""):
        nonlocal count
        task_to_remove = Task(task_string, task_number)
        removed_task = linked_list.remove(task_to_remove)
        if removed_task:
            output_file.write(
                "REMOVED:" + removed_task.task_number + "-" + removed_task.task_string
            )
        else:
            output_file.write("TASK :" + task_to_remove.task_string.strip() + " WAS NOT FOUND\n")

    def searchTask(linked_list, search_string=""):
        if search_string:
            task_to_find = Task(search_string.strip().strip("."))
            output_file.write("SEARCHED:" + search_string + "-" * 60 + "\n")
            found_tasks = linked_list.find(task_to_find)
            if found_tasks != None and found_tasks!= []:
                for task in found_tasks:
                    output_file.write(task.task_number + " " + task.task_string)
            else:
                output_file.write("TASK NOT FOUND\n")
            output_file.write("-" * 60 + "\n")
        else:
            log_error("SEARCH STRING IS EMPTY")

    def completeTask(linked_list, task_string="", task_number=""):
        if task_string or task_number:
            found = False
            temp = linked_list.head
            task_to_complete = Task(task_string, task_number)
            if task_to_complete == temp.data:
                found = True
                temp.data.is_complete = True
                output_file.write(
                    "COMPLETED:" + temp.data.task_number + "-" + task_string
                )
            else:
                while temp.next != None:
                    if task_to_complete == temp.data:
                        found = True
                        temp.data.is_complete = True
                        output_file.write(
                            +"COMPLETED:" + temp.data.task_number + "-" + task_string
                        )
                    temp = temp.next
            if not found:
                log_error(f"CANNOT MARK COMPLETE: TASK {task_to_complete.task_string.strip()} NOT FOUND")
        else:
            log_error("TASK STRING AND TASK NUMBER IS EMPTY")

    def incompleteTask(linked_list, task_string="", task_number=""):
        if task_string or task_number:
            found = False
            temp = linked_list.head
            task_to_incomplete = Task(task_string, task_number)
            if task_to_incomplete == temp.data:
                found = True
                temp.data.is_complete = False
                output_file.write(
                    "UNCOMPLETED:" + temp.data.task_number + "-" + task_string
                )
            else:
                while temp.next != None:
                    if task_to_incomplete == temp.data:
                        found = True
                        temp.data.is_complete = False
                        output_file.write(
                            "UNCOMPLETED:" + temp.data.task_number + "-" + task_string
                        )
                    temp = temp.next
            if not found:
                log_error(f"CANNOT MARK INCOMPLETE TASK {task_to_incomplete.task_string.strip()} NOT FOUND")
        else:
            log_error("TASK STRING AND TASK NUMBER IS EMPTY")

    def statusTask(linked_list):
        # append to file
        output_file.write(
            "Task-Number".ljust(15)
            + "Task-String".ljust(30)
            + "Task-Status"
            + "\n"
            + "-" * 60
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

    def log_error(error_message):
        output_file.write(error_message+ "\n")

    def print_linked_list(linked_list):
        temp = linked_list.head
        while temp:
            print(f"{temp.data} ->", end="")
            temp = temp.next
        print()

    def initiateToDoList(read_input_file):
        file = open(read_input_file, "r")
        lines = file.readlines()
        # initializing empty linked list object
        linked_list = LinkedList()
        nonlocal count
        for line in lines:
            instruction, task_string = line.split(":")
            instruction = instruction.strip().lower()

            if instruction == "add a task":
                addTask(linked_list, task_string)
            elif instruction == "remove task":
                removeTask(linked_list, task_string)
            elif instruction == "search task":
                searchTask(linked_list, task_string)
            elif instruction == "mark complete":
                completeTask(linked_list, task_string)
            elif instruction == "mark incomplete":
                incompleteTask(linked_list, task_string)
            elif instruction == "task status":
                if linked_list.is_empty():
                    output_file.write("No task found")
                else:
                    statusTask(linked_list)
            else:
                log_error("INVALID INSTRUCTION")

            print_linked_list(linked_list)

    initiateToDoList("C:\BITS\Sem 2\DSA\Assignemnt 1\inputPS5.txt")

    output_file.close()


main()


# Handle empty linked list and invlid input
