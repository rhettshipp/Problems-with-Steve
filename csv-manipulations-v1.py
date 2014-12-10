
CIDLIST = []
with open('/Users/rhettshipp1/Desktop/Problems-with-Steve/Data Files/AID_466_data.csv') as f:
    f.next()
    for line in f:
        try:
            hillslope = float(line.split(',')[9])
        except ValueError:
            hillslope = None
        outcome = line.split(',')[2]
        CID = line.split(',')[1]
        if (outcome == "Active" and
            hillslope is not None and
                0.2 < hillslope < 2.0):
            CIDLIST.append(CID)
print CIDLIST