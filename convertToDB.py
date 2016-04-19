import numpy as np
import sqlite3
import os
import pickle
import math

# set the database structure
def convertFileListToDB(fileListName):

    # this gives the fileList
    fileList = open(fileListName,'r')

    # initialize the structure of the database here
    dbFileName = "/Users/LUCEYMACPRO/Dropbox/Data-Patrick/ProzoneData/newProzoneData/POC-exampleGames/Manchester City v FC Bayern Munchen-20131002/database-alt.db"
  
    # remove the database if it exists.
    if os.path.exists(dbFileName):
        os.remove(dbFileName)
    
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()

    # create SQL table
    c.execute('''CREATE TABLE mancityVbayern (half text, time real, playerName text, clubName text, xPos real, yPos real)''')

    # cycle through each trajectory file
    for trajFileName in fileList:
        
        #trajFile = open(trajFileName[0:len(trajFileName)-1],'r')

        # get the trajectory file
        trajFile = np.genfromtxt(trajFileName[0:len(trajFileName)-1], delimiter=',',dtype=[('matchName', 'S50'), ('Half', 'S20'), ('Time', 'f8'), ('PlayerName', 'S50'), ('Club', 'S50'), ('xPos', 'f8'), ('yPos', 'f8') ])

        # now go through each line and put it into the database
        for line in trajFile:

            # Insert a row of data
            c.execute("INSERT INTO mancityVbayern VALUES (?, ?, ?, ?, ?, ?)", (line[11], line[2], line[3], line[4], line[5], line[6]))
            #curr = cursor.execute('''SELECT * FROM bballQuarter WHERE ABSTIME = (? )''', (firstFrame[0],))
            #snapShot = execute_query("""SELECT * FROM bballQuarter WHERE ABSTIME = (? )""",rows[0])

            print line[11], line[2], line[3], line[4], line[5], line[6],

            conn.commit()

    # Close the connection
    conn.close()


# set the database structure
def convertBigTableToDB(bigTableName):
    
    # initialize the structure of the database here
    dbFileName = "/Users/LUCEYMACPRO/Dropbox/Data-Patrick/ProzoneData/newProzoneData/POC-exampleGames/Manchester City v FC Bayern Munchen-20131002/database-bigTable.db"
    
    # remove the database if it exists.
    if os.path.exists(dbFileName):
        os.remove(dbFileName)
    
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()

    # create SQL table
    #c.execute('''CREATE TABLE mancityVbayern (half text, time real, playerName text, clubName text, xPos real, yPos real)''')
    c.execute('''CREATE TABLE mancityVbayern (competition text, matchName text, teamA text, teamB text, eventName text, eventRow text, half integer, time real, player1Name text, player1Team text, player2Name text, payer2Team text, x real, y real, nextEventName text, nextPlayer1Name text, nextPlayer1Team text, nextX real, nextY real, inversionPoss integer, inversionActive integer, offensiveness real, possession text, activeTeam text, transition text, playerTransition text, goalDifference integer, possessionNumber integer, moveNumber integer, lastDirectPlay real,lastCounterAttack real, lastMaintenance real, lastBuildUp real, lastSustainedThreat real, lastFastTempo real, lastCrossing real, lastHighPress real, timeFromPossessionStart real, timeFromSetPlay real, timeFromDirectPlay real,timeFromCounterAttack real, timeFromMaintenance real, timeFromBuildUp real, timeFromSustainedThreat real, timeFromFastTempo real, timeFromCrossing real, timeFromHighPress real, timeToShot real, timeToGoal real, timeToOffside real, possessionRegain text, possessionLoss text, disruption text, moveStart text, oBMPPos real, oBMPNeg real, xG Shot real, goalMove real, dBMPPos real, dBMPNeg real, xGDef real, directPlayPresenceActive real,counterAttackPresenceActive real, maintenancePresenceActive real, buildUpPresenceActive real, sustainedThreatPresenceActive real, fastTempoPresenceActive real, crossingPresenceActive real, highPressPresenceActive real, setPlayPresenceActive real, directPlayPresenceNonActive real, counterAttackPresenceNonActive real, maintenancePresenceNonActive real, buildUpPresenceNonActive real, sustainedThreatPresenceNonActive real, fastTempoPresenceNonActive real, crossingPresenceNonActive real, highPressPresenceNonActive real, setPlayPresenceNonActive real, scoreA integer, scoreB integer, A01_Name text, A01_X real, A01_Y real, A01_vX real, A01_vY real, A01_v real, A01_aX real, A01_aY real, A01_a real, A02_Name text, A02_X real, A02_Y real, A02_vX real, A02_vY real, A02_v real, A02_aX real, A02_aY real, A02_a real, A03_Name text, A03_X real, A03_Y real, A03_vX real, A03_vY real, A03_v real, A03_aX real, A03_aY real, A03_a real,A04_Name text, A04_X real, A04_Y real, A04_vX real, A04_vY real, A04_v real, A04_aX real, A04_aY real, A04_a real, A05_Name text, A05_X real, A05_Y real, A05_vX real, A05_vY real, A05_v real, A05_aX real, A05_aY real, A05_a real, A06_Name text, A06_X real, A06_Y real, A06_vX real, A06_vY real, A06_v real, A06_aX real, A06_aY real, A06_a real, A07_Name text, A07_X real, A07_Y real, A07_vX real, A07_vY real, A07_v real, A07_aX real, A07_aY real, A07_a real, A08_Name text, A08_X real, A08_Y real, A08_vX real, A08_vY real, A08_v real, A08_aX real, A08_aY real, A08_a real, A09_Name text, A09_X real, A09_Y real, A09_vX real, A09_vY real, A09_v real,A09_aX real, A09_aY real, A09_a real, A10_Name text, A10_X real, A10_Y real, A10_vX real, A10_vY real, A10_v real, A10_aX real, A10_aY real, A10_a real, A11_Name text, A11_X real, A11_Y real, A11_vX real, A11_vY real, A11_v real, A11_aX real, A11_aY real, A11_a real, B01_Name text, B01_X real, B01_Y real, B01_vX real, B01_vY real,B01_v real, B01_aX real, B01_aY real, B01_a real, B02_Name text, B02_X real, B02_Y real, B02_vX real, B02_vY real, B02_v real, B02_aX real, B02_aY real, B02_a real, B03_Name text, B03_X real, B03_Y real, B03_vX real, B03_vY real, B03_v real, B03_aX real, B03_aY real, B03_a real, B04_Name text, B04_X real, B04_Y real, B04_vX real, B04_vY real, B04_v real, B04_aX real, B04_aY real, B04_a real, B05_Name text, B05_X real, B05_Y real, B05_vX real, B05_vY real, B05_v real, B05_aX real, B05_aY real, B05_a real, B06_Name text, B06_X real, B06_Y real, B06_vX real, B06_vY real, B06_v real, B06_aX real, B06_aY real, B06_a real, B07_Name text, B07_X real, B07_Y real, B07_vX real, B07_vY real, B07_v real, B07_aX real, B07_aY real, B07_a real, B08_Name text, B08_X real, B08_Y real, B08_vX real, B08_vY real, B08_v real, B08_aX real, B08_aY real, B08_a real, B09_Name text, B09_X real, B09_Y real, B09_vX real, B09_vY real, B09_v real, B09_aX real, B09_aY real, B09_a real, B10_Name text, B10_X real, B10_Y real, B10_vX real, B10_vY real, B10_v real, B10_aX real, B10_aY real, B10_a real, B11_Name text, B11_X real, B11_Y real, B11_vX real, B11_vY real, B11_v real, B11_aX real, B11_aY real, B11_a real)''')


    #c.execute('''CREATE TABLE mancityVbayern (competition text, matchName text, teamA text, teamB text, eventName text)''')

        # get the csv file
    csvFile = np.genfromtxt(bigTableName, delimiter=',',dtype=[ ('competition','S50'), ('matchName','S50'), ('teamA','S50'), ('teamB','S50'), ('eventName','S50'), ('eventRow','S50'), ('half' ,'i8'), ('time' ,'f8'), ('player1Name','S50'), ('player1Team','S50'), ('player2Name','S50'), ('player2Team','S50'), ('x','f8'), ('y','f8'), ('nextEventName','S50'), ('nextPlayer1Name','S50'), ('nextPlayer1Team','S50'), ('nextX','f8'), ('nextY','f8'), ('inversionPoss','i8'), ('inversionActive','i8'), ('offensiveness','f8'), ('possession','S50'), ('activeTeam','S50'), ('transition','S50'), ('playerTransition','S50'), ('goalDifference','i8'), ('possessionNumber','i8'), ('moveNumber','i8'), ('lastDirectPlay','f8'), ('lastCounterAttack','f8'), ('lastMaintenance','f8'), ('lastBuildUp' ,'f8'), ('lastSustainedThreat','f8'),('lastFastTempo','f8'),('lastCrossing','f8'),('lastHighPress','f8'),('timeFromPossessionStart','f8'),('timeFromSetPlay','f8'),('timeFromDirectPlay','f8'),('timeFromCounterAttack','f8'),('timeFromMaintenance','f8'),('timeFromBuildUp','f8'),('timeFromSustainedThreat','f8'),('timeFromFastTempo','f8'),('timeFromCrossing','f8'),('timeFromHighPress','f8'),('timeToShot','f8'),('timeToGoal','f8'),('timeToOffside','f8'),('possessionRegain','S50'),('possessionLoss','S50'),('disruption','S50'),('moveStart','S50'),('oBMPPos','f8'),('oBMPNeg','f8'),('xG Shot','f8'),('goalMove','f8'),('dBMPPos','f8'),('dBMPNeg','f8'),('xGDef','f8'),('directPlayPresenceActive','f8'),('counterAttackPresenceActive','f8'),('maintenancePresenceActive','f8'),('buildUpPresenceActive','f8'),('sustainedThreatPresenceActive','f8'),('fastTempoPresenceActive','f8'),('crossingPresenceActive','f8'),('highPressPresenceActive','f8'),('setPlayPresenceActive','f8'),('directPlayPresenceNonActive','f8'),('counterAttackPresenceNonActive','f8'),('maintenancePresenceNonActive','f8'),('buildUpPresenceNonActive','f8'),('sustainedThreatPresenceNonActive','f8'),('fastTempoPresenceNonActive','f8'),('crossingPresenceNonActive','f8'),('highPressPresenceNonActive','f8'),('setPlayPresenceNonActive','f8'),('scoreA','i8'),('scoreB','i8'),('A01_Name','S50'),('A01_X','f8'),('A01_Y','f8'),('A01_vX','f8'),('A01_vY','f8'),('A01_v','f8'),('A01_aX','f8'),('A01_aY','f8'),('A01_a','f8'),('A02_Name','S50'),('A02_X','f8'),('A02_Y','f8'),('A02_vX','f8'),('A02_vY','f8'),('A02_v','f8'),('A02_aX','f8'),('A02_aY','f8'),('A02_a','f8'),('A03_Name','S50'),('A03_X','f8'),('A03_Y','f8'),('A03_vX','f8'),('A03_vY','f8'),('A03_v','f8'),('A03_aX','f8'),('A03_aY','f8'),('A03_a','f8'),('A04_Name','S50'),('A04_X','f8'),('A04_Y','f8'),('A04_vX','f8'),('A04_vY','f8'),('A04_v','f8'),('A04_aX','f8'),('A04_aY','f8'),('A04_a','f8'),('A05_Name','S50'),('A05_X','f8'),('A05_Y','f8'),('A05_vX','f8'),('A05_vY','f8'),('A05_v','f8'),('A05_aX','f8'),('A05_aY','f8'),('A05_a','f8'),('A06_Name','S50'),('A06_X','f8'),('A06_Y','f8'),('A06_vX','f8'),('A06_vY','f8'),('A06_v','f8'),('A06_aX','f8'),('A06_aY','f8'),('A06_a','f8'),('A07_Name','S50'),('A07_X','f8'),('A07_Y','f8'),('A07_vX','f8'),('A07_vY','f8'),('A07_v','f8'),('A07_aX','f8'),('A07_aY','f8'),('A07_a','f8'),('A08_Name','S50'),('A08_X','f8'),('A08_Y','f8'),('A08_vX','f8'),('A08_vY','f8'),('A08_v','f8'),('A08_aX','f8'),('A08_aY','f8'),('A08_a','f8'),('A09_Name','S50'),('A09_X','f8'),('A09_Y','f8'),('A09_vX','f8'),('A09_vY','f8'),('A09_v','f8'),('A09_aX','f8'),('A09_aY','f8'),('A09_a','f8'),('A10_Name','S50'),('A10_X','f8'),('A10_Y','f8'),('A10_vX','f8'),('A10_vY','f8'),('A10_v','f8'),('A10_aX','f8'),('A10_aY','f8'),('A10_a','f8'),('A11_Name','S50'),('A11_X','f8'),('A11_Y','f8'),('A11_vX','f8'),('A11_vY','f8'),('A11_v','f8'),('A11_aX','f8'),('A11_aY','f8'),('A11_a','f8'),('B01_Name','S50'),('B01_X','f8'),('B01_Y','f8'),('B01_vX','f8'),('B01_vY','f8'),('B01_v','f8'),('B01_aX','f8'),('B01_aY','f8'),('B01_a','f8'),('B02_Name','S50'),('B02_X','f8'),('B02_Y','f8'),('B02_vX','f8'),('B02_vY','f8'),('B02_v','f8'),('B02_aX','f8'),('B02_aY','f8'),('B02_a','f8'),('B03_Name','S50'),('B03_X','f8'),('B03_Y','f8'),('B03_vX','f8'),('B03_vY','f8'),('B03_v','f8'),('B03_aX','f8'),('B03_aY','f8'),('B03_a','f8'),('B04_Name','S50'),('B04_X','f8'),('B04_Y','f8'),('B04_vX','f8'),('B04_vY','f8'),('B04_v','f8'),('B04_aX','f8'),('B04_aY','f8'),('B04_a','f8'),('B05_Name','S50'),('B05_X','f8'),('B05_Y','f8'),('B05_vX','f8'),('B05_vY','f8'),('B05_v','f8'),('B05_aX','f8'),('B05_aY','f8'),('B05_a','f8'),('B06_Name','S50'),('B06_X','f8'),('B06_Y','f8'),('B06_vX','f8'),('B06_vY','f8'),('B06_v','f8'),('B06_aX','f8'),('B06_aY','f8'),('B06_a','f8'),('B07_Name','S50'),('B07_X','f8'),('B07_Y','f8'),('B07_vX','f8'),('B07_vY','f8'),('B07_v','f8'),('B07_aX','f8'),('B07_aY','f8'),('B07_a','f8'),('B08_Name','S50'),('B08_X','f8'),('B08_Y','f8'),('B08_vX','f8'),('B08_vY','f8'),('B08_v','f8'),('B08_aX','f8'),('B08_aY','f8'),('B08_a','f8'),('B09_Name','S50'),('B09_X','f8'),('B09_Y','f8'),('B09_vX','f8'),('B09_vY','f8'),('B09_v','f8'),('B09_aX','f8'),('B09_aY','f8'),('B09_a','f8'),('B10_Name','S50'),('B10_X','f8'),('B10_Y','f8'),('B10_vX','f8'),('B10_vY','f8'),('B10_v','f8'),('B10_aX','f8'),('B10_aY','f8'),('B10_a','f8'),('B11_Name','S50'),('B11_X','f8'),('B11_Y','f8'),('B11_vX','f8'),('B11_vY','f8'),('B11_v','f8'),('B11_aX','f8'),('B11_aY','f8'),('B11_a','f8')], skip_header=1)
    
    # now go through each line and put it into the database
    for line in csvFile:

        print line
        
        # go through each element in the line
        counter = 0
        for item in line:
            if ( (type(item) == float) ):
                if ( math.isnan(item) ):
                    line[counter] = -1000

            counter = counter +1


        print line[0], line[1], line[2], line[3], line[4], line[5], line[6]

        
        # Insert a row of data
        c.execute("INSERT INTO mancityVbayern VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18], line[19], line[20], line[21], line[22], line[23], line[24], line[25], line[26], line[27], line[28], line[29], line[30], line[31], line[32], line[33], line[34], line[35], line[36], line[37], line[38], line[39], line[40], line[41], line[42], line[43], line[44], line[45], line[46], line[47], line[48], line[49], line[50], line[51], line[52], line[53], line[54], line[55], line[56], line[57], line[58], line[59], line[60], line[61], line[62], line[63], line[64], line[65], line[66], line[67], line[68], line[69], line[70], line[71], line[72], line[73], line[74], line[75], line[76], line[77], line[78], line[79], line[80], line[81], line[82], line[83], line[84], line[85], line[86], line[87], line[88], line[89], line[90], line[91], line[92], line[93], line[94], line[95], line[96], line[97], line[98], line[99], line[100], line[101], line[102], line[103], line[104], line[105], line[106], line[107], line[108], line[109], line[110], line[111], line[112], line[113], line[114], line[115], line[116], line[117], line[118], line[119], line[120], line[121], line[122], line[123], line[124], line[125], line[126], line[127], line[128], line[129], line[130], line[131], line[132], line[133], line[134], line[135], line[136], line[137], line[138], line[139], line[140], line[141], line[142], line[143], line[144], line[145], line[146], line[147], line[148], line[149], line[150], line[151], line[152], line[153], line[154], line[155], line[156], line[157], line[158], line[159], line[160], line[161], line[162], line[163], line[164], line[165], line[166], line[167], line[168], line[169], line[170], line[171], line[172], line[173], line[174], line[175], line[176], line[177], line[178], line[179], line[180], line[181], line[182], line[183], line[184], line[185], line[186], line[187], line[188], line[189], line[190], line[191], line[192], line[193], line[194], line[195], line[196], line[197], line[198], line[199], line[200], line[201], line[202], line[203], line[204], line[205], line[206], line[207], line[208], line[209], line[210], line[211], line[212], line[213], line[214], line[215], line[216], line[217], line[218], line[219], line[220], line[221], line[222], line[223], line[224], line[225], line[226], line[227], line[228], line[229], line[230], line[231], line[232], line[233], line[234], line[235], line[236], line[237], line[238], line[239], line[240], line[241], line[242], line[243], line[244], line[245], line[246], line[247], line[248], line[249], line[250], line[251], line[252], line[253], line[254], line[255], line[256], line[257], line[258], line[259], line[260], line[261], line[262], line[263], line[264], line[265], line[266], line[267], line[268], line[269], line[270], line[271], line[272], line[273], line[274], line[275], line[276], line[277], line[278]  ))
#            #curr = cursor.execute('''SELECT * FROM bballQuarter WHERE ABSTIME = (? )''', (firstFrame[0],))
#            #snapShot = execute_query("""SELECT * FROM bballQuarter WHERE ABSTIME = (? )""",rows[0])
#            
#            print line[11], line[2], line[3], line[4], line[5], line[6],
#            
        conn.commit()

    # Close the connection
    conn.close()


