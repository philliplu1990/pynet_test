f = open("show_ip_bgp.txt")
output = f.read()
output = output.splitlines()
for i, line in enumerate(output):
    if line == '':
        new_output = output[i+2:]
        break

main_list = []
for line in new_output:
    main_list.append(line[5:22].strip() + ', ' + line[63:-2])

print main_list
