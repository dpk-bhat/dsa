def main():
    output_file = open("outputPS5.txt", "w")
    task_int = 0
    linked_list = None

    """
    Below is the implementation of Task
    A Task contains task_string, task_number and is_complete field
    Task.task_string will contain the task description
    Task.task_number will contain a unique ID
    Task.is_complete will indicate if the task is marked as complete or not
    """

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

    """
    Below is the implementation of Node
    A Node contains data and next field
    Node.data will have a Task object
    Node.next will have None, which will be replaced by address of next Task
    """

    class Node:
        def __init__(self, data, next=None) -> None:
            self.data = data
            self.next = None

        def __str__(self) -> str:
            return str(self.data)

    """
    Below is the implementaion of Linked List.
    A Linked List contains head, tail and count field
    LinkedList.head will contain address of the first node
    LinkedList.tail will contain address of the last node
    LinkedList.count will contain the number of nodes presenet in the linked list
    This class provides funtion for basic funtionalities i.e. append, find and remove
    """

    class LinkedList:
        def __init__(self) -> None:
            self.head = None
            self.tail = None
            self.count = 0

        def is_empty(self) -> bool:
            return True if self.head == None else False

        def __sizeof__(self) -> int:
            return self.count

        def get_head(self):
            return self.head

        def append(self, task):
            node = Node(task, None)
            try:
                
                """
                Assign the node as head of linked list if linked list is empty
                Else append the node to tail
                return the newly appended task
                """

                if self.is_empty():
                    self.head = node
                    self.tail = node
                else:
                    self.tail.next = node
                    self.tail = node
                self.count += 1
                return task
            except:
                print("Something went wrong during Append")

        def remove(self, task):
            temp = self.head
            try:

                """
                If the linked list is empty log the error and return nothing
                Else search and remove the task from the linked list
                """

                if temp == None:
                    log_error("LINKED LIST IS EMPTY")
                else:

                    """
                    If the head is the task to be removed, remove task and reassign head to next node
                    Else search and remove the task from the llinked list
                    Return the removed task
                    """
                    
                    if temp.data == task:
                        self.head = self.head.next
                        self.count -= 1
                        return temp.data
                    else:
                        while temp.next != None:
                            prev = temp
                            temp = temp.next
                            if temp.data == task:
                                prev.next = temp.next
                                self.count -= 1
                                # If the task to be removed is tail, reasssign tail to previous node
                                if temp == self.tail:
                                    self.tail = prev
                                return temp.data
            except:
                print("Something went wrong during Remove")

        def search(self, task):
            temp = self.head
            found_tasks = []
            try:

                """
                If the linked list is empty log the error and return nothing
                Else search for the task in the linked list
                Return list of tasks found
                """

                if temp == None:
                    log_error("LINKED LIST IS EMPTY")
                else:
                    while temp != None:
                        # If the search string is present in any of the task, append it to the list of found task
                        if (
                            task.task_string
                            in temp.data.task_string.lower().strip().strip(".")
                        ):
                            found_tasks.append(temp.data)
                        temp = temp.next
                return found_tasks
            except:
                print("Something went wrong during search")

    def addTask(task_string=""):
        # Check if task_string is not null/empty
        if task_string:
            # Create a task and append it to the linked list and write in output file
            task_to_add = Task(task_string)
            task = linked_list.append(task_to_add)
            output_file.write("ADDED:" + task.task_number + "-" + task_string)
        else:
            log_error("TASK STRING IS EMPTY")

    def removeTask(task_string="", task_number=""):
        # Check if the task_string or task_number has some value
        if task_string or task_number:
            task_to_remove = Task(task_string, task_number)
            removed_task = linked_list.remove(task_to_remove)
            # Check if removed_task has a task, and if yes, write in the output file
            if removed_task:
                output_file.write(
                    "REMOVED:"
                    + removed_task.task_number
                    + "-"
                    + removed_task.task_string
                )
            else:
                output_file.write(
                    "TASK :" + task_to_remove.task_string.strip() + " WAS NOT FOUND\n"
                )
        else:
            log_error("TASK STRING AND TASK NUMBER IS EMPTY")

    def searchTask(search_string=""):
        # Check if the search_string and linked list is not empty
        if search_string and not linked_list.is_empty():
            task_to_find = Task(search_string.strip().strip("."))
            output_file.write("SEARCHED:" + search_string + "-" * 60 + "\n")
            found_tasks = linked_list.search(task_to_find)

            """
            Check if found_tasks list has any object
            If yes, write it's elements to output file
            Else write the same in output file
            """

            if found_tasks != None and found_tasks != []:
                for task in found_tasks:
                    output_file.write(task.task_number + " " + task.task_string)
            else:
                output_file.write("TASK NOT FOUND\n")
            output_file.write("-" * 60 + "\n")
        else:
            log_error("SEARCH STRING OR LINKED LIST IS EMPTY")

    def completeTask(task_string="", task_number=""):
        # Check if the linked list is empty
        if linked_list.is_empty():
            log_error("LINKED LIST IS EMPTY.")
            return None
        else:
            # Check if the task_string or task_number has some value
            if task_string or task_number:
                found = False
                temp = linked_list.get_head()
                task_to_complete = Task(task_string, task_number)
            
                """
                Check the linked list for the task
                If found, mark as complete and write to output file
                Else write the same in output file
                """

                while temp.next != None:
                    if task_to_complete == temp.data:
                        found = True
                        temp.data.is_complete = True
                        output_file.write(
                            "COMPLETED:" + temp.data.task_number + "-" + task_string
                        )
                    temp = temp.next
                if not found:
                    log_error(
                        f"CANNOT MARK COMPLETE: TASK {task_to_complete.task_string.strip()} NOT FOUND"
                    )
            else:
                log_error("TASK STRING AND TASK NUMBER IS EMPTY")

    def incompleteTask(task_string="", task_number=""):
        # Check if the linked list is empty
        if linked_list.is_empty():
            log_error("LINKED LIST IS EMPTY.")
            return None
        else:
            # Check if the task_string or task_number has some value
            if task_string or task_number:
                found = False
                temp = linked_list.get_head()
                task_to_incomplete = Task(task_string, task_number)
                
                """
                Check the linked list for the task
                If found, mark as complete and write to output file
                Else write the same in output file
                """

                while temp.next != None:
                    if task_to_incomplete == temp.data:
                        found = True
                        temp.data.is_complete = False
                        output_file.write(
                            "UNCOMPLETED:" + temp.data.task_number + "-" + task_string
                        )
                    temp = temp.next
                if not found:
                    log_error(
                        f"CANNOT MARK INCOMPLETE TASK {task_to_incomplete.task_string.strip()} NOT FOUND"
                    )
            else:
                log_error("TASK STRING AND TASK NUMBER IS EMPTY")

    def statusTask():
        if linked_list.is_empty():
            log_error("LINKED LIST IS EMPTY.")
        # Append to file
        output_file.write(
            "Task-Number".ljust(15)
            + "Task-String".ljust(30)
            + "Task-Status"
            + "\n"
            + "-" * 60
        )
        # Print all the task in the linked list
        temp = linked_list.get_head()
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
        # Append appropriate error message to the output file
        output_file.write(error_message + "\n")

    """
    Function for debuggging
    def print_linked_list(linked_list):
        temp = linked_list.get_head()
        while temp:
            print(f"{temp.data} ->", end="")
            print(" " + str(linked_list.count))
            temp = temp.next
        print()
    """

    def initiateToDoList(read_input_file):
        nonlocal linked_list
        linked_list = LinkedList()
        # Read the input file and process each line
        file = open(read_input_file, "r")
        lines = file.readlines()
        # Initializing empty linked list
        for line in lines:
            # Perform operation depending in instruction
            instruction, task_string = line.split(":")
            instruction = instruction.strip().lower()
            if instruction == "add a task":
                addTask(task_string)
            elif instruction == "remove task":
                removeTask(task_string)
            elif instruction == "search task":
                searchTask(task_string)
            elif instruction == "mark complete":
                completeTask(task_string)
            elif instruction == "mark incomplete":
                incompleteTask(task_string)
            elif instruction == "task status":
                statusTask()
            else:
                log_error("INVALID INSTRUCTION")
            
            """
            Printing linked list after each operation for debugging
            print_linked_list(linked_list)
            """

    initiateToDoList("inputPS5.txt")

    # Close the output file after writing
    output_file.close()

main()
