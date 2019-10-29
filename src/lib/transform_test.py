import random
import transform as tr
import unittest 
  
class WindowTest(unittest.TestCase): 
  
    # TODO: test for nd arrays 
    def test_correctly_segment_and_aggregate_1d_vec(self):
        results = []
        data = lambda a: list(range(a))
        g = lambda a, b: tr.window_segment(a, b)
        f = lambda a: tr.window_aggregate(a)
        
        for n in range(1, 1000):
            a = data(n)
            b = random.randint(1, n)  
            result = f(g(a, b))==a
            results.append(results) 
            
        err = results.count(False) 
        self.assertTrue(err==0) 
  
if __name__ == "__main__": 
    unittest.main() 
