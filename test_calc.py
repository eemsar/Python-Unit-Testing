#Testing module für calc.py
#Ausführung des Unit Tests mit: python3 -m unittest test_calc.py

import unittest
import calc

class TestCalc(unittest.TestCase):
    
    #Name der Methode muss mit 'test_' beginnen
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)
        
    def test_sub(self):
        self.assertEqual(calc.sub(10,5),5)
        self.assertEqual(calc.sub(-1,1),-2)
        self.assertEqual(calc.sub(-1,-1),-0)
    
    def test_multi(self):
        self.assertEqual(calc.multi(10,5),50)
        self.assertEqual(calc.multi(-1,1),-1)
        self.assertEqual(calc.multi(-1,-1),1)
    
    def test_div(self):
        self.assertEqual(calc.div(10,5),2)
        self.assertEqual(calc.div(-1,1),-1)
        self.assertEqual(calc.div(-1,-1),1)
        self.assertEqual(calc.div(5,2),2.5)
        #Testing für des Errors
        with self.assertRaises(ValueError):
            calc.div(10,0)
        
        

#Wenn Unit Test ohne langen befehl ausgeführt werden soll dann:
if __name__ == "__main__":
    unittest.main()
    