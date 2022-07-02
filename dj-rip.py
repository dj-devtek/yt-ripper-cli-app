import os
import sys
import multiprocessing as mp

def main():
	print("-"*10, " DJ Ripper Supreme ", "-"*10)
	while True:
		rip_mode = input("Please select rip mode\n1 - Individual\n2 - From file\n: ")
		if rip_mode == "1":
			individual_rip_mode()
			break
		elif rip_mode == "2":
			from_file_rip_mode()
			break
		else:
			print("MESSAGE: Invalid rip mode")
		
# Function to download a line from a input file
def process_line(line):
	elements = line.split("-")
	try:
		download_song(elements[0], elements[1], elements[2].strip())
	except:
		print("-"*40)
		print(f"MESSAGE: There was a problem downloading the song\nFound - {line}")
		print("-"*40)

def from_file_rip_mode():
	print("-"*10, " From File Rip Mode ", "-"*10)
	print("-- Please select a plain text file from the current directory")
	print("-- Each line of the file must be in the format [YouTube link]-[song title]-[song artist]\n")
	rip_filename = input("Rip filename: ")
	rip_filepath = os.getcwd() + "/" + rip_filename
	if os.path.exists(rip_filepath) == False:
		print(f'FILE ERROR: {rip_filename} not found in current directory {os.getcwd()}')
		return
	else:
		file_valid, err = validate_rip_file(rip_filepath)
		if file_valid == False:
			print(err)
			return
		else:
			with open(rip_filepath, "r") as rip_file:
				# Run multiple downloads at a time, should be a bit faster if youtube is throttling download speeds
				lines = rip_file.readlines()
				
				p = mp.Pool(mp.cpu_count())
				p.map(process_line, lines)
				p.close()
				p.join()
			
# Return True if rip file has a valid format
# Otherwise return False with error message
def validate_rip_file(filepath):
	with open(filepath, "r") as rip_file:
		lines = rip_file.readlines()
		for line in lines:
			
			elements = line.split("-")
			if len(elements) != 3:
				return False, f"FORMAT ERROR: rip file must have [YouTube link]-[song title]-[song artist] on each line\nFound - {line}"
			elif "https://www.youtube.com/" not in elements[0]:
				return False, f"FORMAT ERROR: invalid YouTube link\nFound - {line}"
		return True, ""

def individual_rip_mode():
	while True:
		print("-"*10, " Individual Rip Mode ", "-"*10)
		youtube_link = input("YouTube Link: ")
		song_title = input("Title: ")
		song_artist = input("Artist: ")
		
		try:
			download_song(youtube_link, song_title, song_artist)
		except:
			print("MESSAGE: There was a problem downloading the song")
		
		run_arg = input("to continue, press ENTER, otherwise enter any key to quit\n: ")
		if run_arg != "":
			break
		else:
			print("-"*35)
		
def download_song(youtube_link, song_title, song_artist):
	post_process_song_title = song_title.replace(" ", "\ ")
	post_process_song_artist = song_artist.replace(" ", "\ ")

	cmd = f'yt-dlp -o "$HOME/Downloads/{song_title}-{song_artist}.%(ext)s"' \
	f' --add-metadata --postprocessor-args' \
	f' "-metadata artist={post_process_song_artist}' \
	f' -metadata title={post_process_song_title}"' \
	f' -x --audio-format "mp3" "{youtube_link}"'

	os.system(cmd)

if __name__ == "__main__":
	main()
