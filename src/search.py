import webbrowser
import sys
import argparse
import re

#@author AndrewPetrosky

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--movie', action='store_true')
	parser.add_argument('title')
	args = parser.parse_args()

	#Open the web browser to the Netflix search results
	webbrowser.open('https://www.netflix.com/search/' + re.sub(r' ', '%20', args.title))

	#Open the web browser to the Amazon search results
	webbrowser.open('https://www.amazon.com/s/ref=nb_ss_gw/102-1882688-6100927?initialSearch' +
		'=1&url=search-alias%3Daps&field-keywords=' + re.sub(r' ', '+', args.title))

	#Open the web browser to the HBO search results
	if args.movie:
		webbrowser.open('http://www.hbo.com/movies/' + re.sub(r' ', '-', args.title))
	else:
		webbrowser.open('http://www.hbo.com/' + re.sub(r' ', '-', args.title))

if __name__ == "__main__":
 	main()