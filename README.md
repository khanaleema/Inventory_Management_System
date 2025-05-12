**🧠 Advanced OOP-Based Inventory Management System (Python)**






This project is a command-line based Inventory Management System built entirely using Object-Oriented Programming (OOP) principles in Python. It simulates real-world product inventory with support for different product categories like Electronics, Groceries, and Clothing — each modeled as separate classes with unique attributes and behaviors.





**🚀 Features**





📦 Add, Sell, Restock, and Remove Products





🔍 Search Products by Name or Type





📂 Save & Load Inventory from JSON Files





⏳ Automatically Prevent Sale of Expired Groceries




💸 View Total Inventory Value





🧪 Strong Error Handling with Custom Exceptions





**🧱 Clean Folder Structure with Separated Concerns**






**🛠 Technologies Used**





Python 3.x




OOP (Classes, Inheritance, Abstraction)




Abstract Base Classes (abc)





File Handling (JSON)




Custom Exception Handling





**🧪 Example Product Types**




**Electronics**




With brand and warranty details.




**Grocery**





With expiry tracking and date validation.





**Clothing**





Includes size and material information.




**💾 Saving & Loading Inventory**




You can persist your data using simple JSON file storage:




Save to File: Dumps all product data into a .json file.




Load from File: Reads and reconstructs all products back into the system.




**⚠️ Error Handling**




Robust custom exceptions make the system reliable:




ProductNotFoundError




InvalidProductTypeError




NegativeQuantityError




DuplicateProductIDError



**🧰 How to Run**





# Clone the repo



**git clone https://github.com/your-username/inventory-oop-system.git**




**cd inventory-oop-system**




# Run the program



python main.py



**📈 Future Enhancements**




GUI with Tkinter or PyQt





Product category reports





Advanced search filters





Unit testing integration





SQLite or MongoDB persistence





