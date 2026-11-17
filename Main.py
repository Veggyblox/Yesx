// Parent class representing a base User
class User {
    String username;

    public User(String username) {
        this.username = username;
    }

    // 1. METHOD OVERRIDING: 
    // This method will be overridden by the subclass to show runtime polymorphism.
    public void getAccessLevel() {
        System.out.println(username + " has standard guest access.");
    }

    // 2. METHOD OVERLOADING (Part 1):
    // A method with the same name 'displayProfile' but with zero parameters.
    public void displayProfile() {
        System.out.println("User Profile: " + username);
    }

    // 3. METHOD OVERLOADING (Part 2):
    // Same method name 'displayProfile', but overloaded with a boolean parameter 
    // to show status details. Java distinguishes them by their parameter signatures.
    public void displayProfile(boolean showDetails) {
        System.out.println("User Profile: " + username);
        if (showDetails) {
            System.out.println("Account Status: Active");
        }
    }
}

// Subclass inheriting from User
class AdminUser extends User {

    public AdminUser(String username) {
        super(username);
    }

    // METHOD OVERRIDING:
    // Providing a specific implementation for the inherited method 
    // to override the parent class's behavior at runtime.
    @Override
    public void getAccessLevel() {
        System.out.println(username + " has full administrator access!");
    }
}

// Main execution class
public class Main {
    public static void main(String[] args) {
        System.out.println("--- Demonstration of Method Overloading ---");
        User standardUser = new User("Alex");
        
        // Calls the zero-parameter version of displayProfile
        standardUser.displayProfile(); 
        
        // Calls the overloaded version of displayProfile taking a boolean
        standardUser.displayProfile(true); 

        System.out.println("\n--- Demonstration of Method Overriding ---");
        User user1 = new User("Sam");
        User user2 = new AdminUser("BossMan"); // Polymorphism

        // user1 points to User object, executes User's overridden method
        user1.getAccessLevel(); 
        
        // user2 points to AdminUser object, executes AdminUser's overridden method
        user2.getAccessLevel(); 
    }
}
