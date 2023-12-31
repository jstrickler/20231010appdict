# Simplified SQLite3 Wrapper with Multi-Thread Safety

SQLite4 provides a simplified wrapper for SQLite3, along with built-in multi-thread safety.

## Installation

You can easily install SQLite4 using `pip3`:
````bash
pip3 install sqlite4
````
## Usage

````python
from  sqlite4  import  SQLite4

# Init database object, singleton pattern restricts multiple objects per db
database = SQLite4("database.db")
# Connect to db and creates execution thread
database.connect()
# Create test database and specify columns
database.create_table("test", ["foo", "bar"])
# insert
database.insert("test", {"foo": "foo", "bar": "bar"})
# update
database.update("test", {"foo": "fooo", "bar": "baar"}, "1 = 1")
# delete
database.delete("test", "1 == 1")
# select all
database.select("test")
# conditional select
database.select("test", columns=['foo'], condition='foo = "fooo"')
# custom query
database.execute(...)
````

## Multithreaded usage

````python
from  sqlite4.SQLite4  import  SQLite4
import  uuid
import  concurrent.futures

with  concurrent.futures.ThreadPoolExecutor(max_workers=50) as  executor:
	# This example shows how easy sqlite4 handles multithread access under the hood
	db = SQLite4("database.db")
	db.connect()
	db.create_table("test", ["foo", "bar"])
		def  insert():
			db.insert("test", {"foo": str(uuid.uuid4()), "bar": str(uuid.uuid4())})
	futures  = [executor.submit(insert) for  _  in  range(50)]
	concurrent.futures.wait(futures)
````

## How does it work ?

#### Singleton Pattern
The Singleton pattern restricts the instantiation of a class to just one object. When you create an instance of the SQLite4 class, it checks if an instance already exists for the specified database. If one does, it returns the existing instance; otherwise, it creates a new instance for the specified database. This design pattern is particularly useful for managing database connections, as it provides a centralized point of access.
#### Thread Safety with Execution Pipe
To ensure multi-thread safety and prevent potential deadlocks, SQLite4 utilizes an execution pipe. Whenever CRUD methods (Create, Read, Update, Delete) or custom SQL queries are called, the execution requests are sent to this pipe instead of directly accessing the database.
1.  When a CRUD method or custom SQL query is invoked, SQLite4 places the request in a queue that serves as the execution pipe.
2.  In a separate execution thread, the requests are processed one by one from the execution pipe.
3.  The separate thread reads the requests and executes them sequentially on the SQLite database.

# Contribute or Support the Project

Thank you for your interest in contributing to or supporting the SQLite4 project! Your contributions and support play a significant role in improving the library and making it more robust for everyone to use. There are several ways you can get involved:

### Contribute Code

If you are a developer and have ideas for new features, improvements, or bug fixes, we welcome your contributions. To contribute code, follow these steps:

1.  Fork the [SQLite4 repository](https://github.com/achaayb/sqlite4) to your GitHub account.
2.  Create a new branch for your changes: `git checkout -b feature/your-feature-name`.
3.  Implement your changes, following the project's coding standards and guidelines.
4.  Test your changes thoroughly to ensure they work as expected.
5.  Commit your changes and push them to your forked repository.
6.  Open a pull request (PR) to the main SQLite4 repository, describing the changes you made and why they are valuable.

### Report Issues

If you come across any bugs, issues, or have suggestions for improvements, please report them on the [GitHub issue tracker](https://github.com/achaayb/sqlite4/issues). Be as detailed as possible when describing the problem or suggestion to help us understand and address it effectively.

### Documentation

Clear and concise documentation is essential for any open-source project. If you find areas where the documentation can be improved or have ideas for new documentation topics, feel free to contribute to the project's documentation.

### Spread the Word

If you find SQLite4 helpful and valuable, consider spreading the word about it. Share the project with others who might benefit from its features. You can also give the project a star on GitHub to show your support.

### Financial Contributions

While SQLite4 is an open-source project maintained by volunteers, financial contributions help with hosting, maintenance, and future development. You can support the project via GitHub Sponsors

### Provide Feedback

Your feedback is essential for the project's continuous improvement. If you have suggestions or comments on how to make SQLite4 better, we are all ears. Feel free to reach out on the issue tracker or other communication channels provided by the project.

Whether you're contributing code, reporting issues, improving documentation, or providing feedback, your contributions are greatly appreciated. Together, we can make SQLite4 even more reliable and efficient for everyone to use!
