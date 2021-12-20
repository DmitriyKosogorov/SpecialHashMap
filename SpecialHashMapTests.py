from SpecialHashMap import SpecialHashMap
from unittest import TestCase, main


class SHMiloctest(TestCase):
    def test_exercise(self):
        map = SpecialHashMap()
        map["value1"] = 1
        map["value2"] = 2
        map["value3"] = 3
        map["1"] = 10
        map["2"] = 20
        map["3"] = 30
        map["1, 5"] = 100
        map["5, 5"] = 200
        map["10, 5"] = 300
        
        self.assertEqual(10, map.iloc[0])
        self.assertEqual(300, map.iloc[2])
        self.assertEqual(200, map.iloc[5])
        self.assertEqual(3, map.iloc[8])
        
        with self.assertRaises(Exception) as context:
            map.iloc[1000]
        self.assertTrue('list index out of range' in str(context.exception))
        
        with self.assertRaises(Exception) as context:
            map.iloc['0']
        self.assertTrue('list indices must be integers or slices, not str' in str(context.exception))
        map[10] = 300
        with self.assertRaises(Exception) as context:
            map.iloc
        self.assertTrue('iloc Function cannot work with dictionary with nonstring keys' in str(context.exception))
        
        
class SHMploctest(TestCase):
    def test_exercise(self):
        map = SpecialHashMap()
        map["value1"] = 1
        map["value2"] = 2
        map["value3"] = 3
        map["1"] = 10
        map["2"] = 20
        map["3"] = 30
        map["(1, 5)"] = 100
        map["(5, 5)"] = 200
        map["(10, 5)"] = 300
        map["(1, 5, 3)"] = 400
        map["(5, 5, 4)"] = 500
        map["(10, 5, 5)"] = 600
        
        
        self.assertEqual({'1':10,'2':20,'3':30},map.ploc[">=1"])
        self.assertEqual({'1':10, '2':20},map.ploc["<3"])
        self.assertEqual({'(1, 5)':100, '(5, 5)':200, '(10, 5)':300},map.ploc[">0, >0"])
        self.assertEqual({'(10, 5)':300},map.ploc[">=10, >0"])
        self.assertEqual({'(1, 5, 3)':400},map.ploc["<5, >=5, >=3"])
        self.assertEqual({'(1, 5, 3)': 400, '(5, 5, 4)': 500, '(10, 5, 5)': 600},map.ploc["(((<100 <100 <100)))"])
        self.assertEqual({'(10, 5)':300},map.ploc["((>=10,()) >0))"])
        self.assertEqual({},map.ploc[">0, >0, >0,>0 "])
            
        with self.assertRaises(Exception) as context:
            map.ploc['(>0>0>0)']
        self.assertTrue('No separator found' in str(context.exception))
        
        with self.assertRaises(Exception) as context:
            map.ploc['(>0; >0. >0)']
        self.assertTrue('Invalid key for ploc function' in str(context.exception))
        
        with self.assertRaises(Exception) as context:
            map.ploc['(>0; clxkjvlxfcvhilkjfbxlidhb; >0)']
        self.assertTrue('Invalid key for ploc function' in str(context.exception))
        
        with self.assertRaises(Exception) as context:
            map.ploc['(0)']
        self.assertTrue('Invalid key for ploc function' in str(context.exception))
        map[(1,2)]=101
        with self.assertRaises(Exception) as context:
            map.ploc['>0']
        self.assertTrue('ploc Function cannot work with dictionary with nonstring keys' in str(context.exception))

if __name__ == "__main__":
    main()
