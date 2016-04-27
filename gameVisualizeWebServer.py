import csv
import sqlite3
#import numpy as np

from flask import Flask, request, g, render_template, jsonify, url_for, Response, url_for, flash,session


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',t = "Soccer Interface")

#DATABASE = "/Users/Felix/Dropbox/SoccerProject/POC-exampleGames/Manchester City v FC Bayern Munchen-20131002/database-bigTable.db"
#DATABASE = "/Users/yumengzhu/Felix Dropbox/Dropbox/SoccerProject/POC-exampleGames/Manchester City v FC Bayern Munchen-20131002/database.db"
DATABASE = "/home/ubuntu/database-bigTable.db"


app.config.from_object(__name__)

def connect_to_database():
    return sqlite3.connect(app.config['DATABASE'])

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def execute_query(query, args=()):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows


@app.route("/getInitialData/", methods=['GET','POST'])
def getInitialData():
    
    

    global t1_data
    t1_data = execute_query("""SELECT A01_Name, A01_X, A01_Y, A02_Name, A02_X, A02_Y, A03_Name, A03_X, A03_Y,A04_Name, A04_X, A04_Y, A05_Name, A05_X, A05_Y, A06_Name, A06_X, A06_Y, A07_Name, A07_X, A07_Y, A08_Name, A08_X, A08_Y, A09_Name, A09_X, A09_Y, A10_Name, A10_X, A10_Y,A11_Name, A11_X, A11_Y FROM mancityVbayern WHERE half = 0   """ )
    
    global t2_data
    t2_data = execute_query("""SELECT B01_Name, B01_X, B01_Y, B02_Name, B02_X, B02_Y, B03_Name, B03_X, B03_Y,B04_Name, B04_X, B04_Y, B05_Name, B05_X, B05_Y, B06_Name, B06_X, B06_Y, B07_Name, B07_X, B07_Y, B08_Name, B08_X, B08_Y, B09_Name, B09_X, B09_Y, B10_Name, B10_X, B10_Y,B11_Name, B11_X, B11_Y FROM mancityVbayern WHERE half = 0   """ )
    
    global Goal_Time
    Goal_Time = execute_query("""SELECT time FROM mancityVbayern WHERE timeToShot = 10 AND half = 0  """ )
    
    
#    print len(t1_data)

#    outDict = {}
#    outDict["Number"] = len(Goal_Time)
#    outDict["G1"] = Goal_Time[0]
#    outDict["G2"] = Goal_Time[1]
#    outDict["G3"] = Goal_Time[2]
#    outDict["G4"] = Goal_Time[3]
#    out = [outDict,outDict];
#    

#    outDict = {"FrameData":[{"time":"1","name":"a"},{"time":"2","name":"b"}]}
#    print outDict
#    outDict["FrameData"].append({"time":"3", "name":"c"})

#    print out

    outDict = {"Frame":[]};
    for index in range(len(t1_data)):
        outDict["Frame"].append({"A01_Name":t1_data[index][0], "A01_X":t1_data[index][1], "A01_Y":t1_data[index][2], "A02_Name":t1_data[index][3], "A02_X":t1_data[index][4], "A02_Y":t1_data[index][5], "A03_Name":t1_data[index][6], "A03_X":t1_data[index][7], "A03_Y":t1_data[index][8], "A04_Name":t1_data[index][9], "A04_X":t1_data[index][10], "A04_Y":t1_data[index][11], "A05_Name":t1_data[index][12], "A05_X":t1_data[index][13], "A05_Y":t1_data[index][14], "A06_Name":t1_data[index][15], "A06_X":t1_data[index][16], "A06_Y":t1_data[index][17], "A07_Name":t1_data[index][18], "A07_X":t1_data[index][19], "A07_Y":t1_data[index][20], "A08_Name":t1_data[index][21], "A08_X":t1_data[index][22], "A08_Y":t1_data[index][23], "A09_Name":t1_data[index][24], "A09_X":t1_data[index][25], "A09_Y":t1_data[index][26], "A10_Name":t1_data[index][27], "A10_X":t1_data[index][28], "A10_Y":t1_data[index][29], "A11_Name":t1_data[index][30], "A11_X":t1_data[index][31], "A11_Y":t1_data[index][32],"B01_Name":t2_data[index][0], "B01_X":t2_data[index][1], "B01_Y":t2_data[index][2], "B02_Name":t2_data[index][3], "B02_X":t2_data[index][4], "B02_Y":t2_data[index][5], "B03_Name":t2_data[index][6], "B03_X":t2_data[index][7], "B03_Y":t2_data[index][8], "B04_Name":t2_data[index][9], "B04_X":t2_data[index][10], "B04_Y":t2_data[index][11], "B05_Name":t2_data[index][12], "B05_X":t2_data[index][13], "B05_Y":t2_data[index][14], "B06_Name":t2_data[index][15], "B06_X":t2_data[index][16], "B06_Y":t2_data[index][17], "B07_Name":t2_data[index][18], "B07_X":t2_data[index][19], "B07_Y":t2_data[index][20], "B08_Name":t2_data[index][21], "B08_X":t2_data[index][22], "B08_Y":t2_data[index][23], "B09_Name":t2_data[index][24], "B09_X":t2_data[index][25], "B09_Y":t2_data[index][26], "B10_Name":t2_data[index][27], "B10_X":t2_data[index][28], "B10_Y":t2_data[index][29], "B11_Name":t2_data[index][30], "B11_X":t2_data[index][31], "B11_Y":t2_data[index][32],"time":index})
#        print 'Current fruit :', fruits[index]

#    print outDict
    return jsonify(outDict)


    # this will put this as a JSON object
    #ret_data = {"homeTeamDict": homeTeamDict,}
#    #"homeSG": returnedDict["homePlayer2"],   "homeC": returnedDict["homePlayer3"],"homeSF": returnedDict["homePlayer4"], "homePF": returnedDict["homePlayer5"],  "awayPG": returnedDict["awayPlayer1"], "awaySG": returnedDict["awayPlayer2"],   "awayC": returnedDict["awayPlayer3"],"awaySF": returnedDict["awayPlayer4"], "awayPF": returnedDict["awayPlayer5"], "ballInfo": returnedDict["ballInfo"],}
#    return jsonify(outDict)


@app.route("/getFrameData/", methods=['GET','POST'])
def getFrameData():
    
    
    frameNo = int(request.args.get("time"))
    nextTime = float(request.args.get("time"))/10
    
    outDict = {}
    outDict["A01_Name"] = t1_data[frameNo][0]
    outDict["A01_X"] = t1_data[frameNo][1]
    outDict["A01_Y"] = t1_data[frameNo][2]

    outDict["A02_Name"] = t1_data[frameNo][3]
    outDict["A02_X"] = t1_data[frameNo][4]
    outDict["A02_Y"] = t1_data[frameNo][5]

    outDict["A03_Name"] = t1_data[frameNo][6]
    outDict["A03_X"] = t1_data[frameNo][7]
    outDict["A03_Y"] = t1_data[frameNo][8]

    outDict["A04_Name"] = t1_data[frameNo][9]
    outDict["A04_X"] = t1_data[frameNo][10]
    outDict["A04_Y"] = t1_data[frameNo][11]

    outDict["A05_Name"] = t1_data[frameNo][12]
    outDict["A05_X"] = t1_data[frameNo][13]
    outDict["A05_Y"] = t1_data[frameNo][14]

    outDict["A06_Name"] = t1_data[frameNo][15]
    outDict["A06_X"] = t1_data[frameNo][16]
    outDict["A06_Y"] = t1_data[frameNo][17]

    outDict["A07_Name"] = t1_data[frameNo][18]
    outDict["A07_X"] = t1_data[frameNo][19]
    outDict["A07_Y"] = t1_data[frameNo][20]

    outDict["A08_Name"] = t1_data[frameNo][21]
    outDict["A08_X"] = t1_data[frameNo][22]
    outDict["A08_Y"] = t1_data[frameNo][23]

    outDict["A09_Name"] = t1_data[frameNo][24]
    outDict["A09_X"] = t1_data[frameNo][25]
    outDict["A09_Y"] = t1_data[frameNo][26]

    outDict["A10_Name"] = t1_data[frameNo][27]
    outDict["A10_X"] = t1_data[frameNo][28]
    outDict["A10_Y"] = t1_data[frameNo][29]

    outDict["A11_Name"] = t1_data[frameNo][30]
    outDict["A11_X"] = t1_data[frameNo][31]
    outDict["A11_Y"] = t1_data[frameNo][32]

    outDict["B01_Name"] = t2_data[frameNo][0]
    outDict["B01_X"] = t2_data[frameNo][1]
    outDict["B01_Y"] = t2_data[frameNo][2]
    
    outDict["B02_Name"] = t2_data[frameNo][3]
    outDict["B02_X"] = t2_data[frameNo][4]
    outDict["B02_Y"] = t2_data[frameNo][5]
    
    outDict["B03_Name"] = t2_data[frameNo][6]
    outDict["B03_X"] = t2_data[frameNo][7]
    outDict["B03_Y"] = t2_data[frameNo][8]
    
    outDict["B04_Name"] = t2_data[frameNo][9]
    outDict["B04_X"] = t2_data[frameNo][10]
    outDict["B04_Y"] = t2_data[frameNo][11]
    
    outDict["B05_Name"] = t2_data[frameNo][12]
    outDict["B05_X"] = t2_data[frameNo][13]
    outDict["B05_Y"] = t2_data[frameNo][14]
    
    outDict["B06_Name"] = t2_data[frameNo][15]
    outDict["B06_X"] = t2_data[frameNo][16]
    outDict["B06_Y"] = t2_data[frameNo][17]
    
    outDict["B07_Name"] = t2_data[frameNo][18]
    outDict["B07_X"] = t2_data[frameNo][19]
    outDict["B07_Y"] = t2_data[frameNo][20]
    
    outDict["B08_Name"] = t2_data[frameNo][21]
    outDict["B08_X"] = t2_data[frameNo][22]
    outDict["B08_Y"] = t2_data[frameNo][23]
    
    outDict["B09_Name"] = t2_data[frameNo][24]
    outDict["B09_X"] = t2_data[frameNo][25]
    outDict["B09_Y"] = t2_data[frameNo][26]
    
    outDict["B10_Name"] = t2_data[frameNo][27]
    outDict["B10_X"] = t2_data[frameNo][28]
    outDict["B10_Y"] = t2_data[frameNo][29]
    
    outDict["B11_Name"] = t2_data[frameNo][30]
    outDict["B11_X"] = t2_data[frameNo][31]
    outDict["B11_Y"] = t2_data[frameNo][32]

    outDict["time"] = nextTime
    # give the next time
    outDict["nextTime"] = nextTime+0.1
    
    outDict["firstFrameTime"]= nextTime
    outDict["lastFrameTime"] = nextTime
    #   timeStamps = np.unique(rows)
    outDict["noFrames"] = 28000
    
    return jsonify(outDict)
    
#    dataT1 = execute_query("""SELECT * FROM mancityVbayern WHERE time = (? ) AND half = (? ) AND clubName = "Manchester City" """,  (nextTime, "First Half") )
#    
#    dataT2 = execute_query("""SELECT * FROM mancityVbayern WHERE time = (? ) AND half = (? ) AND clubName = "FC Bayern Munchen" """,  (nextTime, "First Half") )

#    outDict = {}
#    outDict["A01_Name"] = dataT1[0][2]
#    outDict["A01_X"] = dataT1[0][4]
#    outDict["A01_Y"] = dataT1[0][5]
#    
#    outDict["A02_Name"] = dataT1[1][2]
#    outDict["A02_X"] = dataT1[1][4]
#    outDict["A02_Y"] = dataT1[1][5]
#
#    outDict["A03_Name"] = dataT1[2][2]
#    outDict["A03_X"] = dataT1[2][4]
#    outDict["A03_Y"] = dataT1[2][5]
#    
#    outDict["A04_Name"] = dataT1[3][2]
#    outDict["A04_X"] = dataT1[3][4]
#    outDict["A04_Y"] = dataT1[3][5]
#
#    outDict["A05_Name"] = dataT1[4][2]
#    outDict["A05_X"] = dataT1[4][4]
#    outDict["A05_Y"] = dataT1[4][5]
#    
#    outDict["A06_Name"] = dataT1[5][2]
#    outDict["A06_X"] = dataT1[5][4]
#    outDict["A06_Y"] = dataT1[5][5]
#    
#    outDict["A07_Name"] = dataT1[6][2]
#    outDict["A07_X"] = dataT1[6][4]
#    outDict["A07_Y"] = dataT1[6][5]
#
#    outDict["A08_Name"] = dataT1[7][2]
#    outDict["A08_X"] = dataT1[7][4]
#    outDict["A08_Y"] = dataT1[7][5]
#    
#    outDict["A09_Name"] = dataT1[8][2]
#    outDict["A09_X"] = dataT1[8][4]
#    outDict["A09_Y"] = dataT1[8][5]
#    
#    outDict["A10_Name"] = dataT1[9][2]
#    outDict["A10_X"] = dataT1[9][4]
#    outDict["A10_Y"] = dataT1[9][5]
#    
#    outDict["A11_Name"] = dataT1[10][2]
#    outDict["A11_X"] = dataT1[10][4]
#    outDict["A11_Y"] = dataT1[10][5]
#    
#    outDict["B01_Name"] = dataT2[0][2]
#    outDict["B01_X"] = dataT2[0][4]
#    outDict["B01_Y"] = dataT2[0][5]
#
#    outDict["B02_Name"] = dataT2[1][2]
#    outDict["B02_X"] = dataT2[1][4]
#    outDict["B02_Y"] = dataT2[1][5]
#
#    outDict["B03_Name"] = dataT2[2][2]
#    outDict["B03_X"] = dataT2[2][4]
#    outDict["B03_Y"] = dataT2[2][5]
#    
#    outDict["B04_Name"] = dataT2[3][2]
#    outDict["B04_X"] = dataT2[3][4]
#    outDict["B04_Y"] = dataT2[3][5]
#    
#    outDict["B05_Name"] = dataT2[4][2]
#    outDict["B05_X"] = dataT2[4][4]
#    outDict["B05_Y"] = dataT2[4][5]
#
#    outDict["B06_Name"] = dataT2[5][2]
#    outDict["B06_X"] = dataT2[5][4]
#    outDict["B06_Y"] = dataT2[5][5]
#    
#    outDict["B07_Name"] = dataT2[6][2]
#    outDict["B07_X"] = dataT2[6][4]
#    outDict["B07_Y"] = dataT2[6][5]
#    
#    outDict["B08_Name"] = dataT2[7][2]
#    outDict["B08_X"] = dataT2[7][4]
#    outDict["B08_Y"] = dataT2[7][5]
#    
#    outDict["B09_Name"] = dataT2[8][2]
#    outDict["B09_X"] = dataT2[8][4]
#    outDict["B09_Y"] = dataT2[8][5]
#    
#    outDict["B10_Name"] = dataT2[9][2]
#    outDict["B10_X"] = dataT2[9][4]
#    outDict["B10_Y"] = dataT2[9][5]
#
#    outDict["B11_Name"] = dataT2[10][2]
#    outDict["B11_X"] = dataT2[10][4]
#    outDict["B11_Y"] = dataT2[10][5]



# -------------- end of this function ------------------

    # get the matrix of the players here
#    homePlayerMatrix = np.zeros((11,2))
#    homePlayerMatrix[0,:] = (playerA01[0][1], playerA01[0][2])
#    homePlayerMatrix[1,:] = (playerA02[0][1], playerA02[0][2])
#    homePlayerMatrix[2,:] = (playerA03[0][1], playerA03[0][2])
#    homePlayerMatrix[3,:] = (playerA04[0][1], playerA04[0][2])
#    homePlayerMatrix[4,:] = (playerA05[0][1], playerA05[0][2])
#    homePlayerMatrix[5,:] = (playerA06[0][1], playerA06[0][2])
#    homePlayerMatrix[6,:] = (playerA07[0][1], playerA07[0][2])
#    homePlayerMatrix[7,:] = (playerA08[0][1], playerA08[0][2])
#    homePlayerMatrix[8,:] = (playerA09[0][1], playerA09[0][2])
#    homePlayerMatrix[9,:] = (playerA10[0][1], playerA10[0][2])
#    homePlayerMatrix[10,:] = (playerA11[0][1], playerA11[0][2])


#   len(timeStamps)

#    print outDict
#    awayPlayerMatrix = np.zeros((11,2))
#    awayPlayerMatrix[0,:] = (playerB01[0][1], playerB01[0][2])
#    awayPlayerMatrix[1,:] = (playerB02[0][1], playerB02[0][2])
#    awayPlayerMatrix[2,:] = (playerB03[0][1], playerB03[0][2])
#    awayPlayerMatrix[3,:] = (playerB04[0][1], playerB04[0][2])
#    awayPlayerMatrix[4,:] = (playerB05[0][1], playerB05[0][2])
#    awayPlayerMatrix[5,:] = (playerB06[0][1], playerB06[0][2])
#    awayPlayerMatrix[6,:] = (playerB07[0][1], playerB07[0][2])
#    awayPlayerMatrix[7,:] = (playerB08[0][1], playerB08[0][2])
#    awayPlayerMatrix[8,:] = (playerB09[0][1], playerB09[0][2])
#    awayPlayerMatrix[9,:] = (playerB10[0][1], playerB10[0][2])
#    awayPlayerMatrix[10,:] = (playerB11[0][1], playerB11[0][2])

# print outDict
#print "test";
    # do role assignment here
    # doRoleAssignment(outDict, homePlayerMatrix, awayPlayerMatrix)

        #return Response(generate(), mimetype='json')

    # this will put this as a JSON object
    #ret_data = {"homeTeamDict": homeTeamDict,}
    #    #"homeSG": returnedDict["homePlayer2"],   "homeC": returnedDict["homePlayer3"],"homeSF": returnedDict["homePlayer4"], "homePF": eturnedDict["homePlayer5"],  "awayPG": returnedDict["awayPlayer1"], "awaySG": returnedDict["awayPlayer2"],   "awayC": returnedDict["awayPlayer3"],"awaySF": returnedDict["awayPlayer4"], "awayPF": returnedDict["awayPlayer5"], "ballInfo": returnedDict["ballInfo"],}



# we do role assignment here
#def doRoleAssignment(inDict, homePlayerMatrix, awayPlayerMatrix):
#
#    # set the template - home - on-field players
#    #                                LB,     LCB,      RCB,       RB,      LCM,       RCM,      ACM,  LW,    ST,  RW
#    homeTemplate = np.matrix('-350,-150; -350, -50; -350,50; -250,50; -200,-50; -200,50; -150,0; -100,-150; 0,+50; -100,150')
#    awayTemplate = homeTemplate*-1
#    
#    # who is the goal-keeper
#    idx = range(0,11)
#    idx = idx[:3] + idx[4:]
#    print idx
#    # player idx 3 is the goalkeeper
#    homeMat = homePlayerMatrix[idx,:]
#    awayMat = awayPlayerMatrix[1:,:]
#    
#    # now get the cost matrix
#    homeCostMat = np.zeros((10,10))
#    awayCostMat = np.zeros((10,10))
#    
#    print homeMat.shape
#    print awayMat.shape
#    
#    
#    for i in range(0,10):
#        for j in range(0,10):
#
#            print i, j
#            homeCostMat[i,j] = np.sqrt(np.power(homeTemplate[i,0] - homeMat[j,0], 2) + np.power(homeTemplate[i,1] - homeMat[j,1], 2))
#            awayCostMat[i,j] = np.sqrt(np.power(awayTemplate[i,0] - awayMat[j,0], 2) + np.power(awayTemplate[i,1] - awayMat[j,1], 2))
#
##
##
##
#    print homeCostMat
#    print awayCostMat
#    # do the Hungarian algorithm here
#    doHungarian(homeCostMat)
#    doHungarian(awayCostMat)
#
#
#def doHungarian(matrix):
#
#
#    from munkres import Munkres, print_matrix
#    print "We do the hungarian algorithm here"
#
#    m = Munkres()
#    indexes = m.compute(matrix)
#    print indexes
#    # bug with print_matrix...
#    #print_matrix(matrix, msg='Lowest cost through this matrix:')
#    total = 0
#
#    print "gets to here"
#    
#    for row, column in indexes:
#        print row, column
#        
#        value = matrix[row][column]
#        print matrix
#        print value
#        total += value
#        print '(%d, %d) -> %d' % (row, column, value)
#    print 'total cost: %d' % total




#@app.route("/retrieveData/", methods=['GET','POST'])
#def retrieveData():
#    
#    print "Something here"
#    # This needed to be POST from the javascript file
#    requestJSONfile = request.get_json()
#    
#    dataDict = {}
#    
#    # read in the trajectory data from the function - info format
#    trajLengthSec = requestJSONfile["trajLength"]
#    
#    # do it for the home team
#    trajHomePG = requestJSONfile["trajVecHomePG"]
#    # maybe have a function to get the proper structure
#    normTrajHomePG = enforceTrajStructure(trajHomePG, trajLengthSec)
#    dataDict = {"homePG": normTrajHomePG}
#    
#    trajHomeSG = requestJSONfile["trajVecHomeSG"]
#    normTrajHomeSG = enforceTrajStructure(trajHomeSG, trajLengthSec)
#    dataDict.update({"homeSG": normTrajHomeSG})
#    
#    trajHomeC = requestJSONfile["trajVecHomeC"]
#    normTrajHomeC = enforceTrajStructure(trajHomeC, trajLengthSec)
#    dataDict.update({"homeC": normTrajHomeC})
#    
#    trajHomeSF = requestJSONfile["trajVecHomeSF"]
#    normTrajHomeSF = enforceTrajStructure(trajHomeSF, trajLengthSec)
#    dataDict.update({"homeSF": normTrajHomeSF})
#    
#    trajHomePF = requestJSONfile["trajVecHomePF"]
#    normTrajHomePF = enforceTrajStructure(trajHomePF, trajLengthSec)
#    dataDict.update({"homePF": normTrajHomePF})
#    
#    trajAwayPG = requestJSONfile["trajVecAwayPG"]
#    normTrajAwayPG = enforceTrajStructure(trajAwayPG, trajLengthSec)
#    dataDict.update({"awayPG": normTrajAwayPG})
#    
#    trajAwaySG = requestJSONfile["trajVecAwaySG"]
#    normTrajAwaySG = enforceTrajStructure(trajAwaySG, trajLengthSec)
#    dataDict.update({"awaySG": normTrajAwaySG})
#    
#    trajAwayC = requestJSONfile["trajVecAwayC"]
#    normTrajAwayC = enforceTrajStructure(trajAwayC, trajLengthSec)
#    dataDict.update({"awayC": normTrajAwayC})
#    
#    trajAwaySF = requestJSONfile["trajVecAwaySF"]
#    normTrajAwaySF = enforceTrajStructure(trajAwaySF, trajLengthSec)
#    dataDict.update({"awaySF": normTrajAwaySF})
#    
#    trajAwayPF = requestJSONfile["trajVecAwayPF"]
#    normTrajAwayPF = enforceTrajStructure(trajAwayPF, trajLengthSec)
#    dataDict.update({"awayPF": normTrajAwayPF})
#    
#    trajBall = requestJSONfile["trajVecBall"]
#    normTrajBall = enforceTrajStructure(trajBall, trajLengthSec)
#    dataDict.update({"ball": normTrajBall})
#    
#    # set the number of plays here
#    noRetrievedPlays = 5
#    
#    # form the info file here and save to S3 bucket
#    getQueryInfoFile(dataDict,noRetrievedPlays, trajLengthSec)
#    
#    # spit it to the S3 bucket
#    import os
#    import paramiko
#    
#    # spit it to the S3 bucket
#    path = "/Users/LUCEYMBP/Dropbox/Projects-Patrick/Flask/hackathonFrontEnd2/"
#    fileName = "info"
#    os.system("aws s3 cp /Users/LUCEYMBP/Dropbox/Projects-Patrick/Flask/hackathonFrontEnd2/info s3://stats-datascience-1/spark/")
#    
#    # now let's do the retrieval
#    dns = "ec2-54-152-93-56.compute-1.amazonaws.com"
#    k = paramiko.RSAKey.from_private_key_file("/Users/LUCEYMBP/AWS/stats-datascience-dev.pem")
#    c = paramiko.SSHClient()
#    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#    
#    
#    print "connecting"
#    c.connect(hostname=dns, username="ec2-user", pkey=k)
#    print "connected"
#    
#    command = "sudo spark-submit --packages TargetHolding/pyspark-cassandra:0.2.7 --master yarn --conf spark.cassandra.connection.host=ec2-54-173-219-73.compute-1.amazonaws.com --conf spark.executor.extraClassPath=/home/hadoop/lib/guava-19.0.jar:/etc/hadoop/conf:/etc/hive/conf:/usr/lib/hadoop-lzo/lib/*:/usr/share/aws/aws-java-sdk/*:/usr/share/aws/emr/emrfs/conf:/usr/share/aws/emr/emrfs/lib/*:/usr/share/aws/emr/emrfs/auxlib/* --conf spark.driver.extraClassPath=/home/hadoop/lib/guava-19.0.jar:/etc/hadoop/conf:/etc/hive/conf:/usr/lib/hadoop-lzo/lib/*:/usr/share/aws/aws-java-sdk/*:/usr/share/aws/emr/emrfs/conf:/usr/share/aws/emr/emrfs/lib/*:/usr/share/aws/emr/emrfs/auxlib/* --files s3://stats-datascience-1/spark/DictionaryTraj-01.csv,s3://stats-datascience-1/spark/DictionaryTraj-02.csv,s3://stats-datascience-1/spark/DictionaryTraj-03.csv,s3://stats-datascience-1/spark/DictionaryTraj-04.csv,s3://stats-datascience-1/spark/DictionaryTraj-05.csv,s3://stats-datascience-1/spark/info --deploy-mode cluster s3://stats-datascience-1/spark/retrieveFromDatabase1.1.py"
#    
#    os.system("aws s3 rm s3://stats-datascience-1/spark/output/  --recursive")
#    stdin , stdout, stderr = c.exec_command(command)
#    # read in the retrieved results
#    if stdout.channel.recv_exit_status() == 0:
#        print "finished"
#        
#        print "Now we have to get the output files"
#        num = noRetrievedPlays
#        os.system("aws s3 cp s3://stats-datascience-1/spark/output/ output --recursive")
#        for n in xrange(num):
#            if n < 10:
#                outputFile = "output/output-0000" + "%i" % n + "/part-00000"
#                # we have to
#                print outputFile
#            #getOutputJSON(outputFile)
#            else:
#                outputFile = "output/output-000" + "%i" % n + "/part-00000"
#
##os.system("rm -r output")
#
#c.close()
#    print "finished this bit"
#    
#    return "poo"
#
#
#
## method to get enforce/normalize trajectory
#def enforceTrajStructure(inTrajVec, trajLength):
#    
#    noCurrFrames = len(inTrajVec)/2
#    # (window * 25fps * 2 (x,y) + 2 extra frame)/2
#    noDesiredFrames = ((int(trajLength)*25*2)+2)/2
#    
#    # get the vectors -
#    xVec = inTrajVec[ ::2] # this gets every second number starting from 0
#    yVec = inTrajVec[ 1::2] # this gets every second number starting from 1
#    print xVec, yVec, noCurrFrames, noDesiredFrames, len(inTrajVec)
#    
#    # do interpolation here to get the t values - for 1 sec 26 frames
#    t = np.linspace(1, noDesiredFrames, len(inTrajVec)/2  )
#    tvals = np.linspace(1, noDesiredFrames, noDesiredFrames) # just single timestamps
#    xinterp = np.interp(tvals, t, xVec)
#    yinterp = np.interp(tvals, t, yVec)
#    
#    print xinterp, yinterp
#    normTrajVec = []
#    # now merge into a single vector
#    for i in range(0,len(xinterp)):
#        # divide by 10 to get into the same frame-of-reference
#        normTrajVec.append([xinterp[i]/10,yinterp[i]/10])
#        print xinterp[i]/10, yinterp[i]/10, normTrajVec
#    
#    return normTrajVec
#
#def getQueryInfoFile(dataDict,noRetrievedPlays, trajLengthSec):
#    
#    # open the info file
#    outFile = open('info-temp','w')
#    
#    # season number
#    outFile.write("2012\n")
#    print("why does it fail")
#    # number of seconds
#    stringos = "%d\n%d\n" %(int(trajLengthSec), noRetrievedPlays )
#    outFile.write(stringos)
#    # number of plays
#    #outFile.write("%d\n" %noRetrievedPlays)
#    # homePG trajectory
#    print dataDict["homePG"]
#    for vals in dataDict["homePG"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
#    # space and new line
#    outFile.write("\n")
#
#print dataDict["homeSG"]
#    for vals in dataDict["homeSG"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
## space and new line
#outFile.write("\n")
#    
#    print dataDict["homeSF"]
#    for vals in dataDict["homeSF"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
#    # space and new line
#    outFile.write("\n")
#
#print dataDict["homePF"]
#    for vals in dataDict["homePF"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
## space and new line
#outFile.write("\n")
#    
#    print dataDict["homeC"]
#    for vals in dataDict["homeC"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
#    # space and new line
#    outFile.write("\n")
#
#print dataDict["awayPG"]
#    for vals in dataDict["awayPG"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
## space and new line
#outFile.write("\n")
#    
#    print dataDict["awaySG"]
#    for vals in dataDict["awaySG"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
## space and new line
#outFile.write("\n")
#    
#    print dataDict["awaySF"]
#    for vals in dataDict["awaySF"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
#    # space and new line
#    outFile.write("\n")
#    
#    print dataDict["awayPF"]
#    for vals in dataDict["awayPF"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
## space and new line
#outFile.write("\n")
#    
#    print dataDict["awayC"]
#    for vals in dataDict["awayC"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
#    # space and new line
#    outFile.write("\n")
#
#print dataDict["ball"]
#    for vals in dataDict["ball"]:
#        inStr = "%2.8f,%2.8f," %(vals[0], vals[1])
#        outFile.write(inStr)
## space and new line
#outFile.write("\n")
#    
#    outFile.close()
#    print("gets to here")
#    
#    newOutFile = open("info","w")
#    outFile = open("info-temp","r")
#    # now remove the commas at the end of the line?
#    i=0
#    for line in outFile:
#        i=i+1
#        print line
#        if (i>3):
#            stros = "%s\n" %(line[0:len(line)-2])
#        else:
#            stros = line
#        newOutFile.write(stros)
#    outFile.close()
#    newOutFile.close()
#
#@app.route("/showRetrievedPlay/", methods=['GET','POST'])
#def showRetrieveData():
#    
#    print "Something here"
#    print request.args.get("playID")
#    
#    playID = request.args.get("playID")
#    
#    if (playID == "Play1"):
#        print "it is play 1"
#        outputFile = "output/output-00000/part-00000"
#        returnedDict = retrievedPlaysClass.visualizeRetrievedPlays(outputFile)
#    
#    if (playID == "Play2"):
#        print "it is play 2"
#        outputFile = "output/output-00001/part-00000"
#        returnedDict = retrievedPlaysClass.visualizeRetrievedPlays(outputFile)
#    
#    if (playID == "Play3"):
#        print "it is play 3"
#        outputFile = "output/output-00002/part-00000"
#        returnedDict = retrievedPlaysClass.visualizeRetrievedPlays(outputFile)
#    
#    if (playID == "Play4"):
#        print "it is play 4"
#        outputFile = "output/output-00003/part-00000"
#        returnedDict = retrievedPlaysClass.visualizeRetrievedPlays(outputFile)
#    
#    if (playID == "Play5"):
#        print "it is play 5"
#        outputFile = "output/output-00004/part-00000"
#        returnedDict = retrievedPlaysClass.visualizeRetrievedPlays(outputFile)
#    
#    # this will put this as a JSON object
#    ret_data = {"homePG": returnedDict["homePlayer1"], "homeSG": returnedDict["homePlayer2"],   "homeC": returnedDict["homePlayer3"],"homeSF": returnedDict["homePlayer4"], "homePF": returnedDict["homePlayer5"],  "awayPG": returnedDict["awayPlayer1"], "awaySG": returnedDict["awayPlayer2"],   "awayC": returnedDict["awayPlayer3"],"awaySF": returnedDict["awayPlayer4"], "awayPF": returnedDict["awayPlayer5"], "ballInfo": returnedDict["ballInfo"],}
#    return jsonify(ret_data)
#
#
#@app.route("/doPrediction/", methods=['GET', 'POST'])
#def doPrediction():
#    
#    import InteractivePrediction
#    print "do prediction here"
#    # we do the prediction from the info file
#    outPrediction = InteractivePrediction.doPrediction()
#    
#    
#    return "poo"
#
#
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)