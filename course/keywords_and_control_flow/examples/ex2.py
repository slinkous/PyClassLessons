import sys



try:
    Cardamom

except Exception as e:
    print "Your Exception:", e
    raise sys.exc_info()


print "The application is now going to fall off the end..."