class Bully:

    def __init__(self, n=5):

        self.n = n
        self.state = [True] * n
        self.leader = n

    def show(self):

        print("\n------ PROCESS STATUS ------")

        for i in range(self.n):

            status = "UP" if self.state[i] else "DOWN"

            if i + 1 == self.leader and self.state[i]:

                print(f"P{i+1} --> {status} [COORDINATOR]")

            else:

                print(f"P{i+1} --> {status}")

    def election(self, pid):

        print(f"\nP{pid} starts ELECTION")

        self.leader = pid

        for i in range(pid + 1, self.n + 1):

            if self.state[i - 1]:

                print(f"P{pid} --> ELECTION --> P{i}")

                print(f"P{i} --> OK")

                self.leader = i

        print(f"P{self.leader} sends COORDINATOR message")

        print(f"P{self.leader} becomes COORDINATOR")

    def up(self, pid):

        if self.state[pid - 1]:

            print(f"P{pid} already UP")

        else:

            self.state[pid - 1] = True

            print(f"P{pid} is now UP")

            self.election(pid)

    def down(self, pid):

        if not self.state[pid - 1]:

            print(f"P{pid} already DOWN")

        else:

            self.state[pid - 1] = False

            print(f"P{pid} is now DOWN")

            if pid == self.leader:

                print("Coordinator failed!")

                for i in range(self.n):

                    if self.state[i]:

                        self.election(i + 1)

                        break

    def message(self, pid):

        if not self.state[pid - 1]:

            print(f"P{pid} is DOWN")

            return

        print(f"\nP{pid} sends message to P{self.leader}")

        if self.state[self.leader - 1]:

            print(f"P{self.leader} replies OK")

        else:

            print("Coordinator not responding")

            self.election(pid)


# MAIN

b = Bully()

print("\n===== BULLY ALGORITHM =====")

while True:

    b.show()

    print("\n1.UP")
    print("2.DOWN")
    print("3.MESSAGE")
    print("4.EXIT")

    ch = int(input("Enter choice : "))

    if ch == 1:

        b.up(int(input("Enter process id : ")))

    elif ch == 2:

        b.down(int(input("Enter process id : ")))

    elif ch == 3:

        b.message(int(input("Enter process id : ")))

    elif ch == 4:

        print("Exiting...")

        break

    else:

        print("Invalid choice")