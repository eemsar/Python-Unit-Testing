import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    #Die setUpClass & tearDownClass werden genau einmal am Anfang und am Ende des gesamten Tests ausgeführt
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    
    
    #setUp und tearDown Funktionen werden benötigt, um das DRY-Prinzip (Dont Repeat Yourself) anwenden zu können.
    #Die Objekte werden als Instanzvariablen erstellen und nicht mehr als lokale Variablen.
    #setUp wird vor jedem Test ausgeführt 
    def setUp(self):
        self.emp_1 = Employee("Emre", "Sarak", 5000)
        self.emp_2 = Employee("Günay", "Bayramov", 4500)
        print("setUP")
        
    #tearDown wird am Ende von einem Test ausgeführt
    def tearDown(self):
        print("tearDown\n")
    
    def test_email(self):
        #Ersten beiden Zeilen der Funktionen werden von der setUp Funktion ersetzt
        #emp_1 = Employee("Emre", "Sarak", 5000)
        #emp_2 = Employee("Günay", "Bayramov", 4500)
        #statt emp_1/2.email muss wegen setUp Funktion ein self davor
        
        print("test_email")
        self.assertEqual(self.emp_1.email, "Emre.Sarak@email.com")
        self.assertEqual(self.emp_2.email, "Günay.Bayramov@email.com")
        
        self.emp_1.first = "Evren"
        self.emp_2.first = "Günel"
        
        self.assertEqual(self.emp_1.email, "Evren.Sarak@email.com")
        self.assertEqual(self.emp_2.email, "Günel.Bayramov@email.com")
        
        
    def test_fullname(self):
        #emp_1 = Employee("Emre", "Sarak", 5000)
        #emp_2 = Employee("Günay", "Bayramov", 4500)
        
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Emre Sarak")
        self.assertEqual(self.emp_2.fullname, "Günay Bayramov")
        
        self.emp_1.first = "Evren"
        self.emp_2.first = "Günel"
        
        self.assertEqual(self.emp_1.fullname, "Evren Sarak")
        self.assertEqual(self.emp_2.fullname, "Günel Bayramov")
        
        
    def test_apply_raise(self):
        #emp_1 = Employee("Emre", "Sarak", 5000)
        #emp_2 = Employee("Günay", "Bayramov", 4500)
        
        print("test_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 4725)
        

        
if __name__ == "__main__":
    unittest.main()