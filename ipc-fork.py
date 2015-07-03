import os, sys

fdr, fdw = os.pipe()

pid = os.fork()

if pid:
    os.close(fdw)
    print "Parent process"
    a1 = os.fdopen(fdr)
    str = a1.read()
    str = str[::-1]
    print "The reverse is " + str
    sys.exit(0)

else:
    os.close(fdr)
    print "child process"
    str1 = raw_input("Enter the string: ")
    b1 = os.fdopen(fdw, 'w')

    b1.write(str1)
    b1.close()
    sys.exit(0)
