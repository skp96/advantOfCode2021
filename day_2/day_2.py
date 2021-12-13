def read_file():
    instructions = []

    with open("input.txt", "r") as planned_course:
        for course in planned_course:
            instructions.append(course.strip())

    return instructions


class CoursePlanning:
    def __init__(self, instructions):
        self.depth_pos = 0
        self.horizontal_pos = 0
        self.aim = 0
        self.instructions = instructions

    def calculate_pos(self):
        for instruction in self.instructions:
            direction, position = instruction.split(" ")
            self.update_pos(direction, int(position))

        return self.depth_pos * self.horizontal_pos

    def update_pos(self, direction, position):
        if direction == "up":
            self.aim -= position
        elif direction == "down":
            self.aim += position
        else:
            self.horizontal_pos += position
            self.depth_pos += (position * self.aim)


if __name__ == "__main__":
    instructions = read_file()
    course_plan = CoursePlanning(instructions)
    print(course_plan.calculate_pos())
