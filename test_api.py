import unittest
from app import app

class BatchJobsApiTests(unittest.TestCase):
    def setUp(self): 
        app.testing = True
        self.client = app.test_client()

    def test_get_all_batch_jobs(self): # to make requests to API endpoints to assert expected results
        response = self.client.get('/batch_jobs')
        data = response.get_json()

        self.assertEqual(response.status_code, 200) # successful request
        self.assertIn('data', data)
        self.assertEqual(len(data['data']), 1000) 

    def test_filter_by_submitted_after(self): # test for filters on timestamp
        response = self.client.get('/batch_jobs?submitted_after=2023-03-01T00:00:00')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('data', data)

    def test_filter_by_max_nodes(self): # test for filters on number of nodes
        response = self.client.get('/batch_jobs?max_nodes=25')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('data', data)

if __name__ == '__main__':
    unittest.main()