class FanEngagementPortal:
    """Manages CRUD operations for fans."""
    
    def init(self):
        self.fans = []

    def add_fan(self):
        """Adds a new fan."""
        name = input("Enter fan name: ")
        email = input("Enter fan email: ")
        comment = input("Enter fan comment: ")
        self.fans.append(Fan(name, email, comment))
        print("Fan added successfully!")

    def list_fans(self):
        """Displays all fans."""
        if not self.fans:
            print("No fans to display.")
        else:
            for i, fan in enumerate(self.fans, start=1):
                print(f"{i}. {fan}")

    def update_fan(self):
        """Updates a fan's details."""
        self.list_fans()
        index = int(input("Enter fan number to update: ")) - 1
        if 0 <= index < len(self.fans):
            self.fans[index].name = input("Enter new name: ")
            self.fans[index].email = input("Enter new email: ")
            self.fans[index].comment = input("Enter new comment: ")
            print("Fan updated successfully!")
        else:
            print("Invalid index. Try again.")

    def delete_fan(self):
        """Deletes a fan."""
        self.list_fans()
        index = int(input("Enter fan number to delete: ")) - 1
        if 0 <= index < len(self.fans):
            self.fans.pop(index)
            print("Fan deleted successfully!")
        else:
            print("Invalid index. Try again.")

    def run(self):
        """Runs the portal with a simple menu."""
        while True:
            print("\n1. Add Fan\n2. List Fans\n3. Update Fan\n4. Delete Fan\n5. Exit")
            choice = input("Enter choice (1-5): ")
            if choice == '1':
                self.add_fan()
            elif choice == '2':
                self.list_fans()
            elif choice == '3':
                self.update_fan()
            elif choice == '4':
                self.delete_fan()
            elif choice == '5':
                print("Exiting the portal. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
                
portal = FanEngagementPortal()
portal.run()
