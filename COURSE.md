# Lab 7: Practicing Test Driven Development

Welcome to the **Practicing Test Driven Development** lab. It is important to understand the workflow for practicing true test driven development by writing the test cases first to describe the behavior of the code, and then writing the code to make the tests pass, thus ensure that it has that behavior. In this lab we will do just that.

## Update a counter

You will start by implementing a test case to test updating a counter. Following REST API guidelines, an update uses a `PUT` request and returns code `200_OK` if successful. Create a counter and then update it.

Then you’ll write the code to make the test pass. If you’re unfamiliar with Flask, note that all of the routes for the counter service are the same; only the method changes.

To start, you will implement a function to update the counter. Per REST API guidelines, an update uses a PUT request and returns a `200_OK` code if successful. Create a function that updates the counter that matches the specified name.

## Read a counter

Next, you will write a test case to read a counter. Following REST API guidelines, a read uses a `GET` request and returns a `200_OK` code if successful. Create a counter and then read it.

Once again, it's time to write code to make a test pass. You will implement the code for read a counter. Per REST API guidelines, a read uses a GET request and returns a `200_OK` code if successful. Create a function that returns the counter that matches the specified name.

## Delete a counter

Now you will write a test case to delete a counter. Per REST API guidelines, a read uses a `DELETE` request and returns a `204_NO_CONTENT` code if successful. Create a function that deletes the counter that matches the specified name.

In this last step, you will again write code to make a test pass. This time, you will implement the code to delete a counter. Per REST API guidelines, a delete uses a `DELETE` request and returns a `204_NO_CONTENT` code if successful.

# Step 1: Write a test for update a counter

You will start by implementing a test case to test updating a counter. Following REST API guidelines, an update uses a PUT request and returns code 200_OK if successful. Create a counter and then update it.

Your Task

In test_counter.py, create a test called test_update_a_counter(self). It should implement the following steps:

- Make a call to Create a counter.
- Ensure that it returned a successful return code.
- Check the counter value as a baseline.
- Make a call to Update the counter that you just created.
- Ensure that it returned a successful return code.
- Check that the counter value is one more than the baseline you measured in step 3.

## Solution

```
def test_update_a_counter(self):
    """It should increment the counter"""
    result = self.client.post("/counters/baz")
    self.assertEqual(result.status_code, status.HTTP_201_CREATED)
    data = result.get_json()
    baseline = data["baz"]
    # Update the counter
    result = self.client.put("/counters/baz")
    self.assertEqual(result.status_code, status.HTTP_200_OK)
    data = result.get_json()
    self.assertEqual(data["baz"], baseline + 1)
```

# Step 2: Implement update a counter

Now you粩te the code to make the test pass. If you宦amiliar with Flask, note that all of the routes for the counter service are the same; only the method changes.

To start, you will implement a function to update the counter. Per REST API guidelines, an update uses a PUT request and returns a 200_OK code if successful. Create a function that updates the counter that matches the specified name.

Your Task

In counter.py, create a function called update_counter(name). It should implement the following steps:

- Create a route for method PUT on endpoint /counters/<name>.
- Create a function to implement that route.
- Increment the counter by 1.
- Return the new counter and a 200_OK return code.

## Solution

```
@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Update a counter"""
    app.logger.info(f"Request to update counter: {name}")

    global COUNTERS
    COUNTERS[name] += 1

    app.logger.info(f"Counter: {name} is now {COUNTERS[name]}")
    return { name: COUNTERS[name] }, status.HTTP_200_OK
```

# Step 3: Write a test for read a counter

Next, you will write a test case to read a counter. Following REST API guidelines, a read uses a GET request and returns a 200_OK code if successful. Create a counter and then read it.

Your Task

In test_counter.py, create a test called test_read_a_counter(self). It should implement the following steps:

- Make a call to create a counter.
- Ensure that it returned a successful return code.
- Make a call to read the counter you just created.
- Ensure that it returned a successful return code.
- Check that the counter value returned is 0.

## Solution

```
def test_read_a_counter(self):
    """It should read the counter"""
    result = self.client.post("/counters/bin")
    self.assertEqual(result.status_code, status.HTTP_201_CREATED)
    # Read the counter
    result = self.client.get("/counters/bin")
    self.assertEqual(result.status_code, status.HTTP_200_OK)
    data = result.get_json()
    self.assertEqual(data["bin"], 0)
```

# Step 4: Implement read a counter

Once again, it’s time to write code to make a test pass. You will implement the code for read a counter. Per REST API guidelines, a read uses a GET request and returns a 200_OK code if successful. Create a function that returns the counter that matches the specified name.

Your Task

In counter.py, create a function called read_counter(name). It should implement the following steps:

- Create a route for method GET on endpoint /counters/<name>.
- Create a function to implement that route.
- Get the current value of the counter.
- Return the counter and a 200_OK return code.

## Solution

```
@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a counter"""
    app.logger.info(f"Request to read counter: {name}")

    counter = COUNTERS[name]

    app.logger.info(f"Counter: {name} is {counter}")
    return { name: counter }, status.HTTP_200_OK
```

# Step 5: Write a test for delete a counter

Now you will write a test case to delete a counter. Per REST API guidelines, a read uses a DELETE request and returns a 204_NO_CONTENT code if successful. Create a function that deletes the counter that matches the specified name.

Your Task

In test_counter.py, create a function called test_delete_a_counter(self). It should implement the following steps:

- Make a call to Create a counter.
- Ensure that it returned a successful return code.
- Make a call to delete the counter you just created.
- Ensure that it returned a successful return code.

## Solution

```
    def test_delete_a_counter(self):
        """It should delete the counter"""
        result = self.client.post("/counters/fob")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        # Delete the counter
        result = self.client.delete("/counters/fob")
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)
```

# Step 6: Implement delete a counter

In this last step, you will again write code to make a test pass. This time, you will implement the code to delete a counter. Per REST API guidelines, a delete uses a DELETE request and returns a 204_NO_CONTENT code if successful.

Your Task

In counter.py, create a function called delete_counter(name). It should implement the following steps:

- Create a route for method DELETE on endpoint /counters/<name>.
- Create a function to implement that route.
- Delete the counter that matches the name.
- Return the counter and a 204_NO_CONTENT return code.

## Solution

```
@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a counter"""
    app.logger.info(f"Request to delete counter: {name}")

    del(COUNTERS[name])

    app.logger.info(f"Counter: {name} has been deleted")
    return '', status.HTTP_204_NO_CONTENT
```
