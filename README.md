# CS440

Create a new branch based off of the most recent version of master and publish the branch on Github:

$ git checkout master
$ git pull origin master
$ git checkout -b branch-name
$ git push -u origin HEAD
After implementing your changes and doing some testing, create a pull request against master in Github.

Address any merge conflicts in the pull request by either using Github's online editor or from the command line:

$ git checkout [your-branch-name]
$ git merge master
Find and address any merge conflicts using a text editor to complete the merge.

Request a review from one or more team members.

Make any necessary fixes after team member(s) have finished their review(s) and request an additional review. Repeat until no further changes are requested. Reviewers should not merge any pull requests of the team member that they are reviewing.

Goal (3/7/2019):
What the program does right now:
looks for a file with name matching the command line argument
opens that file as an XML tree
creates an output file and writes the XML tree

So right now it's a proof of concept that it can handle XML contents from an input file, it just makes a copy of the code inside in a new file.

What needs done:
Adjust behavior so instead of copying the whole input file it only extracts the values we are interested in (those in XML tags with names in the tags[] list)
Use the example shown here under 13.2  Parsing XML http://www.pythonlearn.com/html-007/cfbook014.html
Save each extracted value in a variable with a name matching the tag it was inside
Append each extracted value to the output file

So we should end up with this functionality:
Run the script on a single input XML file
End up with output.txt which contains the values inside the tags in tags[] on individual lines
