# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileSystemEvent


class OnMyWatch:
    # You must set the directory for watch in
    # the constructor
    __watch_directory = None

    def __init__(self, watch_directory_path):
        self.observer = Observer()
        self.__watch_directory = watch_directory_path

    def run(self):
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
        event_type, src_path, dest_path = event.event_type, event.src_path, event.dest_path
        message = f'Watchdog received {event_type} event with src_path - {src_path} dest_path - {dest_path}.'
        print(message)


def main():
    watch = OnMyWatch(r'C:\Users\georgi.naumov\.ollama')
    watch.run()


if __name__ == '__main__':
    main()