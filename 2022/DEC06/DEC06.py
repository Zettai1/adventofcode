most_recent = []; message_mr = []; rec_num = 0; msg_num = 0; found_pkt = False; msg_fnd = False

def checker(recent_items):
    for first, fItem in enumerate(recent_items):
        for second, sItem in enumerate(recent_items):
            if first != second and fItem == sItem:
                return False
    return True
                    
with open("DEC06.txt") as data:
    for line in data:
        most_recent.clear()
        line = line.strip("\n")
        rec_num = 0; msg_num = 0
        for sound_byte in line:
            most_recent.append(sound_byte)
            message_mr.append(sound_byte)
            if not found_pkt:
                rec_num += 1
            if not msg_fnd:
                msg_num += 1

            if not found_pkt:
                if len(most_recent) > 4:
                    del most_recent[0]
                if len(most_recent) == 4:
                    found_pkt = checker(most_recent)
            if not msg_fnd:
                if len(message_mr) > 14:
                    del message_mr[0]
                if len(message_mr) == 14:
                    msg_fnd = checker(message_mr)
            if msg_fnd == True and found_pkt == True: 
                print(f"Packet Number: {rec_num}, Message Packet: {msg_num}"); break