<b>To run</b> : python test_args.py --files_paths /etc/passwd /etc/group

Passwd Parsing
The idea is to parse the UNIX /etc/passwd and /etc/groups files and combine the data into a single json output.
The paths to the passwd and groups file are taken as arguments, defaulting to the standard system path. If the input files are absent or malformed, script indicates an error.
The output is a json object where each key is a username and each value is an object containing the field “uid”, “full_name”, and “groups”. Groups contain a list of all groups the user is a member of.
An example run of such a program might look like:
>>> passwd-parser
{
"list": {
"uid": "38",
"full_name": "Mailing List Manager",
"groups": []
},
"nobody": {
"uid": "65534",
"full_name": "nobody",
"groups": []
},
"lxd": {
"uid": "106",
"full_name": "",
"groups": []
},
"ubuntu": {
"uid": "1000",
"full_name": "Ubuntu",
"groups": [
"adm",
"cdrom",
"dip",
"docker",
"netdev",
"plugdev",
"floppy",
"dialout",
"audio",
"lxd",
"sudo",
"video"
]
},
"man": {
"uid": "6",
"full_name": "man",
"groups": []
}
}

