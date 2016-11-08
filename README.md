# PyleCleaner
Python-based file and folder organizer and cleaner.

Mostly used as a way to clean up my own disorganized external HDD. This will: recursively go through a given folder and remove all duplicate files found in any sub-folder within that folder will be deleted. That is, if the same two files exist in multiple folders, only the first version of those files will be kept. Files are defined to be the same IFF their hashes are the same. File name, type, size, etc. are ignored.

There is an optional folder name which can be given. This will act as the initial folder for initialization. That is - this folder will be the first folder used to seed the list of existing files. Note that BFS will be used to seed the list of existing files. Thus, files in deeper sub-folders will be removed. 

Empty sub-folders are removed. Empty is defined as any folder that has no files except for the .DS_Store Mac pollution file.
