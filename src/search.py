import webbrowser
import sys

#@author AndrewPetrosky

def main():
	title = sys.argv[1]
	webbrowser.open('https://www.netflix.com/search/' + title)

if __name__ == "__main__":
 	main()