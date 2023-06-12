# OLCF Software Services Development Team - Coding Exercise 01 Solution

## Batch Job Records

### Understanding of this project and the job done

Based on what the specifications, I was asked to create a web-app that provides a single RESTful API endpoint for retrieving filtered batch job records from a dataset. <br />
Now this project was really a good point for me to learn Ruby and showcase my proficiency in OOP but I was under time crunch and had to pass on it and did this project in Python using Flask. <br />
As far as db goes since I used Flask CSV data was loaded into memory when the server starts, and the reqd. ETL was performed that used the filtering logic to data based on provided query params. The code ensured that filtered records is returned in JSON-API document format.<br />
Unit tests have been performed which are pretty straightforward and naive.

#### Installation Guide and how to run the code
1. Open the folder in IntelliJ/ VSCode/ any IDE of your choice.
2. Open the terminal and be inside the `support-software-interview-exercise-01` directory.
3. Create a virutal env inside this folder: `python -venv venv`
    => If you haven't ever created a virutal env earlier you can write the command `pip install virtualenv`
4. Activate the virtual env:
    => Windows: `venv\Scripts\activate.bat`
5. Start the server: `python app.py`
6. Access the API endpoint at: `http://localhost:5000/batch_jobs`
7. Query parameters can be given as follows:<br />
    => Get batch jobs submitted after February 28, 2023: `http://localhost:5000/batch_jobs?submitted_after=2023-02-28T00:00:00`<br />
    => Get batch jobs submitted before March 1, 2023: `http://localhost:5000/batch_jobs?submitted_before=2023-03-01T23:59:59`<br />
    => Get batch jobs that used at least 10 nodes: `http://localhost:5000/batch_jobs?min_nodes=10`<br />
    => Get batch jobs that used at most 20 nodes: `http://localhost:5000/batch_jobs?max_nodes=20`<br />
    => Get batch jobs submitted after February 28, 2023 and 
    get batch jobs that used at most 35 nodes: `http://localhost:5000/batch_jobs?submitted_before=2023-03-01T23:59:59&max_nodes=35`
8. How to check for test cases:
    => `BatchJobsApiTests` class that inherits from `unittest.TestCase`. Each test method within the class represents a specific test case. I set up the Flask application in the setUp method and use app.test_client() to create a test client for making requests. We make a request to the `/batch_jobs` endpoint without any filters and assert that the response status code is 200 (indicating a successful request) and that the response data contains the expected number of batch job records.<br />
    => To run the tests, you can execute the test file using `python -m unittest test_api.py`.

#### Future Works

1. Can have an external database like PostgreSQL or SQLite.
2. Pagination can be implemented to handle large datasets.
3. Input Validation can enhance the application in terms of how incorrect requests are handled gracefully alognside providing clients with error messages.
4. Performance optimization, in this half of the work would be done if the whole dataset is dealt with techniques such as indexing, caching or even query optimization.
5. Ofcourse all these features won't be possible on Flask, shifting to a better framework should also be considered.


#### Conclusion
Firstly, thank you for this take home assignment, I had fun doing this assignment. Thank you for considering my application and for your time. Looking forward to hearing more about next steps if we are moving forward with my application. I am confident I can bring great value to the team and we both can create some amazing data products and applications. Thank you!