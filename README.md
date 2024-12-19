# CCT211-CRUD-data-processing-application

What is this application?<br>
Main application<br>
Our application is a personal finance tracker that lets users organize and keep a record of their spending. The main file has CRUD capabilities with functions for adding, updating, deleting records and refreshing the table to make it easily readable. The finance tracker application has been given the catchy name “Coin Compass” for user satisfaction.<br>
Queries<br>
In addition, four SQL queries have been provided to allow users to summarize their transactions in terms of total income versus total expenses, all expenses from a specific category, the average expenses per month, and the highest expense in a certain category.<br><br>

Who will use this application?<br>
	The main demographic of this application is people who struggle with organizing and managing their finances. In particular, this would include young adults who are often irresponsible or inexperienced in handling their income and need help recording their transactions. However, a limitation of targeting this demographic is that seniors of approximately age 70 and older who struggle to use computer applications may not be able to easily access the application. Children and teenagers who do not have many funds available also might not find the application useful.<br><br>

What features are included in this application?<br>
The biggest feature of the application is its ability to create, read, update, and delete entries of a CSV file. The application features a comprehensive table containing a record of purchases including the name of the transaction category (e.g. food, rent, income, etc), how much was exchanged, and a full date system. The application is equipped with an intuitive user interface that displays the table with CSV entries on the left side of the screen and CRUD options on the right so users can see the modifications they make instantaneously. Dialog notifications are also included to confirm user actions, as well as confirm if the action is completed successfully to minimize the chance of input errors in entries.<br><br>

How to use these features?<br>
Creating a Record<br>
If the user wants to create a record, they can fill out the fields on the right side of the window, which allow them to input their desired category, amount, and date; titled accordingly. The “Category” input can only contain alphabetical characters without any numbers or special symbols, and the “Amounts” must only contain numerical inputs, including decimal places. Additionally, the inputted “Date” must follow the sequence ‘Year-Month-Day’, otherwise the output will be invalid and the system will not create a record. 
Deleting a Record<br>
Furthermore, if the user would like to delete a record, they can select one of the listed records featured on the left by clicking it, and then terminate it by clicking “Delete Record” on the right side of the window.<br>
Updating a Record<br>
Lastly, if the user wants to update a record, they must select their desired record on the left side of the window, then re-enter all the information for the “Category”, “Amount”, and “Date” on the right hand side of the screen (all “new record” validation checks remain applicable for this process). The user must then click the “Update Record” button under the input boxes.<br><br>


Hypothetical Example Runthrough<br>
As a user of the platform, I would like to add a record about yesterday’s food spending. First, I click on the “Category” input, where I enter the word “Food”. Next, I add the amount that I spent on food yesterday, which is 15.50. I then add the date that this occurred on, which would be 2024-11-28. Finally, I click the “Add Record” button and receive a dialog window that confirms my entry was successfully added. However, I would like to make a change because I accidentally input the wrong amount of money. To do so, I click the record I just created on the left side of my screen and re-input the information on the right: Food, 16.50, 2024-11-28. Lastly, I click “Update Record” and receive a notification that it is successfully edited. Lastly, I would like to delete this record from the tracker. To do so, I will click on the record I intend to delete on the left side of the window. Once selected, I click “Delete Record,” which erases the desired record from the platform and notifies me that the action was successful.<br><br>

Logices and Limitations<br>
For a user to delete a record on the table, they must physically click on the record rather than utilizing a specific field point as a reference, like a data value. Additionally, one cannot input a currency differing from the one previously used. All income or expenditure must be the same currency or converted for consistency throughout the application. Furthermore, users cannot select more than one record at a time to delete or update. This may cause difficulties with record management and slow down efficiency. Lastly, users cannot add records with multiple dates or date ranges. This can be problematic for inputting income or expenses that occur multiple times a month, once again delaying efficiency. <br>
