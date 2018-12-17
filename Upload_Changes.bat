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
git add Update.bat
echo updated Update.bat
git add database.txt
echo updated database.txt
git add _WINDOWS/Run.bat
echo Updated _WINDOWS/Run.bat
git add _WINDOWS/Run_Debug.bat
echo Updated _WINDOWS/Run_Debug.bat
echo -----------------

echo ------System-----
echo commiting to master
git commit -m "Updated software"
echo Finished committing
echo -----------------

echo ------System-----
echo pushing to origin
git push origin
echo Upload finished
echo -----------------
