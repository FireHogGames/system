@echo off

echo adding files
git add System_Core.py
git add LICENSE
git add .gitignore
git add Upload_Changes.bat
git add Run.bat

pause

echo commiting to master
git commit -m "Updated software"
echo Finished committing

pause

echo pushing to origin
git push origin

echo Upload finished
pause