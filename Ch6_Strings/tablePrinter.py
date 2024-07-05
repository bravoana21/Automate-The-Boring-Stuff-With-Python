def printTable(tableData):

    # Get the maximum width for each column
    colWidths = [0] * len(tableData)
    for col in range(len(tableData)):
        longestString = 0
        for item in tableData[col]:
            if longestString < len(item):
                longestString = len(item)
        colWidths[col] = longestString

    # Print the table with right-justifies columns
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]) + ' ', end = '')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)