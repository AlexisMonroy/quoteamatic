from openpyxl import load_workbook
import time
import datetime

print("STARTING")
count = 1
sbs = load_workbook(filename= 'sbs.xlsx', data_only=True)

sbs_ws = sbs["1. CBP_40HC"]
sheet_header = sbs_ws["A1"]
renew_date = sbs_ws["A2"]
rep_info = sbs_ws["B2:W2"]
carrier_header = sbs_ws["A4"]
carrier_info = sbs_ws["B4:W4"]
effective_date = sbs_ws["A6:W6"]
expiration_date = sbs_ws["A7:W7"]
aws_destinations = sbs_ws["A9:A33"]
aws_code = sbs_ws["B9:B33"]
ripi_destinations = sbs_ws["A35:A58"]
ripi_code = sbs_ws["B35:B58"]
ipi_destinations = sbs_ws["A60:A117"]
ipi_code = sbs_ws["B60:B117"]
comm_bullet = sbs_ws["A8:W8"]
aws_cost = sbs_ws["C4:W33"]
ripi_cost = sbs_ws["C4:W58"]
ipi_cost = sbs_ws["C4:W117"]

sbs_header_dict = {"Sheet": None}
rep_dict = {"Rep":[]}
carrier_dict = {"Carrier": []}
renew_date_dict = {"Renewal Date": None}
effect_date_dict = {"Effective Date": []}
expire_date_dict = {"Expiration Date": []}
comm_bullet_dict = {"Comm Bullet": []}
aws_dest_dict = {"AWS Destinations": []}
aws_code_dict = {"AWS Code": []}
ripi_dest_dict = {"Ripi Destinations": []}
ripi_code_dict = {"Ripi Code": []}
ipi_dest_dict = {"IPI Destinations": []}
ipi_code_dict = {"IPI Code": []}
aws_cost_dict = {"CMA": [], "CMA-2": [], "COSCO":[], "EMC":[], "Hapag":[], "HMM":[], "HMM-2":[], "MSC":[], "OOCL":[], "ONE":[], "SM Line":[], "YML":[], "ZIM":[], "WHL":[], "WHL-2":[], "Matson":[], "CMA EXX":[], "CULine":[], "CULine-2":[], "CULine-3":[], "Transfar": [], "SeaLead":[]}
ripi_cost_dict = {"CMA": [], "CMA-2": [], "COSCO":[], "EMC":[], "Hapag":[], "HMM":[], "HMM-2":[], "MSC":[], "OOCL":[], "ONE":[], "SM Line":[], "YML":[], "ZIM":[], "WHL":[], "WHL-2":[], "Matson":[], "CMA EXX":[], "CULine":[], "CULine-2":[], "CULine-3":[], "Transfar": [], "SeaLead":[]}
ipi_cost_dict = {"CMA": [], "CMA-2": [], "COSCO":[], "EMC":[], "Hapag":[], "HMM":[], "HMM-2":[], "MSC":[], "OOCL":[], "ONE":[], "SM Line":[], "YML":[], "ZIM":[], "WHL":[], "WHL-2":[], "Matson":[], "CMA EXX":[], "CULine":[], "CULine-2":[], "CULine-3":[], "Transfar": [], "SeaLead":[]}

#this gets the header
if sheet_header.value != None:
    header = sheet_header.value
    sbs_header_dict.update({"Sheet": header})

#this gets the renewal date
if renew_date.value != None:

    renew = renew_date.value[9:]
    renew_date_dict.update({"Renewal Date": renew})

#this gets the rep info
for row in rep_info:
    for cell in row:
        for key in rep_dict:
            if cell.value != None:
                str_cell = str(cell)
                #print(str_cell)
                            #Convert col letter to int equivalent
                col_pos = ord(str_cell[-3])

                            #get row position
                row_pos = str_cell[-2]

                            #get next column position
                next_col_pos = chr(col_pos + count)

                            #get next cell position
                next_cell = sbs_ws[(next_col_pos + row_pos)]

                            #get next cell value
                cell_value = next_cell.value
                #print(cell_value)
                rep_dict[key].append(cell_value)
                count += 1
                    
        count = 1

#this gets the carrier info, could probably rewrite this to be more efficient
carrier_header_value = carrier_header.value
if carrier_header_value != None and carrier_header_value == "Carrier":
    for row in carrier_info:
        for cell in row:
            for key in carrier_dict:
                if cell.value == None:
                    str_cell = str(cell)
                    #print(str_cell)
                                #Convert col letter to int equivalent
                    col_pos = ord(str_cell[-3])

                                #get row position
                    row_pos = str_cell[-2]

                                #get next column position
                    next_col_pos = chr(col_pos + count)

                                #get next cell position
                    next_cell = sbs_ws[(next_col_pos + row_pos)]

                                #get next cell value
                    cell_value = next_cell.value
                    #print(cell_value)
                    carrier_dict[key].append(cell_value)
                    count += 1
                else:
                    str_cell = str(cell)
                    #print(str_cell)
                                #Convert col letter to int equivalent
                    col_pos = ord(str_cell[-3])

                                #get row position
                    row_pos = str_cell[-2]

                                #get next column position
                    next_col_pos = chr(col_pos + count)

                                #get next cell position
                    next_cell = sbs_ws[(next_col_pos + row_pos)]

                                #get next cell value
                    cell_value = next_cell.value
                    #print(cell_value)
                    carrier_dict[key].append(cell_value)
                    count += 1
                        
            count = 1

#this gets the effective date
for row in effective_date:
    for cell in row:
        for key in effect_date_dict:
        
            str_cell = str(cell)

            col_pos = ord(str_cell[-3])

            row_pos = str_cell[-2]

            next_col_pos = chr(col_pos + count)

            next_cell = sbs_ws[(next_col_pos + row_pos)]

            cell_value = next_cell.value
                #print(cell_value)
            if cell_value != None:
                str_cell_value = str(cell_value)
                effect_date_dict["Effective Date"].append(str_cell_value[:10])
                count += 1
                    
        count = 1

#this gets the expiration date
for row in expiration_date:
    for cell in row:
        for key in expire_date_dict:
        
            str_cell = str(cell)
          
            col_pos = ord(str_cell[-3])

            row_pos = str_cell[-2]

            next_col_pos = chr(col_pos + count)

            next_cell = sbs_ws[(next_col_pos + row_pos)]

            cell_value = next_cell.value
                #print(cell_value)
            if cell_value != None:
                str_cell_value = str(cell_value)
                expire_date_dict["Expiration Date"].append(str_cell_value[:10])
                count += 1
                    
        count = 1

#this gets the comm bullet
for row in comm_bullet:
    for cell in row:
        for key in comm_bullet_dict:
        
            str_cell = str(cell)
          
            col_pos = ord(str_cell[-3])

            row_pos = str_cell[-2]

            next_col_pos = chr(col_pos + count)

            next_cell = sbs_ws[(next_col_pos + row_pos)]

            cell_value = next_cell.value
                #print(cell_value)
            if cell_value != None:
                str_cell_value = str(cell_value)
                comm_bullet_dict["Comm Bullet"].append(str_cell_value)
                count += 1
                    
        count = 1


aws_dest_row_count = 0
aws_dest_count = 0
for row in aws_destinations:
    aws_dest_row_count += 1

#this gets the AWS destinations
for row in aws_destinations:
    for cell in row:
        for key in aws_dest_dict:
            if cell.value != None and cell.value == "Destinations":
                head_cell = str(cell)

                for number in range(aws_dest_row_count - 1):
                    if "." in head_cell:
                        check_str_cell = len(head_cell[head_cell.index(".") + 1:])
                        if check_str_cell < 4:
        
                            str_cell = head_cell
                            
                            col_pos = str_cell[-3]

                            row_pos = str_cell[-2]
                        
                            next_row_pos = str(int(row_pos) + count)

                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            aws_dest_dict["AWS Destinations"].append(cell_value)
                            count += 1
                            
                        else:
                            str_cell = str(head_cell)
                            
                            col_pos = str_cell[-3]

                            row_pos = str_cell[-2]

                            next_row_pos = str(int(row_pos) + count)
                            
                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            aws_dest_dict["AWS Destinations"].append(cell_value)
                            count += 1
                            
        count = 1

#this gets aws_code, same as above:
aws_code_row_count = 0
aws_code_count = 0
for row in aws_code:
    aws_code_row_count += 1

for row in aws_code:
    for cell in row:
        for key in aws_code_dict:
            if cell.value != None and cell.value == "Code":
                head_cell = str(cell)

                for number in range(aws_code_row_count - 1):
                    if "." in head_cell:
                        check_str_cell = len(head_cell[head_cell.index(".") + 1:])
                        if check_str_cell < 4:
        
                            str_cell = head_cell
                            
                            col_pos = str_cell[-3]

                            row_pos = str_cell[-2]
                        
                            next_row_pos = str(int(row_pos) + count)

                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            aws_code_dict["AWS Code"].append(cell_value)
                            count += 1
                            
                        else:
                            str_cell = str(head_cell)
                            
                            col_pos = str_cell[-3]

                            row_pos = str_cell[-2]

                            next_row_pos = str(int(row_pos) + count)
                            
                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            aws_code_dict["AWS Code"].append(cell_value)
                            count += 1
                            
        count = 1

#this gets ripi_destinations, same as aws_destinations:
ripi_dest_row_count = 0
ripi_dest_count = 0
for row in ripi_destinations:
    ripi_dest_row_count += 1

for row in ripi_destinations:
    for cell in row:
        for key in ripi_dest_dict:
            if cell.value != None and cell.value == "Below are all RIPI":
                head_cell = str(cell)

                for number in range(ripi_dest_row_count - 1):
                    if "." in head_cell:
                        check_str_cell = len(head_cell[head_cell.index(".") + 1:])
                    
                        if check_str_cell < 16:
                          
                            str_cell = head_cell
                          
                            col_pos = str_cell[-4]

                            row_pos = str_cell[-3:-1]
                        
                            next_row_pos = str(int(row_pos) + count)

                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            ripi_dest_dict["Ripi Destinations"].append(cell_value)
                            count += 1
                            
                        else:
                      
                            str_cell = str(head_cell)
    
                            col_pos = str_cell[-3]

                            row_pos = str_cell[-2]

                            next_row_pos = str(int(row_pos) + count)
                            
                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            ripi_dest_dict["Ripi Destinations"].append(cell_value)
                            count += 1
                            
        count = 1

#this gets ripi_code, same as aws_code:
ripi_code_row_count = 0
ripi_code_count = 0
for row in ripi_code:
    ripi_code_row_count += 1
for row in ripi_code:
    for cell in row:
        for key in ripi_code_dict:
            if cell.value == None:
                head_cell = str(cell)

                for number in range(ripi_code_row_count - 1):
                    if "." in head_cell:
                        check_str_cell = len(head_cell[head_cell.index(".") + 1:])
                        if check_str_cell < 16:
        
                            str_cell = head_cell
                            
                            col_pos = str_cell[-4]

                            row_pos = str_cell[-3:-1]
                        
                            next_row_pos = str(int(row_pos) + count)

                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            ripi_code_dict["Ripi Code"].append(cell_value)
                            count += 1
                            
                        else:
                            str_cell = str(head_cell)
                            
                            col_pos = str_cell[-3]

                            row_pos = str_cell[-2]

                            next_row_pos = str(int(row_pos) + count)
                            
                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            ripi_code_dict["Ripi Code"].append(cell_value)
                            count += 1
                            
        count = 1

#this gets ipi_destinations, same as aws_destinations and ripi_destinations:
ipi_dest_row_count = 0
ipi_dest_count = 0
for row in ipi_destinations:
    ipi_dest_row_count += 1

for row in ipi_destinations:
    for cell in row:
        for key in ipi_dest_dict:
            if cell.value != None and cell.value == "Below are all IPI/MLB":
                head_cell = str(cell)

                for number in range(ipi_dest_row_count - 1):
                    if "." in head_cell:
                        check_str_cell = len(head_cell[head_cell.index(".") + 1:])
                        if check_str_cell < 16:
        
                            str_cell = head_cell
                            
                            col_pos = str_cell[-4]

                            row_pos = str_cell[-3:-1]
                        
                            next_row_pos = str(int(row_pos) + count)

                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            ipi_dest_dict["IPI Destinations"].append(cell_value)
                            count += 1
                            
                        else:
                            str_cell = str(head_cell)
                            
                            col_pos = str_cell[-3]

                            row_pos = str_cell[-2]

                            next_row_pos = str(int(row_pos) + count)
                            
                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            ipi_dest_dict["IPI Destinations"].append(cell_value)
                            count += 1
                            
        count = 1

#this gets ipi_code, same as aws_code and ripi_code:
ipi_code_row_count = 0
ipi_code_count = 0
for row in ipi_code:
    ipi_code_row_count += 1

for row in ipi_code:
    for cell in row:
        for key in ipi_code_dict:
            if cell.value == None:
                head_cell = str(cell)

                for number in range(ipi_code_row_count - 1):
                    if "." in head_cell:
                        check_str_cell = len(head_cell[head_cell.index(".") + 1:])
                        if check_str_cell < 16:
        
                            str_cell = head_cell
                            
                            col_pos = str_cell[-4]

                            row_pos = str_cell[-3:-1]
                        
                            next_row_pos = str(int(row_pos) + count)

                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            ipi_code_dict["IPI Code"].append(cell_value)
                            count += 1
                            
                        else:
                            str_cell = str(head_cell)
                            
                            col_pos = str_cell[-3]

                            row_pos = str_cell[-2]

                            next_row_pos = str(int(row_pos) + count)
                            
                            next_cell = sbs_ws[(col_pos + next_row_pos)]

                            cell_value = next_cell.value
                                
                            ipi_code_dict["IPI Code"].append(cell_value)
                            count += 1
                            
        count = 1

aws_row_count = 0
aws_count = 5
for row in aws_cost:
    aws_row_count += 1

#this gets the AWS cost
for row in aws_cost:
    for cell in row:
        for key in aws_cost_dict:
            if cell.value != None and cell.value == key:
                head_cell = str(cell)
                
                head_col_pos = head_cell[-3]

                head_row_pos = head_cell[-2]

                head_next_row_pos = str(int(head_row_pos) + aws_count)

                head_next_cell = sbs_ws[(head_col_pos + head_next_row_pos)]
                
                head_cell_value = head_next_cell.value
                str_head_next_cell = str(head_next_cell)
                
                for number in range(aws_row_count - 6):
                    if "." in str_head_next_cell:
                                check_str_cell = len(str_head_next_cell[str_head_next_cell.index(".") + 1:])
                                if check_str_cell < 4:
                
                                    str_cell = str(head_next_cell)
                                    
                                    col_pos = str_cell[-3]

                                    row_pos = str_cell[-2]
                                
                                    next_row_pos = str(int(row_pos) + count)

                                    next_cell = sbs_ws[(col_pos + next_row_pos)]

                                    cell_value = next_cell.value
                                        
                                    aws_cost_dict[key].append(cell_value)
                                    count += 1
                                    
                                else:
                                    str_cell = str(head_next_cell)
                                    
                                    col_pos = str_cell[-3]

                                    row_pos = str_cell[-2]

                                    next_row_pos = str(int(row_pos) + count)
                                    
                                    next_cell = sbs_ws[(col_pos + next_row_pos)]

                                    cell_value = next_cell.value
                                        
                                    aws_cost_dict[key].append(cell_value)
                                    count += 1
                                    
                count = 1                                

ripi_row_count = 0
ripi_count = 31
for row in ripi_cost:
    ripi_row_count += 1

#this gets ripi_cost
for row in ripi_cost:
    for cell in row:
        for key in ripi_cost_dict:
            if cell.value != None and cell.value == key:
                head_cell = str(cell)
        
                head_col_pos = head_cell[-3]

                head_row_pos = head_cell[-2]

                head_next_row_pos = str(int(head_row_pos) + ripi_count)

                head_next_cell = sbs_ws[(head_col_pos + head_next_row_pos)]
                
                head_cell_value = head_next_cell.value
                str_head_next_cell = str(head_next_cell)
                
                for number in range(ripi_row_count - 32):
                    if "." in str_head_next_cell:
                                check_str_cell = len(str_head_next_cell[str_head_next_cell.index(".") + 1:])
                                if check_str_cell < 4:
                
                                    str_cell = str(head_next_cell)
                                    
                                    col_pos = str_cell[-3]

                                    row_pos = str_cell[-2]
                                
                                    next_row_pos = str(int(row_pos) + count)

                                    next_cell = sbs_ws[(col_pos + next_row_pos)]
                                  
                                    cell_value = next_cell.value
                                        
                                    ripi_cost_dict[key].append(cell_value)
                                    count += 1
                                    
                                else:
                                    str_cell = str(head_next_cell)
                                    
                                    col_pos = str_cell[-4]

                                    row_pos = str_cell[-3:-1]

                                    next_row_pos = str(int(row_pos) + count)
                                    
                                    next_cell = sbs_ws[(col_pos + next_row_pos)]
                                    
                                    cell_value = next_cell.value
                                        
                                    ripi_cost_dict[key].append(cell_value)
                                    count += 1
                                    
                count = 1

ipi_row_count = 0
ipi_count = 56
for row in ipi_cost:
    ipi_row_count += 1

for row in ipi_cost:
    for cell in row:
        for key in ipi_cost_dict:
            if cell.value != None and cell.value == key:
                head_cell = str(cell)
    
                head_col_pos = head_cell[-3]

                head_row_pos = head_cell[-2]

                head_next_row_pos = str(int(head_row_pos) + ipi_count)

                head_next_cell = sbs_ws[(head_col_pos + head_next_row_pos)]
                
                head_cell_value = head_next_cell.value
                str_head_next_cell = str(head_next_cell)
                
                for number in range(ipi_row_count - 57):
                    if "." in str_head_next_cell:
                                check_str_cell = len(str_head_next_cell[str_head_next_cell.index(".") + 1:])
                                if check_str_cell < 4:
                
                                    str_cell = str(head_next_cell)
                                
                                    col_pos = str_cell[-3]

                                    row_pos = str_cell[-2]
                                
                                    next_row_pos = str(int(row_pos) + count)

                                    next_cell = sbs_ws[(col_pos + next_row_pos)]
                                  
                                    cell_value = next_cell.value
                                        
                                    ipi_cost_dict[key].append(cell_value)
                                    count += 1
                                    
                                else:
                                    str_cell = str(head_next_cell)
                             
                                    col_pos = str_cell[-4]

                                    row_pos = str_cell[-3:-1]

                                    next_row_pos = str(int(row_pos) + count)
                                    
                                    next_cell = sbs_ws[(col_pos + next_row_pos)]
                                    
                                    cell_value = next_cell.value
                                        
                                    ipi_cost_dict[key].append(cell_value)
                                    count += 1
                                    
                count = 1
                

print("Sheet Header: " + str(sbs_header_dict) + "\n")
print("Renewal Date: " + str(renew_date_dict) + "\n")
print("Reps:\n" + str(rep_dict) + "\n")
print("Carriers:\n" + str(carrier_dict) + "\n")
print("Effective Date: " + str(effect_date_dict) + "\n")
print("Expiration Date: " + str(expire_date_dict) + "\n")
print("Comm Bullet: " + str(comm_bullet_dict) + "\n")
print("AWS Cost: " + str(aws_cost_dict) + "\n")
print("Ripi Cost: " + str(ripi_cost_dict) + "\n")
print("Ipi Cost: " + str(ipi_cost_dict) + "\n")
print("AWS Destinations: " + str(aws_dest_dict) + "\n")
print("AWS Codes: " + str(aws_code_dict) + "\n")
print("Ripi Destinations: " + str(ripi_dest_dict) + "\n")
print("Ripi Codes: " + str(ripi_code_dict) + "\n")
print("Ipi Destinations: " + str(ipi_dest_dict) + "\n")
print("Ipi Codes: " + str(ipi_code_dict) + "\n")

with open("C:/Users/amonroy.lax/Documents/dev/py_text/readme.txt", "w") as f:
    f.write("Sheet Header: " + str(sbs_header_dict) + "\n")
    f.write("\n")
    f.write("Renewal Date: " + str(renew_date_dict) + "\n")
    f.write("\n")
    f.write("Reps:\n" + str(rep_dict) + "\n")
    f.write("\n")
    f.write("Carriers:\n" + str(carrier_dict) + "\n")
    f.write("\n")
    f.write("Effective Date: " + str(effect_date_dict) + "\n")
    f.write("\n")
    f.write("Expiration Date: " + str(expire_date_dict) + "\n")
    f.write("\n")
    f.write("Comm Bullet: " + str(comm_bullet_dict) + "\n")
    f.write("\n")
    f.write("AWS Cost: " + str(aws_cost_dict) + "\n")
    f.write("\n")
    f.write("Ripi Cost: " + str(ripi_cost_dict) + "\n")
    f.write("\n")
    f.write("Ipi Cost: " + str(ipi_cost_dict) + "\n")
    f.write("\n")
    f.write("AWS Destinations: " + str(aws_dest_dict) + "\n")
    f.write("\n")
    f.write("AWS Codes: " + str(aws_code_dict) + "\n")
    f.write("\n")
    f.write("Ripi Destinations: " + str(ripi_dest_dict) + "\n")
    f.write("\n")
    f.write("Ripi Codes: " + str(ripi_code_dict) + "\n")
    f.write("\n")
    f.write("Ipi Destinations: " + str(ipi_dest_dict) + "\n")
    f.write("\n")
    f.write("Ipi Codes: " + str(ipi_code_dict) + "\n")
    f.write("\n")
    f.write("END")
    f.write("\n")

    f.close()    

#open readmeCOPY.txt and count the number of lines and the number of words in the file:
with open("C:/Users/amonroy.lax/Documents/dev/py_text/readme.txt", "r") as f:
    data = f.read()
    lines = data.splitlines()
    words = data.split()
    len_lines = len(lines)
    len_words = len(words)
    str_lines = str(len_lines)
    str_words = str(len_words)
    f.close()
    
    print("Number of lines: " + str_lines)
    print("Number of words: " + str_words)

with open("C:/Users/amonroy.lax/Documents/dev/py_text/readme.txt", "a") as f:
    f.write("Number of lines: " + str_lines)
    f.write("\n")
    f.write("Number of words: " + str_words)
    f.write("\n")
    f.close()

print("END")
