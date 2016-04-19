import convertToDB
import gameVisualizeWebServer

# first read in the tracking data

# give the list of the player trajectories then we can get a SQL db
#fileListName = "/Users/LUCEYMACPRO/Dropbox/Data-Patrick/ProzoneData/newProzoneData/POC-exampleGames/Manchester City v FC Bayern Munchen-20131002/fileList.txt"
#fileName = "/Users/LUCEYMACPRO/Dropbox/Projects-Patrick/python/src/Game Visualiser/BigTable data/13.10.02 Manchester City v FC Bayern Munchen.csv"

# we convert the raw trajectories to a dB here
#convertToDB.convertFileListToDB(fileListName)
# ---------- convert to big table ------------------
#convertToDB.convertBigTableToDB(fileName)

# now visualize game - visualize using browser
gameVisualizeWebServer.visualizeGame()




# get occupancy maps
#visualizeWebBrowser.plotOcc()




# align to a template - just manually set one


# segment based on game-state

