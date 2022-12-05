import multiprocessing
import random


quotes = [
    "Choice is an illusion created between those with power and those without.",
    "What's really going to bake your noodle later on is, would you still have broken it if I hadn't said anything?",
    "The Matrix is everywhere. It is all around us. Even now in this very room.",
    "What you know you can't explain, but you feel it. You've felt it your entire life.",
    "Fate, it seems, is not without a sense of irony.",
    "I can only show you the door, you're the one that has to walk through it."
]


def writer(strings_to_write: [str], filename: str):
    with open(filename, 'w', encoding='utf-8') as wf:
        for _ in range(250_000):
            line_to_write = random.choice(strings_to_write)
            wf.write(line_to_write + ' ')


def main():
    processes = []
    for i in range(multiprocessing.cpu_count() // 2):
        new_proc_file = "file_" + str(i + 1) + ".txt"
        new_proc_name = "proc-" + str(i + 1)
        new_process = multiprocessing.Process(target=writer, args=(quotes, new_proc_file), name=new_proc_name)
        new_process.start()
        processes.append(new_process)

    for prc in processes:
        prc.join(timeout=10)


if __name__ == '__main__':
    main()
