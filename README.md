# PII-Data-Masking-Forms

**This system aims to protect sensitive information such as names, addresses, phone numbers, and other identifiable data by applying masking techniques in real-time.
The project also includes a dynamic threshold feature that triggers alerts or actions when the number of detected PII entries exceeds a predefined limit.**

**Technology Stack**
Frontend:

1. HTML/CSS: For creating the user interface of the forms.
   Backend:

2. Python: Handles the logic for masking personally identifiable information (PII) based on the predefined threshold.
   Data Masking Logic:

3. Custom Python Algorithms: Logic for detecting and masking sensitive information in the form fields.
   Deployment:

4. Glitch (considered): As a deployment platform for hosting the application. Offers free hosting for lightweight projects.
   Potential Cloud Option: Consideration of other cloud platforms for active deployment while managing potential AWS fees.
   Version Control:

5. GitHub: Code repository for version control and collaboration.
   GitHub Repo
   Open-Source Tools:

**Installation Guide**

Prerequisites:
https://github.com/PournimaTivatane12/PII-Data-Masking-Forms/blob/main/Prerequisites

**Usage**

The PII Data Masking Forms project allows users to mask sensitive Personally Identifiable Information (PII) entered through forms.
This usage guide will help you understand how to interact with the project after installation.

Running the Application Locally
After completing the installation steps, you can run the application locally by executing the following command:

python app.py

Accessing the Web Application
Open your web browser and go to http://localhost:5000 (or the port defined in your settings).
You will be presented with a form interface where you can input data.
The form will automatically detect and mask any PII based on the specified masking rules.
Example Input
When you submit the form, the backend processes the data, detecting sensitive PII and masking it. For example:

Input:

Name: John Doe
Email: john.doe@example.com
Phone: +1234567890

Output:

Name: J*** D**
Email: j***.d*@example.com
Phone: +12**********

Customizing Masking Thresholds
The application is designed with a default masking threshold of 10. This means that when the number of sensitive characters exceeds this threshold, the data will be masked.
You can customize this threshold by editing the .env file:

Open the .env file located in the root directory.
Change the MASKING_THRESHOLD value to your desired limit.

MASKING_THRESHOLD=15
API Endpoints
The project also exposes some API endpoints for interacting with the PII masking logic. These endpoints can be accessed programmatically or via tools like Postman or curl.

POST /mask
Description: Accepts JSON input, detects PII in the fields, and returns masked data.
Example Request:

curl -X POST http://localhost:5000/mask -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'

Example Response:

{
  "name": "J*** D**",
  "email": "j***.d*@example.com"
}
Deployed Version

Once the application is deployed, you can use the deployed URL instead of localhost. The deployed version behaves similarly to the local version but is hosted in the cloud for ease of access and sharing.

**Screenshots**

![image](https://github.com/user-attachments/assets/31011684-e4d4-4308-80ce-2ec2fae717b4)

![image](https://github.com/user-attachments/assets/19f84578-f4bc-4d04-b663-60a4dc92e056)


The PII Data Masking Forms project offers a comprehensive solution for handling and protecting Personally Identifiable Information (PII) in forms. Below are the key features:

1. Automatic PII Detection
The system detects sensitive data such as names, emails, phone numbers, and other PII entered into the form.
Uses customizable rules to identify PII without needing manual input on what fields are sensitive.

3. Data Masking
Automatically masks detected PII according to the predefined rules.
Ensures sensitive information like emails, phone numbers, and personal names are safely obscured before storage or further processing.
The masking format can be customized (e.g., partial masking of email addresses or phone numbers).

5. Customizable Masking Threshold
Offers an environment variable (MASKING_THRESHOLD) that allows users to set the threshold for triggering data masking.
Allows for flexibility in defining when and how data should be masked, based on the size or sensitivity of the input.

7. User-Friendly Interface
Simple and intuitive HTML-based form interface for easy user interaction.
Users can easily submit personal data while being confident that sensitive details will be masked appropriately.

9. API Access for Developers
Exposes REST API endpoints that allow developers to send PII data programmatically and receive masked responses.
Ideal for integrating with other systems that handle sensitive data.

11. Error Handling and Validation
Includes validation for common input types like email addresses and phone numbers to ensure correct formatting before data is processed.
Provides error messages for invalid inputs, improving the user experience.

13. Cross-Platform Deployment
Can be deployed across various platforms, including local environments, cloud providers, and lightweight hosting solutions like Glitch or Cyclic.
Easy to set up and run without requiring extensive infrastructure.

15. Open-Source and Extensible
Fully open-source and customizable, allowing developers to extend or modify the masking rules to fit specific use cases.
Contributions and improvements are welcomed from the community.


**Contributions & License**

Contributions are welcome and greatly appreciated! If you have any ideas, bug reports, or suggestions for improvements, feel free to contribute to the project.

How to Contribute

Fork the Repository: Click the "Fork" button at the top of this page to create your own copy of the repository.
Clone Your Fork: Clone your forked repository to your local machine.

git clone https://github.com/PournimaTivatane12/PII-Data-Masking-Forms
Create a New Branch: Create a new branch for your contribution.

git checkout -b feature/your-feature-name
Make Your Changes: Implement your feature or fix and commit your changes.

git commit -m "Add feature: your-feature-name"
Push to Your Fork: Push the changes to your forked repository.

git push origin feature/your-feature-name
Submit a Pull Request: Open a pull request from your fork to the original repository for review.

Contribution Guidelines

Ensure your code follows the style and structure of the existing codebase.
Write clear and concise commit messages.
Include relevant documentation and update the README if necessary.
Provide tests if you are introducing new functionality.
Thank you for your interest in contributing to this project!

License
This project is licensed under the MIT License.





























