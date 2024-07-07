class Customer:
    def __init__(self):
        self.is_registered = False
        self.is_logged_in = False
        self.name = ""
        self.age = 0
        self.location = ""
        self.mobile_number = ""
        self.password = ""
        self.menu()

    def menu(self):
        menus = (
            """
    Welcome to the Healthcare Platform!
         1. Register
         2. Login
         3. Get Treatment
         4. edit profile
         5. password change
                     """
        )
        print(menus)
        choice = input("Enter your choice: ")
        if choice == "1":
            self.register()
        elif choice == "2":
            self.login()
        elif choice == "3":
            self.solved()
        elif choice == "4":
             self.edit_profile()
        elif choice == "5":
             self.password_change()     
               
        else:
            print("Other features pending...")
            self.menu()

    def register(self):
        print("Welcome to our platform!")
        while True:
           self.name = str(input("Enter your name: "))
           if self.name.isalpha():
               break
           else: print("please! name abc me hi dale")
        while True:
            try:   
               self.age = int(input(f"{self.name} Enter your age: "))
               break
            except ValueError:
             print(f"{self.name} please! age numbers me fill kre")
        while True:
             self.location = str(input(f" {self.name} Enter your preferred location: "))

             if self.location.isalpha():
                 break
             else:
                 print(f"{self.name}please! name abc me hi enter kre")
        

        while True:
            self.mobile_number = input(f" {self.name} Enter your mobile number: ")
            if len(self.mobile_number) == 10 and self.mobile_number.isdigit():
                break
            else:
                print(f"  {self.name} Please enter a valid 10-digit mobile number.")
    
        self.password = input(f"   {self.name} Enter your password: ")
         
        while True:
            confirm_password = input(f"{self.name} Confirm your password: ")
            if self.password == confirm_password:
                break
            else:
                print(f" {self.name} Passwords do not match. Please try again.")
        
        
        print(f"Wow! {self.name}, you have successfully registered.")
        self.is_registered = True
        self.menu()

    def login(self):
        if not self.is_registered:
            print(f"  {self.name} Oh! Sorry, you need to register first.")
            self.menu()
            return

        while True:
            login_name = input(f"{self.name} Enter your name: ")
            if login_name == self.name:
                break
            else:
                print(f" {self.name} Please enter the correct name.")

        while True:
            login_password = input(f"{self.name} Enter your password: ")
            if login_password == self.password:
                break
            else:
                print(f"  {self.name} Your password is incorrect. Please try again.")

        print(f"{self.name}, you have logged in successfully. Now visit our platform to solve your problems.")
        self.is_logged_in = True
        self.menu()

    def solved(self):
        if not self.is_registered:
            print("Oh! Sorry, you need to register first.")
            self.menu()
            return
        if not self.is_logged_in:
            print("Oh! Sorry, you need to login first.")
            self.menu()
            return

        network = input("Where did you hear about our platform? ")
        print(f"{self.name}, we are sorry that you are facing health-related problems. We will try our best to help you with your treatment on our platform. Please enter the number corresponding to your disease from the list below to get the solution.")
        
        user_input = input("""
                          1. Diabetes          -> Increased thirst, frequent urination, fatigue.
                          2. Hypertension      -> Often asymptomatic, but can include headaches, shortness of breath, and nosebleeds.
                          3. Asthma	          -> Shortness of breath, wheezing, chest tightness, and coughing.
                          4. Arthritis	      -> Joint pain, stiffness, swelling, and reduced range of motion.
                          5. Allergies	      -> Sneezing, itching, runny nose, watery eyes, and rashes.
                          6. Chronic Back Pain -> Persistent aching or stiffness along the spine, sharp localized pain.
                          7. Depression	      -> Persistent sadness, loss of interest, changes in sleep and appetite.
                          8. Obesity	          -> Excess body weight, difficulty in physical activity, increased risk of other diseases.
                          9. Migraine	      -> Severe, throbbing headache, sensitivity to light and sound, nausea.
                          10. Gastroesophageal Reflux Disease -> Heartburn, regurgitation, difficulty swallowing.
                          11. Malaria	      -> Fever, chills, sweating, headache, nausea, and vomiting.
                          12. Common Cold	  -> Sneezing, runny nose, sore throat, cough, and congestion.
                          13. Normal Fever	  -> Elevated body temperature, sweating, chills, headache, muscle aches.
                          14. Dengue	          -> High fever, severe headache, pain behind the eyes, joint and muscle pain.
                          """)

        treatments = {
            "1": "Your treatment is: Metformin, Insulin, Sulfonylureas.",
            "2": "Your treatment is: ACE inhibitors, Beta-blockers, Diuretics.",
            "3": "Your treatment is: Inhaled corticosteroids, Beta-agonists.",
            "4": "Your treatment is: NSAIDs, Corticosteroids, DMARDs.",
            "5": "Your treatment is: Antihistamines, Decongestants, Steroids.",
            "6": "Your treatment is: NSAIDs, Muscle relaxants, Opioids.",
            "7": "Your treatment is: SSRIs, SNRIs, Tricyclic antidepressants.",
            "8": "Your treatment is: Orlistat, Phentermine, Metformin.",
            "9": "Your treatment is: Triptans, NSAIDs, Ergotamines.",
            "10": "Your treatment is: Antacids, H2 blockers, Proton pump inhibitors.",
            "11": "Your treatment is: Chloroquine, Artemisinin-based combination therapies.",
            "12": "Your treatment is: Antihistamines, Decongestants, Cough suppressants.",
            "13": "Your treatment is: Acetaminophen, Ibuprofen, Aspirin.",
            "14": "Your treatment is: Acetaminophen, Oral rehydration therapy.",
        }

        print(treatments.get(user_input, "Others pending..."))
        self.menu()

    def edit_profile(self):
         if not self.is_logged_in:
            print(self.name,"Oh! Sorry, you need to login first.")
            self.menu()
            return
         while True:
          new_name = str(input(f"{self.name} enter new name:"))
          if new_name.isalpha():
              break
          else: print(f"{self.name} please! abc me se enter kre")
         new_name = self.name
         while True:
          try:
            new_age = int(input(f"{self.name} enter your age"))
            break
          except ValueError: 
           print(f"{self.name} enter your numbers types age")
         new_age = self.age
         while True:
            new_location = str(input(f"{self.name} enter your location "))
            if new_location.isalpha():
                break
            else: print(f"{self.name} please! enter a valid location ")
            new_location = self.location
         while True:
            new_mobile_number =input(f"  {self.name} Enter your mobile number: ")
            if len(new_mobile_number) == 10 and new_mobile_number.isdigit():
                new_mobile_number = self.mobile_number
                break
            else:
                print(f" {self.name} Please enter a valid 10-digit mobile number.")
             

         print(f" {self.name} Yahh! YOUR PROFILE EDIT SUCCESSFULLY ") 

    def password_change(self):
        if not self.is_logged_in:
            print(self.name,"Oh! Sorry, you need to login first.")
            self.menu()
            return
        
        old_password = input(f" {self.name} enter your old password ")
        if old_password == self.password:
            new_password = input(f"{self.name} enter your new password")
        else: print(f"{self.name} please! enter your correct old password")
        confirm_new_password = input(f"{self.name} enter your again password")
        while True:
         if new_password == confirm_new_password:
             break
         else: print(f"{self.name}please! enter your correct password")
        print(f"{self.name} ypur password successfully changed")

obj = Customer()           

class Doctor:
    def __init__(self):
        self.name=" "




doc =Doctor()        
