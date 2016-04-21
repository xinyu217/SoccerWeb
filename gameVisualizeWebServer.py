import csv
import sqlite3
#import numpy as np

from flask import Flask, request, g, render_template, jsonify, url_for, Response, url_for, flash,session

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',t = "Soccer Interface")

DATABASE = "/Users/Felix/Dropbox/SoccerProject/POC-exampleGames/Manchester City v FC Bayern Munchen-20131002/database.db"

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
    
    #print "Something here"
    #print request.args.get("teamID")
    
    # get the times or number of frames
    
    # maybe return the first timeFrame - get the object for all files here
    rows = execute_query("""SELECT time FROM mancityVbayern WHERE Half = 0""")
    #print "number of rows are"
#    timeStamps = np.unique(rows)
    #print "number of timeStamps are"
    #print len(timeStamps)
    
#    firstFrameVal = np.min(timeStamps)
    #print rows[0][0], 0
    #print type(rows[0])
    halfNo = 0
    
    global timeVec
#    timeVec = timeStamps

    # had to change the rows[0] as it was a tuple (0.0,)
#    firstRow = execute_query("""SELECT * FROM mancityVbayern WHERE time = (?) AND half = (?)""",  (rows[3][0], int(0)) )
    #print firstRow
    
    
    
    
    
    
    
    playerA01 = execute_query("""SELECT A01_Name text, A01_X real, A01_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA02 = execute_query("""SELECT A02_Name text, A02_X real, A02_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA03 = execute_query("""SELECT A03_Name text, A03_X real, A03_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA04 = execute_query("""SELECT A04_Name text, A04_X real, A04_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA05 = execute_query("""SELECT A05_Name text, A05_X real, A05_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA06 = execute_query("""SELECT A06_Name text, A06_X real, A06_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA07 = execute_query("""SELECT A07_Name text, A07_X real, A07_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA08 = execute_query("""SELECT A08_Name text, A08_X real, A08_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA09 = execute_query("""SELECT A09_Name text, A09_X real, A09_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA10 = execute_query("""SELECT A10_Name text, A10_X real, A10_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerA11 = execute_query("""SELECT A11_Name text, A11_X real, A11_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    
    playerB01 = execute_query("""SELECT B01_Name text, B01_X real, B01_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB02 = execute_query("""SELECT B02_Name text, B02_X real, B02_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB03 = execute_query("""SELECT B03_Name text, B03_X real, B03_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB04 = execute_query("""SELECT B04_Name text, B04_X real, B04_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB05 = execute_query("""SELECT B05_Name text, B05_X real, B05_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB06 = execute_query("""SELECT B06_Name text, B06_X real, B06_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB07 = execute_query("""SELECT B07_Name text, B07_X real, B07_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB08 = execute_query("""SELECT B08_Name text, B08_X real, B08_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB09 = execute_query("""SELECT B09_Name text, B09_X real, B09_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB10 = execute_query("""SELECT B10_Name text, B10_X real, B10_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )
    playerB11 = execute_query("""SELECT B11_Name text, B11_X real, B11_Y real FROM mancityVbayern WHERE time = (? ) AND Half = (? )""",  (rows[0][0], int(0)) )

    outDict = {}
    outDict["A01_Name"] = playerA01[0][0]
    outDict["A01_X"] = playerA01[0][1]
    outDict["A01_Y"] = playerA01[0][2]

    outDict["A02_Name"] = playerA02[0][0]
    outDict["A02_X"] = playerA02[0][1]
    outDict["A02_Y"] = playerA02[0][2]

    outDict["A03_Name"] = playerA03[0][0]
    outDict["A03_X"] = playerA03[0][1]
    outDict["A03_Y"] = playerA03[0][2]

    outDict["A04_Name"] = playerA04[0][0]
    outDict["A04_X"] = playerA04[0][1]
    outDict["A04_Y"] = playerA04[0][2]

    outDict["A05_Name"] = playerA05[0][0]
    outDict["A05_X"] = playerA05[0][1]
    outDict["A05_Y"] = playerA05[0][2]

    outDict["A06_Name"] = playerA06[0][0]
    outDict["A06_X"] = playerA06[0][1]
    outDict["A06_Y"] = playerA06[0][2]
    
    outDict["A07_Name"] = playerA07[0][0]
    outDict["A07_X"] = playerA07[0][1]
    outDict["A07_Y"] = playerA07[0][2]

    outDict["A08_Name"] = playerA08[0][0]
    outDict["A08_X"] = playerA08[0][1]
    outDict["A08_Y"] = playerA08[0][2]

    outDict["A09_Name"] = playerA09[0][0]
    outDict["A09_X"] = playerA09[0][1]
    outDict["A09_Y"] = playerA09[0][2]

    outDict["A10_Name"] = playerA10[0][0]
    outDict["A10_X"] = playerA10[0][1]
    outDict["A10_Y"] = playerA10[0][2]

    outDict["A11_Name"] = playerA11[0][0]
    outDict["A11_X"] = playerA11[0][1]
    outDict["A11_Y"] = playerA11[0][2]
    
    outDict["B01_Name"] = playerB01[0][0]
    outDict["B01_X"] = playerB01[0][1]
    outDict["B01_Y"] = playerB01[0][2]
    
    outDict["B02_Name"] = playerB02[0][0]
    outDict["B02_X"] = playerB02[0][1]
    outDict["B02_Y"] = playerB02[0][2]
    
    outDict["B03_Name"] = playerB03[0][0]
    outDict["B03_X"] = playerB03[0][1]
    outDict["B03_Y"] = playerB03[0][2]
    
    outDict["B04_Name"] = playerB04[0][0]
    outDict["B04_X"] = playerB04[0][1]
    outDict["B04_Y"] = playerB04[0][2]
    
    outDict["B05_Name"] = playerB05[0][0]
    outDict["B05_X"] = playerB05[0][1]
    outDict["B05_Y"] = playerB05[0][2]
    
    outDict["B06_Name"] = playerB06[0][0]
    outDict["B06_X"] = playerB06[0][1]
    outDict["B06_Y"] = playerB06[0][2]
    
    outDict["B07_Name"] = playerB07[0][0]
    outDict["B07_X"] = playerB07[0][1]
    outDict["B07_Y"] = playerB07[0][2]
    
    outDict["B08_Name"] = playerB08[0][0]
    outDict["B08_X"] = playerB08[0][1]
    outDict["B08_Y"] = playerB08[0][2]
    
    outDict["B09_Name"] = playerB09[0][0]
    outDict["B09_X"] = playerB09[0][1]
    outDict["B09_Y"] = playerB09[0][2]
    
    outDict["B10_Name"] = playerB10[0][0]
    outDict["B10_X"] = playerB10[0][1]
    outDict["B10_Y"] = playerB10[0][2]

    outDict["B11_Name"] = playerB11[0][0]
    outDict["B11_X"] = playerB11[0][1]
    outDict["B11_Y"] = playerB11[0][2]
    
    outDict["time"] = rows[0]
    # give the next time
    outDict["nextTime"] = rows[1]
    
    outDict["firstFrameTime"]= rows[0]
    outDict["lastFrameTime"] = rows[len(rows)-1]
    outDict["noFrames"] = 28000


    # this will put this as a JSON object
    #ret_data = {"homeTeamDict": homeTeamDict,}
#    #"homeSG": returnedDict["homePlayer2"],   "homeC": returnedDict["homePlayer3"],"homeSF": returnedDict["homePlayer4"], "homePF": returnedDict["homePlayer5"],  "awayPG": returnedDict["awayPlayer1"], "awaySG": returnedDict["awayPlayer2"],   "awayC": returnedDict["awayPlayer3"],"awaySF": returnedDict["awayPlayer4"], "awayPF": returnedDict["awayPlayer5"], "ballInfo": returnedDict["ballInfo"],}
    return jsonify(outDict)


@app.route("/getFrameData/", methods=['GET','POST'])
def getFrameData():
    
    frameNo = int(request.args.get("time"))
    nextTime = float(request.args.get("time"))/10
    
    dataT1 = execute_query("""SELECT * FROM mancityVbayern WHERE time = (? ) AND half = (? ) AND clubName = "Manchester City" """,  (nextTime, "First Half") )
    
    dataT2 = execute_query("""SELECT * FROM mancityVbayern WHERE time = (? ) AND half = (? ) AND clubName = "FC Bayern Munchen" """,  (nextTime, "First Half") )

    outDict = {}
    outDict["A01_Name"] = dataT1[0][2]
    outDict["A01_X"] = dataT1[0][4]
    outDict["A01_Y"] = dataT1[0][5]
    
    outDict["A02_Name"] = dataT1[1][2]
    outDict["A02_X"] = dataT1[1][4]
    outDict["A02_Y"] = dataT1[1][5]

    outDict["A03_Name"] = dataT1[2][2]
    outDict["A03_X"] = dataT1[2][4]
    outDict["A03_Y"] = dataT1[2][5]
    
    outDict["A04_Name"] = dataT1[3][2]
    outDict["A04_X"] = dataT1[3][4]
    outDict["A04_Y"] = dataT1[3][5]
    
    outDict["A05_Name"] = dataT1[4][2]
    outDict["A05_X"] = dataT1[4][4]
    outDict["A05_Y"] = dataT1[4][5]
    
    outDict["A06_Name"] = dataT1[5][2]
    outDict["A06_X"] = dataT1[5][4]
    outDict["A06_Y"] = dataT1[5][5]
    
    outDict["A07_Name"] = dataT1[6][2]
    outDict["A07_X"] = dataT1[6][4]
    outDict["A07_Y"] = dataT1[6][5]
    
    outDict["A08_Name"] = dataT1[7][2]
    outDict["A08_X"] = dataT1[7][4]
    outDict["A08_Y"] = dataT1[7][5]
    
    outDict["A09_Name"] = dataT1[8][2]
    outDict["A09_X"] = dataT1[8][4]
    outDict["A09_Y"] = dataT1[8][5]
    
    outDict["A10_Name"] = dataT1[9][2]
    outDict["A10_X"] = dataT1[9][4]
    outDict["A10_Y"] = dataT1[9][5]
    
    outDict["A11_Name"] = dataT1[10][2]
    outDict["A11_X"] = dataT1[10][4]
    outDict["A11_Y"] = dataT1[10][5]
    
    outDict["B01_Name"] = dataT2[0][2]
    outDict["B01_X"] = dataT2[0][4]
    outDict["B01_Y"] = dataT2[0][5]
    
    outDict["B02_Name"] = dataT2[1][2]
    outDict["B02_X"] = dataT2[1][4]
    outDict["B02_Y"] = dataT2[1][5]

    outDict["B03_Name"] = dataT2[2][2]
    outDict["B03_X"] = dataT2[2][4]
    outDict["B03_Y"] = dataT2[2][5]
    
    outDict["B04_Name"] = dataT2[3][2]
    outDict["B04_X"] = dataT2[3][4]
    outDict["B04_Y"] = dataT2[3][5]
    
    outDict["B05_Name"] = dataT2[4][2]
    outDict["B05_X"] = dataT2[4][4]
    outDict["B05_Y"] = dataT2[4][5]
    
    outDict["B06_Name"] = dataT2[5][2]
    outDict["B06_X"] = dataT2[5][4]
    outDict["B06_Y"] = dataT2[5][5]
    
    outDict["B07_Name"] = dataT2[6][2]
    outDict["B07_X"] = dataT2[6][4]
    outDict["B07_Y"] = dataT2[6][5]
    
    outDict["B08_Name"] = dataT2[7][2]
    outDict["B08_X"] = dataT2[7][4]
    outDict["B08_Y"] = dataT2[7][5]
    
    outDict["B09_Name"] = dataT2[8][2]
    outDict["B09_X"] = dataT2[8][4]
    outDict["B09_Y"] = dataT2[8][5]
    
    outDict["B10_Name"] = dataT2[9][2]
    outDict["B10_X"] = dataT2[9][4]
    outDict["B10_Y"] = dataT2[9][5]
    
    outDict["B11_Name"] = dataT2[10][2]
    outDict["B11_X"] = dataT2[10][4]
    outDict["B11_Y"] = dataT2[10][5]
    


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

    outDict["time"] = nextTime
    # give the next time
    outDict["nextTime"] = nextTime+0.1
    
    outDict["firstFrameTime"]= nextTime
    outDict["lastFrameTime"] = nextTime
#   timeStamps = np.unique(rows)
    outDict["noFrames"] = 28000
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
    return jsonify(outDict)


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