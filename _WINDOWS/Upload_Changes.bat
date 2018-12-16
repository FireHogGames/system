@echo off

echo ------System-----
echo adding files
git add System_Core.py
echo Updated System_Core.py
git add LICENSE
echo Updated LICENSE
git add .gitignore
echo Updated .gitignore
git add Upload_Changes.bat
echo updated Upload_Changes.bat
git add Run.bat
echo updated Run.bat
echo -----------------

pause

echo ------System-----
echo commiting to master
git commit -m "Updated software"
echo Finished committing
echo -----------------

pause

echo ------System-----
echo pushing to origin
git push origin
echo Upload finished
echo -----------------

pause