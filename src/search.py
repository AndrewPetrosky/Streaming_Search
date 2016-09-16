import webbrowser
import sys

#@author AndrewPetrosky

def main():
	title = sys.argv[1]
	webbrowser.open('https://www.netflix.com/search/' + title)
	webbrowser.open('https://www.amazon.com/s/ref=nb_ss_gw/102-1882688-6100927?initialSearch=1&url=search-alias%3Daps&field-keywords='
		+ title + '&Go.x=0&Go.y=0&Go=Go')
	#https://www.hbonow.com/feature/PROD775717/sisters?cid=undefined

if __name__ == "__main__":
 	main()