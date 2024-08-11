# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileSystemEvent

# Here you must specify a valid path to ollama directory
WATCH_DIRECTORY_PATH = r'C:\Users\georgi.naumov\.ollama'


class OnMyWatch:
    # You must set the directory for watch in
    # the constructor
    __watch_directory = None

    def __init__(self, watch_directory_path: str):
        self.observer = Observer()
        self.__watch_directory = watch_directory_path

    def run(self) -> None:
        event_handler = Handler()
        self.observer.schedule(event_handler, self.__watch_directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent) -> None:
        event_type, src_path, dest_path, is_directory = event.event_type, event.src_path, event.dest_path, event.is_directory
        directory_or_file = 'directory' if is_directory else 'file'
        message = f'Watchdog received {event_type} {directory_or_file} event with src_path - {src_path} dest_path - {dest_path}.'
        print(message)


def main():
    watch = OnMyWatch(WATCH_DIRECTORY_PATH)
    watch.run()


if __name__ == '__main__':
    main()
