# UMich ULCS Course Monitor

## About

With the [Two Course Limit](https://cse.engin.umich.edu/academics/for-current-students/advising/enrollment/) rules for UMich EECS Upper Level courses, if you want to enroll in more than two ULCS, you had better pay attention to whether the third course has its waitlist open so that you can get in the list early enough. This script is designed to monitor the open seats in the ULCS course you want to enroll in. As soon as the available seats become 0, it will send a notifying email.

## Getting Started

- Install `bs4`
    ```bash
    $ pip3 install bs4
    ```

- Configure `SENDER_EMAIL`, `SENDER_PASSWORD`, `RECEIVER_EMAIL`, and `INTERVAL`.

- Add the courses you want to monitor in `main()`. For example, EECS 482:

    ```python
    Monitor(482)
    ```

- Run the script

    ```bash
    $ python3 monitor.py
    ```

- To exit, press `Ctrl+C`.

    - If the process failed to exit properly, refer to [this link](https://superuser.com/questions/446808/how-to-manually-stop-a-python-script-that-runs-continuously-on-linux).

## Deployment on CAEN

Not all of us have a server available or a laptop running all day long. Deploying the program on [CAEN](https://caen.engin.umich.edu/connect/linux-login-service/) is then a good choice.

- First, [connect to CAEN's Linux Remote Login Service using Secure Shell (SSH)](https://teamdynamix.umich.edu/TDClient/76/Portal/KB/ArticleDet?ID=5002)
- `git clone` the project and follow the configuration above.

We will use `tmux` to run the program so that it will continue running after the ssh session disconnects. Learn more about other [approaches](https://unix.stackexchange.com/questions/479/keep-processes-running-after-ssh-session-disconnects) and a beginner [guide](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) to `tmux`.

- Start `tmux` with a new session

  ```bash
  $ tmux
  ```

  Note: `tmux` should have been installed on CAEN.

- Run the program in the session

  ```bash
  $ python3 monitor.py
  ```

- Detach from the session by pressing `C-b d`, which means press `Ctrl+b`, release, and then press `d`.

- Disconnect ssh as you want

  ```bash
  $ exit
  ```

- After reconnecting to ssh, attach to `tmux` session

  ```bash
  $ tmux attach
  ```

  The program should be still running properly.

## Acknowledgement

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
- [tmux cheatsheet](https://gist.github.com/andreyvit/2921703)