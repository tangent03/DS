class Ring:

    def __init__(self, n=5):

        self.n = n
        self.active = set(range(1, n + 1))
        self.coordinator = n

    def election(self, pid):

        if pid not in self.active:

            print(f"P{pid} is DOWN")

            return

        print(f"\nP{pid} starts ELECTION")

        current = pid
        highest = pid

        nxt = (current % self.n) + 1

        while nxt != pid:

            if nxt in self.active:

                print(f"P{current} --> P{nxt}")

                highest = max(highest, nxt)

                current = nxt

            else:

                print(f"P{nxt} is DOWN")

            nxt = (nxt % self.n) + 1

        self.coordinator = highest

        print(f"P{highest} sends COORDINATOR message")

        print(f"P{highest} becomes COORDINATOR")

    def up(self, pid):

        if pid in self.active:

            print(f"P{pid} already UP")

        else:

            self.active.add(pid)

            print(f"P{pid} is now UP")

    def down(self, pid):

        if pid not in self.active:

            print(f"P{pid} already DOWN")

        else:

            self.active.remove(pid)

            print(f"P{pid} is now DOWN")

            if pid == self.coordinator:

                print("Coordinator failed!")

                if self.active:

                    self.election(min(self.active))

                else:

                    self.coordinator = None

    def show(self):

        print("\nActive Processes :", sorted(self.active))

        if self.coordinator:

            print("Coordinator : P" + str(self.coordinator))

        else:

            print("No Coordinator")


# MAIN

r = Ring()

print("\n===== RING ALGORITHM =====")

while True:

    r.show()

    print("\n1.ELECTION")
    print("2.UP")
    print("3.DOWN")
    print("4.EXIT")

    ch = int(input("Enter choice : "))

    if ch == 1:

        r.election(int(input("Enter process id : ")))

    elif ch == 2:

        r.up(int(input("Enter process id : ")))

    elif ch == 3:

        r.down(int(input("Enter process id : ")))

    elif ch == 4:

        print("Exiting...")

        break

    else:

        print("Invalid choice")