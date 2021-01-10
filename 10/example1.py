#Exceptions
import signal

def resp_timeout(signum, frame):
    raise TimeoutError("time is over!")

if __name__ == '__main__':

    timeout = 5
    signal.signal(signal.SIGALRM, resp_timeout)

    try:
        signal.alarm(timeout)
        num = int(input("Enter a number: "))
        signal.alarm(0)
        print(f"Your number is: {num}")
    except ValueError:
        print("number invalid, end..")
    except KeyboardInterrupt:
        print("\nFinished by user!")
  

        