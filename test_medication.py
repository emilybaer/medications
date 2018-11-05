import unittest
import medication

class TestMedication(unittest.TestCase):

    def test_get_medications_by_id(self):
        medications_by_id = medication.get_medications_by_id(list_of_medications())
        expected = hash_of_medications()
        self.assertEqual(medications_by_id, expected)

    def test_get_generics(self):
        test_cases = [
            {
                'test_name': 'single rxcui',
                'active_only': False,
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'3',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'4',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    }
                ],
                'expected': {
                    '100': ['1', '2']
                }
            },
            {
                'test_name': 'multiple rxcui',
                'active_only': False,
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'3',
                        'rxcui':'101',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'4',
                        'rxcui':'101',
                        'generic':False,
                        'active':True
                    }
                ],
                'expected': {
                    '100': ['1'],
                    '101': ['3']
                }
            },
            {
                'test_name': 'inactive rxcui, active_only=True',
                'active_only': True,
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':True,
                        'active':False
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'3',
                        'rxcui':'101',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'4',
                        'rxcui':'101',
                        'generic':False,
                        'active':False
                    }
                ],
                'expected': {
                    '101': ['3']
                }
            },
            {
                'test_name': 'inactive rxcui, active_only=False',
                'active_only': False,
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':True,
                        'active':False
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'3',
                        'rxcui':'101',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'4',
                        'rxcui':'101',
                        'generic':False,
                        'active':False
                    }
                ],
                'expected': {
                    '100': ['1'],
                    '101': ['3']
                }
            }
        ]

        for test in test_cases:
            generics = medication.get_generics(
                medications=test['medications'],
                active_only=test['active_only']
            )
            self.assertEqual(generics, test['expected'], test['test_name'])


    def test_get_prescription_updates(self):
        test_cases = [
            {
                'test_name': 'prescription needs updating to generic',
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    },
                ],
                'prescriptions': [
                    {
                        'medication_id':'1',
                        'id':'a'
                    }
                ],
                'expected_updates': [
                    {
                        'prescription_id':'a',
                        'medication_id':'2'
                    }
                ]
            },
            {
                'test_name': 'prescription has no generics',
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                ],
                'prescriptions': [
                    {
                        'medication_id':'1',
                        'id':'a'
                    }
                ],
                'expected_updates': []
            },
            {
                'test_name': 'prescription already uses generic',
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                ],
                'prescriptions': [
                    {
                        'medication_id':'1',
                        'id':'a'
                    }
                ],
                'expected_updates': []
            },
            {
                'test_name': 'prescription has multiple generic options',
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'3',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                ],
                'prescriptions': [
                    {
                        'medication_id':'1',
                        'id':'a'
                    }
                ],
                'expected_updates': [
                    {
                        'prescription_id':'a',
                        'medication_id':'2'
                    }
                ]
            },
            {
                'test_name': 'multiple generic subtitutions',
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    },
                    {
                        'id':'3',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    }
                ],
                'prescriptions': [
                    {
                        'medication_id':'1',
                        'id':'a'
                    }
                ],
                'expected_updates': [
                    {
                        'prescription_id':'a',
                        'medication_id':'2'
                    }
                ]
            },
            {
                'test_name': 'prescription medication not in medication list',
                'medications': [
                    {
                        'id':'1',
                        'rxcui':'100',
                        'generic':False,
                        'active':True
                    },
                    {
                        'id':'2',
                        'rxcui':'100',
                        'generic':True,
                        'active':True
                    }
                ],
                'prescriptions': [
                    {
                        'medication_id':'5',
                        'id':'a'
                    }
                ],
                'expected_updates': []
            }
        ]

        for test in test_cases:
            updates = medication.get_prescription_updates(
                test['medications'],
                test['prescriptions']
            )
            self.assertEqual(updates, test['expected_updates'], test['test_name'])

def list_of_medications():
    return [
        {
            'id':'564aab6f3032360003000000',
            'ndc':'000000001',
            'rxcui':'01010',
            'description':'Aspirin 10 MG',
            'generic':True,
            'active':True,
            'created_at':'2015-11-17T04:22:07.390Z',
            'updated_at':'2015-11-17T04:22:07.390Z'
        },
        {
            'id':'564aab6f3032360003010000',
            'ndc':'000000002',
            'rxcui':'01010',
            'description':'Bayer 10 MG',
            'generic':False,
            'active':True,
            'created_at':'2015-11-17T04:22:07.475Z',
            'updated_at':'2015-11-17T04:22:07.475Z'
        },
        {
            'id':'564aab6f3032360003020000',
            'ndc':'000000003',
            'rxcui':'01050',
            'description':'Aspirin 50 MG',
            'generic':True,
            'active':True,
            'created_at':'2015-11-17T04:22:07.528Z',
            'updated_at':'2015-11-17T04:22:07.528Z'
        },
    ]

def hash_of_medications():
    return {
        '564aab6f3032360003000000': {
            'id':'564aab6f3032360003000000',
            'ndc':'000000001',
            'rxcui':'01010',
            'description':'Aspirin 10 MG',
            'generic':True,
            'active':True,
            'created_at':'2015-11-17T04:22:07.390Z',
            'updated_at':'2015-11-17T04:22:07.390Z'
        },
        '564aab6f3032360003010000': {
            'id':'564aab6f3032360003010000',
            'ndc':'000000002',
            'rxcui':'01010',
            'description':'Bayer 10 MG',
            'generic':False,
            'active':True,
            'created_at':'2015-11-17T04:22:07.475Z',
            'updated_at':'2015-11-17T04:22:07.475Z'
        },
        '564aab6f3032360003020000': {
            'id':'564aab6f3032360003020000',
            'ndc':'000000003',
            'rxcui':'01050',
            'description':'Aspirin 50 MG',
            'generic':True,
            'active':True,
            'created_at':'2015-11-17T04:22:07.528Z',
            'updated_at':'2015-11-17T04:22:07.528Z'
        },
    }

if __name__ == '__main__':
    unittest.main()
