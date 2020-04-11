import psutil




# for proc in psutil.process_iter(['pid', 'name', 'username','memory_percent','memory_full_info']):
#     print(proc.info)

# print(psutil.Process(name='System Information.exe'))

import os
# import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls

proc = find_procs_by_name("System Information.exe")[0]

print(proc.memory_percent())
print(proc.cpu_percent())