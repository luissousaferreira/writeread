import os

print("\n\n\n----- WRITE SPEED -----")
os.system("sync; dd if=/dev/zero of=tempfile bs=1M count=1024; sync")
print("Recalculating...\n")
os.system("sync; dd if=/dev/zero of=tempfile bs=1M count=1024; sync")


print("\n\n----- READ SPEED -----")

print("Clearing cache:")
os.system("sudo /sbin/sysctl -w vm.drop_caches=3")

print("\nCalculating Read Speed")
os.system("dd if=tempfile of=/dev/null bs=1M count=1024")