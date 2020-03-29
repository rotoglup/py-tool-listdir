Simple python script that lists all files contained in a folder tree.

Outputs a JSON representation to `stdout` structured for **easy diffing**.

Used to compare archive copies of the same folders, after a `robocopy` for example.

> **TODO** Include a SHA checksum of the files contents

Usage
------------------------------------------------------------------------------

```
python listdir.py "root_folder_A" > "folder_A_listing.json"
```

> On Windows, use UNC syntax if there are paths too long : ex. `\\?\C:\Temp`

The JSON output will have the following form :

```
{
	".": {
		files: [
			{
				"file": "some_file_name",
				"mtime": ...,
				"size": ...
			},
			...
		],
		path: "."
	},
	"subfolder_1" : ...
	"subfolder_2" : ...
}
```