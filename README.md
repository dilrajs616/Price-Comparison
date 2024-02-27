# Pre-Requisits for project setup:
1. Python (preferably latest version) installed on your device.
2. MongoDB account.

# Steps for project setup.
1. Clone this repository on your pc.
2. In the project repository, open terminal and type "python.exe -m venv venv" to create a virtual environment.
3. In terminal run "venv\Scripts\activate.bat" to activate the virtual environment.
4. Check bottom right of your VS Code, if it says "3.12.1 64-bit" (your global python version) that means virtual environment has not been selected as the python interpreter for this directory.
5. To set venv enterpreter, click on "3.12.1 64-bit" (your global python version) on the bottom right side of your screen, it will open a propmt on the top to select python interpreter. Now click on "Enter interpreter path...", now go to the venv>Scripts>python.exe in working directory and copy its path. Now paste this path in the prompt to enter interpreter path. After this you have to kill the terminal and open new terminal.
6. Now the bottom right of VS Code should say "3.12.1 ('venv':venv)" (your python version in virtual environment).
7. Run "pip install -r requirements.txt". This should install all the external libraries that are required to run this project.
8. In main directory create ".env" file.
9. In terminal type "python.exe" and click enter. Type "import secrets" and then print(secrets.token_hex(20)). Copy the result.
10. In ".env" file type "SECRET_KEY=" and paste the secret key that you copied from terminal.
11. Now go to your MongoDB account on browser create a new cluster and copy its URI. In this URI replace "<password>" with your cluster's password.
12. Again go to ".env" file and type "MONGO_URI=" in next line and paste your URI with replaced password and save the file.
13. All set. Run "flask run" in working directory to run the project.
