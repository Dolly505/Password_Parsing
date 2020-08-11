import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description='...Passwd Parsing...')
    parser.add_argument('--file_paths',
                        '-f',
                        nargs='+',
                        required=False,
                        default=['/etc/passwd', '/etc/group'],
                        help='root path of passwd file and group file'
                        )

    args, unknown_args = parser.parse_known_args()
    return args

def user_details(files):
    """Get user details JSON. 
    
    :param: files: List of file paths
    :type: files: list
    :return: return dictionary of user details
    :rtype: dict
    """

    # Check if both files are present and also if input is valid
    user_details = {}
    passwd_file = None
    group_file = None
    for f in files:
        if os.path.isfile(f):
            if "passwd" in f:
                passwd_file = f
            elif "group" in f:
                group_file = f
            else:
                raise ValueError('{} is inValid, File must be passwd or group'.format(f))
        else:
            raise ValueError('{} is not present'.format(f))
            return


    # By here we know both files are present and we are good to go ahead
    # Let's get user details from /etc/passwd as we can get everything except group

    # read file line by line and split the string as we know the format
    # User might have given both files in random order, we cannot assume.
    with open(passwd_file) as pass_file:
        for line in pass_file:
            line = line.split(":")
            if len(line) == 7:
                username = line[0]
                uid = line[2]
                full_name = line[4]
                # Ideally all entry will be unique, but still a safe check to do
                if username not in user_details:
                    user_details[username] = {}
                else:
                    # This means we saw same user value in passwd file which seems invalid config
                    raise Exception ('**** Passwd file has same user twice ****')
                user_details[username]["uid"] = uid
                user_details[username]["full_name"] = full_name
                user_details[username]["groups"] = []

    # Now we need to read group file and keep adding the group name to the user that we find

    with open(group_file) as g_file:
        for line in g_file:
            line = line.split(":")
            if len(line) == 4:
                group_name = line[0]
                user = line[3]
                user = user.rstrip()
                if user:
                    user = user.split(",")
                    for u in user:
                        user_details[u]["groups"].append(group_name)

    print("Final User Details are: {}".format(user_details))


def main(args):
    """Main.

    :param args: Arguments from cli parser
    :type: ArgumentParser
    """
    # host = args.host
    # current_user = args.user
    files = args.file_paths

    user_details(files=files)
    print('Files are: {}'.format(files))


if __name__ == '__main__':
    main(parse_args())


