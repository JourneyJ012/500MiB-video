import sys 
import pathlib 
import subprocess
import json 
import math 

def seconds_to_hhmmss(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def get_video_duration_seconds(file_path) -> int:
    try:
        result = subprocess.run(
            [
                'ffprobe',
                '-v', 'error', 
                '-show_entries', 'format=duration',
                '-of', 'json', 
                file_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        metadata = json.loads(result.stdout)
        duration = float(metadata['format']['duration'])
        return math.floor(duration)
    
    except (KeyError, ValueError, FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to get video duration: {e}")

def main():
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        exit(1)

    video_path = pathlib.Path(sys.argv[1])
    if not video_path.is_file():
        print(f"Fatal: {sys.argv[1]} is not a file.")

    running_duration = 0
    total_duration = get_video_duration_seconds(sys.argv[1])
    next_file = sys.argv[1]
    i = 0
    while True: 
        i += 1
        start_timestamp = seconds_to_hhmmss(max(0, running_duration - 5))

        if (running_duration >= total_duration):
            break

        this_iter_output_path = f"output-{i}.mp4"
        subprocess.run(["ffmpeg", 
                        "-ss", str(start_timestamp), 
                        "-i", next_file, 
                        "-c:v", "hevc_nvenc", 
                        "-fs", "512M", 
                        this_iter_output_path])
        
        running_duration += get_video_duration_seconds(this_iter_output_path)

if __name__ == "__main__":
    main()