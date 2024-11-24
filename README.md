# 500MiB-video

Split a video into multiple chunks no larger than a set 500MiB. 

## Getting Started

This project depends on [ffmpeg](https://github.com/FFmpeg/FFmpeg). If you're using an arch or debian-based Linux distribution, you can use [the bootstrap script](./script/bootstrap) to install it:

```bash
$ chmod +x ./script/bootstrap
$ ./script/bootstrap
```

If you're using anything else... glhf &lt;3

## Usage

Just pass any file you want to split to the script: 
```
bash
$ ./src/main.py /mnt/e/myvideo.mp4
```

## FAQ

Q: I want to convert multiple files
A: Read up on the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy), then do `find /path/to/my/dir -type f -name *.mkv | xargs ./src/main.py`

Q: I was the script to (X)
A: You can fork this repo and make it do (X) 

## License

Do what you want I'm not a cop (MIT no attribution)