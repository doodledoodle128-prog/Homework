def shutdown():
    print("Shutting down...")

call = input("Do you want to shutdown?: ").lower()
if call == "yes":
    shutdown()
