#3.1
#1. Git vs. GitHub
#Git is the local version control, GitHub hosts git repositories online for collaboration
#2. Terminal vs. Command Line
#Terminal is the software that hosts the command line, command line is the interface
#3. Local vs. Remote Repository
#Local repository exists on your device, remote exists on a hosting platform like github
#4. Version Control
#Git repositories - software which keeps track of changes made to a project so you can revert/merge them later on
#5. Staging Area
#where changes are stored before being committed
#6. git add
#adds changes made to a/all files to the staging area
#7. git commit
#Creates and stores a new version including the changes in the staging area
#8. git push
#Updates the remote repository with changes made and committed locally
#9. git status
# shows changes not yet staged, staged changes, untracked files, branch info, etc.
#10. git pull
#Gets latest version of repository from remote
#11. pwd
#prints working directory
#12. ls
#lists contents of current directory
#13. cd
#changes current directory
#14. nano
#open a file in nano (built-in text editor)
#15. touch
#update access/modification times if file exists or create a new one with that name
#16. mv
#move a file from one location to another
#17. rm
#permanently delete files/directories
#18. cat
#prints contents of a file

#3.2
#You have been plopped into Judy’s directory system. What command will tell you what your current working directory is?
#pwd
#The terminal responds by saying you are in ∼/python decal/judy decal. What command will list all the files in your current working directory?
#ls -a
#Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py. You will need to pull the brianna repo repository to find the updated file. What command(s) will let you move to the correct repository and pull the latest changes?
#cd ../brianna_repo
#git pull origin main
#How would you move this new homework.py to the homework/ folder in your personal repository?
#mv homework.py ../judy_decal/homework/homework.py (assuming you're still in brianna_repo where we moved in the last question)
#How would you move yourself to the same repository as homework.py?
#cd ../judy_decal/homework
#You want to see the contents of homework.py in your terminal, how would you do this?
#cat homework.py or nano homework.py, depending on what you want to do
#Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository?
#git add .
#git commit -m "done with homework"
#git push origin main
#Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy” do wrong when trying to push?)
#Judy is behind the remote repository, meaning her pushing could replace more recent changes.  You should always pull first before pushing
#What absolute path will allow you to move to Recents/?
#~/Recents

#4.1
def check_data_type(val):
    return str(type(val).__name__)

#4.2
def is_even(val):
    return val % 2 == 0

#5
def add_all(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

#6.1
def dupe_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i)
        new_list.append(i)
    return new_list

#6.2
def square(num): #originally missing semicolon to define function
    return num * num

print(dupe_list([1,2,3,4,5]))