class Student:
    def __init__(self, name, credits, points):
        self.name = name
        self.credits = float(credits)
        self.points = float(points)

    def gpa(self):
        return self.points/self.credits


def makeStudent(line):
    # line  contains name, credits, and points
    # returns a corresponding Student object
    name, credits, points = line.split() #以空格为分隔符號
    return Student(name, credits, points)


def main():
    # Open the input file for reading
    filename = input('Enter the name of the grade file: ')
    with open(filename, 'r') as infile:
        # Set best to the record for the first student in the file
        best = makeStudent(infile.readline())

        # Process subsequent lines of the file
        for line in infile:
            # Turn the line into a student record
            s = makeStudent(line)
            # If this student is best so far, remember it
            if s.gpa() > best.gpa():
                best = s

    # Print information about the best student
    print('The best student is: ', best.name)
    print('Credits: ', best.credits)
    print('GPA: ', best.gpa())


if __name__ == '__main__':
    main()