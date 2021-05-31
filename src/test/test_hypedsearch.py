import unittest
import sys    

class Test_Main(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, "../hypedsearch")
        import hypedsearch
        print("setUp run")
        
    def test_add_pass(self):
        self.assertEqual(2, 2, "Should pass")
        print("test_add_pass run")

    #def test_main_pass(self):
    #    main_arguments = hypedsearch.Main_Arguments()
    #    main_arguments.spectra_folder = "C:\MyFolder"
    #    self.assertEqual(main_arguments.spectra_folder, "C:\MyFolder", "spectra_folder is incorrect")      
        
if __name__ == "__main__":
    unittest.main()

