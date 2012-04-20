
def main():
    startApplication("astudio")
    mouseClick(waitForObjectItem(":Artec Studio_MenuBar", "File"))
    mouseClick(waitForObject(":File.Exit_MenuItem"))

