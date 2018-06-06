import os
import unittest

from brain.core.ConfigurationManager.DnaLoader import DnaLoader
from brain.core.Models.Dna import Dna


class TestDnaLoader(unittest.TestCase):

    def setUp(self):
        if "/tests" in os.getcwd():
            self.dna_test_file = "modules/test_valid_dna.yml"
        else:
            self.dna_test_file = "tests/modules/test_valid_dna.yml"

    def tearDown(self):
        pass

    def test_get_yaml_config(self):

        expected_result = {'brain_supported_version': [0.1],
                           'author': 'Alexander Paul P. Quinit',
                           'type': 'neuron',
                           'name': 'neuron_test',
                           'tags': ['test']}

        dna_file_content = DnaLoader(self.dna_test_file).get_yaml_config()

        self.assertEqual(dna_file_content, expected_result)

    def test_get_dna(self):

        expected_result = Dna()
        expected_result.name = "neuron_test"
        expected_result.module_type = "neuron"
        expected_result.tags = ['test']
        expected_result.author = 'Alexander Paul P. Quinit'
        expected_result.brain_supported_version = [0.1]

        dna_to_test = DnaLoader(self.dna_test_file).get_dna()

        self.assertTrue(dna_to_test.__eq__(expected_result))

    def test_load_dna(self):
        # test with a valid DNA file
        dna_to_test = DnaLoader(self.dna_test_file)._load_dna()

        self.assertTrue(isinstance(dna_to_test, Dna))

        # test with a non valid DNA file
        if "/tests" in os.getcwd():
            dna_invalid_test_file = "modules/test_invalid_dna.yml"
        else:
            dna_invalid_test_file = "tests/modules/test_invalid_dna.yml"

        self.assertIsNone(DnaLoader(dna_invalid_test_file)._load_dna())

    def test_check_dna(self):
        # check with valid DNA file
        test_dna = {'brain_supported_version': [0.1],
                    'author': 'Alexander Paul P. Quinit',
                    'type': 'neuron',
                    'name': 'neuron_test',
                    'tags': ['test']}

        self.assertTrue(DnaLoader(file_path=self.dna_test_file)._check_dna_file(test_dna))

        # invalid DNA file, no name
        test_dna = {'brain_supported_version': [0.1],
                    'author': 'Alexander Paul P. Quinit',
                    'type': 'neuron',
                    'tags': ['test']}

        self.assertFalse(DnaLoader(file_path=self.dna_test_file)._check_dna_file(test_dna))

        # invalid DNA file, no type
        test_dna = {'brain_supported_version': [0.1],
                    'author': 'Alexander Paul P. Quinit',
                    'name': 'neuron_test',
                    'tags': ['test']}

        self.assertFalse(DnaLoader(file_path=self.dna_test_file)._check_dna_file(test_dna))

        # invalid DNA, wrong type
        test_dna = {'brain_supported_version': [0.1],
                    'author': 'Alexander Paul P. Quinit',
                    'type': 'doesnotexist',
                    'name': 'neuron_test',
                    'tags': ['test']}

        self.assertFalse(DnaLoader(file_path=self.dna_test_file)._check_dna_file(test_dna))

        # invalid DNA, no brain_supported_version
        test_dna = {'author': 'Alexander Paul P. Quinit',
                    'type': 'neuron',
                    'name': 'neuron_test',
                    'tags': ['test']}
        self.assertFalse(DnaLoader(file_path=self.dna_test_file)._check_dna_file(test_dna))

        # invalid DNA, brain_supported_version empty
        test_dna = {'brain_supported_version': [],
                    'author': 'Alexander Paul P. Quinit',
                    'type': 'neuron',
                    'name': 'neuron_test',
                    'tags': ['test']}

        self.assertFalse(DnaLoader(file_path=self.dna_test_file)._check_dna_file(test_dna))

        # invalid DNA, brain_supported_version wrong format
        test_dna = {'brain_supported_version': ['0.1.1'],
                    'author': 'Alexander Paul P. Quinit',
                    'type': 'neuron',
                    'name': 'neuron_test',
                    'tags': ['test']}

        self.assertFalse(DnaLoader(file_path=self.dna_test_file)._check_dna_file(test_dna))
