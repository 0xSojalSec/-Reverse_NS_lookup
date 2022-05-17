import argparse
import requests
from bs4 import BeautifulSoup
from termcolor import colored

def main(args):
	url = f"https://host.io/ns/{args.domain.strip()}" 
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')
	tags = soup.find_all('a', class_ = 'border-b border-gray-400')
	for tag in tags:
		print(colored(tag.get_text('href'), 'green'))
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', help="The server to perform the attack on.", required=True)
	args = parser.parse_args()
	main(args)
