import unittest

from tientrocap import tien_tro_cap

class TestTroCap(unittest.TestCase):

    def test_base(self):
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 2, 't'), 1500)  
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)   
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)    
        self.assertEqual(tien_tro_cap(1000, 2, 'g'), 1800) 
        self.assertEqual(tien_tro_cap(1000, 4, 'g'), 2000) 

    def test_dependents(self):
        self.assertEqual(tien_tro_cap(1000, -3, 't'), -1)  
        self.assertEqual(tien_tro_cap(1000, 0, 't'), 0)  
        self.assertEqual(tien_tro_cap(1000, 0, 't'), 0)   
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)    
        self.assertEqual(tien_tro_cap(1000, 2, 't'), 1500)  
        self.assertEqual(tien_tro_cap(1000, 2, 't'), 1500)  
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)  
        self.assertEqual(tien_tro_cap(1000, -4, 'g'), -1)   
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)    
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)  
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)  
        self.assertEqual(tien_tro_cap(1000, 2, 'g'), 1800)        
        self.assertEqual(tien_tro_cap(1000, 2, 'g'), 1800)  
        self.assertEqual(tien_tro_cap(1000, 4, 'g'), 2000)

    def test_age_group(self):
        self.assertEqual(tien_tro_cap(1000, 0, 't'), 0)  
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 0, 'A'), 0)  
    
    def test_tro_cap(self):
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)   
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)  
        self.assertEqual(tien_tro_cap(1000, -3, 't'), -1)  
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 0, 't'), 0)   
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)    
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)   
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)   
        self.assertEqual(tien_tro_cap(0, 3, 't'), 0)   
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)   
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)   
        self.assertEqual(tien_tro_cap(1000, -3, 't'), -1)   
        self.assertEqual(tien_tro_cap(1000, 0, 't'), 0)   
        self.assertEqual(tien_tro_cap(1000, 0, 't'), 0)   
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)  
        self.assertEqual(tien_tro_cap(0, 3, 't'), 0)   
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)   
        self.assertEqual(tien_tro_cap(1000, 3, 't'), 1800)   
        self.assertEqual(tien_tro_cap(1000, -4, 'g'), -1)   
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(0, 0, 'g'), 0)  
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)    
        self.assertEqual(tien_tro_cap(0, 1, 'g'), 0)    
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)    
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)    
        self.assertEqual(tien_tro_cap(1000, 4, 'g'), 2000)
        self.assertEqual(tien_tro_cap(0, 4, 'g'), 0)
        self.assertEqual(tien_tro_cap(1000, 2, 'g'), 1800) 
        self.assertEqual(tien_tro_cap(1000, 2, 'g'), 1800) 
        self.assertEqual(tien_tro_cap(1000, 2, 'g'), 1800) 
        self.assertEqual(tien_tro_cap(1000, 4, 'g'), 2000)
        self.assertEqual(tien_tro_cap(0, 4, 'g'), 0)
        self.assertEqual(tien_tro_cap(1000, 4, 'g'), 2000)
        self.assertEqual(tien_tro_cap(1000, 4, 'g'), 2000)

        
if __name__ == "__main__":
    unittest.main()
