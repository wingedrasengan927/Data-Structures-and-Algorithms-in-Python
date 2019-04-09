

'''To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.'''

from collections import deque

# Let's implement the code of a printing machine with help of a queue

class PrintingMachine():
    def __init__(self):
        self.document = deque([])

    def insert_paper(self, paper):
        self.document.append(paper)

    def start_printing(self):
        while self.document:
            print("Printing {}...".format(self.document.popleft()))
        if not self.document:
            print("Completed")

# let's define the document to be printed
nitwMag = PrintingMachine()

# let's add the papers
nitwMag.insert_paper("Cover Page front")
nitwMag.insert_paper("Acknowledgement")
nitwMag.insert_paper("Words of Appraisal")
nitwMag.insert_paper("Meet the Team")
nitwMag.insert_paper("Index")
nitwMag.insert_paper("Content")
nitwMag.insert_paper("Cover page back")

# Let's starts printing
nitwMag.start_printing()








