import os
from pathlib import Path

# Uncomment for a set source
# destParentPath = os.path.join(os.getcwd(),"dest")

# Uncomment for a set source
# sourceParentPath = "/shared/QW/Client_Files"

print("Input source (directory to clone): ")
sourceParentPath = input();


print("Input destination (where to clone to): ")
destParentPath = input();

if (not os.path.isdir(destParentPath)):
	print("Creating destination directory: " + destParentPath)
	os.mkdir(destParentPath)

print()
print("Source Parent: " + sourceParentPath)
print("Destination Parent: " + destParentPath)
print()

def recreate(sourceDir, destDir):
	# iterate over files in
	# that directory
	print("Recreating " + sourceDir + " in " + destDir)
	for f in os.listdir(sourceDir):
		sourcePath = os.path.join(sourceDir, f)
		print("sourcePath: " + sourcePath)
		destPath = os.path.join(destDir, f)
		print("destPath: " + destPath)

		if (os.path.isdir(sourcePath)):
			print("Making dir: " + destPath)
			os.mkdir(destPath)

			print("Recurring")
			recreate(sourcePath, destPath)
		elif(os.path.isfile(sourcePath)):
			Path(destPath).touch()

		print()

if (os.path.isdir(sourceParentPath) and os.path.isdir(destParentPath)):
	recreate(sourceParentPath, destParentPath)
else:
	print("Error: source is not a directory")
