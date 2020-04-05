# 못품
def solution(directory, command):
    answer = directory

    for c in command:
        if c[0] is 'm':
            answer.append(c[6:])
        elif c[0] is 'r':
            for d in directory:
                split_directory = d.split('/')
                print(split_directory, c[4:])
                if c[4:] in split_directory:
                    answer.pop(answer.index(d))

        # elif c[0] is 'c':
        #     split_command = c.split(' ')
        #     for d in directory:
        #
        #     directory.append()
        directory = answer
        answer = directory

    return directory


print(solution(
[
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
],
[
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]))
# [
# "/",
# "/root",
# "/root/abcd",
# "/root/abcd/etc",
# "/root/abcd/hello",
# "/root/tmp",
# "/root/tmp/hello",
# "/root/tmp/hello/tmp"
# ]

# print(solution(["/"],
#                [
#                    "mkdir /a",
#                    "mkdir /a/b",
#                    "mkdir /a/b/c",
#                    "cp /a/b /",
#                    "rm /a/b/c"
#                ]))
# [
# "/",
# "/a",
# "/a/b",
# "/b",
# "/b/c"
# ]