# Name:B V K Prasanth
# Email:budigiv1@udayton.edu
# This is the only file you need to work on. You do NOT need to modify other files
class Node:  # Using this to Create the Node used for DFS and BFS
    def __init__(self, data, prevPathList, childs):
        self.data = data
        self.prevPathList = prevPathList
        self.childs = childs

# Below are the functions you need to implement. For the first project, you only need to finish implementing bfs() and dfs()
def BFSFndNeibrs( puzzlestr, removedLst):
    posNeibrs = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }  # predefined Paths
    strtpos = int(puzzlestr.index('8'))  # Getting the start position of the blank space
    paths = posNeibrs[puzzlestr.index('8')]  # to get paths
    paths = lstStr(paths)  # converting the list to string
    neibrs = posNeibrs[puzzlestr.index('8')]  # converting the paths to next child elements
    for i in range(0, len(neibrs)): # this logic is used to swap the neighbouring elements
        temp = puzzlestr
        endpos = int(neibrs[i])
        if (strtpos < endpos):
            neibrs[i] = temp[0:strtpos] + temp[endpos] + temp[strtpos + 1:endpos] + temp[strtpos] + temp[endpos + 1:]
        else:
            neibrs[i] = temp[0:endpos] + temp[strtpos] + temp[endpos + 1:strtpos] + temp[endpos] + temp[strtpos + 1:]
    pathlist = strInt(paths)
    NeibrstempList = []
    pathTempList = []


# below 2loop is used to remove already visited nodes from paths and neighbours
    for i in range(0, len(neibrs)):
        if neibrs[i] in removedLst:
            NeibrstempList.append(neibrs[i])
            pathTempList.append(pathlist[i])

    for i in range(0, len(NeibrstempList)):
        neibrs.remove(NeibrstempList[i])
        pathlist.remove(pathTempList[i])
    return neibrs, pathlist


def Paths(puzzlestr):
    posNeibrs = {
        0: [1, 3],
        1: [0, 4, 5],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 8],
        7: [4, 6, 8],
        8: [5, 7]
    }
    Paths = posNeibrs[puzzlestr.index('8')]
    return Paths


def lstStr(puzzle):  # This will return list to String
    puzzle = map(lambda x: str(x), puzzle)
    string = ''.join(puzzle)
    return string


def strInt(puzzle):  # This will return String to Integer List
    strlist = []
    for i in range(0, len(puzzle)):
        strlist.append(puzzle[i])
    intList = list(map(lambda x: int(x), strlist))
    return intList


# here you need to implement the Breadth First Search Method
def bfs(puzzle):
    flag = 0  # Root Node flag
    queue = []  # queue for not expanded elements
    removedLst = []  # Variable records the visited nodes
    prevPathList = []  # Records the previous paths in the node
    goalNode = Node('', [], [])  # Initializing the goal node
    puzzleDict = {}  # Creating an empty Dictionary to uniquely identify the elements
    puzzleStr = lstStr(puzzle)  # Converts List to string
    queue.insert(0, puzzleStr)  # Inserting initial element at the start
    strtpos = int(puzzleStr.index('8'))  # Referencing the initial path for future reference
    while len(queue) != 0:  # Loop will iterate until queue is empty
        Neibrs, paths = BFSFndNeibrs(puzzleStr, removedLst)  # Return start position, Neighbours nodes,paths
        if flag == 0:  # This is only for Creation of root Node
            n = Node(puzzleStr, prevPathList, paths)  # Creating Root Node
            puzzleDict[puzzleStr] = [strtpos]  # Adding the root element
            flag += 1  # Updating the initial flag
        queue = Neibrs[::-1] + queue  # Queue updated
        for i in range(0, len(paths)):  # Neighbour Nodes Created
            updatedPaths = Paths(puzzleStr)  # To get Updated Paths
            puzzleDict[Neibrs[i]] = puzzleDict[puzzleStr] + [paths[i]]  # Updating new paths in the Dictionary
            n = Node(puzzleStr, n.prevPathList + [paths[i]], updatedPaths)  # Except Root Node
            if Neibrs[i] == '012345678':  # Condition to check whether it reached goal state or not
                goalNode = n  # If yes then target path will assigned to  goalNode
                break  # Breaks the loop
        if goalNode.data != '':  # If it is not empty break the loop
            break  # Breaks the loop
        else:
            removedLst.append(queue[-1])  # Already Visited Nodes will be recorded
            queue.pop()  # Expanded Node Popped
            puzzleStr = queue[-1]  # String updated
    return puzzleDict['012345678']  # Returning the goal state element


# here you need to implement the Depth First Search Method
def dfs(puzzle):
    flag = 0  # Root Node flag
    stack = []  # Stack for not expanded elements
    removedLst = []  # Variable records the visited nodes
    prevPathList = []  # Records the previous paths in the node
    goalNode = Node('', [], [])  # Initializing the goal node
    puzzleDict = {}  # Creating an empty Dictionary to uniquely identify the elements
    puzzleStr = lstStr(puzzle)  # Converts List to string
    stack.append(puzzleStr)  # Appending initial element
    strtpos = int(puzzleStr.index('8'))  # Referencing the initial path for future reference
    while len(stack) != 0:  # Loop will iterate until Stack is empty
        Neibrs, paths = BFSFndNeibrs(puzzleStr, removedLst)  # Return start position, Neighbours nodes,paths
        if flag == 0:  # This is only for Creation of root Node
            n = Node(puzzleStr, prevPathList, paths)  # Creating Root Node
            puzzleDict[puzzleStr] = [strtpos]  # Adding the root element
            stack.append(puzzleStr)  # updating in the stack
            flag += 1  # Updating the initial flag
        if len(paths) != 0:
            pathElement = min(paths)  # Finding the Minimum of the paths list
            Neibrs = [Neibrs[paths.index(pathElement)]]  # Finding the Minimum of the Neighbours list
            paths = [pathElement]  # Creating the new path element
            puzzleStr = Neibrs[0]  # updating the cursor
            puzzleDict[puzzleStr] = puzzleDict[stack[-1]] + [paths[0]]  # updating the dictionary with previous and current paths
            stack = stack + [puzzleStr]  # Updating Stack
            removedLst.append(puzzleStr)  # Adding to removed List
            updatedPaths = Paths(puzzleStr)  # To get Updated Paths
            n = Node(puzzleStr, prevPathList, updatedPaths)  # Creating node
        else:
            updatedPaths = Paths(puzzleStr)  # If cursor has reached last node
            n = Node(puzzleStr, prevPathList, updatedPaths)  # nodes will be updated
            removedLst.append(puzzleStr)  # removedList is updated
            puzzleStr = stack[-1]  # Since tree doesnt have any roots further we will backtrack them
            stack.pop()  # popping up the stack


        if puzzleStr == '012345678': #Enters when current cursor is goal state
            break # Breaking the loop
    return puzzleDict['012345678'] #returning the result

# This will be for next project
def astar(puzzle):
    list1 = []
    init = 0
    ExpandedList = []  # List for expanded Elements
    MemoryList = []  # List for Memory Elements
    VisitedList = []  # List to remove visited Nodes
    HeuristicDict = heuristicCalc(puzzle)  # Calculating Heuristic values
    puzzleStr = lstStr(puzzle)  # This function will take list and convert it into String
    Neibrs, Pathlist = BFSFndNeibrs(puzzleStr, VisitedList)  # initial Expansion for the root node
    intitialPath = puzzle.index(8)  # To find the initial position of the node
    ExpandedTempDict = {
        "nodeName": puzzleStr,
        "gCost": 0,
        "hCost": HeuristicDict[8],
        "pathList": [intitialPath],
        "parent": ""
    }  # creating th Dict for Expanded State
    MemoryList.append(ExpandedTempDict)  # Append the node into Memory
    VisitedList.append(puzzleStr)  # To Eliminate the loop
    while len(MemoryList) > 0:  # Will loop until the memory list is Empty
        prevStrDict = list(filter(lambda x: x["nodeName"] == puzzleStr, MemoryList))[
            0]  # Getting the data of previous Node
        for i in range(0, len(Neibrs)):  # This loop is used to add the neibhours to the memory List
            ExpandedFlag = list(filter(lambda x: x["nodeName"] == puzzleStr,
                                       ExpandedList))  # used to check if the node is visited or not
            if len(ExpandedFlag) == 0:  # checking of the above variable
                ExpandedTempDict = {
                    "nodeName": Neibrs[i],
                    "gCost": prevStrDict["gCost"] + 1,
                    "hCost": HeuristicDict[Pathlist[i]],
                    "pathList": prevStrDict["pathList"] + [Pathlist[int(i)]],
                    "parent": puzzleStr
                }  # Dict creation for memory list
                MemoryList.append(ExpandedTempDict) # Appending Node in to Memory
        MemoryList, PuzzleStrDict = RemoveFromMemory(MemoryList, puzzleStr)  # This Function will remove Expanded nodes from memory list
        ExpandedList.append(PuzzleStrDict)  # Appending the current Expanded Node to the list
        VisitedList.append(PuzzleStrDict["nodeName"])  # Appending Current node to Visited List
        if puzzleStr == '012345678':  # If Expanded node is 012345678 then break the loop
            break
        puzzleStr = MinimumFromMemoryList(MemoryList)["nodeName"]  # Get the monimum cost node from the Memory List
        Neibrs, Pathlist = BFSFndNeibrs(puzzleStr, VisitedList)  # Expanding the Neighbours
    for i in ExpandedList: # this loop is to get the goal node
        if i["nodeName"] == "012345678":  # Filtering the Expanded list for 012345678
            list1.extend(i["pathList"])  # Extending to the List1
    return list1

# Finding the minimum element from the Memory
def MinimumFromMemoryList(MemoryList):
    flag = 0
    minimumFcost = 0
    TempDict = {
        "nodeName": "",
        "gCost": 0,
        "hCost": 0,
        "pathList": [],
        "parent": ""
    }  # Taken temporary dict for minimim Dict
    for i in MemoryList:  # looping through memorylist to find minimum F cost node
        if flag == 0:
            minimumFcost = i["gCost"]+i["hCost"]
            TempDict["nodeName"] = i["nodeName"]
            TempDict["gCost"] = i["gCost"]
            TempDict["hCost"] = i["hCost"]
            TempDict["pathList"] = i["pathList"]
            TempDict["parent"] = i["parent"]
            flag += 1
        else:
            if i["gCost"]+i["hCost"] < minimumFcost:
                minimumFcost = i["gCost"]+i["hCost"]
                TempDict["nodeName"] = i["nodeName"]
                TempDict["gCost"] = i["gCost"]
                TempDict["hCost"] = i["hCost"]
                TempDict["pathList"] = i["pathList"]
                TempDict["parent"] = i["parent"]
            else:
                pass
    return TempDict

#Removing the nodes from the Memory
def RemoveFromMemory(MemoryList, puzzleStr):
    temp = list(filter(lambda x: x["nodeName"] == puzzleStr, MemoryList))  # find the puzzleString Dict in the Memory List
    for i in temp:
        MemoryList.remove(i)  # Will Remove the object from the list
    TempDict = MinimumFromMemoryList(temp)
    return MemoryList, TempDict  # will return the update memoryList and Puzzle String Dict

#Calculating the Heuristic values
def heuristicCalc(values):
    heuristicDict = {}
    for i in values:
        heuristicDict[i] = abs(i-values.index(i))
    return heuristicDict