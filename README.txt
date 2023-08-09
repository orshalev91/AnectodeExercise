Anecdote Plugins Exercise - Instructions

1. Open a terminal or command prompt.

2. Navigate to the directory containing the 'main.py' and 'test.py' files.

3. Install "requests" library using the next command:
    python -m pip install requests

4. Enter a dummyapi.io token in 'evidences\base_evidence.py' line 3 "MY_TOKEN" variable, or use the provided token

5. Run the 'main.py' file with the follong command: 
    python -m main

6. The script will perform a connectivity test and will print the connection status.
   If the connectivity test failed the script will stop.
   If the connectivity test passed the script will continue and will gather the users and posts evidences:
        "UserEvidence" - the class will collect all the users data and will save it in a json file called "users.json"
        "PostEvidence" - the function will collect the last 50 posts (if exists), add to each post its relevant comments and will save the data in a json file called "posts.json"

    In case an api call will fail the files won't get created

7. To run unittests use the next command: 
    python -m unittest test.py
    