Development using 
Google Cloud Platform
And
Visual Studio Code
Table of Contents

Setting up in the Google Cloud
Creating Your Project
Claim your Education Credits as in the email you received.
You will need to use your smcm.edu account for all your interactions with the Google Cloud Platform.
Goto https://console.cloud.google.com .
Tick the box to accept the Terms of Service.
Click Agree and Continue.
Click Select a Project.
Click New Project (in the top right corner.
In Project Name type your name and -00 (as in simon-read-00).
Your Organization and Location should be smcm.edu.
Click on the button that says Create
In the Notifications panel (to the right) under your project name, click Select Project.
Select the three bars in the top left of the window.
Select Cloud Overview
Select Dashboard
Creating Your Server
From the Dashboard, under Resources click Compute Engine.
Possibly click on enable
In the new panel at the top, click on Create Instance.
Click on Enable
Navigate back to Compute Engine
In name, put your name then -instance-00 (as in simon-read-instance-00)
Select Region as us-central-1 (Iowa) (probably the default).
Select Any for Zone (probably the default).
Ensure General purpose is selected.
Ensure E2 is selected.
In the left panel, select OS and Storage
Select Change.
Under Operating System select “Ubuntu”
Ensure the Version is Ubuntu 20.04 LTS.
Click Select
Click on Networking in the left panel
Under the Firewall heading check the boxes “Allow HTTP Traffic” and “Allow HTTPS Traffic”
Scroll down click on default in Network Interfaces.
Click the dropdown to expand “Default” under “Network Interfaces”
Ensure under External IPv4 Address “Ephemeral” is selected. (probably default)
Under Network Service Tier select Standard
Click Create at the bottom of the window
Stopping Your Instance
Remember to Stop your instance every time you have finished working with it, or it will continue to charge against your Educational Credits and you will run out!

In the Compute Engine – VM Instances window
Select the three dots for your instance (you may need to scroll the main screen to see all the options under this menu).
Select Stop
The Status icon will change from a tick mark in a green circle to a white square in a grey circle.
Restarting Your Instance
In the Compute Engine – VM Instances window
Select the three dots for your instance
Select Start
In the modal window that comes up click Start
The Status icon will change from a white square in a grey circle to a tick mark in a green circle.

Setting Up Visual Studio Code
Installing Visual Studio Code
Download Visual Studio Code from https://code.visualstudio.com/download and follow the installation instructions.
Installing Visual Studio Code Extensions
Open Visual Studio Code
Click on View:Extensions
In the Search Bar, search for the following extensions and click install for each one:
Remote Development (by Microsoft)
Remote – SSH (by Microsoft)
Python (The Microsoft Developed Extension)
Django (by Baptiste Darthenay)
MarkDown All In One (by Yu Zhang)
GitHub Markdown Preview (by Matt Bierner)
Getting SSH for Windows 
You should already have SSH on your computer (applicable to macbook, windows, and Linux machines). Open a terminal and type the command “ssh”. As long as it doesn't return an error, you have an SSH client installed.

IF RUNNING THE COMMAND “ssh” IT DOESN’T RETURN AN ERROR, YOU CAN SKIP ALL OF THIS AND MOVE TO FIND YOUR EXTERNAL IP ADDRESS
Installing PowerShell on Windows
PowerShell should already be installed on your computer, if it is not then follow the instructions at https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5
Installing the OpenSSH client on Windows
The OpenSSH client should have been installed when you installed the Remote Development plug-in for Visual Studio Code.  If that is not the case then follow the instructions at https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui&pivots=windows-server-2025
Testing your OpenSSH installation
Search for and open the PowerShell application (running regular should work just fine)
Type ssh <username>@login.cs.smcm.edu to log in to the CS server as you did in Computer Architecture and/or Programming Languages
You should be asked if a key is okay, accept it.
Check that you are at the server by typing hostname.  You should get the response prometheus.

Cygwin Warning
You may have Cygwin (a Unix emulation suite) installed and this might be what’s used by Remote – SSH later.  If you think this is the case, consult an expert but you might try the following:
Locate the cygwin directory (usually C:\cygwin).
Copy your ed25519 key from C:\Users\<username>/.ssh
Paste it into Cygwin’s .ssh directory
Start bash.exe in Cygwin’s bin directory
Type the command chmod 400 .ssh/ed25519
Getting SSH for macOS
SSH is installed by default in macOS.  All you need to do is open the Terminal application to get a Unix Command line.
Getting SSH for Linux
Most Linux distributions install the SSH client by default (but not the server, which you will not need).  If you find that your distribution has not installed the client, then use Google to find instructions specific to your distribution.
All you need to do is to open a Terminal and type your commands there.
To Find the External IP Address of your VM Instance
Make sure your instance is running.
Scroll the VM instances window to the left (or is it right) until you see the External IP box.
The dotted quad in that box is your external IP.
Connecting to your Google Cloud VM through Visual Studio Code
Setting up a SSH Keypair. 
You will need to do this for every unique computer you want to connect to the cloud. These keypairs will also work for multiple different instances, you do not have to create a new keypair for every VM instance you create.
Open Windows Powershell or Linux Terminal or Macbook Terminal
Run the command: ssh-keygen -t ed25519
Click enter 3 times
Run the command: cat .ssh/id_ed25519.pub
Copy the output of the above command
Navigate to your Google Cloud VM Dashboard
On the left side of the page, click the 3 line dropdown menu and navigate to the Compute Engine tab. 
On the left side, scroll down until you see the metadata tab, click this to open it.
Click on the SSH keys tab.
Click on “Add SSH Key”
Paste in the output of the command we ran earlier that you copied, and save.
Connecting in Visual Studio Code
Open the command palette by pressing F1 (Windows) or pressing CTRL+SHIFT+P (ChromeBook) or CMD+SHIFT+P (MacBook)
In the popup, enter “Remote-SSH: Connect to Host” and press enter
In the prompt to enter the host, and the username next to the key you put into the Google Cloud VM ssh key section, for example, johndoe
Then, next to your username and @, add the external IP address to your Google Cloud vm
It will look like this johndoe@123.456.78.901
Hit enter
It is important to note that if you’re working across multiple computers, you must use the name of each machine, so if machine 1 is john, and machine 2 is johndoe you must use the respective names
From here, a new Visual Studio Code window should appear. Select Linux in the drop down menu for the cloud software type
You may need to enter “yes” or “continue” into the console to accept the new SSH footprint, if prompted

Using the Visual Studio Code Editor
Top left of VS, press File
Click “Open Folder”
Navigate to the folder you want to open, then click “Open Folder”
In your explorer, you should now be able to access the files you want to work with!

Setting up your Google Cloud VM
Installing all the dependencies and apps your Virtual Machine will need
Enter the console for your Virtual Machine, this can be done in various ways YOU ONLY NEED TO FOLLOW ONE OF THESE STEPS TO OPEN YOUR TERMINAL, YOU DO NOT NEED TO DO ALL 3
Open a Windows Powershell and type the command “ssh johndoe@123.456.78.901” where in you replace johndoe@123.456.78.901 with your credentials and the ip address you want to connect to
Connect to the virtual machine on Visual Studio and open terminal, which will automatically enter the VM <- Easiest Way
On the google cloud console where you activate the VM, click on the ssh button. This will open a new window that is linked to the VM
Creating a shared workgroup
Open terminal (CTRL+J on Windows and Chromebook, CMD+J on Macbook)
sudo mkdir /home/shared_workspace
sudo groupadd sharedgroup
sudo usermod -aG sharedgroup name (repeat for however many users need access, where name is the name of the users youve connected from)
sudo chown -R root:sharedgroup /home/shared_workspace
sudo chmod -R 2770 /home/shared_workspace
sudo chmod g+s /home/shared_workspace
This creates a folder in the home directory called shared_workspace where all users added in step C are able to access and modify files
Restart your Google Cloud VM Session to update user permissions



Important Notice: You will need separate Virtual Machines for CCC and CDSpec. Please follow the instructions for the creation of a VM twice. You will NOT need to create a new keypair for this new virtual machine however.

Installing everything necessary
In your first virtual machine do the following:
Part I: CCC Installation & Execution
Configuring your Virtual Machine for git, python, and other dependencies
cd /home/shared_workspace
sudo apt update
sudo apt upgrade -y
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-dev
sudo apt install git
git config --global user.name "****" (between “” needs to be the github username”
git config --global user.email "****" (between the “” needs to be the github email address”
git init
git clone https://github.com/swbn1/ChesapeakeCommunityConnect-FA24
python3.10 -m ensurepip
python3.10 -m pip install --upgrade pip 
sudo apt install libapache2-mod-wsgi-py3
Select Y to continue
sudo apt install mariadb-server
Select Y to continue
sudo mysql_secure_installation
Return for no current password
Select Y to set the new root password to software_startup_simulator
Select Y to remove anonymous users
Select Y to disallow remote root login
Select Y to remove test database
Select Y to reload data table privileges
sudo apt install -y postgresql
Installing your CCC Requirements
cd /home/shared_workspace/ChesapeakeCommunityConnect-FA24/cccSite
If you were working on this 3/19/2025 or previously, run 
git pull origin main
git pull origin development
python3.10 -m pip install -r requirements.txt
python3.10 -m pip install python-magic
python3.10 -m pip install googlemaps
To run the website:
python3.10 manage.py makemigrations
python 3.10 manage.py migrate
python 3.10 manage.py runserver 8080
If you’re using Visual Studio Code, this should give you a prompt that says “Your application running on port 8080 is available”. Click on “Open in Browser”
Alternatively, enter “http://127.0.0.1:8080/” in your browser
Setting up YOUR working environment



In your second virtual machine do the following:
Part 2: CDSpec Installation & Execution
Configuring your Virtual Machine for git, python, and other dependencies
cd /home/shared_workspace
sudo apt update 
sudo apt install python3
sudo apt install git
git config --global user.name "****" (between “” needs to be the github username”
git config --global user.email "****" (between the “” needs to be the github email address”
git init
git clone https://github.com/swbn1/CDSpecCollab_COSC4012020-FA24
sudo apt-get install python3-pip
Press y and then enter when prompted
sudo apt install python3-django
Press y and then enter when prompted
sudo apt install libapache2-mod-wsgi-py3
Press y and then enter when prompted
sudo apt install mariadb-server
Press y and then enter when prompted
sudo mysql_secure_installation
Return for no current password
Select Y to set the new root password to software_startup_simulator
Select Y to remove anonymous users
Select Y to disallow remote root login
Select Y to remove test database
Select Y to reload data table privileges
sudo apt install postgresql
Press y and then enter when prompted
Installing your CDSpec requirements
cd CDSpecCollab_COSC4012020-FA24/Deployed\ Version/cd_spec_viewer_web/
pip install -r requirements.txt
curl -sS https://bootstrap.pypa.io/get-pip.py | python3
pip install whitenoise
pip install crispy-bootstrap4
Configuring Postgres
sudo systemctl status postgresql
Press CTRL+C to go back to cmd line prompt
sudo -i -u postgres
psql
ALTER USER postgres PASSWORD 'PASS';
\q
exit
sudo nano /etc/postgresql/*/main/pg_hba.conf
Navigate to:
# Database administrative login by Unix domain socket
local   all             postgres                                peer
Change “peer” to “md5” (without quotations)
Ctrl + X
Y
Enter
sudo systemctl restart postgresql
To run the website
cd shared_workspace/CDSpecCollab_COSC4012020-FA24/Deployed\ Version/cd_spec_viewer_web/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
If you’re using Visual Studio Code, this should give you a prompt that says “Your application running on port 8000 is available”. Click on “Open in Browser”
Alternatively, enter “http://127.0.0.1:8000/” in your browser

Basic Github Linux Instructions
Please note, everywhere it says “branchname” replace that with the name of your chosen branch.

git branch - Shows the branches loaded to your machine, the branch with an asterisk (*) next to it is the branch you are currently working within

git checkout branchname - Moves you to the branch entered

git status - Shows the current status of your branch and the files within it

git checkout -b branchname - Creates a new branch and switches to it


Uploading Your Changes To Github
The following 2 commands need to be run everytime you want to push to github
git add .
git commit -m “Information about this push” - Saves changes to your local repository
git push -u origin branchname
This command only needs to be run once. If youre on branch abc and run this once you will not need to run it again
git push
After you have run the previous command, this is what you will use to push updates to github

Pulling Changes From Github
git pull origin branchname
Downloads updates from github, and merges them with your local branch






pip install crispy-bootstrap4



